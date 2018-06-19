import wx
import sys
import os
import sqlite3
connDictionary = sqlite3.connect("Dictionary.db")
cDictionary = connDictionary.cursor()
cDictionary.execute("SELECT * FROM englishdata")
Dictionary = cDictionary.fetchall()

connRedBox = sqlite3.connect("RedBox.db")
cRedBox = connRedBox.cursor()
cRedBox.execute("SELECT * FROM englishdata")
RedBox = cRedBox.fetchall()

connYellowBox = sqlite3.connect("YellowBox.db")
cYellowBox = connYellowBox.cursor()
cYellowBox.execute("SELECT * FROM englishdata")
YellowBox = cYellowBox.fetchall()

connGreenBox = sqlite3.connect("GreenBox.db")
cGreenBox = connGreenBox.cursor()
cGreenBox.execute("SELECT * FROM englishdata")
GreenBox = cGreenBox.fetchall()

sys.path.append('C:\Users\sanh.mai\Desktop\Makememad/Dictionary')
sys.path.append('C:\Users\sanh.mai\Desktop\Makememad/RedBox')
sys.path.append('C:\Users\sanh.mai\Desktop\Makememad/YellowBox')
sys.path.append('C:\Users\sanh.mai\Desktop\Makememad/GreenBox')
id_exit = 1
id_start = 2
id_name = 3
id_dictionary = 4
id_redBox = 5
id_yellowBox = 6
id_greenBox = 6
id_done = 8
id_question = 9
id_clock = 10
color = wx.Colour(178, 187, 216, 22)


class DialogStart(wx.Dialog):

    def __init__(self, *args, **kw):
        super(DialogStart, self).__init__(*args, **kw)

        self.InitUI()
        self.SetSize((500, 205))
        self.Centre()
        self.SetTitle("Sentence")

    def InitUI(self):

        panel = wx.Panel(self)
        vbox = wx.BoxSizer(wx.VERTICAL)
        hbox = wx.BoxSizer(wx.HORIZONTAL)
        img = wx.Image("C:\Users\sanh.mai\Desktop\Makememad/Dictionary/river.jpg")
        self.imageCtrl = wx.Bitmap(img)

        vbox.Add(0, 50)
        vbox.Add(wx.StaticText(self, label='What is the sentence for this picture?'), flag=wx.LEFT, border=20)
        textctrl = wx.TextCtrl(self, size=(300, 20), style=wx.TE_PROCESS_ENTER)
        vbox.Add(textctrl, flag=wx.LEFT, border=20)

        hbox.Add(wx.StaticBitmap(self, bitmap=self.imageCtrl), flag=wx.LEFT | wx.TOP, border=10)
        hbox.Add(vbox)
        self.SetSizer(hbox)
        textctrl.Bind(wx.EVT_TEXT_ENTER, self.OnTextEnter)

    def OnTextEnter(self, e):
        print e.GetString()
        self.Destroy()


class makememad(wx.Frame):

    def __init__(self, parent, title, style):  # main create
        super(makememad, self).__init__(parent, title=title, style=style,
                                        size=(800, 600))
        self.Maximize()
        self.Show()
        self.InitUI()

    def InitUI(self):
        menubar = wx.MenuBar()
        pnl = wx.Panel(self)
        vbox = wx.BoxSizer(wx.VERTICAL)
        vbox1 = wx.BoxSizer(wx.VERTICAL)
        vbox2 = wx.BoxSizer(wx.VERTICAL)
        vbox3 = wx.BoxSizer(wx.VERTICAL)
        vbox4 = wx.BoxSizer(wx.VERTICAL)
        hbox = wx.BoxSizer(wx.HORIZONTAL)

        # Create main panel with DictionaryListCtrl, RedBoxListCtrl, YellowBoxListCtrl, GreenBoxListCtrl
        self.listctrl = wx.ListCtrl(pnl, id=-1, style=wx.LC_REPORT)
        self.listctrl.InsertColumn(0, "Word", width=55)
        self.listctrl.InsertColumn(1, "Sentence", width=400)
        for i in Dictionary:
            self.listctrl.Append([i[0], i[1]])

        self.listctrl.Bind(wx.EVT_LIST_ITEM_ACTIVATED, self.OnDictionary)

        self.listctrl2 = wx.ListCtrl(pnl, id=-1, style=wx.LC_REPORT)
        self.listctrl2.InsertColumn(0, "Word", width=55)
        self.listctrl2.InsertColumn(1, "Sentence", width=400)
        for i in RedBox:
            self.listctrl2.Append([i[0], i[1]])

        self.listctrl3 = wx.ListCtrl(pnl, id=-1, style=wx.LC_REPORT)
        self.listctrl3.InsertColumn(0, "Word", width=55)
        self.listctrl3.InsertColumn(1, "Sentence", width=400)
        for i in YellowBox:
            self.listctrl3.Append([i[0], i[1]])

        self.listctrl4 = wx.ListCtrl(pnl, id=-1, style=wx.LC_REPORT)
        self.listctrl4.InsertColumn(0, "Word", width=55)
        self.listctrl4.InsertColumn(1, "Sentence", width=400)
        for i in GreenBox:
            self.listctrl4.Append([i[0], i[1]])

        vbox1.Add(10, 5)
        vbox1.Add(wx.StaticBitmap(pnl, 100, wx.Bitmap('dictionary.png')), flag=wx.LEFT, border=10)
        vbox1.Add(wx.StaticText(pnl, label='Dictionary'), flag=wx.LEFT, border=10)
        vbox1.Add(self.listctrl, flag=wx.LEFT | wx.RIGHT | wx.BOTTOM, border=10, proportion=1)

        vbox2.Add(10, 5)
        vbox2.Add(wx.StaticBitmap(pnl, 100, wx.Bitmap('RedBox.png')), flag=wx.LEFT, border=10)
        vbox2.Add(wx.StaticText(pnl, label='RedBox'), flag=wx.LEFT, border=10)
        vbox2.Add(self.listctrl2, flag=wx.LEFT | wx.RIGHT | wx.BOTTOM, border=10, proportion=1)

        vbox3.Add(10, 5)
        vbox3.Add(wx.StaticBitmap(pnl, 100, wx.Bitmap('YellowBox.png')), flag=wx.LEFT, border=10)
        vbox3.Add(wx.StaticText(pnl, label='YellowBox'), flag=wx.LEFT, border=10)
        vbox3.Add(self.listctrl3, flag=wx.LEFT | wx.RIGHT | wx.BOTTOM, border=10, proportion=1)

        vbox4.Add(10, 5)
        vbox4.Add(wx.StaticBitmap(pnl, 100, wx.Bitmap('GreenBox.png')), flag=wx.LEFT, border=10)
        vbox4.Add(wx.StaticText(pnl, label='GreenBox'), flag=wx.LEFT, border=10)
        vbox4.Add(self.listctrl4, flag=wx.LEFT | wx.RIGHT | wx.BOTTOM, border=10, proportion=1)

        hbox.Add(vbox1, 1, wx.EXPAND)
        hbox.Add(vbox2, 1, wx.EXPAND)
        hbox.Add(vbox3, 1, wx.EXPAND)
        hbox.Add(vbox4, 1, wx.EXPAND)
        vbox.Add(hbox, 1, wx.EXPAND)

        # Create Toolbar
        self.toolbar = self.CreateToolBar(style=wx.TB_TEXT | wx.TB_FLAT | wx.TB_HORIZONTAL)
        self.toolbar.SetBackgroundColour(color)
        self.toolbar.AddTool(id_exit, 'Exit', wx.Bitmap('exit.png'), shortHelp="Exit App")
        self.toolbar.EnableTool(id_exit, False)
        self.toolbar.AddTool(id_start, 'Start', wx.Bitmap('run.png'), shortHelp="Start Learning")
        self.toolbar.AddTool(id_name, 'Name', wx.Bitmap('name.png'), shortHelp="What's your name")
        self.toolbar.AddTool(id_question, 'How to use', wx.Bitmap('question.png'), shortHelp="How to use this app")
        self.toolbar.AddTool(id_clock, 'Repeat', wx.Bitmap('clock.png'), shortHelp="Repeat in time")
        self.toolbar.AddTool(id_clock, 'Number', wx.Bitmap('run.png'), shortHelp="Number of new word per day")
        self.toolbar.SetBackgroundColour(color)
        self.toolbar.AddTool(id_dictionary, 'Dictionary', wx.Bitmap('dictionary.png'), shortHelp="New Word")
        self.toolbar.AddTool(id_redBox, 'RedBox', wx.Bitmap('RedBox.png'), shortHelp="Box 1")
        self.toolbar.AddTool(id_yellowBox, 'YellowBox', wx.Bitmap('yellowBox.png'), shortHelp="Box 2")
        self.toolbar.AddTool(id_greenBox, 'GreenBox', wx.Bitmap('GreenBox.png'), shortHelp="Box 3")
        self.toolbar.AddTool(id_done, 'Done', wx.Bitmap('done.png'), shortHelp="Already Learned")
        self.toolbar.Realize()

        # Create Statusbar
        self.statusbar = self.CreateStatusBar()
        self.statusbar.SetStatusText('Ready')

        # Menubar Append Menu`s
        self.SetMenuBar(menubar)
        self.Show(True)
        self.SetSizer(vbox)

        # Event Start.
        self.Bind(wx.EVT_TOOL, self.OnStart, id=id_start)

        # Event Quit.
        self.Bind(wx.EVT_TOOL, self.OnQuit, id=id_exit)

    def OnQuit(self, e):
        self.Close()

    def OnStart(self, e):
        self.toolbar.EnableTool(id_exit, True)
        diaeng = DialogStart(None, title="Give me the sentence")
        diaeng.ShowModal()
        diaeng.Destroy()

    def OnDictionary(self, e):
        u = e.GetText()

        # Delete from Dictionary and refresh the Dictionary
        connDictionary = sqlite3.connect("Dictionary.db")
        cDictionary = connDictionary.cursor()
        cDictionary.execute("SELECT * FROM englishdata WHERE word = '{}'".format(u))
        data = cDictionary.fetchone()
        print data
        cDictionary.execute("DELETE FROM englishdata WHERE word = '{}'".format(u))
        connDictionary.commit()
        cDictionary.execute("SELECT * FROM englishdata")
        Dictionary = cDictionary.fetchall()
        self.listctrl.DeleteAllItems()
        for i in Dictionary:
            self.listctrl.Append([i[0], i[1]])
        connDictionary.close()

        # Add to RedBox and refresh the RedBox
        connRedBox = sqlite3.connect("RedBox.db")
        cRedBox = connRedBox.cursor()
        cRedBox.execute("INSERT INTO englishdata VALUES (?,?)", (data))
        connRedBox.commit()
        cRedBox.execute("SELECT * FROM englishdata")
        RedBox = cRedBox.fetchall()
        self.listctrl2.DeleteAllItems()
        for i in RedBox:
            self.listctrl2.Append([i[0], i[1]])
        connRedBox.close()

    def OnButton(self, e):
        id = e.GetId()
        name = self.listimage[id][0: -4]


if __name__ == '__main__':
    app = wx.App()
    makememad(None, title='Make me Mad', style=wx.ICONIZE)
    app.MainLoop()
