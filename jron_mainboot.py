from kivy.lang import Builder
from kivy.properties import ObjectProperty

from kivymd.app import MDApp
from kivymd.uix.boxlayout import MDBoxLayout
from kivy.core.window import Window
Window.size = 1280, 1000

KV = '''
<ContentNavigationDrawer>

    ScrollView:

        MDList:
        
        
        
        
        
# Added ListItems in Menu Bar Screen







            OneLineListItem:
                text: "Wi-Fi"
                on_press:
                    root.nav_drawer.set_state("close")
                    root.screen_manager.current = "scr 1"

            OneLineListItem:
                text: "Location"
                on_press:
                    root.nav_drawer.set_state("close")
                    root.screen_manager.current = "scr 2"
            OneLineListItem:
                text: "Bluetooth"
                on_press:
                    root.nav_drawer.set_state("close")
                    root.screen_manager.current = "scr 3"
            OneLineListItem:
                text: ""
                on_press:
                    root.nav_drawer.set_state("close")
                     
            OneLineListItem:
                text: "About US"
                on_press:
                    root.nav_drawer.set_state("close")
                    root.screen_manager.current = "scr 5"
            OneLineListItem:
                text: "GitHub"
                on_press:
                    root.nav_drawer.set_state("close")
                    root.screen_manager.current = "scr 6"
            OneLineListItem:
                text: ""
                on_press:
                    root.nav_drawer.set_state("close")
                    root.screen_manager.current = "scr 7"
            OneLineListItem:
                text: "JRON Solo"
                on_press:
                    root.nav_drawer.set_state("close")
                    root.screen_manager.current = "scr 8"
            OneLineListItem:
                text: "Background"

                on_press:
                    root.nav_drawer.set_state("close")
                    root.screen_manager.current = "scr 9"
            OneLineListItem:
                text: ""
                on_press:
                    root.nav_drawer.set_state("close")
                    root.screen_manager.current = "scr 10"
            OneLineListItem:
                text: "VPN"
                on_press:

                on_press:
                    root.nav_drawer.set_state("close")
                    root.screen_manager.current = "scr 11"
            OneLineListItem:
                text: "Users"
                on_press:
                    root.nav_drawer.set_state("close")
                    root.screen_manager.current = "scr 12"


            OneLineListItem:
                text: "Storage"
                on_press:
                    root.nav_drawer.set_state("close")
                    root.screen_manager.current = "scr 13"
            OneLineListItem:
                text: "USB/DVD"
                on_press:
                    root.nav_drawer.set_state("close")
                    root.screen_manager.current = "scr 14"
                    
                    
#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>#
                                                       # SCREEN
#<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<#
            

MDScreen:

    MDToolbar:
        id: toolbar
        pos_hint: {"top": 1}
        elevation: 10
        title: "JRON Software"
        left_action_items: [["menu", lambda x: nav_drawer.set_state("open")]]

    MDNavigationLayout:
        x: toolbar.height

        ScreenManager:
            id: screen_manager

            MDScreen:
                name: "scr 1"


                 
                MDLabel:
                    text: "Security Type:                                                 Status:"
                    font_name: 'mon2.ttf'
                    pos_hint: {"center_x": .937, "center_y": .75}
                MDLabel:
                    text: "Name"
                    font_name: 'mon1.ttf'
                    pos_hint: {"center_x": .75, "center_y": .75}
                MDLabel:
                    text: "Visible Networks:"
                    font_name: 'mon2.ttf'
                    pos_hint: {"center_x": .935, "center_y": .85}
                MDIconButton:
                    icon: "wifi"
                    pos_hint: {"center_x": .8, "center_y": .5}
                MDIconButton:
                    icon: "wifi"
                    pos_hint: {"center_x": .8, "center_y": .6}
                MDLabel:
                    text: "iPhone                                                      WWP4                                                                 Online"
                    font_name: 'mon1.ttf'
                    pos_hint: {"center_x": .5, "center_y": .59}
                    size_hint: 0.5,.1
                    canvas.before:
                        Color:
                            rgb: rgba(0, 42, 42, 1)
                        RoundedRectangle:
                            size: self.size
                            pos: self.pos
                            radius: [6]
                MDLabel:
                    text: "TP-Link240Vireless                            SEC40                                                                 Online"
                    font_name: 'mon1.ttf'
                    pos_hint: {"center_x": .5, "center_y": .5}
                    size_hint: 0.5,.1
                    canvas.before:
                        Color:
                            rgb: rgba(0, 42, 42, 1)
                        RoundedRectangle:
                            size: self.size
                            pos: self.pos
                            radius: [6]
                    MDIconButton:
                        icon: 'wifi'
                        pos_hint: {"center_x": .5, "center_y": .59}
                Button:
                    text:'Connect'
                    size_hint: .2,.1
                    background_color: 1,1,1,0
                    pos_hint: {"center_x": .5, "center_y": .28}
                    canvas.before:
                        Color:
                            rgb: rgba(149,118,256,256)
                        RoundedRectangle:
                            size: self.size
                            pos: self.pos
                            radius: [6]




#######################################111111111111111111111111##################################
            MDScreen:
                name: "scr 3"

                MDLabel:
                    text: "Screen 2"
                    halign: "center"
                    font_name: "mon1.ttf"
            MDScreen:
                name: "scr 4"

                MDLabel:
                    text: "Screen 2"
                    halign: "center"
                    font_name: "mon1.ttf"
            MDScreen:
                name: "scr 5"

                MDLabel:
                    text: "Screen 2"
                    halign: "center"
                    font_name: "mon1.ttf"
            MDScreen:
                name: "scr 6"
                MDLabel:
                    text: "Screen 2"
                    halign: "center"
                    font_name: "mon1.ttf"
            MDScreen:
                name: "scr 7"

                MDLabel:
                    text: "Screen 2"
                    halign: "center"
                    font_name: "mon1.ttf"
            MDScreen:
                name: "scr 8"

                MDLabel:
                    text: "Screen 2"
                    halign: "center"
                    font_name: "mon1.ttf"
            MDScreen:
                name: "scr 9"

                MDLabel:
                    text: "Screen 2"
                    halign: "center"
                    font_name: "mon1.ttf"
            MDScreen:
                name: "scr 10"

                MDLabel:
                    text: "Screen 2"
                    halign: "center"
                    font_name: "mon1.ttf"
            MDScreen:
                name: "scr 11"

                MDLabel:
                    text: "Screen 2"
                    halign: "center"
                    font_name: "mon1.ttf"
            MDScreen:
                name: "scr 12"

                MDLabel:
                    text: "Screen 2"
                    halign: "center"
                    font_name: "mon1.ttf"
            
###################################################
            MDScreen:
                name: "scr 2"

                MDLabel:
                    text: "Screen 2"
                    halign: "center"
                    font_name: "mon1.ttf"

        MDNavigationDrawer:
            id: nav_drawer

            ContentNavigationDrawer:
                screen_manager: screen_manager
                nav_drawer: nav_drawer
'''


class ContentNavigationDrawer(MDBoxLayout):
    screen_manager = ObjectProperty()
    nav_drawer = ObjectProperty()


class TestNavigationDrawer(MDApp):
    def build(self):
        self.theme_cls.theme_style = 'Dark'
        return Builder.load_string(KV)


TestNavigationDrawer().run()
