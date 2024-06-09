from kivy.app import App
from webview import WebView


class BrowserApp(App):
    def build(self):
        self.browser = WebView('https://math-up.ru',
                               enable_javascript=True,
                               enable_downloads=True,
                               enable_zoom=True)


BrowserApp().run()
