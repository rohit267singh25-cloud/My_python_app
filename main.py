from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button

class Calculator(GridLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.cols = 4

        self.display = TextInput(multiline=False, readonly=True, font_size=32)
        self.add_widget(self.display)

        buttons = [
            "7","8","9","/",
            "4","5","6","*",
            "1","2","3","-",
            "0",".","=","+",
            "C"
        ]

        for b in buttons:
            btn = Button(text=b, font_size=24)
            btn.bind(on_press=self.on_button)
            self.add_widget(btn)

    def on_button(self, instance):
        text = instance.text

        if text == "C":
            self.display.text = ""
        elif text == "=":
            try:
                self.display.text = str(eval(self.display.text))
            except:
                self.display.text = "Error"
        else:
            self.display.text += text

class CalculatorApp(App):
    def build(self):
        return Calculator()

CalculatorApp().run()
