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
- Liberoffice

## Connecting to my account at the Uni storage server
smb://yk112.files.uni-freiburg.de/home/yk112

# VPN
All of them can be connected with openVPN intergrated in GNOME network manager interface

## Uni
According to the Beratung Rechenzentrum der Universität Freiburg, `openconnect` and `network-manager-openconnect` works better in Linux.

VPN Protocol: Fortinet SSL VPN

Gateway: fortivpn.uni-freiburg.de

User Agent: yk112@email.uni-freiburg.de

Token Mode: RSA SecurID manually entered

User: <StudentID> @uni-freiburg.de

Password: <eduroam password>

## Surfshark
https://support.surfshark.com/hc/en-us/articles/360012109779-Connect-to-Surfshark-VPN-using-Ubuntu-Network-Manager

