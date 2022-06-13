import kivy
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.recycleview import RecycleView

kivy.require("2.0.0")


class RV(RecycleView):
    def __init__(self, **kwargs):
        super(RV, self).__init__(**kwargs)


class View(BoxLayout):
    def __init__(self, **kwargs):
        super(View, self).__init__(**kwargs)

        # msgs = RV()
        # msgs.data = [{"text": "Bienvenue sur le terminal SocketAPP"}]

        # clients = RV()
        # clients.data = [{"text": "void"} for i in range(10)]

        # syntax : self.ids.<id>
        self.ids.clients_rv.data = [{"text": "void"} for i in range(10)]
        self.ids.msg_rv.data = [{"text": "Bienvenue sur le terminal SocketAPP"}]


class SocketApp(App):
    def build(self):
        self.mainView = View()
        return self.mainView


if __name__ == '__main__':
    SocketApp().run()