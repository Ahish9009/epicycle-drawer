# ignore Kivy's log
import os
os.environ["KIVY_NO_CONSOLELOG"] = "1"
# kivy for input
from kivy.config import Config
Config.set('graphics', 'fullscreen', '0')
Config.set('graphics', 'width', '600')
Config.set('graphics', 'height', '600')
from kivy.interactive import InteractiveLauncher
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.graphics import Line

points_touched = []

class drawInput(Widget):

    def on_touch_down(self, touch):    
        
        global points_touched # not a good method, have to change
        with self.canvas: 
            touch.ud["line"] = Line(points=(touch.x, touch.y))
            points_touched += [int(touch.x/2)+int(touch.y/2)*1j]

    def on_touch_move(self, touch):
        
        global points_touched
        touch.ud["line"].points += (touch.x, touch.y)
        points_touched += [int(touch.x/2) + int(touch.y/2)*1j]
        
class drawingBoard(App):

    def build(self):
        return drawInput()

