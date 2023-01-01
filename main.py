from kivy.config import Config
Config.set("graphics", "width", "1280")
Config.set("graphics", "height", "720")
Config.set("graphics", "resizable", "0")

from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
#from kivy.lang import Builder


#Builder.load_file("teszt.kv")
class AlapWidget(FloatLayout):
    pass

# alap widget felépítése
class TesztApp(App):
    def build(self):
        return AlapWidget()

# a fent felépített widget futtatása
TesztApp().run()
