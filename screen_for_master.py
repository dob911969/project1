from kivymd.app import MDApp
from kivy.lang.builder import Builder
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.factory import Factory
from kivy.core.window import Window
from kivymd.uix.screen import MDScreen
from kivymd.uix.boxlayout import MDBoxLayout
from kivy.metrics import dp
from kivymd.uix.label import MDLabel
from kivy.uix.image import Image
from kivymd.uix.button import MDRaisedButton
from kivy.uix.scrollview import ScrollView
from kivy.uix.gridlayout import GridLayout  # Import GridLayout
from master_floor import FloorScreen
from master_room import RoomScreen
from master_roomcategory import roomcategoryScreen
from master_roomtariff import TariffScreen
from master_roomnature import RoomnatureScreen
from master_status import statusScreen
from master_idcard import IdtypeScreen



# Master Screen Class
class MasterScreen(MDScreen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        Window.size = (900, 900)  # Window size for the Master screen

        # Main Layout with vertical orientation
        main_layout = MDBoxLayout(orientation="vertical", padding=10, spacing=10)

        # Title layout with the school logo, label, and wall clock
        title_layout = MDBoxLayout(orientation="horizontal", size_hint_y=None, height=dp(70), spacing=10, padding=10)
        title_layout.md_bg_color = (0.9, 0.9, 0.9, 1)  # Light gray background

        # Logo image
        logo = Image(source="C:/KIVYMD_PROJECTS/DHARMAGATPUR_SCHOOL/logo and signature/school_logo.png",
                     size_hint=(None, None), size=(70, 70))
        
        # Title Label
        title_label = MDLabel(text="Create Master",
                              halign="center",
                              valign="center",
                              font_style="H5",
                              bold=True)

       
        # Add widgets to the title layout
        title_layout.add_widget(logo)
        title_layout.add_widget(title_label)
       

        # Add the title layout to the main layout
        main_layout.add_widget(title_layout)

       
        
        # Create a GridLayout for the buttons
        button_layout = GridLayout(cols=1, padding=10, spacing=10, size_hint_y=None, height=900)

        
        # Buttons for navigating to different screens
        button_layout.add_widget(MDRaisedButton(text="Floor", on_press=self.switch_to_floor))
        button_layout.add_widget(MDRaisedButton(text="Room", on_press=self.switch_to_room))
        button_layout.add_widget(MDRaisedButton(text="Roomcategory", on_press=self.switch_to_roomcategory))
        button_layout.add_widget(MDRaisedButton(text="Roomtariff", on_press=self.switch_to_roomtariff))
        button_layout.add_widget(MDRaisedButton(text="Roomnature", on_press=self.switch_to_roomnature))
        button_layout.add_widget(MDRaisedButton(text="Status", on_press=self.switch_to_status))
        button_layout.add_widget(MDRaisedButton(text="Idtype", on_press=self.switch_to_idtype))
        
        

        # Add the scrollable content to the main layout
        main_layout.add_widget(button_layout)

        # Add the main layout to the screen
        self.add_widget(main_layout)

    # Navigation functions
    def switch_to_floor(self, instance):
        self.manager.current = "Floor"
    def switch_to_room(self, instance):
        self.manager.current = "Room"
    def switch_to_roomcategory(self, instance):
        self.manager.current = "Roomcategory"
    def switch_to_roomtariff(self, instance):
        self.manager.current = "Roomtariff"
    def switch_to_roomnature(self, instance):
        self.manager.current = "Roomnature"
    def switch_to_status(self, instance):
        self.manager.current = "Status"
    def switch_to_idtype(self, instance):
        self.manager.current = "Idtype"

    
    
# KV Language String
KV = '''
ScreenManager:
    MasterScreen:
    FloorScreen:
    RoomScreen:
    roomcategoryScreen:
    TariffScreen:
    RoomnatureScreen:
    statusScreen:
    IdtypeScreen:

    
   

<MasterScreen>:
    name: "Master"

<FloorScreen>:
    name: "Floor"
    MDBoxLayout:
        orientation: "vertical"
        MDRaisedButton:
            text: "Back to Master"
            on_press: root.manager.current = "Master"
<RoomScreen>:
    name: "Room"
    MDBoxLayout:
        orientation: "vertical"
        MDRaisedButton:
            text: "Back to Master"
            on_press: root.manager.current = "Master"
<roomcategoryScreen>:
    name: "Roomcategory"
    MDBoxLayout:
        orientation: "vertical"
        MDRaisedButton:
            text: "Back to Master"
            on_press: root.manager.current = "Master"
<TariffScreen>:
    name: "Roomtariff"
    MDBoxLayout:
        orientation: "vertical"
        MDRaisedButton:
            text: "Back to Master"
            on_press: root.manager.current = "Master"
<RoomnatureScreen>:
    name: "Roomnature"
    MDBoxLayout:
        orientation: "vertical"
        MDRaisedButton:
            text: "Back to Master"
            on_press: root.manager.current = "Master"
<statusScreen>:
    name: "Status"
    MDBoxLayout:
        orientation: "vertical"
        MDRaisedButton:
            text: "Back to Master"
            on_press: root.manager.current = "Master"
<IdtypeScreen>:
    name: "Idtype"
    MDBoxLayout:
        orientation: "vertical"
        MDRaisedButton:
            text: "Back to Master"
            on_press: root.manager.current = "Master"




'''

# Master App Class to load the KV layout
class MasterApp(MDApp):
    def build(self):
        self.theme_cls.theme_style = "Light"
        self.theme_cls.primary_palette = "Blue"
        return Builder.load_string(KV)

if __name__ == '__main__':
    MasterApp().run()