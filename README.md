# My-Kodi-Scripts

These scripts are used to customize buttons on a Harmony 665 remote with LG C8 TV for controlling Kodi running on a Nvidia Shield with flirc as IR reciever. These should be compatible with other IR solutions, but IR codes will change based on TV/remote. The keymap addon for Kodi can be used to identify IR codes. 

The .xml file is a keymap file, and should be placed in \internal\Android\data\org.xbmc.kodi\files\.kodi\userdata\keymaps

The .py python scripts should be placed in their own folder, keymap is set to look for them in /storage/emulated/0/scripts/

An activity for the Nvidia shield is set up on MyHarmony, buttons are assigned under remote buttons and assigned to either LG TV or NVida shield

Keymap commands in global will work everywhere unless overwritten by a subgroup. Be sure to duplicate all fullscreenvideo keymaps to videoosd keymaps so that buttons work regardless if controls are on screen or not. 

Disable unwanted commands when in video with noop
