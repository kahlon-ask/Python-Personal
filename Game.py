from kivy.app import App
from kivy.lang import Builder
from kivy.properties import StringProperty
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.clock import Clock
from kivy.uix.screenmanager import ScreenManager, Screen
import datetime
import time

kv = """
ScreenManager:
    PlayingScreen:
    Upgrade_Window:

<PlayingScreen>:
    name: "PlayScreen"
    BoxLayout:
        orientation: 'vertical'
        MenuBar:
            size_hint: 1, 0.1
        MainGame:

<Upgrade_Window>:
    name: "Upgrade_Window"
    BoxLayout:
        orientation: 'vertical'
        MenuBar:
            size_hint: 1, 0.1
        Upgrade_Options:

<Upgrade_Options>:
    name: "Upgrade"
    BoxLayout:
        Label:
            id: test123
            text: app.todaystr         # access todaystr

<MenuBar@BoxLayout>:
    Button:
        text: "Main Game"
        on_release: app.root.current = "PlayScreen"
    Button:
        text: "Upgrades"
        on_release: app.root.current = "Upgrade_Window"

<MainGame>: 
    # name: "MainGame"
    cols: 4
    rows: 8
    # orientation: "lr-tb"
    Label:
        text : app.todaystr  # access todaystr
    Button:
        text: "Start"
        size_hint: 1, 1
        on_press : root.start()
"""


class PlayingScreen(Screen):
    pass


class Upgrade_Window(Screen):
    pass


class MainGame(GridLayout):
    today = datetime.datetime(2009, 1, 1)
    # todaystr = StringProperty("1/1/2009")
    started = False
    daylength = 0.01

    def _timer(self, dt):
        self._update("Time")

    def _update(self, why):
        if not self.started:
            self.started = True
            Clock.schedule_interval(self._timer, self.daylength)
        if why == "Time":
            self.today = self.today + datetime.timedelta(days=1)
            self.timer = time.time()
        app = App.get_running_app()  # get to app in python
        app.todaystr = str(self.today.month) + "/" + str(self.today.day) + "/" + str(self.today.year)

    def start(self):
        self._update("null")


class Upgrade_Options(BoxLayout):
    pass


class MainGameApp(App):
    todaystr = StringProperty("1/1/2009") 

    def build(self):
        return Builder.load_string(kv)


MainGameApp().run()