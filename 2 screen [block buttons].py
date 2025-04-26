from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.clock import Clock


class SecondScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        layout = BoxLayout(orientation='vertical', padding=[20, 20, 20, 20], spacing=10)

        # Текст
        layout.add_widget(Label(
            text="Виміряйте пульс за 15 секунд.",
            font_size='18sp',
            size_hint_y=None,
            height=40
        ))
        layout.add_widget(Label(
            text="Результат запишіть у відповідне поле.",
            font_size='18sp',
            size_hint_y=None,
            height=40
        ))

        input_layout = BoxLayout(orientation='horizontal', spacing=10, size_hint_y=None, height=50)
        input_layout.add_widget(Label(
            text="Введіть результат:",
            font_size='18sp',
            size_hint_x=None,
            width=150
        ))
        self.text_input = TextInput(
            text="",
            multiline=False,
            font_size='18sp',
            size_hint_x=0.7
        )
        input_layout.add_widget(self.text_input)
        layout.add_widget(input_layout)

        # "Почати"
        start_button = Button(
            text="Почати",
            font_size='18sp',
            size_hint_y=None,
            height=50
        )
        start_button.bind(on_press=self.on_start)
        layout.add_widget(start_button)

        self.add_widget(layout)

    def on_start(self, instance):
        self.text_input.disabled = True
        instance.disabled = True
        Clock.schedule_once(self.enable_widgets, 15)
        print(f"Результат: {self.text_input.text}")

    def enable_widgets(self, dt):
        self.text_input.disabled = False
        self.children[0].children[-1].disabled = False


class MyApp(App):
    def build(self):
        screen_manager = ScreenManager()
        screen_manager.add_widget(SecondScreen(name='second'))
        return screen_manager


if __name__ == '__main__':
    MyApp().run()