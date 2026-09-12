#!/usr/bin/env python3
import copy
import os
from pathlib import Path

import requests
import yaml

OPENWEBUI_URL = "https://openwebui.uni-freiburg.de"
OPENWEBUI_TOKEN = "TYPE-YOUR-API-HERE"
CONFIG_PATH = Path(os.environ.get("CONTINUE_CONFIG_PATH", "~/.continue/config.yaml")).expanduser()


def int_or_none(value):
    try:
        return int(value) if value is not None else None
    except (TypeError, ValueError):
        return None


def fetch_models():
    headers = {
        "Authorization": f"Bearer {OPENWEBUI_TOKEN}",
        "Accept": "application/json",
    }

    resp = requests.get(f"{OPENWEBUI_URL}/api/models", headers=headers, timeout=30)
    resp.raise_for_status()

    ctype = resp.headers.get("content-type", "")
    if "application/json" not in ctype:
        raise RuntimeError(f"Expected JSON, got {ctype}: {resp.text[:300]}")

    payload = resp.json()

    # Handle common response shapes
    if isinstance(payload, list):
        return payload

    if isinstance(payload, dict):
        for key in ("data", "models", "items", "result"):
            if isinstance(payload.get(key), list):
                return payload[key]

    raise RuntimeError(f"Unsupported models response shape: {type(payload)}")


def extract_model_id(model):
    if isinstance(model, str):
        return model
    if not isinstance(model, dict):
        return str(model)

    return (
        model.get("id")
        or model.get("name")
        or model.get("model")
        or model.get("slug")
        or "unknown-model"
    )


def extract_metadata(model):
    """
    Read metadata if the API provides it.
    We look for common key names and also nested `metadata`.
    """
    if not isinstance(model, dict):
        return {}

    # Merge nested metadata into the main dict if present
    merged = dict(model)
    nested = model.get("metadata")
    if isinstance(nested, dict):
        merged.update(nested)

    meta = {}

    # Context length candidates
    for key in (
        "context_length",
        "contextLength",
        "max_context_length",
        "maxContextLength",
        "context_window",
        "contextWindow",
        "max_input_tokens",
        "maxInputTokens",
    ):
        val = int_or_none(merged.get(key))
        if val:
            meta["contextLength"] = val
            break

    # Output token limit candidates
    for key in (
        "max_tokens",
        "maxTokens",
        "max_output_tokens",
        "maxOutputTokens",
        "max_completion_tokens",
        "maxCompletionTokens",
        "completion_tokens",
    ):
        val = int_or_none(merged.get(key))
        if val:
            meta["maxTokens"] = val
            break

    # Only use explicit roles if the API actually provides them
    roles = merged.get("roles")
    if isinstance(roles, list) and all(isinstance(r, str) for r in roles):
        meta["roles"] = roles

    return meta


def find_template(existing_models, model_id):
    """
    Prefer an exact existing config entry for the same model id.
    Otherwise, use the first OpenAI entry as a template.
    """
    if isinstance(existing_models, list):
        for item in existing_models:
            if isinstance(item, dict) and item.get("model") == model_id:
                base = copy.deepcopy(item)
                base.pop("name", None)
                base.pop("model", None)
                return base

        for item in existing_models:
            if isinstance(item, dict) and item.get("provider") == "openai":
                base = copy.deepcopy(item)
                base.pop("name", None)
                base.pop("model", None)
                return base

    return None


def default_template():
    return {
        "provider": "openai",
        "apiBase": f"{OPENWEBUI_URL}/api",
        "apiKey": OPENWEBUI_TOKEN,
        "roles": ["chat", "edit", "apply"],
        "defaultCompletionOptions": {
            "contextLength": 262144,
            "maxTokens": 32768,
        },
    }


def build_entry(model, template):
    mid = extract_model_id(model)
    meta = extract_metadata(model)

    entry = copy.deepcopy(template)
    entry["name"] = model.get("name") if isinstance(model, dict) and model.get("name") else mid
    entry["model"] = mid

    # Preserve template roles unless explicit roles are provided by metadata
    if "roles" in meta:
        entry["roles"] = meta["roles"]

    opts = entry.get("defaultCompletionOptions") or {}
    opts = copy.deepcopy(opts)

    if "contextLength" in meta:
        opts["contextLength"] = meta["contextLength"]

    if "maxTokens" in meta:
        opts["maxTokens"] = meta["maxTokens"]

    entry["defaultCompletionOptions"] = opts
    return entry


def main():
    models = fetch_models()

    if CONFIG_PATH.exists():
        with CONFIG_PATH.open("r") as f:
            cfg = yaml.safe_load(f) or {}
    else:
        cfg = {}

    existing_models = cfg.get("models", [])
    base = find_template(existing_models, None) or default_template()

    new_models = []
    for model in models:
        mid = extract_model_id(model)
        template = find_template(existing_models, mid) or base
        new_models.append(build_entry(model, template))

    cfg["models"] = new_models

    with CONFIG_PATH.open("w") as f:
        yaml.safe_dump(cfg, f, sort_keys=False, allow_unicode=True)

    print(f"Updated {CONFIG_PATH} with {len(new_models)} models.")


if __name__ == "__main__":
    main()
