# az ablak méretének beállítása
from kivy.config import Config
Config.set("graphics", "width", "1280")
Config.set("graphics", "height", "720")
# az ablak átméretezhetőségének tiltása=0, engedélyezése=1
Config.set("graphics", "resizable", "0")

from kivy.app import App
# from kivy.uix.widget import Widget
from kivy.uix.label import Label


# alap widget felépítése
class TesztApp(App):
    def build(self):
       # return widget()
# cimke a widget helyén
        return Label(text="ELSŐ CIMKE",
# betű magasság,  dőlt, vastag és a szín megadása. Az utolsó paraméter az átlátszóság
                     font_size=60,italic=True, bold=True,color=(0.7,0.5,0.2,1))



# a fent felépített widget futtatása
TesztApp().run()
