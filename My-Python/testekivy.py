from kivy.app import App
from kivy.uix.boxlayout import BoxLayout

class Ola(BoxLayout):
    pass

class Testekivy(App):
    def build(self):
        return Ola()
Testekivy().run()
