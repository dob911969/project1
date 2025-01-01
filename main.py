from kivy.lang import Builder
from kivy.core.window import Window
from kivy.uix.image import Image
from kivy.uix.scrollview import ScrollView
from kivy.uix.gridlayout import GridLayout
from kivymd.app import MDApp
from kivymd.uix.screen import MDScreen
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.button import MDRaisedButton
from kivymd.uix.label import MDLabel
from kivy.clock import Clock
from kivy.lang import Builder
from screen_for_master import MasterScreen
from master_floor import FloorScreen
from master_room import RoomScreen
from master_roomcategory import roomcategoryScreen
from master_roomtariff import TariffScreen
from master_roomnature import RoomnatureScreen
from master_status import statusScreen
from roomstatus import RoomstatusScreen
from master_idcard import IdtypeScreen
from customer import CustomerScreen
from checkinn import CheckinnScreen



    
class HomeScreen(MDScreen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        Window.size = (900, 790)  # Set window size
        
        # Main layout
        main_layout = MDBoxLayout(orientation="vertical", spacing=10)

        # Title section
        title_layout = MDBoxLayout(orientation="horizontal", size_hint_y=None, height=80, padding=10)
        title_layout.md_bg_color = (0.2, 0.2, 0.8, 1)  # Dark blue background

        logo = Image(source="logo and signature/school_logo.png", size_hint=(None, None), size=(70, 70))
        title_label = MDLabel(
            text="Hotel-RADISION",
            font_style="H4",
            bold=True,
            theme_text_color="Custom",
            text_color=(1, 1, 0, 1),  # Yellow text
            halign="center",
            valign="center",
        )
        
        
        title_layout.add_widget(logo)
        title_layout.add_widget(title_label)
        

        # Add title to main layout
        main_layout.add_widget(title_layout)

        
       

        # Dashboard image
        dashboard_image = Image(source="logo and signature/school_logo.png", allow_stretch=True, keep_ratio=False)
        dashboard_frame = MDBoxLayout(size_hint=(1, None), height=900, padding=10)
        dashboard_frame.add_widget(dashboard_image)
        main_layout.add_widget(dashboard_frame)

        # Left menu
        menu_layout = MDBoxLayout(orientation="vertical", size_hint=(None, 1), width=250, md_bg_color=(0.3, 0.3, 0.3, 1))
        menu_title = MDLabel(
            text="Menu",
            font_style="H5",
            bold=True,
            theme_text_color="Custom",
            text_color=(1, 1, 0, 1),  # Yellow text
            halign="center",
            size_hint_y=None,
            height=50,
        )
        menu_layout.add_widget(menu_title)

        buttons = [
            ("Master", self.switch_to_master),
            ("Roomstatus", self.switch_to_roomstatus),
            ("Customer", self.switch_to_customer),
            ("Checkinn", self.switch_to_checkinn),
            #("Fee Collection", self.switch_to_feecollection),
            #("Mark Entry", self.switch_to_markentry),
            #("Mark Sheet", self.switch_to_marksheet),
           
            
        ]
        for text, callback in buttons:
            menu_layout.add_widget(
                MDRaisedButton(
                    text=text,
                    md_bg_color=(0.2, 0.2, 0.8, 1),
                    size_hint_y=None,
                    height=50,
                    theme_text_color="Custom",
                    text_color=(1, 1, 1, 1),
                    on_press=callback,
                )
            )

        # Add layouts to the screen
        main_box = MDBoxLayout()
        main_box.add_widget(menu_layout)
        main_box.add_widget(main_layout)
        self.add_widget(main_box)

      


    def switch_to_master(self, instance):
        print(f"self.manager: {self.manager}")
        self.manager.current = "Create_Master"

    def switch_to_roomstatus(self, instance):
        self.manager.current = "Roomstatus"

    def switch_to_customer(self, instance):
        self.manager.current = "Customer"

    def switch_to_checkinn(self, instance):
        self.manager.current = "Checkinn"
    #def switch_to_feecollection(self, instance):
        #self.manager.current = "Feecollection"

    #def switch_to_markentry(self, instance):
        #self.manager.current = "Markentry"
    #def switch_to_marksheet(self, instance):
        #self.manager.current = "Marksheet"


# KV Language String
KV = '''
ScreenManager:
    HomeScreen:
    MasterScreen:
    FloorScreen:
    RoomScreen:
    roomcategoryScreen:
    TariffScreen:
    RoomnatureScreen:
    statusScreen:
    RoomstatusScreen:
    IdtypeScreen:
    CustomerScreen:
    CheckinnScreen:

    

    
    

<HomeScreen>:
    name: "Home"


<MasterScreen>:
    name: "Create_Master"
    MDBoxLayout:
        orientation: "vertical"
        MDRaisedButton:
            text: "Back to Home"
            on_press: root.manager.current = "Home"
<FloorScreen>
    name: "Floor"
    MDBoxLayout:
        orientation: "vertical"
        MDRaisedButton:
            text: "Back to Home"
            on_press: root.manager.current = "Home"
<RoomScreen>
    name: "Room"
    MDBoxLayout:
        orientation: "vertical"
        MDRaisedButton:
            text: "Back to Home"
            on_press: root.manager.current = "Home"
<roomcategoryScreen>
    name: "Roomcategory"
    MDBoxLayout:
        orientation: "vertical"
        MDRaisedButton:
            text: "Back to Home"
            on_press: root.manager.current = "Home"
<TariffScreen>
    name: "Roomtariff"
    MDBoxLayout:
        orientation: "vertical"
        MDRaisedButton:
            text: "Back to Home"
            on_press: root.manager.current = "Home"
<RoomnatureScreen>
    name: "Roomnature"
    MDBoxLayout:
        orientation: "vertical"
        MDRaisedButton:
            text: "Back to Home"
            on_press: root.manager.current = "Home"
<statusScreen>
    name: "Status"
    MDBoxLayout:
        orientation: "vertical"
        MDRaisedButton:
            text: "Back to Home"
            on_press: root.manager.current = "Home"
<RoomstatusScreen>
    name: "Roomstatus"
    MDBoxLayout:
        orientation: "vertical"
        MDRaisedButton:
            text: "Back to Home"
            on_press: root.manager.current = "Home"
<IdtypeScreen>
    name: "Idtype"
    MDBoxLayout:
        orientation: "vertical"
        MDRaisedButton:
            text: "Back to Home"
            on_press: root.manager.current = "Home"
<CustomerScreen>
    name: "Customer"
    MDBoxLayout:
        orientation: "vertical"
        MDRaisedButton:
            text: "Back to Home"
            on_press: root.manager.current = "Home"
<CheckinnScreen>
    name: "Checkinn"
    MDBoxLayout:
        orientation: "vertical"
        MDRaisedButton:
            text: "Back to Home"
            on_press: root.manager.current = "Home"

'''
        

        


        

class DharmagatpurApp(MDApp):
    def build(self):
        Builder.load_string(KV)
        screen_manager = Builder.load_string(KV)
        return screen_manager


if __name__ == "__main__":
    DharmagatpurApp().run()