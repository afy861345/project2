from kivy import *
from kivymd import *
from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.core.window import Window

Window.size=(300,500)
nav_helper="""
Screen:
    MDNavigationLayout:
        ScreenManager:
            Screen:
                BoxLayout:
                    orientation:"vertical"
                    MDTopAppBar:
                        title:"ali"
                        left_action_items:[["menu",lambda x:nav_drawer.set_state("toggle")]]
                    Widget:
        MDNavigationDrawer:
            id:nav_drawer
            BoxLayout:
                orientation:"vertical"
                Image:
                    source:"rownaz.png"
                MDLabel:
                    text:"ali"
                    font_style:"Subtitle1"
                    size_hint_y:None
                    height:self.texture_size[1]
                MDLabel:
                    text:"ali@gmail.com"
                    font_style:"Caption"
                    size_hint_y:None
                    height:self.texture_size[1]
                ScrollView:
                    MDList:
                        OneLineIconListItem:
                            text:"profile"
                            IconLeftWidget:
                                icon:"login.ping"
                        OneLineListItem:
                            text:"userinfo" 
                        OneLineListItem:
                            text:"upload" 
                        OneLineListItem:
                            text:"download" 
                        OneLineListItem:
                            text:"log out"  

"""

class Kivo(MDApp):
    def build(self):
        screen=Builder.load_string(nav_helper)
        return screen
 
if __name__ == "__main__":
    Kivo().run()