from kivy.config import Config
Config.set('graphics', 'resizable', False)

import kivy
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.popup import Popup
from kivy.uix.image import Image
from kivy.properties import StringProperty, ObjectProperty
from kivy.uix.filechooser import FileChooserListView
from kivy.uix.video import Video
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.boxlayout import BoxLayout

import tkinter as tk
from tkinter import filedialog

from sub_maker import *
from video_maker import *


class ScreenManagement(ScreenManager):
    def __init__(self, **kwargs):
        super(ScreenManagement, self).__init__(**kwargs)
        self.add_widget(EnterAffirmations(name="enter_affirmations"))
        self.add_widget(LoadingScreen(name="loading_screen"))
        self.add_widget(SublimalPlayer(name="sublimal_player"))


class EnterAffirmations(Screen):
    def __init__(self, **kwargs):
        super(EnterAffirmations, self).__init__(**kwargs)

        self.cols = 2

        self.add_widget(Label(text="Title", size_hint = (None, None), size=(40, 50), pos=(200, 550)))
        self.title = TextInput(multiline = False, size_hint = (None, None), size=(500, 100), pos=(400, 500))
        self.add_widget(self.title)

        self.add_widget(Label(text="Affirmations", size_hint = (None, None), size=(100, 50), pos=(200, 300)))
        self.affirmations = TextInput(multiline = True, size_hint = (None, None), size=(500, 250), pos=(400, 200))
        self.add_widget(self.affirmations)

        self.btn1 = Button(text="Start", size=(100, 50), size_hint = (None, None), pos=(0, 0))
        self.btn1.bind(on_press=self.start)
        self.add_widget(self.btn1)

    def start(self, event):
        if (len(self.title.text) == 0) or (len(self.affirmations.text) == 0) or (len(self.title.text) > 20):
            btn3 = Button(text='OK', size=(100, 50), size_hint = (None, None))
            popup = Popup(title='Invalid arguments', content=btn3, auto_dismiss=False, size=(200, 200), size_hint = (None, None))
            btn3.bind(on_press=popup.dismiss)
            popup.open()

        else:
            app = App.get_running_app()

            app.TITLE = self.title.text
            app.AFFIRMATIONS = self.affirmations.text

            app.IMGPATH = str(self.get_imagepath())

            if (app.IMGPATH == ''):
                btn3 = Button(text='OK', size=(100, 50), size_hint = (None, None))
                popup = Popup(title='Please choose a valid file', content=btn3, auto_dismiss=False,  size=(200, 200), size_hint = (None, None))
                btn3.bind(on_press=popup.dismiss)
                popup.open()

            app.AUDIOPATH = str(self.get_audiopath())
            if (app.AUDIOPATH == ''):
                btn3 = Button(text='OK', size=(100, 50), size_hint = (None, None))
                popup = Popup(title='Please choose a valid file', content=btn3, auto_dismiss=False, size=(200, 200), size_hint = (None, None))
                btn3.bind(on_press=popup.dismiss)
                popup.open()

            else:
                self.manager.current = "loading_screen"


    @staticmethod
    def get_imagepath():
        root = tk.Tk()
        root.withdraw()

        return(filedialog.askopenfilename(title='Select an image', filetypes=[
                    ("Image", "*.jpeg"),
                    ("Image", "*.png"),
                    ("Image", "*.jpg"),
                ]))
    
    @staticmethod
    def get_audiopath():
        root = tk.Tk()
        root.withdraw()

        return(filedialog.askopenfilename(title='Select an audio', filetypes=[
                    ("Audio", "*.wav"),
                    ("Audio", "*.mp3"),
                ]))

# This part causes an error whenever you click anywhere on the window.
# Idk how to fix it.
class LoadingScreen(GridLayout, Screen):
    def __init__(self, **kwargs):
        super(LoadingScreen, self).__init__(**kwargs)
        self.rows = 2

        self.add_widget(Label(text='Loading, please do not click anywhere and wait.'))

        self.on_enter
    
    def on_enter(self):
        app = App.get_running_app()
        sub_creator(app.TITLE, app.AFFIRMATIONS, app.AUDIOPATH)

        if(video_creator(app.TITLE, app.IMGPATH) == 'complete'):
            self.manager.current = "sublimal_player"



class SublimalPlayer(GridLayout, Screen):
    def __init__(self, **kwargs):
        super(SublimalPlayer, self).__init__(**kwargs)
        self.rows = 4

        self.on_enter

    def on_enter(self):
        app = App.get_running_app()

        title = app.TITLE

        self.btnPlay = Button(text="Play", size=(100, 50), size_hint = (None, None))
        self.btnPlay.bind(on_press=self.play)
        
        self.btnPause = Button(text="Pause", size=(100, 50), size_hint = (None, None))
        self.btnPause.bind(on_press=self.pause)

        self.btnExit = Button(text="Exit", size=(100, 50), size_hint = (None, None))
        self.btnExit.bind(on_press=self.exit)

        self.video = Video(source='subliminals/videos/' + title + '.mp4')
        self.video.state='play'
        self.video.options = {'eos': 'loop'}
        self.video.allow_stretch=True

        self.add_widget(self.video)

        self.add_widget(self.btnPlay)
        self.add_widget(self.btnPause)
        self.add_widget(self.btnExit)


    def play(self, event):
        self.video.state = 'play'
        
    def pause(self, event):
        self.video.state = 'pause'

    def exit(self, event):
        self.video.state = 'stop'
        self.manager.current = 'enter_affirmations'


class MyApp(App):
    TITLE = StringProperty('')
    AFFIRMATIONS = StringProperty('')
    IMGPATH = StringProperty('')
    AUDIOPATH = StringProperty('')

    def build(self):
        self.title = 'Subliminally GUI'
        self.icon = 'lib/.assets/icon.png'
        return ScreenManagement()

if __name__ == '__main__':
    MyApp().run()

