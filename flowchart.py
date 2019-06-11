from kivy.app import App
from kivy.lang import Builder
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.boxlayout import BoxLayout

from kivy.uix.widget import Widget

from kivy.uix.image import Image
from kivy.uix.bubble import Bubble
from kivy.uix.scatter import Scatter
lis = [[2,1],[3,1],[4,2]]
class cut_copy_paste(Bubble):
    pass

class root(BoxLayout):
    count = 1
    def __init__(self, flowchart_list, **kwargs):
        super(root, self).__init__(**kwargs)
        self.flowchart_list = flowchart_list
        self.ids.lbl.text = "22222222"
    def btn(self):
        self.kp = cut_copy_paste()
        self.count+=1
        if self.count%2==0:
            self.add_widget(self.kp)
        else:
            self.remove_widget(self.children[0])
        print(self.flowchart_list)

class MainApp(App):
    def __init__(self, flowchart_list, **kwargs):
        super(MainApp, self).__init__(**kwargs)
        self.flowchart_list = flowchart_list

    def build(self):
        k = root(self.flowchart_list)
        
        return k

# if __name__ == '__main__':
#     MainApp().run()
