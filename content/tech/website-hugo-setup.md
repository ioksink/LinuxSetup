---
title: "Setup a website by Hugo and Papermod"
date: 2026-09-13
draft: false
---

This is the setup log of this exact website with Hugo's protocol, Papermod theme, and hosted by github pages.

This is originally my personal github repo to store all my note markdown files that I used to distribute guidelines or introductions to my peers. Since markdown files can be directly rendered by github, my notes can directly turn into a plain website without any effort...... right?

Hmm...... yes! There are already frameworks for setting up static websites, for example, [Hugo](https://gohugo.io/).

Pick a theme from [their website](https://themes.gohugo.io/). I took [Papermod](https://github.com/adityatelange/hugo-PaperMod/) because it is super minimalist and plain.

Further instructions about Hugo or Papermod can be found in [Hugo documentation](https://gohugo.io/documentation/) and [Papermod wiki](https://github.com/adityatelange/hugo-PaperMod/wiki). If specific issues are not stated in both documentation pages, look into the [discussions in github](https://github.com/adityatelange/hugo-PaperMod/discussions). You might find someone with the same issue previously.

# Turn an exisiting github repo into a webpage

```bash
# Create Hugo files inside your existing repo without overwriting git
hugo new site . --force --format yaml

# Add a theme (e.g., PaperMod) as a git submodule (pointer to the original github repo)
git submodule add https://github.com/adityatelange/hugo-PaperMod.git themes/PaperMod

# Tell Hugo to use the theme
echo 'theme = "PaperMod"' >> hugo.toml
```

This `hugo.toml` is the most important config file.

# Test the site locally

```bash
hugo server -D
```

Open http://localhost:1313 in your browser.

# Publish the website

When you are ready, publish the website according this this [guide](https://gohugo.io/host-and-deploy/host-on-github-pages/). You need to copy the script from this guide to tell github how to deploy according to hugo protocol.

# Fine tuning

## hugo.toml

The file `hugo.toml` is not the only format that hugo recognise. You can also use yaml and json.

The toml format is the default format which has the essentials like:

```toml
baseURL = 'https://example.org/'
languageCode = 'en-us'
title = 'My New Hugo Site'
theme = "PaperMod"
```

You can also use yaml. For example, this is the `hugo.yaml` file for this exact website:

```yaml
baseURL: "https://ioksink.github.io/MelissasNotebook/"
locale: "en-uk"
title: "Melissa's Notebook"
theme: ["PaperMod"]
copyright: © 2026 Melissa Kueh
```

and other parameters.

At the top right corner, there are several tabs to click on. This is also set in `hugo.yaml`. In this website, I have these tabs:

```yaml
menu:
  main:
    - name: "News"
      url: /News/
      weight: 10
    - name: "Uni Guide"
      url: /uni/
      weight: 20
    - name: "Tech"
      url: /tech/
      weight: 30
    - name: Blog
      url: /Blog/
      weight: 40
    - name: Note
      url: /Note/
      weight: 50
```

## Post yaml

You must specify the title and date in yaml at the top of every post. For plain text posts, I am using this template:

```yaml
---
title: "My title here"
date: 2026-07-19
draft: false
---
```

## Set cover image for posts

To add a cover image in this post, use this template at the top of `index.md` and put the markdown file and the image file in the same folder. The markdown file in this folder must be named `index.md`.

file structure

```
my-project/
└── content/
    └── cover_image/
        ├── image.png
        └── index.md

```

```yaml
---
title: Cover Image
description: This page is created to test the cover image functionality in Hugo.
summary: This is a test page to verify that the cover image is displayed correctly in Hugo.
date: 2026-04-11
draft: true
cover:
    image: image.png
    alt: "A sample cover image"
    caption: "This is a caption for the cover image."
---
```

## date and last modified time

file structure

```
my-project/
└── layout/
    └── partials/
        └── post_meta.html

```

content of `post_meta.html`

```html
{{- $scratch := newScratch }}

{{- if not .Date.IsZero -}}
{{- $scratch.Add "meta" (slice (printf "<span title='%s'>%s</span>" (.Date) (.Date | time.Format (default "January 2, 2006" .Site.Params.DateFormat)))) }}
{{- end }}

{{- if not .Lastmod.IsZero -}}
{{- $scratch.Add "meta" (slice (printf "<span title='Last updated %s'>Last updated on %s</span>" (.Lastmod) (.Lastmod | time.Format (default "January 2, 2006" .Site.Params.DateFormat)))) }}
{{- end }}

{{- if (.Param "ShowReadingTime") -}}
{{- $scratch.Add "meta" (slice (i18n "read_time" .ReadingTime | default (printf "%d min" .ReadingTime))) }}
{{- end }}

{{- if (.Param "ShowWordCount") -}}
{{- $scratch.Add "meta" (slice (i18n "words" .WordCount | default (printf "%d words" .WordCount))) }}
{{- end }}

{{- with (partial "author.html" .) }}
{{- $scratch.Add "meta" (slice .) }}
{{- end }}

{{- with ($scratch.Get "meta") }}
{{- delimit . "&nbsp;·&nbsp;" | safeHTML -}}
{{- end -}}
```

safeHTML is the most important command to correctly render the syntax.


