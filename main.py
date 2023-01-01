
from kivy.app import App
from kivy.uix.widget import Widget

# alap widget felépítése
class TesztApp(App):
    def build(self):
        return Widget()

# a fent felépített widget futtatása
TesztApp().run()



