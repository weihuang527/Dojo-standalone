#!/usr/bin/env python
# -*- coding: UTF-8 -*-
#
# generated by wxGlade 0.8.1 on Mon Jul 16 17:56:08 2018
#

import wx
import wx.adv
import wx.grid

# begin wxGlade: dependencies
# end wxGlade

# begin wxGlade: extracode
# end wxGlade


class ControlPanel(wx.Frame):
    def __init__(self, *args, **kwds):
        # begin wxGlade: ControlPanel.__init__
        kwds["style"] = kwds.get("style", 0) | wx.DEFAULT_FRAME_STYLE
        wx.Frame.__init__(self, *args, **kwds)
        self.SetSize((454, 534))
        
        # Menu Bar
        self.frame_menubar = wx.MenuBar()
        wxglade_tmp_menu = wx.Menu()
        wxglade_tmp_menu.Append(0, "Import", "")
        self.Bind(wx.EVT_MENU, self.Import, id=0)
        wxglade_tmp_menu.Append(1, "Open Dojo File Folder", "")
        self.Bind(wx.EVT_MENU, self.SelectDojoFile, id=1)
        wxglade_tmp_menu.Append(2, "Copy Dojo Files", "")
        self.Bind(wx.EVT_MENU, self.ExportDojoFiles, id=2)
        wxglade_tmp_menu.Append(3, "Export Images", "")
        self.Bind(wx.EVT_MENU, self.ExportImages, id=3)
        wxglade_tmp_menu.Append(4, "Export Segmentation", "")
        self.Bind(wx.EVT_MENU, self.ExportSegmentation, id=4)
        wxglade_tmp_menu.AppendSeparator()
        wxglade_tmp_menu.Append(5, "Exit", "")
        self.Bind(wx.EVT_MENU, self.Exit, id=5)
        self.frame_menubar.Append(wxglade_tmp_menu, "File")
        wxglade_tmp_menu = wx.Menu()
        wxglade_tmp_menu.Append(61, "Undo", "")
        self.Bind(wx.EVT_MENU, self.Undo, id=61)
        wxglade_tmp_menu.Append(62, "Redo", "")
        self.Bind(wx.EVT_MENU, self.Redo, id=62)
        self.frame_menubar.Append(wxglade_tmp_menu, "Edit")
        wxglade_tmp_menu = wx.Menu()
        wxglade_tmp_menu.Append(701, "Grab Cut", "")
        self.Bind(wx.EVT_MENU, self.GrabCut, id=701)
        wxglade_tmp_menu_sub = wx.Menu()
        wxglade_tmp_menu_sub.Append(7021, "3D Watershed", "")
        self.Bind(wx.EVT_MENU, self.Watershed3D, id=7021)
        wxglade_tmp_menu_sub.Append(7022, "Stable Matching", "")
        self.Bind(wx.EVT_MENU, self.StableMatching, id=7022)
        wxglade_tmp_menu.Append(wx.ID_ANY, "Interlayer Connection", wxglade_tmp_menu_sub, "")
        wxglade_tmp_menu.Append(703, "Superpixelization", "")
        self.Bind(wx.EVT_MENU, self.SuperPixel, id=703)
        wxglade_tmp_menu.Append(704, "User Defined", "")
        self.Bind(wx.EVT_MENU, self.UserDefined, id=704)
        self.frame_menubar.Append(wxglade_tmp_menu, "Plugins")
        wxglade_tmp_menu = wx.Menu()
        item = wxglade_tmp_menu.Append(wx.ID_ANY, "About Dojo", "")
        self.Bind(wx.EVT_MENU, self.AboutDojo, id=item.GetId())
        self.frame_menubar.Append(wxglade_tmp_menu, "Help")
        self.SetMenuBar(self.frame_menubar)
        # Menu Bar end
        self.frame_statusbar = self.CreateStatusBar(1)
        self.panel_URL = wx.Panel(self, wx.ID_ANY)
        self.DojoHTTP = wx.adv.HyperlinkCtrl(self.panel_URL, wx.ID_ANY, "http://10.0.0.1/dojo/", "")
        self.notebook_1 = wx.Notebook(self, wx.ID_ANY)
        self.nb1_3DMerge = wx.Panel(self.notebook_1, wx.ID_ANY)
        self.grid1 = wx.grid.Grid(self.nb1_3DMerge, 1, size=(1, 1))
        self.checkbox_1 = wx.CheckBox(self.nb1_3DMerge, 1000, "")
        self.Execute1 = wx.Button(self.nb1_3DMerge, 11, "Execute")
        self.Clear1 = wx.Button(self.nb1_3DMerge, 12, "Clear")
        self.nb2_3DDisconnect = wx.Panel(self.notebook_1, wx.ID_ANY)
        self.grid2 = wx.grid.Grid(self.nb2_3DDisconnect, 2, size=(1, 1))
        self.Execute2 = wx.Button(self.nb2_3DDisconnect, 21, "Execute")
        self.Clear2 = wx.Button(self.nb2_3DDisconnect, 22, "Clear")
        self.nb3_2DDisconnect = wx.Panel(self.notebook_1, wx.ID_ANY)
        self.grid3 = wx.grid.Grid(self.nb3_2DDisconnect, 3, size=(1, 1))
        self.Execute3 = wx.Button(self.nb3_2DDisconnect, 31, "Execute")
        self.Clear3 = wx.Button(self.nb3_2DDisconnect, 32, "Clear")
        self.nb4_3DReplace = wx.Panel(self.notebook_1, wx.ID_ANY)
        self.grid4 = wx.grid.Grid(self.nb4_3DReplace, 4, size=(1, 1))
        self.Execute4 = wx.Button(self.nb4_3DReplace, 41, "Execute")
        self.Clear4 = wx.Button(self.nb4_3DReplace, 42, "Clear")
        self.nb5_2DReplace = wx.Panel(self.notebook_1, wx.ID_ANY)
        self.grid5 = wx.grid.Grid(self.nb5_2DReplace, 5, size=(1, 1))
        self.Execute5 = wx.Button(self.nb5_2DReplace, 51, "Execute")
        self.Clear5 = wx.Button(self.nb5_2DReplace, 52, "Clear")

        self.__set_properties()
        self.__do_layout()

        self.Bind(wx.grid.EVT_GRID_CMD_CELL_RIGHT_CLICK, self.AppendRowsCols1, id=1)
        self.Bind(wx.EVT_BUTTON, self.Execute1_3DMerge, id=11)
        self.Bind(wx.EVT_BUTTON, self.Clear1_3DMerge, id=12)
        self.Bind(wx.grid.EVT_GRID_CMD_CELL_RIGHT_CLICK, self.AppendRowsCols2, id=2)
        self.Bind(wx.EVT_BUTTON, self.Execute2_3Disconnect, id=21)
        self.Bind(wx.EVT_BUTTON, self.Clear2_3Disconnect, id=22)
        self.Bind(wx.grid.EVT_GRID_CMD_CELL_RIGHT_CLICK, self.AppendRowsCols3, id=3)
        self.Bind(wx.EVT_BUTTON, self.Execute3_2Disconnect, id=31)
        self.Bind(wx.EVT_BUTTON, self.Clear3_2Disconnect, id=32)
        self.Bind(wx.grid.EVT_GRID_CMD_CELL_RIGHT_CLICK, self.AppendRowsCols4, id=4)
        self.Bind(wx.EVT_BUTTON, self.Execute4_3DReplace, id=41)
        self.Bind(wx.EVT_BUTTON, self.Clear4_3DReplace, id=42)
        self.Bind(wx.grid.EVT_GRID_CMD_CELL_RIGHT_CLICK, self.AppendRowsCols5, id=5)
        self.Bind(wx.EVT_BUTTON, self.Execute5_2DReplace, id=51)
        self.Bind(wx.EVT_BUTTON, self.Clear5_2DReplace, id=52)
        # end wxGlade

    def __set_properties(self):
        # begin wxGlade: ControlPanel.__set_properties
        self.SetTitle("Dojo Control Panel")
        _icon = wx.NullIcon
        _icon.CopyFromBitmap(wx.Bitmap("../icons/Mojo2_16.png", wx.BITMAP_TYPE_ANY))
        self.SetIcon(_icon)
        self.frame_statusbar.SetStatusWidths([-1])

        # statusbar fields
        frame_statusbar_fields = ["Target Mojo Folder: None"]
        for i in range(len(frame_statusbar_fields)):
            self.frame_statusbar.SetStatusText(frame_statusbar_fields[i], i)
        self.grid1.CreateGrid(10, 3)
        self.grid1.SetSelectionMode(wx.grid.Grid.SelectRows)
        self.grid1.SetColLabelValue(0, "Conn1")
        self.grid1.SetColLabelValue(1, "Conn2")
        self.grid1.SetColLabelValue(2, "Conn3")
        self.Execute1.SetMinSize((88, 26))
        self.grid2.CreateGrid(10, 2)
        self.grid2.SetSelectionMode(wx.grid.Grid.SelectRows)
        self.grid2.SetColLabelValue(0, "Target Id")
        self.grid2.SetColSize(0, 120)
        self.grid2.SetColLabelValue(1, "Dilute(+)/Erode(-)")
        self.grid2.SetColSize(1, 120)
        self.Execute2.SetMinSize((88, 26))
        self.grid3.CreateGrid(10, 2)
        self.grid3.SetSelectionMode(wx.grid.Grid.SelectRows)
        self.grid3.SetColLabelValue(0, "Image No")
        self.grid3.SetColSize(0, 120)
        self.grid3.SetColLabelValue(1, "Target Id")
        self.grid3.SetColSize(1, 120)
        self.Execute3.SetMinSize((88, 26))
        self.grid4.CreateGrid(10, 2)
        self.grid4.SetSelectionMode(wx.grid.Grid.SelectRows)
        self.grid4.SetColLabelValue(0, "Target Id")
        self.grid4.SetColSize(0, 120)
        self.grid4.SetColLabelValue(1, "Destination Id")
        self.grid4.SetColSize(1, 120)
        self.Execute4.SetMinSize((88, 26))
        self.grid5.CreateGrid(10, 3)
        self.grid5.SetSelectionMode(wx.grid.Grid.SelectRows)
        self.grid5.SetColLabelValue(0, "Image No")
        self.grid5.SetColSize(0, 100)
        self.grid5.SetColLabelValue(1, "Target Id")
        self.grid5.SetColSize(1, 100)
        self.grid5.SetColLabelValue(2, "Destination Id")
        self.grid5.SetColSize(2, 100)
        self.Execute5.SetMinSize((88, 26))
        # end wxGlade

    def __do_layout(self):
        # begin wxGlade: ControlPanel.__do_layout
        s0 = wx.BoxSizer(wx.VERTICAL)
        s5 = wx.BoxSizer(wx.VERTICAL)
        s52 = wx.BoxSizer(wx.HORIZONTAL)
        s51 = wx.BoxSizer(wx.HORIZONTAL)
        s4 = wx.BoxSizer(wx.VERTICAL)
        s42 = wx.BoxSizer(wx.HORIZONTAL)
        s41 = wx.BoxSizer(wx.HORIZONTAL)
        s3 = wx.BoxSizer(wx.VERTICAL)
        s32 = wx.BoxSizer(wx.HORIZONTAL)
        s31 = wx.BoxSizer(wx.HORIZONTAL)
        s2 = wx.BoxSizer(wx.VERTICAL)
        s22 = wx.BoxSizer(wx.HORIZONTAL)
        s21 = wx.BoxSizer(wx.HORIZONTAL)
        s1 = wx.BoxSizer(wx.VERTICAL)
        s13 = wx.BoxSizer(wx.HORIZONTAL)
        s12 = wx.BoxSizer(wx.HORIZONTAL)
        s11 = wx.BoxSizer(wx.HORIZONTAL)
        ss1 = wx.BoxSizer(wx.HORIZONTAL)
        URL_Text = wx.StaticText(self.panel_URL, wx.ID_ANY, "URL")
        ss1.Add(URL_Text, 0, wx.ALIGN_CENTER_VERTICAL | wx.ALIGN_RIGHT | wx.ALL, 4)
        ss1.Add(self.DojoHTTP, 0, wx.ALL, 4)
        self.panel_URL.SetSizer(ss1)
        s0.Add(self.panel_URL, 0, wx.ALL | wx.EXPAND, 0)
        bitmap_1 = wx.StaticBitmap(self.nb1_3DMerge, wx.ID_ANY, wx.Bitmap("./../icons/Merge3D_32.png", wx.BITMAP_TYPE_ANY))
        s11.Add(bitmap_1, 0, wx.ALIGN_CENTER | wx.ALL, 5)
        label1 = wx.StaticText(self.nb1_3DMerge, wx.ID_ANY, "3D Merge")
        s11.Add(label1, 1, wx.ALIGN_CENTER | wx.ALL, 5)
        s1.Add(s11, 0, 0, 0)
        s1.Add(self.grid1, 1, wx.ALL | wx.EXPAND, 5)
        s12.Add(self.checkbox_1, 0, wx.ALL, 5)
        label_1 = wx.StaticText(self.nb1_3DMerge, wx.ID_ANY, "Select the most overlapped one at each layer\n")
        s12.Add(label_1, 0, wx.ALL, 5)
        s1.Add(s12, 0, wx.ALL, 5)
        s13.Add(self.Execute1, 0, wx.ALIGN_CENTER_VERTICAL | wx.ALIGN_RIGHT | wx.ALL, 5)
        s13.Add(self.Clear1, 0, wx.ALIGN_BOTTOM | wx.ALIGN_RIGHT | wx.ALL, 5)
        s1.Add(s13, 0, wx.ALIGN_RIGHT | wx.ALL, 5)
        self.nb1_3DMerge.SetSizer(s1)
        bitmap_2 = wx.StaticBitmap(self.nb2_3DDisconnect, wx.ID_ANY, wx.Bitmap("./../icons/Split3D_32.png", wx.BITMAP_TYPE_ANY))
        s21.Add(bitmap_2, 0, wx.ALIGN_CENTER | wx.ALL, 5)
        label2 = wx.StaticText(self.nb2_3DDisconnect, wx.ID_ANY, "3D Disconnect")
        s21.Add(label2, 1, wx.ALIGN_CENTER | wx.ALL, 5)
        s2.Add(s21, 0, 0, 0)
        s2.Add(self.grid2, 1, wx.ALL | wx.EXPAND, 5)
        s22.Add(self.Execute2, 0, wx.ALIGN_CENTER_VERTICAL | wx.ALIGN_RIGHT | wx.ALL, 5)
        s22.Add(self.Clear2, 0, wx.ALIGN_BOTTOM | wx.ALIGN_RIGHT | wx.ALL, 5)
        s2.Add(s22, 0, wx.ALIGN_RIGHT | wx.ALL, 5)
        self.nb2_3DDisconnect.SetSizer(s2)
        bitmap_3 = wx.StaticBitmap(self.nb3_2DDisconnect, wx.ID_ANY, wx.Bitmap("./../icons/Split2D_32.png", wx.BITMAP_TYPE_ANY))
        s31.Add(bitmap_3, 0, wx.ALIGN_CENTER | wx.ALL, 5)
        label3 = wx.StaticText(self.nb3_2DDisconnect, wx.ID_ANY, "2D Disconnect")
        s31.Add(label3, 1, wx.ALIGN_CENTER | wx.ALL, 5)
        s3.Add(s31, 0, 0, 0)
        s3.Add(self.grid3, 1, wx.ALL | wx.EXPAND, 5)
        s32.Add(self.Execute3, 0, wx.ALIGN_CENTER_VERTICAL | wx.ALIGN_RIGHT | wx.ALL, 5)
        s32.Add(self.Clear3, 0, wx.ALIGN_BOTTOM | wx.ALIGN_RIGHT | wx.ALL, 5)
        s3.Add(s32, 0, wx.ALIGN_RIGHT | wx.ALL, 5)
        self.nb3_2DDisconnect.SetSizer(s3)
        bitmap_4 = wx.StaticBitmap(self.nb4_3DReplace, wx.ID_ANY, wx.Bitmap("./../icons/Replace3D_32.png", wx.BITMAP_TYPE_ANY))
        s41.Add(bitmap_4, 0, wx.ALIGN_CENTER | wx.ALL, 5)
        label4 = wx.StaticText(self.nb4_3DReplace, wx.ID_ANY, "3D Replace")
        s41.Add(label4, 1, wx.ALIGN_CENTER | wx.ALL, 5)
        s4.Add(s41, 0, 0, 0)
        s4.Add(self.grid4, 1, wx.ALL | wx.EXPAND, 5)
        s42.Add(self.Execute4, 0, wx.ALIGN_CENTER_VERTICAL | wx.ALIGN_RIGHT | wx.ALL, 5)
        s42.Add(self.Clear4, 0, wx.ALIGN_BOTTOM | wx.ALIGN_RIGHT | wx.ALL, 5)
        s4.Add(s42, 0, wx.ALIGN_RIGHT | wx.ALL, 5)
        self.nb4_3DReplace.SetSizer(s4)
        bitmap_5 = wx.StaticBitmap(self.nb5_2DReplace, wx.ID_ANY, wx.Bitmap("./../icons/Replace2D_32.png", wx.BITMAP_TYPE_ANY))
        s51.Add(bitmap_5, 0, wx.ALIGN_CENTER | wx.ALL, 5)
        label5 = wx.StaticText(self.nb5_2DReplace, wx.ID_ANY, "2D Replace")
        s51.Add(label5, 1, wx.ALIGN_CENTER | wx.ALL, 5)
        s5.Add(s51, 0, 0, 0)
        s5.Add(self.grid5, 1, wx.ALL | wx.EXPAND, 5)
        s52.Add(self.Execute5, 0, wx.ALIGN_CENTER_VERTICAL | wx.ALIGN_RIGHT | wx.ALL, 5)
        s52.Add(self.Clear5, 0, wx.ALIGN_BOTTOM | wx.ALIGN_RIGHT | wx.ALL, 5)
        s5.Add(s52, 0, wx.ALIGN_RIGHT | wx.ALL, 5)
        self.nb5_2DReplace.SetSizer(s5)
        self.notebook_1.AddPage(self.nb1_3DMerge, "3D Merge")
        self.notebook_1.AddPage(self.nb2_3DDisconnect, "3D Disconnect")
        self.notebook_1.AddPage(self.nb3_2DDisconnect, "2D Disconnect")
        self.notebook_1.AddPage(self.nb4_3DReplace, "3D Replace")
        self.notebook_1.AddPage(self.nb5_2DReplace, "2D Replace")
        s0.Add(self.notebook_1, 1, wx.EXPAND, 0)
        self.SetSizer(s0)
        self.Layout()
        # end wxGlade

    def Import(self, event):  # wxGlade: ControlPanel.<event_handler>
        print("Event handler 'Import' not implemented!")
        event.Skip()

    def SelectDojoFile(self, event):  # wxGlade: ControlPanel.<event_handler>
        print("Event handler 'SelectDojoFile' not implemented!")
        event.Skip()

    def ExportDojoFiles(self, event):  # wxGlade: ControlPanel.<event_handler>
        print("Event handler 'ExportDojoFiles' not implemented!")
        event.Skip()

    def ExportImages(self, event):  # wxGlade: ControlPanel.<event_handler>
        print("Event handler 'ExportImages' not implemented!")
        event.Skip()

    def ExportSegmentation(self, event):  # wxGlade: ControlPanel.<event_handler>
        print("Event handler 'ExportSegmentation' not implemented!")
        event.Skip()

    def Exit(self, event):  # wxGlade: ControlPanel.<event_handler>
        print("Event handler 'Exit' not implemented!")
        event.Skip()

    def Undo(self, event):  # wxGlade: ControlPanel.<event_handler>
        print("Event handler 'Undo' not implemented!")
        event.Skip()

    def Redo(self, event):  # wxGlade: ControlPanel.<event_handler>
        print("Event handler 'Redo' not implemented!")
        event.Skip()

    def GrabCut(self, event):  # wxGlade: ControlPanel.<event_handler>
        print("Event handler 'GrabCut' not implemented!")
        event.Skip()

    def Watershed3D(self, event):  # wxGlade: ControlPanel.<event_handler>
        print("Event handler 'Watershed3D' not implemented!")
        event.Skip()

    def StableMatching(self, event):  # wxGlade: ControlPanel.<event_handler>
        print("Event handler 'StableMatching' not implemented!")
        event.Skip()

    def SuperPixel(self, event):  # wxGlade: ControlPanel.<event_handler>
        print("Event handler 'SuperPixel' not implemented!")
        event.Skip()

    def UserDefined(self, event):  # wxGlade: ControlPanel.<event_handler>
        print("Event handler 'UserDefined' not implemented!")
        event.Skip()

    def AboutDojo(self, event):  # wxGlade: ControlPanel.<event_handler>
        print("Event handler 'AboutDojo' not implemented!")
        event.Skip()

    def AppendRowsCols1(self, event):  # wxGlade: ControlPanel.<event_handler>
        print("Event handler 'AppendRowsCols1' not implemented!")
        event.Skip()

    def Execute1_3DMerge(self, event):  # wxGlade: ControlPanel.<event_handler>
        print("Event handler 'Execute1_3DMerge' not implemented!")
        event.Skip()

    def Clear1_3DMerge(self, event):  # wxGlade: ControlPanel.<event_handler>
        print("Event handler 'Clear1_3DMerge' not implemented!")
        event.Skip()

    def AppendRowsCols2(self, event):  # wxGlade: ControlPanel.<event_handler>
        print("Event handler 'AppendRowsCols2' not implemented!")
        event.Skip()

    def Execute2_3Disconnect(self, event):  # wxGlade: ControlPanel.<event_handler>
        print("Event handler 'Execute2_3Disconnect' not implemented!")
        event.Skip()

    def Clear2_3Disconnect(self, event):  # wxGlade: ControlPanel.<event_handler>
        print("Event handler 'Clear2_3Disconnect' not implemented!")
        event.Skip()

    def AppendRowsCols3(self, event):  # wxGlade: ControlPanel.<event_handler>
        print("Event handler 'AppendRowsCols3' not implemented!")
        event.Skip()

    def Execute3_2Disconnect(self, event):  # wxGlade: ControlPanel.<event_handler>
        print("Event handler 'Execute3_2Disconnect' not implemented!")
        event.Skip()

    def Clear3_2Disconnect(self, event):  # wxGlade: ControlPanel.<event_handler>
        print("Event handler 'Clear3_2Disconnect' not implemented!")
        event.Skip()

    def AppendRowsCols4(self, event):  # wxGlade: ControlPanel.<event_handler>
        print("Event handler 'AppendRowsCols4' not implemented!")
        event.Skip()

    def Execute4_3DReplace(self, event):  # wxGlade: ControlPanel.<event_handler>
        print("Event handler 'Execute4_3DReplace' not implemented!")
        event.Skip()

    def Clear4_3DReplace(self, event):  # wxGlade: ControlPanel.<event_handler>
        print("Event handler 'Clear4_3DReplace' not implemented!")
        event.Skip()

    def AppendRowsCols5(self, event):  # wxGlade: ControlPanel.<event_handler>
        print("Event handler 'AppendRowsCols5' not implemented!")
        event.Skip()

    def Execute5_2DReplace(self, event):  # wxGlade: ControlPanel.<event_handler>
        print("Event handler 'Execute5_2DReplace' not implemented!")
        event.Skip()

    def Clear5_2DReplace(self, event):  # wxGlade: ControlPanel.<event_handler>
        print("Event handler 'Clear5_2DReplace' not implemented!")
        event.Skip()

# end of class ControlPanel

class DojoControlPanel(wx.App):
    def OnInit(self):
        self.ControlPanel = ControlPanel(None, wx.ID_ANY, "")
        self.SetTopWindow(self.ControlPanel)
        self.ControlPanel.Show()
        return True

# end of class DojoControlPanel

if __name__ == "__main__":
    app = DojoControlPanel(0)
    app.MainLoop()