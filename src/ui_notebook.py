# -*- coding: utf-8 -*-
import wx

class MyNotebook(wx.Notebook):
    def __init__(self, parent, id):
        wx.Notebook.__init__(self, parent, id, size=(21, 21), style=wx.BK_DEFAULT)



