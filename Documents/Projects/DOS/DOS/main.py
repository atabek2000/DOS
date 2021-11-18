from kivymd.app import MDApp
from kivy.lang.builder import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.core.window import Window
from kivy.properties import *

import time
from threading import Timer
import pyttsx3

speak_engine = pyttsx3.init()
# def speak():
#     what = 'Hello'
#     print( what )
#     speak_engine.say( what )
#     speak_engine.runAndWait()
    
#     speak_engine.stop()

Window.size = (400,600)

class AuthScreen(Screen):
    pass

class MainScreen(Screen):
    pass

class NavigationLayout(Screen):
    pass

# Create the screen manager
sm = ScreenManager()
sm.add_widget(AuthScreen(name='menu'))
sm.add_widget(MainScreen(name='profile'))
# sm.add_widget(UploadScreen(name='upload'))
# sm.add_widget(ContentNavigationDrawer(name='cndrawer'))


class DemoApp(MDApp):
    
    def checkTextField(self, instance):
        print('Hello world')

    def build(self):
        screen = Builder.load_file('kivy.kv')
        
        return screen
DemoApp().run()
