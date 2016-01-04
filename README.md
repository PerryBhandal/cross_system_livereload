# cross_system_livereload

Proving "If it's stupid but it works, it's not stupid" wrong since January 4th, 2016.

Requirements
---
Python packages:

Flask (I'm running Python 3.4, but any version that supports Flask should work.)
sniffer

Linux binaries:

xdotool
curl

Usage
---
Cross System LiveReload has two components:

client.py - Run this on the system that you want to live reload changes onn. Have a browser pointing to the page you wish to live reload and ensure xdotool is installed.

scent.py - This is a script for sniffer. Modify it to include the appropriate watch paths/extensions and set the client's IP address.

Each time sniffer detects a change it'll make a call to the Flask instance running in client.py which will hit ctrl + r using xdotool.
