import clr

import wpf
import os

from System.Windows import Application, Window
import System
FilePath = os.path.dirname(os.path.dirname(__file__))


class SimpleDialog(Window):
    TextReturn = " "

    def __init__(self, xaml_file_name, title, labelname):
        self.Icon = System.Windows.Media.Imaging.BitmapImage(System.Uri(r"{}\Image\{}".format(FilePath, "Makememad.PNG"), System.UriKind.Relative))
        wpf.LoadComponent(self, xaml_file_name)
        self.title = title
        self.labelname = labelname
        self.Title = self.title
        self.label.Content = labelname
        global TextReturn
        self.TextReturn = "Cancel"

    def OnCancel(self, sender, args):
        global TextReturn
        self.TextReturn = "Cancel"
        self.Close()

    def OnOK(self, sender, args):
        global TextReturn
        self.TextReturn = "OK"
        self.Close()
