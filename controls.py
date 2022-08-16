#!/usr/bin/python
# -*- coding: utf-8 -*-
import xbmcaddon
import xbmcgui

line1 = 'Controls'
line2 = \
    '''
scrollup = see control list
scrolldown = ----
red = screensaver 
green = Refresh Keymaps, Increase Kodi Volume 
yellow = Scan Item 
blue = Mark Watched 

ChannelDown = Previous Letter 
ChannelUp = Next Letter
SkipPrevious button = Previous video
SkipNext button = Next video

---------Video----------------- ---------Global----------
1 =                                               Settings
2 = Small Skip Backwards              Favorites
3 = Small Skip Forwards                Sort: Last Played 
4 = Next Audio Track                    Sort: Sort Title  
5 = Show Subtitles                        Sort: Year  
6 = Next Subtitle Track                 Sort: Date Added  
7 = OSD Audio Settings                Update Library  
8 = Subtitle Delay Adjustments     Clean Library  
9 = Search for subtitles                 Trakt addon  
0 = Home Menu
E = Information
o/+ = Shield settings'''

xbmcgui.Dialog().textviewer(line1, line2)
