# az ablak méretének beállítása
from kivy.config import Config

Config.set("graphics", "width", "1280")
Config.set("graphics", "height", "720")
# az ablak átméretezhetőségének tiltása=0, engedélyezése=1
Config.set("graphics", "resizable", "0")

from kivy.app import App
from kivy.uix.widget import Widget
# from kivy.uix.label import Label
from kivy.uix.button import Button


class AlapWidget(Widget):
    def __init__(self):
        super().__init__()
        gomb1 = Button(text="GOMB 1", size=(100, 50), poz=(0, 0),id="gomb1")

        gomb1.bind(on_press=self.hello_gomb)
        self.add_widget(gomb1)

    def hello_gomb(self,instance):
        print("HELLO")


# alap widget felépítése
class TesztApp(App):
    def build(self):
        return AlapWidget()

    # return widget()


# cimke a widget helyén
# return Label(text="ELSŐ CIMKE",
# betű magasság,  dőlt, vastag és a szín megadása. Az utolsó paraméter az átlátszóság
#   font_size=60,italic=True, bold=True,color=(0.7,0.5,0.2,1))


# a fent felépített widget futtatása
TesztApp().run()
