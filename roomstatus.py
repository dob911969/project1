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

class RoomstatusScreen(MDScreen):
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
        title_label = MDLabel(text="Room Status",
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

        self.roomstatusid_input = MDTextField(hint_text="Roomstatus ID", disabled=True, size_hint_x=None, width=200)
        grid_layout.add_widget(self.roomstatusid_input)
        self.roomcategory_input = MDTextField(hint_text="Room Category", size_hint_x=None, width=200)
        grid_layout.add_widget(self.roomcategory_input)
        self.roomtariff_input = MDTextField(hint_text="Room Tariff", size_hint_x=None, width=200)
        grid_layout.add_widget(self.roomtariff_input)
        self.roomno_input = MDTextField(hint_text="Room No", size_hint_x=None, width=200)
        grid_layout.add_widget(self.roomno_input)
        self.floorno_input = MDTextField(hint_text="Floor No", size_hint_x=None, width=200)
        grid_layout.add_widget(self.floorno_input)
        self.roomstatus_input = MDTextField(hint_text="Room Status", size_hint_x=None, width=200)
        grid_layout.add_widget(self.roomstatus_input)

        main_layout.add_widget(grid_layout)

        #Button Layout
        btn_layout=MDBoxLayout(size_hint=(1, None), height=dp(50), spacing=10)
        btn_layout.md_bg_color = (1, 0.95, 0.85, 1)  # Light peach background

        add_button = MDRaisedButton(text="Add", on_release=self.save_roomstatus)
        btn_layout.add_widget(add_button)
        update_button = MDRaisedButton(text="Update", on_release=self.update_record)
        btn_layout.add_widget(update_button)
        delete_button = MDRaisedButton(text="Delete", on_release=self.delete_record)
        btn_layout.add_widget(delete_button)
        search_button = MDRaisedButton(text="Search", on_release=self.search_roomstatus_records)
        btn_layout.add_widget(search_button)
        reset_button = MDRaisedButton(text="Reset", on_release=self.reset_fields)
        btn_layout.add_widget(reset_button)
        fetchroomcategory_button = MDRaisedButton(text="Fetch Room Category", on_release=self.populate_roomcategory)
        btn_layout.add_widget(fetchroomcategory_button)
        fetchroomtariff_button = MDRaisedButton(text="Fetch Room Tariff", on_release=self.populate_roomtariff)
        btn_layout.add_widget(fetchroomtariff_button)
        fetchroomno_button = MDRaisedButton(text="Fetch Room No", on_release=self.populate_roomno)
        btn_layout.add_widget(fetchroomno_button)
        fetchfloorno_button = MDRaisedButton(text="Fetch Floor No", on_release=self.populate_floorno)
        btn_layout.add_widget(fetchfloorno_button)
        fetchroomstatus_button = MDRaisedButton(text="Fetch Room Status", on_release=self.populate_roomstatus)
        btn_layout.add_widget(fetchroomstatus_button)
        
        
        main_layout.add_widget(btn_layout)

        #Data Table for Displaying Records
        table_layout = MDBoxLayout( padding=10)
        table_layout.md_bg_color = (0.9, 1, 0.9, 1)  # Light green background
        self.table = MDDataTable(
            size_hint=(1, None),
            height=dp(420),
            column_data=[
                ("Roomstatus_ID", dp(30)),
                ("Room Category", dp(30)),
                ("Room Tarif", dp(30)),
                ("Room No", dp(30)),
                ("Floor No", dp(30)),
                ("Room Status", dp(30)),
                
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
        self.generate_roomstatusid()
        self.load_roomstatus_records_to_table()
        #Calling of Functions-1
        #Calling of Functions-2
        #Calling of Functions-3
        #Calling of Functions-4
        #Calling of Functions-5
        #Calling of Functions-6
        
    
    #============For Data Base , Autoid , Auto Registration No , Auto Current Date========================
    #roomstatusid , roomcategory , roomtariff , roomno , floorno , roomstatus
    def initialize_database(self):
        """Initialize the database and create the class table if it does not exist."""
        conn = sqlite3.connect("radision.db")
        cursor = conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS roomstatus (
                roomstatusid INTEGER PRIMARY KEY AUTOINCREMENT,
                roomcategory TEXT NOT NULL ,
                roomtariff REAL NOT NULL ,
                roomno TEXT NOT NULL ,
                floorno TEXT NOT NULL ,
                roomstatus TEXT NOT NULL
            )
        ''')
        conn.commit()
        conn.close()

    def generate_roomstatusid(self):
        """Generate the next class ID."""
        conn = sqlite3.connect("radision.db")
        cursor = conn.cursor()
        cursor.execute("SELECT MAX(roomstatusid) FROM roomstatus")
        last_roomstatusid = cursor.fetchone()[0]
        self.roomstatusid_input.text = str((last_roomstatusid or 0) + 1)
        conn.close()

    
    #============For Populating Data from Other Table==================================

    def populate_roomcategory(self, instance):
        conn = sqlite3.connect("radision.db")
        cursor = conn.cursor()
        try:
            cursor.execute("SELECT roomcategory FROM roomcategory order by roomcategory ASC")
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
                caller=self.roomcategory_input,
                items=menu_items,
                width_mult=4,
            )
            self.menu.open()
        except Exception as e:
            self.show_confirmation_dialog(f"Error: {e}")
        finally:
            conn.close()

    def roomcategory_menu_callback(self, selected_roomcategory):
        self.roomcategory_input.text = selected_roomcategory
        self.menu.dismiss()

    def populate_roomtariff(self, instance):
        conn = sqlite3.connect("radision.db")
        cursor = conn.cursor()
        try:
            selected_roomcategory=self.roomcategory_input.text.strip()
            cursor.execute("SELECT tariffamount FROM tariff where roomtype=? ",(selected_roomcategory,))
            roomtariff = cursor.fetchall()

            if not roomtariff:
                self.show_confirmation_dialog("No category found in the database.")
                return

            menu_items = [
                {
                    "text": str(roomtar[0]),
                    "viewclass": "OneLineListItem",
                    "on_release": lambda x=roomtar[0]: self.roomtariff_menu_callback(x),
                }
                for roomtar in roomtariff
            ]

            self.menu = MDDropdownMenu(
                caller=self.roomtariff_input,
                items=menu_items,
                width_mult=4,
            )
            self.menu.open()
        except Exception as e:
            self.show_confirmation_dialog(f"Error: {e}")
        finally:
            conn.close()

    def roomtariff_menu_callback(self, selected_roomtariff):
        self.roomtariff_input.text = str(selected_roomtariff)
        self.menu.dismiss()

    def populate_roomno(self, instance):
        conn = sqlite3.connect("radision.db")
        cursor = conn.cursor()
        try:
            selected_roomcategory=self.roomcategory_input.text.strip()
            cursor.execute("SELECT roomno FROM roomnature where roomnature=? ",(selected_roomcategory,))
            roomnature = cursor.fetchall()

            if not roomnature:
                self.show_confirmation_dialog("No category found in the database.")
                return

            menu_items = [
                {
                    "text": roomnat[0],
                    "viewclass": "OneLineListItem",
                    "on_release": lambda x=roomnat[0]: self.roomnature_menu_callback(x),
                }
                for roomnat in roomnature
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

    def roomnature_menu_callback(self, selected_roomnature):
        self.roomno_input.text = selected_roomnature
        self.menu.dismiss()

    def populate_floorno(self, instance):
        conn = sqlite3.connect("radision.db")
        cursor = conn.cursor()
        try:
            selected_roomno=self.roomno_input.text.strip()
            cursor.execute("SELECT floorno FROM room where roomno=? ",(selected_roomno,))
            floorno = cursor.fetchall()

            if not floorno:
                self.show_confirmation_dialog("No floor found in the database.")
                return

            menu_items = [
                {
                    "text": fln[0],
                    "viewclass": "OneLineListItem",
                    "on_release": lambda x=fln[0]: self.floorno_menu_callback(x),
                }
                for fln in floorno
            ]

            self.menu = MDDropdownMenu(
                caller=self.floorno_input,
                items=menu_items,
                width_mult=4,
            )
            self.menu.open()
        except Exception as e:
            self.show_confirmation_dialog(f"Error: {e}")
        finally:
            conn.close()

    def floorno_menu_callback(self, selected_floorno):
        self.floorno_input.text = selected_floorno
        self.menu.dismiss()

    def populate_roomstatus(self, instance):
        conn = sqlite3.connect("radision.db")
        cursor = conn.cursor()
        try:
            
            cursor.execute("SELECT status FROM status  ")
            status = cursor.fetchall()

            if not status:
                self.show_confirmation_dialog("No floor found in the database.")
                return

            menu_items = [
                {
                    "text": sta[0],
                    "viewclass": "OneLineListItem",
                    "on_release": lambda x=sta[0]: self.roomstatus_menu_callback(x),
                }
                for sta in status
            ]

            self.menu = MDDropdownMenu(
                caller=self.roomstatus_input,
                items=menu_items,
                width_mult=4,
            )
            self.menu.open()
        except Exception as e:
            self.show_confirmation_dialog(f"Error: {e}")
        finally:
            conn.close()

    def roomstatus_menu_callback(self, selected_status):
        self.roomstatus_input.text = selected_status
        self.menu.dismiss()






    #============For Adding/Saving Records and Loading Records to Table and Selection of Row from table==================================

    def save_roomstatus(self, *args):
        id=self.roomstatusid_input.text.strip()
        category=self.roomcategory_input.text.strip()
        tariff=self.roomtariff_input.text.strip()
        roomno=self.roomno_input.text.strip()
        floorno=self.floorno_input.text.strip()
        status=self.roomstatus_input.text.strip()
        
         
        #roomstatusid , roomcategory , roomtariff , roomno , floorno , roomstatus
        if not all([id,category,tariff,roomno,floorno,status]):
            self.show_confirmation_dialog("Please fill all fields ")
            return

        conn = sqlite3.connect("radision.db")
        cursor = conn.cursor()
        #floorid,floorno
        cursor.execute('''
            INSERT INTO roomstatus (roomstatusid , roomcategory , roomtariff , roomno , floorno , roomstatus)
            VALUES (?, ?,?,?,?,?)
        ''', (id,category,tariff,roomno,floorno,status))
        conn.commit()
        conn.close()
        self.show_confirmation_dialog("Roomstatus saved successfully!")
        self.reset_fields()
        self.load_roomstatus_records_to_table()

    def load_roomstatus_records_to_table(self):
        #roomstatusid , roomcategory , roomtariff , roomno , floorno , roomstatus
        self.table.row_data = []  # Clear previous data
        conn = sqlite3.connect("radision.db")
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM roomstatus ORDER BY roomstatusid DESC")
        rows = cursor.fetchall()
        conn.close()
        self.table.row_data = [(str(r[0]), r[1],r[2],r[3],r[4],r[5]) for r in rows]

    def on_row_select(self, instance_table, instance_row):
        """Populate fields when a row is selected."""
        selected_row = instance_row.text
        for row in self.table.row_data:
            if row[0] == selected_row:
                self.roomstatusid_input.text=row[0]
                self.roomcategory_input.text=row[1]
                self.roomtariff_input.text=str(row[2])
                self.roomno_input.text=row[3]
                self.floorno_input.text=row[4]
                self.roomstatus_input.text=row[5]
                break
    #============For Updating Records==================================
    def update_record(self, *args):
        id=self.roomstatusid_input.text.strip()
        category=self.roomcategory_input.text.strip()
        tariff=self.roomtariff_input.text.strip()
        roomno=self.roomno_input.text.strip()
        floorno=self.floorno_input.text.strip()
        status=self.roomstatus_input.text.strip()
       

        # Validation: Check for required fields
        if not all([id,category,tariff,roomno,floorno,status]):
            self.show_confirmation_dialog("Please fill all fields!")
            return
        
        try:
            conn = sqlite3.connect("radision.db")
            cursor = conn.cursor()

            # Check if record exists before updating
            cursor.execute('SELECT 1 FROM roomstatus WHERE roomstatusid = ?', (id,))
            if not cursor.fetchone():
                self.show_confirmation_dialog(f"No record found with Roomstaus ID {id}.")
                conn.close()
                return

            # Update the record
            #roomstatusid , roomcategory , roomtariff , roomno , floorno , roomstatus
            cursor.execute('''
                UPDATE roomstatus
                SET roomcategory=?,
                roomtariff =?,
                roomno=?,
                floorno=?,
                roomstatus=?
                WHERE roomstatusid = ?
            ''', (category,tariff,roomno,floorno,status,id))
            conn.commit()

            self.show_confirmation_dialog("Record updated successfully!")
        except sqlite3.Error as e:
            self.show_confirmation_dialog(f"Database error occurred: {e}")
        finally:
            conn.close()
            self.reset_fields()
            self.load_roomstatus_records_to_table()
    #============For Deleting Records==================================

    def delete_record(self, *args):
        id=self.roomstatusid_input.text.strip()
        category=self.roomcategory_input.text.strip()
        tariff=self.roomtariff_input.text.strip()
        roomno=self.roomno_input.text.strip()
        floorno=self.floorno_input.text.strip()
        status=self.roomstatus_input.text.strip()

        # Validation: Check for required fields
        if not all([id,category,tariff,roomno,floorno,status]):
            self.show_confirmation_dialog("Please fill all fields and with image!")
            return

        conn = sqlite3.connect("radision.db")
        cursor = conn.cursor()
        cursor.execute('DELETE FROM roomstatus WHERE roomstatusid = ?', (id,))
        conn.commit()
        conn.close()
        self.show_confirmation_dialog(" Record deleted successfully!")
        self.reset_fields()
        self.load_roomstatus_records_to_table()

    #============For Searcing Records==================================

    def search_roomstatus_records(self, *args):
        """Search and filter employee records based on search input."""
        search_query = self.roomstatus_input.text.strip()
       
        # Connect to the database
        conn = sqlite3.connect("radision.db")
        cursor = conn.cursor()

        if search_query :
            #roomstatusid , roomcategory , roomtariff , roomno , floorno , roomstatus
            # Search by Name or Reg_No (case insensitive)
            cursor.execute('''
                SELECT roomstatusid , roomcategory , roomtariff , roomno , floorno , roomstatus
                FROM roomstatus
                WHERE LOWER(roomstatus) LIKE ? OR LOWER(roomcategory) LIKE ?
            ''', (f'%{search_query.lower()}%', f'%{search_query.lower()}%'))
        else:
            # Fetch all records if no search query
            cursor.execute('''
                SELECT roomstatusid , roomcategory , roomtariff , roomno , floorno , roomstatus
                FROM roomstatus
            ''')

        # Fetch data and close connection
        rows = cursor.fetchall()
        conn.close()
        self.load_roomstatus_records_to_table()

        # Reload table data
        self.load_filtered_data_for_search(rows)

    def load_filtered_data_for_search(self, rows):
        """Reload the table with filtered employee data."""
        self.table.row_data = []  # Clear existing rows
    
        for row in rows:
            # Append records to the table row_data
            self.table.row_data.append((
                row[0],  # roomstatusid
                row[1],  # roomcategory
                row[2],  # roomtariff
                row[3],  # roomno
                row[4],  # floorno
                row[5],  # roomstatus
                
            ))
    #============For Clearing Fields after adding or saving==================================

    def clear_fields(self, *args):#For Clearing Fields 
        pass
    #============For setting Fields after adding or saving==================================

    def reset_fields(self, *args):
        """Reset all input fields, clear the search input, and reload the table with unfiltered data."""
        #roomstatusid , roomcategory , roomtariff , roomno , floorno , roomstatus
        self.generate_roomstatusid()
        
        self.roomcategory_input.text = ""
        self.roomtariff_input.text = ""  # This is your search input field
        self.roomno_input.text = ""
        self.floorno_input.text = ""
        self.roomstatus_input= ""
        
    
        # Fetch and reload all employee records into the table
        conn = sqlite3.connect("radision.db")
        cursor = conn.cursor()
    
        cursor.execute('''
            SELECT roomstatusid , roomcategory , roomtariff , roomno , floorno , roomstatus
            FROM roomstatus
        ''')
        rows = cursor.fetchall()
        conn.close()

        # Load unfiltered data into the table
        self.load_filtered_data_for_search(rows)
        
    # ================= Dialog Function =================
    def show_confirmation_dialog(self, message):
        dialog = MDDialog(
            text=message,
            buttons=[MDRectangleFlatButton(text="OK", on_release=lambda x: dialog.dismiss())]
        )
        dialog.open()

class roomstatusApp(MDApp):
    def build(self):
        self.theme_cls.theme_style = "Light"
        self.theme_cls.primary_palette = "Blue"
        return RoomstatusScreen()

    

if __name__ == "__main__":
    roomstatusApp().run()

