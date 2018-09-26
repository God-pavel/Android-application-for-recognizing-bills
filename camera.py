from kivy.uix.boxlayout import BoxLayout
from kivy.app import App
from kivy.uix.camera import Camera
from kivy.uix.button import Button



class CameraApp(App):
    def build(self):
        bl = BoxLayout(orientation='vertical')
        # bl1 = BoxLayout(background_color = [1,0,0,1])
        # btn = Button(pos=(0,0),size_hint = (.5,1),on_press=self.btn_press)
        bl.add_widget(Camera(play=True))
        bl.add_widget(Button(pos=(0,0),size_hint = (1,.5),on_press=self.btn_press,text = 'capture'))
        return bl
    def btn_press(self,instance):
        instance.text = 'capture again'



if __name__ == '__main__':
    CameraApp().run()
