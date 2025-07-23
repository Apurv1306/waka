from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.clock import mainthread
import threading
import os

# Ensure working directory is writable for known_faces
if not os.path.exists('known_faces'):
    os.makedirs('known_faces')

# Import (or exec) your Flask app here
import python-app  # Assumes your main Flask app is named 'python-app.py' (rename if needed)

class MainLayout(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.orientation = 'vertical'
        self.server_thread = None
        self.flask_running = False

        self.button = Button(text="Start Flask Server", font_size=24)
        self.button.bind(on_press=self.toggle_flask)
        self.add_widget(self.button)

    @mainthread
    def update_button_text(self, text):
        self.button.text = text

    def toggle_flask(self, instance):
        if not self.flask_running:
            self.server_thread = threading.Thread(
                target=python-app.app.run,
                kwargs={'host': '0.0.0.0', 'port': 5000, 'debug': False, 'threaded': True, 'use_reloader': False},
                daemon=True
            )
            self.server_thread.start()
            self.flask_running = True
            self.update_button_text("Stop Flask Server")
        else:
            # Stopping Flask gracefully on Android requires custom logic
            self.flask_running = False
            self.update_button_text("Start Flask Server")

class FaceApp(App):
    def build(self):
        return MainLayout()

if __name__ == "__main__":
    FaceApp().run()
