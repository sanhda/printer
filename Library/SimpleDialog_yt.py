import clr

import wpf
import os

from System.Windows import Application, Window
import System


class SimpleDialog(Window):
    TextReturn = ""

    def __init__(self, xaml_file_name, title, labelname):
        wpf.LoadComponent(self, xaml_file_name)
        self.title = title
        self.labelname = labelname
        self.Title = self.title
        self.label.Content = labelname
        global TextReturn
        self.TextReturn = "Cancel"

    def OnCancel(self, sender, args):
        self.TextReturn = "Cancel"
        self.Close()

    def OnOK(self, sender, args):
        global TextReturn
        self.TextReturn = self.textbox.Text
        self.Close()
