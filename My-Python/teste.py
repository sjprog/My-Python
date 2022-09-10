from kivy.app import App
from kivy.uix.button import Button

class TestApp(App):
    def build(self):
        return Button(text='Hello World')

TestApp().run()

layout = BoxLayout(padding=10)
button = Button(text='My first button')
layout.add_widget(button)