# -*- coding: utf-8 -*-
import wx
from my_glob import LOG
from my_session import MySession
import ui_res as res

###########################################################################
# MENU IDs
###########################################################################
ID_OPEN = wx.ID_HIGHEST + 1
ID_EXIT = wx.ID_HIGHEST + 2
ID_SETTINGS = wx.ID_HIGHEST + 3

class MyMainFrame(wx.Frame):
    """
    This is main frame class for MyCoder
    """
    def __init__(self, parent, title):
        wx.Frame.__init__(self, parent, -1, title)
        self._statusBar = self.CreateStatusBar()
        self.createClientArea()

    ###########################################################################
    # UI Process
    ###########################################################################
    def createClientArea(self):
        self.initWindow()
        self.createMenuBar()
        # self.createToolbar()
        # self.createPanels()
        self.createStatusbar()
        self.bindEvents()

    def initWindow(self):
        # Set system menu icon
        self.SetIcon(res.m_title.GetIcon())
        # Set pos size
        p = MySession().get(MyMainFrame.__name__)
        if p is None:
            self.SetSize((800, 600))
            self.Center()
        else:
            self.SetSize(p["size"])
            self.SetPosition(p["pos"])

    def createMenuBar(self):
        mb = wx.MenuBar()
        file_menu = wx.Menu()
        item = wx.MenuItem(file_menu, ID_OPEN, u"打开", u"打开文件")
        item.SetBitmap(res.m_open.GetBitmap())
        file_menu.AppendItem(item)
        file_menu.AppendSeparator()
        item = wx.MenuItem(file_menu, ID_EXIT, u"关闭\tCtrl+Q", u"关闭应用")
        item.SetBitmap(res.m_exit.GetBitmap())
        file_menu.AppendItem(item)
        options_menu = wx.Menu()
        item = wx.MenuItem(file_menu, ID_SETTINGS, u"设置", u"设置应用")
        item.SetBitmap(res.m_settings.GetBitmap())
        options_menu.AppendItem(item)
        mb.Append(file_menu, u"文件")
        mb.Append(options_menu, u"选项")
        self.SetMenuBar(mb)

    def createStatusbar(self):
        self._statusBar.SetStatusText("Ready")

    ###########################################################################
    # Events Process
    ###########################################################################
    def bindEvents(self):
        self.Bind(wx.EVT_CLOSE, self.OnCloseWindow)

    def OnCloseWindow(self, evt):
        pos = self.GetPosition()
        size = self.GetSize()
        MySession().set(MyMainFrame.__name__, {"pos": pos, "size": size})
        self.Destroy()
