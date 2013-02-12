#!/usr/bin/env python
# -*- coding: iso-8859-15 -*-
# generated by wxGlade 0.6.5 (standalone edition) on Mon Feb 11 22:40:58 2013
#
# Kindle Paste
# Converts 2 '\x0A' Unicode characters to '\x0D'
# This fixes formatting errors when pasting.
# Please add this fix to the 'Kindle for PC' software.
#

import wx

# begin wxGlade: extracode
# end wxGlade

class MyFrame(wx.Frame):
    def __init__(self, *args, **kwds):
        # begin wxGlade: MyFrame.__init__
        kwds["style"] = wx.DEFAULT_FRAME_STYLE
        wx.Frame.__init__(self, *args, **kwds)
        self.text_ctrl_1 = wx.TextCtrl(self, -1, "", style=wx.TE_MULTILINE | wx.HSCROLL)

        self.__set_properties()
        self.__do_layout()

        self.Bind(wx.EVT_TEXT, self.evtTextEdit, self.text_ctrl_1)
        # end wxGlade

    def __set_properties(self):
        # begin wxGlade: MyFrame.__set_properties
        self.SetTitle("Kindle Paste")
        self.SetSize((500, 400))
        # end wxGlade

    def __do_layout(self):
        # begin wxGlade: MyFrame.__do_layout
        sizer_1 = wx.BoxSizer(wx.VERTICAL)
        sizer_1.Add(self.text_ctrl_1, 1, wx.EXPAND, 0)
        self.SetSizer(sizer_1)
        self.Layout()
        # end wxGlade

    def evtTextEdit(self, event):  # wxGlade: MyFrame.<event_handler>
        #print dir(event)
        obj = event.GetEventObject()
        temp = event.String
        #print dir(temp)
        s = temp.replace(u'\xA0\xA0',u'\x0D')
        #print s
        obj.SetValue(s)
        obj.Refresh()

# end of class MyFrame
if __name__ == "__main__":
    app = wx.PySimpleApp(0)
    wx.InitAllImageHandlers()
    frame_1 = MyFrame(None, -1, "")
    app.SetTopWindow(frame_1)
    frame_1.Show()
    app.MainLoop()