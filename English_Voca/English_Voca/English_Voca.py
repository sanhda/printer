import wpf

from System.Windows import Application, Window

class MyWindow(Window):
    def __init__(self):
        wpf.LoadComponent(self, 'English_Voca.xaml')
    
    def OnRun(self, sender, e):
        pass
    
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
        pass
    
    def OnNumber(self, sender, e):
        pass
    
    def OnQuestion(self, sender, e):
        pass
    
    def OnExit(self, sender, e):
        pass
    
    def OnButtonDictionary(self, sender, e):
        pass
    
    OnButtonRedBoxdef OnButtonGreenBox(self, sender, e):
        pass
    
    def OnButtonGreenBox(self, sender, e):
        pass
    
    def OnButtonRedBox(self, sender, e):
        pass
    
    def OnButtonGreenBox(self, sender, e):
        pass
    
    def OnButtonGreenBox(self, sender, e):
        pass
    
    def OnButtonYellowBox(self, sender, e):
        pass
    

if __name__ == '__main__':
    Application().Run(MyWindow())
