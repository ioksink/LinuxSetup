# Keyboards
Most of the keyboards I use are preinstalled in Fedora using ibus framework, including English GB/US, German, Japanese (Anthy), Taiwan Chinese (Chewing).

Taiwanese input method in linux has not been updated for a long time, but it does exist under ibus-rime.
1. install ibus-rime: `sudo dnf install ibus-rime` (should be preinstalled in Fedora)
2. download dictionary (banlam.dict.yaml) and scheme (blg_tai.schema.yaml) from [this repo](https://github.com/a-thok/rime-hokkien) and place them in `/usr/share/rime-data/` with sudo privilege. Note that other schemes in the repo are Tsuan and Tsiang dialects.
3. Switch to rime input method. In the drop-down setting list, press 「部屬」. Toggle input method with ctrl+` to 「閩南語台灣音」。


# Packages for daily tasks
- firewalld
- Chromium
- Thunderbird
- Strawberry
- VLC
- GIMP (Not so much these days)
- Audacity (Not so much these days)
- Calibre with [plugins](https://plugins.calibre-ebook.com/):
  - Chinese Text Conversion
  - EpubMerge
  - EpubSplit
  - DeDRM
  - DeACSM (not working on my Ubuntu)

One may also try this commandline tool to turn ASCM to DRM-free Epub. [Github](https://github.com/esn/knock)

## Study and research
- Rstudio -> see [Setup R in Fedora](Setup_R_in_Fedora.md)
- Codium
- Zotero
- Obsidian
- Element
- Liberoffice (writter and calc are preinstalled)
