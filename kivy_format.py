from kivymd.app import MDApp
from kivy.metrics import dp
from kivy.core.window import Window
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.button import MDRaisedButton
from kivymd.uix.textfield import MDTextField
from kivymd.uix.label import MDLabel
from kivymd.uix.gridlayout import MDGridLayout
from kivymd.uix.dialog import MDDialog
from kivymd.uix.datatables import MDDataTable
from kivymd.uix.screen import MDScreen
from kivymd.uix.button import MDRectangleFlatButton
import sqlite3
from kivymd.uix.menu import MDDropdownMenu
import random
from kivymd.uix.filemanager import MDFileManager
import os
from datetime import datetime
from kivy.uix.image import Image

class kivyformatScreen(MDScreen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        Window.size = (900, 600)
        #self.theme_cls.theme_style = "Light"
        # primary_palette=['Red', 'Pink', 'Purple', 'DeepPurple', 'Indigo', 'Blue', 'LightBlue', 'Cyan', 'Teal', 'Green', 'LightGreen', 'Lime', 
        # 'Yellow', 'Amber', 'Orange', 'DeepOrange', 'Brown', 'Gray', 'BlueGray']
        #self.theme_cls.primary_palette = "Blue"
        #background color code
        #window title
        #color theme

        # Root layout
       
        main_layout = MDBoxLayout(orientation="vertical", padding=10, spacing=10)

        #title layout

        # Title layout with the school logo, label, and wall clock
        title_layout = MDBoxLayout(orientation="horizontal", size_hint_y=None, height=dp(70), spacing=10, padding=10)
        title_layout.md_bg_color = (0.9, 0.9, 0.9, 1)  # Light gray background

        logo = Image(source="C:/KIVYMD_PROJECTS/DHARMAGATPUR_SCHOOL/logo and signature/school_logo.png",
                     size_hint=(None, None), size=(70, 70))
        title_label = MDLabel(text="School Management System",
                              halign="center",
                              valign="center",
                              font_style="H5",
                              bold=True)

        

        title_layout.add_widget(logo)
        title_layout.add_widget(title_label)
       
        main_layout.add_widget(title_layout)

        #Input Field Grid Layout
        grid_layout=MDGridLayout(cols=9, size_hint_y=None, height=dp(200), padding=10)
        grid_layout.md_bg_color = (0.95, 0.95, 1, 1)  # Light blue background

        self.subjectid_input = MDTextField(hint_text="Sample ID", disabled=True, size_hint_x=None, width=200)
        grid_layout.add_widget(self.subjectid_input)
        self.classno_input = MDTextField(hint_text="Sample No", size_hint_x=None, width=200)
        grid_layout.add_widget(self.classno_input)
        self.subjectname_input = MDTextField(hint_text="Sample Name", size_hint_x=None, width=200)
        grid_layout.add_widget(self.subjectname_input)

        main_layout.add_widget(grid_layout)

        #Button Layout
        btn_layout=MDBoxLayout(size_hint=(1, None), height=dp(50), spacing=10)
        btn_layout.md_bg_color = (1, 0.95, 0.85, 1)  # Light peach background

        add_button = MDRaisedButton(text="Add")
        btn_layout.add_widget(add_button)
        update_button = MDRaisedButton(text="Update")
        btn_layout.add_widget(update_button)
        delete_button = MDRaisedButton(text="Delete")
        btn_layout.add_widget(delete_button)
        search_button = MDRaisedButton(text="Search")
        btn_layout.add_widget(search_button)
        reset_button = MDRaisedButton(text="Reset")
        btn_layout.add_widget(reset_button)
        
        main_layout.add_widget(btn_layout)

        #Data Table for Displaying Records
        table_layout = MDBoxLayout( padding=10)
        table_layout.md_bg_color = (0.9, 1, 0.9, 1)  # Light green background
        self.table = MDDataTable(
            size_hint=(1, None),
            height=dp(420),
            column_data=[
                ("SID", dp(10)),
                ("Reg_No", dp(20)),
                ("Reg_Date", dp(20)),
                ("Name", dp(25)),
                ("Gender", dp(20)),
                ("DOB", dp(20)),
                ("ClassNO", dp(20)),
                ("Reg_Fee", dp(20)),
                ("School_Fee", dp(20)),
                ("Comp_Fee", dp(20)),
                ("Lib_Fee", dp(20)),
                ("Father", dp(20)),
                ("Mother", dp(20)),
                ("Contact", dp(20)),
                ("Address", dp(30)),
                ("Status", dp(20)),
            ],
            row_data=[],
            use_pagination=True,
            rows_num=10
        )
        #self.table.bind(on_row_press=self.on_row_select)
        main_layout.add_widget(self.table)
        #self.table.bind(on_row_press=self.on_row_select)
        main_layout.add_widget(table_layout)


        self.add_widget(main_layout)
        #Calling of Functions-1
        #Calling of Functions-2
        #Calling of Functions-3
        #Calling of Functions-4
        #Calling of Functions-5
        #Calling of Functions-6
        
    
    #============For Data Base , Autoid , Auto Registration No , Auto Current Date========================
    
    def initialize_database(self):#For Database Datatype
        pass
    def generate_employee_id(self):#For genrating auto id
        pass
    def generate_employee_registration(self):#For Genrating auto Registration No
        pass
    def generate_registration_date(self):# For Genrating auto Current Date
        pass

    #============For Uploading Image==================================================

    def open_file_manager(self, *args):# in case of image upload
        pass
    def select_path(self, path):#incase of image upload
        pass
    def exit_manager(self, *args):#incase of image upload
        pass

    #============For Populating Data from Other Table==================================

    def populate_class(self, instance):# For Populating data of anothe table in current table
        pass
    def class_menu_callback(self, selected_class):# For Populating data of anothe table in current table
        pass

    #============For Adding/Saving Records and Loading Records to Table and Selection of Row from table==================================

    def save_record(self, *args):# in case of saving data
        pass
    def load_records_to_table(self):# For displaying record in table or treeview
        pass
    def on_row_select(self, instance_table, instance_row):# For displaying record in table or treeview
        pass
    #============For Updating Records==================================
    def update_record(self, *args):# For update record
        pass
    #============For Deleting Records==================================

    def delete_record(self, *args):#For deleting Record
        pass
    #============For Searcing Records==================================
    def search_records(self, *args):#For Searching Records 
        pass
    def load_filtered_data_for_search(self, rows):# For Searching Record
        pass

    #============For Clearing Fields after adding or saving==================================

    def clear_fields(self, *args):#For Clearing Fields 
        pass
    #============For setting Fields after adding or saving==================================

    def reset_fields(self, *args):#For Clearing Fields 
        pass
    # ================= Dialog Function =================
    def show_confirmation_dialog(self, message):
        dialog = MDDialog(
            text=message,
            buttons=[MDRectangleFlatButton(text="OK", on_release=lambda x: dialog.dismiss())]
        )
        dialog.open()

class kivyformatApp(MDApp):
    def build(self):
        self.theme_cls.theme_style = "Light"
        self.theme_cls.primary_palette = "Blue"
        return kivyformatScreen()

    

if __name__ == "__main__":
    kivyformatApp().run()

