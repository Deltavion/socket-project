import kivy
from kivy.app import App
import socket
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.recycleview import RecycleView

kivy.require("2.0.0")


class RV(RecycleView):
    def __init__(self, **kwargs):
        super(RV, self).__init__(**kwargs)


class View(BoxLayout):
    def __init__(self, **kwargs):
        super(View, self).__init__(**kwargs)
        self.cols = 2


        self.username.text = socket.gethostname()
        self.ip.text = socket.gethostbyname(socket.gethostname())


        #msgs = RV()
        #msgs.data = [{"text": "Bienvenue sur le terminal SocketAPP"}]
        #self.add_widget(msgs)

        self.clients = RV()
        self.clients.data = [{"text": "void"} for i in range(10)]

        self.add_widget(self.clients)

    def refresh_client(self):
        self.clients.refresh_from_data(data=[{"text": "coucou"}])


class SocketApp(App):
    def build(self):
        self.mainView = View()
        return self.mainView

    def refresh_client(self):
        self.mainView.refresh_client()



if __name__ == '__main__':
    SocketApp().run()