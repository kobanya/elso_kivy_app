# az ablak méretének beállítása
from kivy.config import  Config
Config.set("graphics","width", "1280")
Config.set("graphics","height", "720")
# az ablak átméretezhetőségének tiltása=0, engedélyezése=1
Config.set("graphics","resizable", "0")

from kivy.app import App
from kivy.uix.widget import Widget

# alap widget felépítése
class TesztApp(App):
    def build(self):
        return Widget()

# a fent felépített widget futtatása
TesztApp().run()



