#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import wx
from ui_mainframe import MyMainFrame
from my_glob import LOG
from my_conf import MyConf

class MyApp(wx.App):
    """
    This is app class for MyCoder
    """
    def OnInit(self):
        LOG.debug("OnInit")
        # init conf
        p = os.getcwd()
        p = os.path.join(p, "settings.ini")
        MyConf(p)

        #cfg = MyConf()
        #LOG.debug(cfg.get("GENERAL", "VER"))
        #cfg.set("GENERAL", "VER", "1.100.1")
        # setup MainFrame
        frame = MyMainFrame(None, "Simple wxPython App")
        self.SetTopWindow(frame)
        frame.Show(True)
        return True

