import clr
import wpf
import os
import random
import csv
import re
from System.Windows import Application, Window
import System
import sys
import shutil
import ConfigParser
# File Path
FilePath = os.path.dirname(__file__)
sys.path.append(FilePath)
os.chdir(FilePath)
from Library import SimpleDialog_yt as SPD, SimpleDialog_noTextBox_yt as SPD_notextbox, SimpleDialog_with2label_1image_yt as SPD_2label
from Library import SimpleDialog_1La_1Te_1Im_yt as SPD_1La_1Te_1Im
# List of files
Dictionary_files = os.listdir(r"{}\Dictionary".format(FilePath))
RedBox_files = os.listdir(r"{}\RedBox".format(FilePath))
YellowBox_files = os.listdir(r"{}\YellowBox".format(FilePath))
GreenBox_files = os.listdir(r"{}\GreenBox".format(FilePath))


def GetItem(path, listview):
    """Prepare List View Items
    """
    listview.Items.Clear()
    for i in os.listdir(path):
        StackPanel = System.Windows.Controls.StackPanel()
        Image = System.Windows.Controls.Image()
        Image.Source = System.Windows.Media.Imaging.BitmapImage(System.Uri(r"{}\{}".format(path, i), System.UriKind.Relative))
        Image.Margin = System.Windows.Thickness(5)
        Image.Height = 150
        Image.Width = 150
        listview.Items.Add(Image)


def Refresh(path1, path2):
    # Refresh Items, delete same items (Cannot move, then copy and refresh)
    for i in os.listdir(path1):
        if i in os.listdir(path2):
            os.chdir(path1)
            os.remove(i)


class MyWindow(Window):
    def __init__(self, xaml_file_name):
        """ Prepare Icon, Refresh Items, Get Items for ListView
        """
        wpf.LoadComponent(self, xaml_file_name)
        self.Image_Source(self.Image_Dictionary, "Dictionary.PNG")
        self.Image_Source(self.Image_RedBox, "RedBox.PNG")
        self.Image_Source(self.Image_YellowBox, "YellowBox.PNG")
        self.Image_Source(self.Image_GreenBox, "GreenBox.PNG")
        self.Image_Source(self.Image_Clock, "Clock.PNG")
        self.Image_Source(self.Image_Done, "Done.PNG")
        self.Image_Source(self.Image_Exit, "Exit.PNG")
        self.Image_Source(self.Image_Name, "Name.PNG")
        self.Image_Source(self.Image_Question, "Question.PNG")
        self.Image_Source(self.Image_Run, "Run.PNG")
        self.Image_Source(self.Image_Number, "Number.PNG")
        self.Image_Source(self.Image_Number, "Number.PNG")
        self.Icon = System.Windows.Media.Imaging.BitmapImage(System.Uri(r"{}\Image\{}".format(FilePath, "Makememad.PNG"), System.UriKind.Relative))
        Refresh(r"{}\Dictionary".format(FilePath), r"{}\RedBox".format(FilePath))
        # Refresh(r"D:\Makememad\RedBox", r"D:\Makememad\YellowBox")
        # Refresh(r"D:\Makememad\YellowBox", r"D:\Makememad\GreenBox")
        self.GetItems()

    def Image_Source(self, source, picturename):
        # Set Icon
        source.Source = System.Windows.Media.Imaging.BitmapImage(System.Uri(r"{}\Image\{}".format(FilePath, picturename), System.UriKind.Relative))

    def GetItems(self):
        # Dictionary Items
        GetItem(r"{}\Dictionary".format(FilePath), self.ListView_Dictionary)
        # RedBox Items
        GetItem(r"{}\RedBox".format(FilePath), self.ListView_RedBox)
        # YellowBox Items
        GetItem(r"{}\YellowBox".format(FilePath), self.ListView_YellowBox)
        # GreenBox Items
        GetItem(r"{}\GreenBox".format(FilePath), self.ListView_GreenBox)

    def OnRun(self, sender, e):
        """ Run method
        """
        os.chdir(FilePath)
        # Read the Name
        parser = ConfigParser.SafeConfigParser()
        parser.read('Information.ini')
        Name = parser.get("Information", "Name")
        RedBox_files = os.listdir(r"{}\RedBox".format(FilePath))
        if len(RedBox_files) >= 3:
            random_number = 3
        else:
            random_number = len(RedBox_files)
        # Random item
        random_items = random.sample(RedBox_files, random_number)
        for random_item in random_items:
            dialog = SPD_1La_1Te_1Im.SimpleDialog("SimpleDialog_1La_1Te_1Im.xaml", "The sentence for this image is :", r"{}\RedBox\{}".format(FilePath, random_item))
            dialog.ShowDialog()
            with open('dictionary.csv') as csvfile:
                reader = csv.reader(csvfile)
                for row in reader:
                    if row[0] == os.path.splitext(random_item)[0]:
                        voca = row[0]
                        sentence = re.sub(r"\W", "", row[1]).upper()
            sentence_input = re.sub(r"\W", "", dialog.TextReturn).upper()
            # Compare input
            if sentence.upper() != sentence_input:
                # Punish for Wrong
                for i in range(10):
                    wrong_dialog = SPD_notextbox.SimpleDialog("SimpleDialog_Wrong.xaml", "UnCorrect", "Hello the World. My name is {} And I am very Stupid".format(Name))
                    wrong_dialog.ShowDialog()
                    # Punish for Liar
                    if wrong_dialog.TextReturn == "Cancel":
                        honest_dialog = SPD_notextbox.SimpleDialog("SimpleDialog_Wrong.xaml", "UnCorrect", "The gift for your liar. Please take it")
                        honest_dialog.ShowDialog()
                        for i in range(5):
                            wrong_dialog = SPD_notextbox.SimpleDialog("SimpleDialog_Wrong.xaml", "UnCorrect", "Hello the World. My name is ... and I am very Stupid")
                            wrong_dialog.ShowDialog()

    def OnDictionary(self, sender, e):
        pass

    def OnGreenBox(self, sender, e):
        pass

    def OnYellowBox(self, sender, e):
        pass

    def OnRedBox(self, sender, e):
        pass

    def OnDone(self, sender, e):
        pass

    def OnClock(self, sender, e):
        pass

    def OnName(self, sender, e):
        os.chdir(FilePath)
        # Show Dialog
        dialog_name = SPD.SimpleDialog("SimpleDialog.xaml", "Information", "Enter your Name")
        dialog_name.ShowDialog()
        try:
            parser.remove_section("Information")
        except:
            pass
        # Write to the ini file for Information
        parser = ConfigParser.SafeConfigParser()
        parser.read('Information.ini')
        # Add Section
        try:
            parser.add_section("Information")
        except:
            pass
        # Save Setting
        parser.set("Information", "Name", dialog_name.TextReturn)
        with open('Information.ini', 'w') as configfile:
            parser.write(configfile)

    def OnNumber(self, sender, e):
        pass

    def OnQuestion(self, sender, e):
        pass

    def OnExit(self, sender, e):
        self.Close()

    def OnButtonDictionary(self, sender, e):
        """ Move Item to RedBox, then Delete in Dictionary
        """
        if sender.SelectedItem:
            index = sender.SelectedIndex
            os.chdir(FilePath)
            # Show Dialog Asking
            dialog = SPD_notextbox.SimpleDialog("SimpleDialog_noTextBox.xaml", "Learn this Picture", "Do you want to learn this picture?")
            dialog.ShowDialog()
            # Looking in CSV file for Voca
            if dialog.TextReturn == "OK":
                with open('dictionary.csv') as csvfile:
                    reader = csv.reader(csvfile)
                    for row in reader:
                        if row[0] == os.path.split(os.path.splitext(str(sender.SelectedItem.Source))[0])[1]:
                            voca = row[0]
                            sentence = row[1]
                # Show Dialog Voca
                dialog2 = SPD_2label.SimpleDialog("SimpleDialog_with2label_1image.xaml", "Vocabulary: {}".format(voca), "Sentence: {}".format(sentence), str(sender.SelectedItem.Source))
                dialog2.ShowDialog()
                # Copy to the RedBox
                Destination = str(sender.SelectedItem.Source).replace("Dictionary", "RedBox")
                shutil.copy(str(sender.SelectedItem.Source), Destination)
                # Remove Item in Dictionary
                sender.Items.RemoveAt(index)
            # Get Item for RedBox again
            GetItem(r"{}\RedBox".format(FilePath), self.ListView_RedBox)

    def OnButtonRedBox(self, sender, e):
        print sender.SelectedItem

    def OnButtonYellowBox(self, sender, e):
        print sender.SelectedItem

    def OnButtonGreenBox(self, sender, e):
        print sender.SelectedItem


if __name__ == '__main__':
    MyWindow('English_Voca.xaml').ShowDialog()
