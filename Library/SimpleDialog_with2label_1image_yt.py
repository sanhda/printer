import clr

import wpf
import os

from System.Windows import Application, Window
import System
FilePath = os.path.dirname(os.path.dirname(__file__))


class SimpleDialog(Window):

    def __init__(self, xaml_file_name, label, textblock, imagepath):
        wpf.LoadComponent(self, xaml_file_name)
        self.Icon = System.Windows.Media.Imaging.BitmapImage(System.Uri(r"{}\Image\{}".format(FilePath, "Makememad.PNG"), System.UriKind.Relative))
        self.label.Content = label
        self.textblock.Text = textblock
        self.image.Source = System.Windows.Media.Imaging.BitmapImage(System.Uri(imagepath, System.UriKind.Relative))
        self.image.Height = 150
        self.image.Width = 150
        global TextReturn
        self.TextReTurn = "Cancel"

    def OnOK(self, sender, args):
        self.Close()
