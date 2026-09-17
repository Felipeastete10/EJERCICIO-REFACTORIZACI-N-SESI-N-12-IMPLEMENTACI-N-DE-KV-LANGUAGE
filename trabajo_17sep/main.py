from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import StringProperty

class CalculatorLayout(BoxLayout):
    display_text = StringProperty('')

    def on_button_press(self, button_text: str) -> None:
        if button_text == 'C':
            self.display_text = ''
        elif button_text == '=':
            try:
                result = eval(self.display_text)
                if isinstance(result, float) and result.is_integer():
                    result = int(result)
                self.display_text = str(result)
            except Exception:
                self.display_text = 'Error'
        else:
            if self.display_text == 'Error':
                self.display_text = ''
            self.display_text += button_text


class CalculadoraApp(App):
    def build(self):
        return CalculatorLayout()

if __name__ == '__main__':
    CalculadoraApp().run()