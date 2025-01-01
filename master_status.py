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

class statusScreen(MDScreen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        Window.size = (900, 600)
       
        main_layout = MDBoxLayout(orientation="vertical", padding=10, spacing=10)

      
        # Title layout with the school logo, label, and wall clock
        title_layout = MDBoxLayout(orientation="horizontal", size_hint_y=None, height=dp(70), spacing=10, padding=10)
        title_layout.md_bg_color = (0.9, 0.9, 0.9, 1)  # Light gray background

        logo = Image(source="C:\KIVYMD_PROJECTS\HOTEL_RADISION\logo and signature\school_logo.png",
                     size_hint=(None, None), size=(70, 70))
        title_label = MDLabel(text="Master-Status",
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

        self.statusid_input = MDTextField(hint_text="Status ID", disabled=True, size_hint_x=None, width=200)
        grid_layout.add_widget(self.statusid_input)
        self.status_input = MDTextField(hint_text="Status", size_hint_x=None, width=200)
        grid_layout.add_widget(self.status_input)
        

        main_layout.add_widget(grid_layout)

        #Button Layout
        btn_layout=MDBoxLayout(size_hint=(1, None), height=dp(50), spacing=10)
        btn_layout.md_bg_color = (1, 0.95, 0.85, 1)  # Light peach background

        add_button = MDRaisedButton(text="Add",on_release=self.save_status)
        btn_layout.add_widget(add_button)
        update_button = MDRaisedButton(text="Update",on_release=self.update_record)
        btn_layout.add_widget(update_button)
        delete_button = MDRaisedButton(text="Delete",on_release=self.delete_record)
        btn_layout.add_widget(delete_button)
        search_button = MDRaisedButton(text="Search")
        btn_layout.add_widget(search_button)
        reset_button = MDRaisedButton(text="Reset",on_release=self.reset_fields)
        btn_layout.add_widget(reset_button)
        
        main_layout.add_widget(btn_layout)

        #Data Table for Displaying Records
        table_layout = MDBoxLayout( padding=10)
        table_layout.md_bg_color = (0.9, 1, 0.9, 1)  # Light green background
        self.table = MDDataTable(
            size_hint=(1, None),
            height=dp(420),
            column_data=[
                ("status_ID", dp(30)),
                ("status", dp(30)),
                
            ],
            row_data=[],
            use_pagination=True,
            rows_num=10
        )
        #self.table.bind(on_row_press=self.on_row_select)
        main_layout.add_widget(self.table)
        self.table.bind(on_row_press=self.on_row_select)
        main_layout.add_widget(table_layout)


        self.add_widget(main_layout)
        self.initialize_database()
        self.generate_statusid()
        self.load_status_records_to_table()
        
        #Calling of Functions-3
        #Calling of Functions-4
        #Calling of Functions-5
        #Calling of Functions-6
        
    
    #============For Data Base , Autoid , Auto Registration No , Auto Current Date========================
    
    def initialize_database(self):
        """Initialize the database and create the class table if it does not exist."""
        conn = sqlite3.connect("radision.db")
        cursor = conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS status (
                statusid INTEGER PRIMARY KEY AUTOINCREMENT,
                status TEXT NOT NULL  
            )
        ''')
        conn.commit()
        conn.close()

    def generate_statusid(self):
        """Generate the next class ID."""
        conn = sqlite3.connect("radision.db")
        cursor = conn.cursor()
        cursor.execute("SELECT MAX(statusid) FROM status")
        last_statusid = cursor.fetchone()[0]
        self.statusid_input.text = str((last_statusid or 0) + 1)
        conn.close()

    #============For Adding/Saving Records and Loading Records to Table and Selection of Row from table==================================

    def save_status(self, *args):
        statusid=self.statusid_input.text.strip()
        status=self.status_input.text.strip()
        
         
        #contact_no = self.contact_no_field.text.strip()
        if not all([statusid,status]):
            self.show_confirmation_dialog("Please fill all fields ")
            return

        conn = sqlite3.connect("radision.db")
        cursor = conn.cursor()
        #statusid,status
        cursor.execute('''
            INSERT INTO status (statusid,status)
            VALUES (?, ?)
        ''', (statusid,status))
        conn.commit()
        conn.close()
        self.show_confirmation_dialog("status saved successfully!")
        self.reset_fields()
        self.load_status_records_to_table()

    def load_status_records_to_table(self):
        """Load records from the database into the table."""
        self.table.row_data = []  # Clear previous data
        conn = sqlite3.connect("radision.db")
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM status ORDER BY statusid DESC")
        rows = cursor.fetchall()
        conn.close()
        self.table.row_data = [(str(r[0]), r[1]) for r in rows]

    def on_row_select(self, instance_table, instance_row):
        """Populate fields when a row is selected."""
        selected_row = instance_row.text
        for row in self.table.row_data:
            if row[0] == selected_row:
                self.statusid_input.text=row[0]
                self.status_input.text=row[1]
                break
    #============For Updating Records==================================
    def update_record(self, *args):
        statusid=self.statusid_input.text.strip()
        status=self.status_input.text.strip()
       

        # Validation: Check for required fields
        if not all([statusid,status]):
            self.show_confirmation_dialog("Please fill all fields!")
            return
        
        try:
            conn = sqlite3.connect("radision.db")
            cursor = conn.cursor()

            # Check if record exists before updating
            cursor.execute('SELECT 1 FROM status WHERE statusid = ?', (statusid,))
            if not cursor.fetchone():
                self.show_confirmation_dialog(f"No record found with status ID {statusid}.")
                conn.close()
                return

            # Update the record
            #statusid , status
            cursor.execute('''
                UPDATE status
                SET status=?
                WHERE statusid = ?
            ''', (status , statusid))
            conn.commit()

            self.show_confirmation_dialog("Employee record updated successfully!")
        except sqlite3.Error as e:
            self.show_confirmation_dialog(f"Database error occurred: {e}")
        finally:
            conn.close()
            self.reset_fields()
            self.load_status_records_to_table()
    #============For Deleting Records==================================

    def delete_record(self, *args):
        statusid=self.statusid_input.text.strip()
        status=self.status_input.text.strip()
        

        # Validation: Check for required fields
        if not all([statusid,status]):
            self.show_confirmation_dialog("Please fill all fields and with image!")
            return

        conn = sqlite3.connect("radision.db")
        cursor = conn.cursor()
        cursor.execute('DELETE FROM status WHERE statusid = ?', (statusid,))
        conn.commit()
        conn.close()
        self.show_confirmation_dialog(" Record deleted successfully!")
        self.reset_fields()
        self.load_status_records_to_table()
    #============For Searcing Records==================================
    def search_records(self, *args):#For Searching Records 
        pass
    def load_filtered_data_for_search(self, rows):# For Searching Record
        pass

    #============For Clearing Fields after adding or saving==================================

    def clear_fields(self, *args):#For Clearing Fields 
        pass
    #============For setting Fields after adding or saving==================================

    def reset_fields(self, *args):
        """Reset all input fields, clear the search input, and reload the table with unfiltered data."""
        # Reset all form input fields
        self.generate_statusid()
        self.status_input.text = ""
        
    # ================= Dialog Function =================
    def show_confirmation_dialog(self, message):
        dialog = MDDialog(
            text=message,
            buttons=[MDRectangleFlatButton(text="OK", on_release=lambda x: dialog.dismiss())]
        )
        dialog.open()

class statusApp(MDApp):
    def build(self):
        self.theme_cls.theme_style = "Light"
        self.theme_cls.primary_palette = "Blue"
        return statusScreen()

    

if __name__ == "__main__":
    statusApp().run()

