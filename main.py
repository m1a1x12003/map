import os
# 強制使用 ANGLE (DirectX) 後端，避免 OpenGL 錯誤
os.environ['KIVY_GL_BACKEND'] = 'angle_sdl2'

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
import webbrowser

class TestApp(App):
    def build(self):
        layout = BoxLayout(orientation='vertical')
        self.input = TextInput(hint_text="請輸入地址，用空格或換行分隔", multiline=True)
        btn = Button(text="執行導航", on_press=self.run_navigation)

        layout.add_widget(self.input)
        layout.add_widget(btn)
        return layout

    def run_navigation(self, instance):
        addresses = self.input.text.replace("\n", " ").split()
        if not addresses:
            return

        # 起點先用假座標測試 (台北車站)
        origin = "25.0478,121.5170"
        destination = addresses[-1]
        waypoints = "|".join(addresses[1:-1])

        maps_url = (
            f"https://www.google.com/maps/dir/?api=1"
            f"&origin={origin}"
            f"&destination={destination}"
            f"&waypoints={waypoints}"
            f"&travelmode=driving"
        )
        print("導航網址：", maps_url)
        webbrowser.open(maps_url)

if __name__ == "__main__":
    TestApp().run()
