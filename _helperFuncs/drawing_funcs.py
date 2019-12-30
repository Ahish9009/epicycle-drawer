# ignore Kivy's log
import os
os.environ["KIVY_NO_CONSOLELOG"] = "1"
# kivy for input
from kivy.config import Config
Config.set('graphics', 'fullscreen', '0')
Config.set('graphics', 'width', '800')
Config.set('graphics', 'height', '800')
from kivy.interactive import InteractiveLauncher
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.graphics import Line

pointsTouched = []

class DrawInput(Widget):

    def on_touch_down(self, touch):    
        
        global pointsTouched # not a good method, have to change
        with self.canvas: 
            touch.ud["line"] = Line(points=(touch.x, touch.y))
            pointsTouched += [int(touch.x/2)+int(touch.y/2)*1j]

    def on_touch_move(self, touch):
        
        global pointsTouched
        touch.ud["line"].points += (touch.x, touch.y)
        pointsTouched += [int(touch.x/2) + int(touch.y/2)*1j]
        
class drawingBoard(App):

    def build(self):
        return DrawInput()

