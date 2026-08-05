# Current system setup

[fastfetch screenshot](https://github.com/ioksink/LinuxSetup/blob/master/fastfetch-20260805.jpg?raw=true)

# GNOME Tweak
Fonts
- Interface Text: Lucida Sans Unicode
- Document Text: SF Pro Display
- Monospace Text: Cascadia Code (FiraCode Nerd Font for terminal p10k theme)

Appearance
- Cursor: Sunity-cursors
- Icons: Papirus-Dark
- Legacy Applications: Adwaita (default)

## GNOME Extensions
Managed by GNOME extesion manager
- Just Perfection
- Date Menu Formatter
- WeatherPanel
- Dash to Dock

## Background/Wallpapers

The wallpapers added by the users are in `~/.local/share/backgrounds`, no special permission required. The default distro backgrounds and gnome backgrounds are in `/usr/share/backgrounds/`, making changes to this folder would require admin authority.

# VPN
All of them can be connected with openVPN intergrated in GNOME network manager interface

## Uni
According to the Beratung Rechenzentrum der Universität Freiburg, `openconnect` and `network-manager-openconnect` works better in Linux.
- VPN Protocol: Fortinet SSL VPN
- Gateway: fortivpn.uni-freiburg.de
- User Agent: [StudentID]@email.uni-freiburg.de
- Token Mode: RSA SecurID manually entered
- User: [StudentID]@uni-freiburg.de
- Password: [eduroam password]

## Surfshark
Log in to surfshare account in web browser and follow the instructions [here](https://support.surfshark.com/hc/en-us/articles/360012109779-Connect-to-Surfshark-VPN-using-Ubuntu-Network-Manager). It can also be managed by openconnect in gnome network manager in Setting.
