from kivy.lang import Builder

from kivymd.app import MDApp

KV = '''
<MagicButton@MagicBehavior+MDRectangleFlatButton>


MDFloatLayout:

    MagicButton:
        text: "WOBBLE EFFECT"
        on_release: self.wobble()
        pos_hint: {"center_x": .5, "center_y": .3}

    
'''


class Example(MDApp):
    def build(self):
        return Builder.load_string(KV)


Example().run()