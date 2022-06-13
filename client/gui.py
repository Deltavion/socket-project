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

        self.ids.clients_rv.data = [{"text": "void"} for i in range(10)]
        self.ids.msg_rv.data = [{"text": "Bienvenue sur le terminal SocketAPP", "color": (0, 0, 0, 1)}]


class SocketApp(App):
    def build(self):
        return View()


if __name__ == '__main__':
    SocketApp().run()