from kivy.kivy import App
from kivy.kivy import Label

class TestApp(App):
    def build(self):
        return Label(text='Olá Mundo')

TestApp().run()

