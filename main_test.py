from kivy.app import App
from kivy.uix.button import Button
from kivy.config import Config
from kivy.uix.floatlayout import FloatLayout
from kivy.lang import Builder
import time



class MyApp(App):
    def build(self):

        fl = FloatLayout()
        fl.add_widget(Button(text = "capture",
        font_size = 100,
        on_press = self.btn_press,
        background_color = [1,0,0,1],
        background_normal = "",
        size_hint = (1,.5)))
        return fl
    def btn_press(self,instance):
        instance.text = "capture again"




if __name__ == '__main__':
    MyApp().run()
