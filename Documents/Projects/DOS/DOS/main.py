from kivymd.app import MDApp
from kivy.lang.builder import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.core.window import Window
from kivy.properties import *
from firebase import firebase

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
user_name = '';
class AuthScreen(Screen):
    def do_reg(self, name, email):
        fbase = firebase.FirebaseApplication('https://doss-6eb8c-default-rtdb.firebaseio.com/', None)
        data = {
            'Name': name,
            'Email': email
        }
        fbase.post('doss-6eb8c-default-rtdb/Doss_users', data)
        global user_name
        user_name = name
        self.manager.current = 'profile'
    def do_skip(self):
        self.manager.current = 'profile'

class MainScreen(Screen):
    def speak(self):
        global user_name
        what = 'Hello'
        print( what )
        speak_engine.say( 'Привет ' + user_name )
        speak_engine.runAndWait()
        speak_engine.stop()
    

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
