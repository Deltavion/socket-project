import kivy
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout

import socket
kivy.require("2.0.0")


class View(BoxLayout):
    def __init__(self, **kwargs):
        super(View, self).__init__()
        self.username.text = socket.gethostname()
        self.ip.text = socket.gethostbyname(socket.gethostname())


class PacketApp(App):
    def build(self):
        return View()


packetApp = PacketApp()
packetApp.run()
