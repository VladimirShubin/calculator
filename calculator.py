import kivy
from kivy.app import App
from kivy.core.window import Window
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout
Window.size = (640, 480)
Window.clearcolor = (19/255, 21/255, 22/255, 1)
Window.title = 'App'

class MyApp(App):
    def update_label(self):
        self.label.text = self.formula

    def add_number(self, instance):
        if self.formula == "0":
            self.formula = ''

        self.formula += str(instance.text)
        self.update_label()

    def add_operation (self, instance):

        self.formula += str(instance.text)
        self.update_label()

    def calc_result (self, instance):
        self.label.text = str(eval(self.label.text))
        self.formula = '0'

    def build(self):
        self.formula = '0'
        box_layout = BoxLayout(orientation='vertical')
        grid_layout = GridLayout(rows=6, cols=4, size_hint_x=None, size_hint_y=None, width=640, height=350, padding=[0,0,160,0])
        self.label = Label(text='0', halign='right', valign='center', size_hint=(1.02, 1.5), font_size=32, text_size=(320, 640 * .5))
        box_layout.add_widget(self.label)

        grid_layout.add_widget(Button(text='7', on_press = self.add_number, background_color=(3/255, 132/255, 154/255, 1), font_size=32))
        grid_layout.add_widget(Button(text='8', on_press = self.add_number, background_color=(3/255, 132/255, 154/255, 1), font_size=32))
        grid_layout.add_widget(Button(text='9', on_press = self.add_number, background_color=(3/255, 132/255, 154/255, 1), font_size=32))
        grid_layout.add_widget(Button(text='*', on_press = self.add_operation, background_color=(3/255, 132/255, 154/255, 1), font_size=32))

        grid_layout.add_widget(Button(text='4', on_press = self.add_number, background_color=(3/255, 132/255, 154/255, 1), font_size=32))
        grid_layout.add_widget(Button(text='5', on_press = self.add_number, background_color=(3/255, 132/255, 154/255, 1), font_size=32))
        grid_layout.add_widget(Button(text='6', on_press = self.add_number, background_color=(3/255, 132/255, 154/255, 1), font_size=32))
        grid_layout.add_widget(Button(text='-', on_press = self.add_operation, background_color=(3/255, 132/255, 154/255, 1), font_size=32))

        grid_layout.add_widget(Button(text='1', on_press = self.add_number, background_color=(3/255, 132/255, 154/255, 1), font_size=32))
        grid_layout.add_widget(Button(text='2', on_press = self.add_number, background_color=(3/255, 132/255, 154/255, 1), font_size=32))
        grid_layout.add_widget(Button(text='3', on_press = self.add_number, background_color=(3/255, 132/255, 154/255, 1), font_size=32))
        grid_layout.add_widget(Button(text='+', on_press = self.add_operation, background_color=(3/255, 132/255, 154/255, 1), font_size=32))

        grid_layout.add_widget(Button(text='/', on_press = self.add_operation, background_color=(3 / 255, 132 / 255, 154 / 255, 1), font_size=32))
        grid_layout.add_widget(Button(text='0', on_press=self.add_number, background_color=(3 / 255, 132 / 255, 154 / 255, 1), font_size=32))
        grid_layout.add_widget(Button(text='.', on_press=self.add_operation, background_color=(3 / 255, 132 / 255, 154 / 255, 1), font_size=32))
        grid_layout.add_widget(Button(text='=', on_press=self.calc_result, background_color=(3 / 255, 132 / 255, 154 / 255, 1), font_size=32))
        box_layout.add_widget(grid_layout)
        return box_layout

if __name__ == '__main__':
    MyApp().run()