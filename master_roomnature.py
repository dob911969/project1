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

class RoomnatureScreen(MDScreen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        Window.size = (900, 600)
       
        main_layout = MDBoxLayout(orientation="vertical", padding=10, spacing=10)

        #title layout

        # Title layout with the school logo, label, and wall clock
        title_layout = MDBoxLayout(orientation="horizontal", size_hint_y=None, height=dp(70), spacing=10, padding=10)
        title_layout.md_bg_color = (0.9, 0.9, 0.9, 1)  # Light gray background

        logo = Image(source="C:/KIVYMD_PROJECTS/DHARMAGATPUR_SCHOOL/logo and signature/school_logo.png",
                     size_hint=(None, None), size=(70, 70))
        title_label = MDLabel(text="Master-Room Nature",
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

        self.roomnatureid_input = MDTextField(hint_text="Roomnature ID", disabled=True, size_hint_x=None, width=200)
        grid_layout.add_widget(self.roomnatureid_input)
        self.roomno_input = MDTextField(hint_text="Room No", size_hint_x=None, width=200)
        grid_layout.add_widget(self.roomno_input)
        self.roomnature_input = MDTextField(hint_text="Room Nature", size_hint_x=None, width=200)
        grid_layout.add_widget(self.roomnature_input)

        main_layout.add_widget(grid_layout)

        #Button Layout
        btn_layout=MDBoxLayout(size_hint=(1, None), height=dp(50), spacing=10)
        btn_layout.md_bg_color = (1, 0.95, 0.85, 1)  # Light peach background

        add_button = MDRaisedButton(text="Add", on_release=self.save_roomnature)
        btn_layout.add_widget(add_button)
        update_button = MDRaisedButton(text="Update",on_release=self.update_record)
        btn_layout.add_widget(update_button)
        delete_button = MDRaisedButton(text="Delete",on_release=self.delete_record)
        btn_layout.add_widget(delete_button)
        search_button = MDRaisedButton(text="Search")
        btn_layout.add_widget(search_button)
        reset_button = MDRaisedButton(text="Reset",on_release=self.reset_fields)
        btn_layout.add_widget(reset_button)
        fetchroom_button = MDRaisedButton(text="Fetch Room", on_release=self.populate_roomno)
        btn_layout.add_widget(fetchroom_button)
        fetchroomcategory_button = MDRaisedButton(text="Fetch Roomcategory", on_release=self.populate_roomcategory)
        btn_layout.add_widget(fetchroomcategory_button)
        
        main_layout.add_widget(btn_layout)

        #Data Table for Displaying Records
        table_layout = MDBoxLayout( padding=10)
        table_layout.md_bg_color = (0.9, 1, 0.9, 1)  # Light green background
        self.table = MDDataTable(
            size_hint=(1, None),
            height=dp(420),
            column_data=[
                ("Roomnature_ID", dp(30)),
                ("Room_No", dp(30)),
                ("Room Nature", dp(30)),
            ],
            row_data=[],
            use_pagination=True,
            rows_num=10
        )
        self.table.bind(on_row_press=self.on_row_select)
        main_layout.add_widget(self.table)
        #self.table.bind(on_row_press=self.on_row_select)
        main_layout.add_widget(table_layout)


        self.add_widget(main_layout)
        self.initialize_database()
        self.generate_roomnatureid()
        self.load_roomnature_records_to_table()
        #Calling of Functions-1
        #Calling of Functions-2
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
            CREATE TABLE IF NOT EXISTS roomnature (
                roomnatureid INTEGER PRIMARY KEY AUTOINCREMENT,
                roomno TEXT NOT NULL ,
                roomnature TEXT NOT NULL 
            )
        ''')
        conn.commit()
        conn.close()

    def generate_roomnatureid(self):
        """Generate the next class ID."""
        conn = sqlite3.connect("radision.db")
        cursor = conn.cursor()
        cursor.execute("SELECT MAX(roomnatureid) FROM roomnature")
        last_roomnatureid = cursor.fetchone()[0]
        self.roomnatureid_input.text = str((last_roomnatureid or 0) + 1)
        conn.close()

   

    #============For Populating Data from Other Table==================================

    def populate_roomno(self, instance):
        conn = sqlite3.connect("radision.db")
        cursor = conn.cursor()
        try:
            cursor.execute("SELECT roomno FROM room order by roomno ASC")
            room = cursor.fetchall()

            if not room:
                self.show_confirmation_dialog("No category found in the database.")
                return

            menu_items = [
                {
                    "text": ro[0],
                    "viewclass": "OneLineListItem",
                    "on_release": lambda x=ro[0]: self.room_menu_callback(x),
                }
                for ro in room
            ]

            self.menu = MDDropdownMenu(
                caller=self.roomno_input,
                items=menu_items,
                width_mult=4,
            )
            self.menu.open()
        except Exception as e:
            self.show_confirmation_dialog(f"Error: {e}")
        finally:
            conn.close()

    def room_menu_callback(self, selected_room):
        self.roomno_input.text = selected_room
        self.menu.dismiss()

    def populate_roomcategory(self, instance):
        conn = sqlite3.connect("radision.db")
        cursor = conn.cursor()
        try:
            cursor.execute("SELECT roomcategory FROM roomcategory")
            roomcategory = cursor.fetchall()

            if not roomcategory:
                self.show_confirmation_dialog("No category found in the database.")
                return

            menu_items = [
                {
                    "text": roomcat[0],
                    "viewclass": "OneLineListItem",
                    "on_release": lambda x=roomcat[0]: self.roomcategory_menu_callback(x),
                }
                for roomcat in roomcategory
            ]

            self.menu = MDDropdownMenu(
                caller=self.roomnature_input,
                items=menu_items,
                width_mult=4,
            )
            self.menu.open()
        except Exception as e:
            self.show_confirmation_dialog(f"Error: {e}")
        finally:
            conn.close()

    def roomcategory_menu_callback(self, selected_roomcategory):
        self.roomnature_input.text = selected_roomcategory
        self.menu.dismiss()





    #============For Adding/Saving Records and Loading Records to Table and Selection of Row from table==================================

    def save_roomnature(self, *args):
        roomnatureid=self.roomnatureid_input.text.strip()
        roomno=self.roomno_input.text.strip()
        roomnature=self.roomnature_input.text.strip()
        
         
        #contact_no = self.contact_no_field.text.strip()
        if not all([roomnatureid,roomno,roomnature]):
            self.show_confirmation_dialog("Please fill all fields ")
            return

        conn = sqlite3.connect("radision.db")
        cursor = conn.cursor()
        #floorid,floorno
        cursor.execute('''
            INSERT INTO roomnature (roomnatureid,roomno,roomnature)
            VALUES (?, ?,?)
        ''', (roomnatureid,roomno,roomnature))
        conn.commit()
        conn.close()
        self.show_confirmation_dialog("Roomnature saved successfully!")
        self.roomno_input.text = ""
        self.generate_roomnatureid()
        self.load_roomnature_records_to_table()

    def load_roomnature_records_to_table(self):
        """Load records from the database into the table."""
        self.table.row_data = []  # Clear previous data
        conn = sqlite3.connect("radision.db")
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM roomnature ORDER BY roomnatureid DESC")
        rows = cursor.fetchall()
        conn.close()
        self.table.row_data = [(str(r[0]), r[1],r[2]) for r in rows]

    def on_row_select(self, instance_table, instance_row):
        """Populate fields when a row is selected."""
        selected_row = instance_row.text
        for row in self.table.row_data:
            if row[0] == selected_row:
                self.roomnatureid_input.text=row[0]
                self.roomno_input.text=row[1]
                self.roomnature_input.text=row[2]
                break
    #============For Updating Records==================================
    def update_record(self, *args):
        roomnatureid=self.roomnatureid_input.text.strip()
        roomno=self.roomno_input.text.strip()
        roomnature=self.roomnature_input.text.strip()
       

        # Validation: Check for required fields
        if not all([roomnatureid,roomno , roomnature]):
            self.show_confirmation_dialog("Please fill all fields!")
            return
        
        try:
            conn = sqlite3.connect("radision.db")
            cursor = conn.cursor()

            # Check if record exists before updating
            cursor.execute('SELECT 1 FROM roomnature WHERE roomnatureid = ?', (roomnatureid,))
            if not cursor.fetchone():
                self.show_confirmation_dialog(f"No record found with Roomnature ID {roomnatureid}.")
                conn.close()
                return

            # Update the record
            #floorid , floorno
            cursor.execute('''
                UPDATE roomnature
                SET roomno=?,
                roomnature =?
                WHERE roomnatureid = ?
            ''', (roomnatureid,roomno , roomnature))
            conn.commit()

            self.show_confirmation_dialog("Record updated successfully!")
        except sqlite3.Error as e:
            self.show_confirmation_dialog(f"Database error occurred: {e}")
        finally:
            conn.close()
            self.reset_fields()
            self.load_roomnature_records_to_table()
    #============For Deleting Records==================================

    def delete_record(self, *args):
        roomnatureid=self.roomnatureid_input.text.strip()
        roomno=self.roomno_input.text.strip()
        roomnature=self.roomnature_input.text.strip()
        

        # Validation: Check for required fields
        if not all([roomnatureid,roomno,roomnature]):
            self.show_confirmation_dialog("Please fill all fields and with image!")
            return

        conn = sqlite3.connect("radision.db")
        cursor = conn.cursor()
        cursor.execute('DELETE FROM roomnature WHERE roomnatureid = ?', (roomnatureid,))
        conn.commit()
        conn.close()
        self.show_confirmation_dialog(" Record deleted successfully!")
        self.reset_fields()
        self.load_roomnature_records_to_table()
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
        self.generate_roomnatureid()
        self.roomno_input.text = ""
        self.roomnature_input.text =""
    # ================= Dialog Function =================
    def show_confirmation_dialog(self, message):
        dialog = MDDialog(
            text=message,
            buttons=[MDRectangleFlatButton(text="OK", on_release=lambda x: dialog.dismiss())]
        )
        dialog.open()

class roomnatureApp(MDApp):
    def build(self):
        self.theme_cls.theme_style = "Light"
        self.theme_cls.primary_palette = "Blue"
        return RoomnatureScreen()

    

if __name__ == "__main__":
    roomnatureApp().run()

