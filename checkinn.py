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

class CheckinnScreen(MDScreen):
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
        title_label = MDLabel(text="Checkinn",
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

        self.checkinnid_input = MDTextField(hint_text="Checkinn ID", disabled=True, size_hint_x=None, width=200)
        grid_layout.add_widget(self.checkinnid_input)
        self.mobileno_input = MDTextField(hint_text="Mobileno No", size_hint_x=None, width=200)
        grid_layout.add_widget(self.mobileno_input)
        self.custname_input = MDTextField(hint_text="Customer Name", size_hint_x=None, width=200)
        grid_layout.add_widget(self.custname_input)
        self.address_input = MDTextField(hint_text="Address", disabled=True, size_hint_x=None, width=200)
        grid_layout.add_widget(self.address_input)
        self.idtype_input = MDTextField(hint_text="Idtype", disabled=True, size_hint_x=None, width=200)
        grid_layout.add_widget(self.idtype_input)
        self.roomno_input = MDTextField(hint_text="Roomno", disabled=True, size_hint_x=None, width=200)
        grid_layout.add_widget(self.roomno_input)
        self.roomcategory_input = MDTextField(hint_text="Room Category", disabled=True, size_hint_x=None, width=200)
        grid_layout.add_widget(self.roomcategory_input)
        self.roomtariff_input = MDTextField(hint_text="Room Tariff", disabled=True, size_hint_x=None, width=200)
        grid_layout.add_widget(self.roomtariff_input)
        self.floorno_input = MDTextField(hint_text="Floor No", disabled=True, size_hint_x=None, width=200)
        grid_layout.add_widget(self.floorno_input)
        self.checkinndt_input = MDTextField(hint_text="Checkinn Date", disabled=True, size_hint_x=None, width=200)
        grid_layout.add_widget(self.checkinndt_input)

        main_layout.add_widget(grid_layout)

        #Button Layout
        btn_layout=MDBoxLayout(size_hint=(1, None), height=dp(50), spacing=10)
        btn_layout.md_bg_color = (1, 0.95, 0.85, 1)  # Light peach background

        add_button = MDRaisedButton(text="Add", on_release=self.save_checkinn)
        btn_layout.add_widget(add_button)
        update_button = MDRaisedButton(text="Update", on_release=self.update_record)
        btn_layout.add_widget(update_button)
        delete_button = MDRaisedButton(text="Delete", on_release=self.delete_record)
        btn_layout.add_widget(delete_button)
        search_button = MDRaisedButton(text="Search", on_release=self.search_checkinn_records)
        btn_layout.add_widget(search_button)
        reset_button = MDRaisedButton(text="Reset", on_release=self.reset_fields)
        btn_layout.add_widget(reset_button)
        fetchmobileno_button = MDRaisedButton(text="Fetch Customer Mobile No", on_release=self.populate_mobileno)
        btn_layout.add_widget(fetchmobileno_button)
        fetchroomno_button = MDRaisedButton(text="Fetch Avilable Room  No", on_release=self.populate_roomno)
        btn_layout.add_widget(fetchroomno_button)
        
        main_layout.add_widget(btn_layout)

        #Data Table for Displaying Records
        table_layout = MDBoxLayout( padding=10)
        table_layout.md_bg_color = (0.9, 1, 0.9, 1)  # Light green background
        self.table = MDDataTable(
            size_hint=(1, None),
            height=dp(420),
            column_data=[
                ("Checkinn ID", dp(30)),
                ("Mobile No", dp(30)),
                ("Customer Name", dp(30)),
                ("Address", dp(30)),
                ("Idtype", dp(20)),
                ("Room No", dp(20)),
                ("Room Category", dp(30)),
                ("Room Tariff", dp(30)),
                ("Floor No", dp(30)),
                ("Checkinn Date", dp(30)),
                
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
        self.generate_checkinnid()
        self.generate_checkinn_date()
        self.load_checkinn_records_to_table()
        #Calling of Functions-1
        #Calling of Functions-2
        #Calling of Functions-3
        #Calling of Functions-4
        #Calling of Functions-5
        #Calling of Functions-6
        
    
    #============For Data Base , Autoid , Auto Registration No , Auto Current Date========================
    # checkinnid ,mobileno ,custname ,address ,idtype ,roomno ,roomcategory , roomtariff ,floorno,checkinndt  
    def initialize_database(self):
        """Initialize the database and create the class table if it does not exist."""
        conn = sqlite3.connect("radision.db")
        cursor = conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS checkinn (
                checkinnid INTEGER PRIMARY KEY AUTOINCREMENT,
                mobileno TEXT NOT NULL ,
                custname TEXT NOT NULL ,
                address TEXT NOT NULL ,
                idtype TEXT NOT NULL,
                roomno TEXT NOT NULL,
                roomcategory TEXT NOT NULL,
                roomtariff REAL NOT NULL,
                floorno TEXT NOT NULL,
                checkinndt TEXT NOT NULL 
                
            )
        ''')
        conn.commit()
        conn.close()

    def generate_checkinnid(self):
        """Generate the next class ID."""
        conn = sqlite3.connect("radision.db")
        cursor = conn.cursor()
        cursor.execute("SELECT MAX(checkinnid) FROM checkinn")
        last_checkinnid = cursor.fetchone()[0]
        self.checkinnid_input.text = str((last_checkinnid or 0) + 1)
        conn.close()

    def generate_employee_registration(self):#For Genrating auto Registration No
        pass
    def generate_checkinn_date(self):
        """Set the current date in the date input field."""
        self.checkinndt_input.text = datetime.now().strftime("%Y-%m-%d")

    #============For Uploading Image==================================================

    def open_file_manager(self, *args):# in case of image upload
        pass
    def select_path(self, path):#incase of image upload
        pass
    def exit_manager(self, *args):#incase of image upload
        pass

    #============For Populating Data from Other Table==================================

    def populate_mobileno(self, instance):
        conn = sqlite3.connect("radision.db")
        cursor = conn.cursor()
        try:
            cursor.execute("SELECT mobileno FROM customer ")
            mobileno = cursor.fetchall()

            if not mobileno:
                self.show_confirmation_dialog("No category found in the database.")
                return

            menu_items = [
                {
                    "text": mob[0],
                    "viewclass": "OneLineListItem",
                    "on_release": lambda x=mob[0]: self.mobileno_menu_callback(x),
                }
                for mob in mobileno
            ]

            self.menu = MDDropdownMenu(
                caller=self.mobileno_input,
                items=menu_items,
                width_mult=4,
            )
            self.menu.open()
        except Exception as e:
            self.show_confirmation_dialog(f"Error: {e}")
        finally:
            conn.close()

    def mobileno_menu_callback(self, selected_mobileno):
        self.mobileno_input.text = selected_mobileno
        self.fetch_customer_details(selected_mobileno)
        self.menu.dismiss()

    def fetch_customer_details(self, mobileno):
        conn = sqlite3.connect("radision.db")
        cursor = conn.cursor()
        try:
            cursor.execute(
                "SELECT name, address, idtype FROM customer WHERE mobileno = ?", (mobileno,)
            )
            customer = cursor.fetchone()

            if not customer:
                self.show_confirmation_dialog(f"No details found for Mobile No {mobileno}.")
                return

            # Unpack and populate the input fields
            custname, address, idtype = customer
            self.custname_input.text = custname
            self.address_input.text = address
            self.idtype_input.text = idtype
            
        except Exception as e:
            self.show_confirmation_dialog(f"Error: {e}")
        finally:
            conn.close()

    def populate_roomno(self, instance):
        conn = sqlite3.connect("radision.db")
        cursor = conn.cursor()
        try:
            cursor.execute("SELECT roomno FROM roomstatus where roomstatus='AVILABLE' ")
            roomno = cursor.fetchall()

            if not roomno:
                self.show_confirmation_dialog("No Roomno found in the database.")
                return

            menu_items = [
                {
                    "text": mob[0],
                    "viewclass": "OneLineListItem",
                    "on_release": lambda x=mob[0]: self.roomno_menu_callback(x),
                }
                for mob in roomno
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

    def roomno_menu_callback(self, selected_roomno):
        self.roomno_input.text = selected_roomno
        self.fetch_room_details(selected_roomno)
        self.menu.dismiss()

    def fetch_room_details(self, roomno):
        conn = sqlite3.connect("radision.db")
        cursor = conn.cursor()
        try:
            cursor.execute(
                "SELECT roomcategory, roomtariff, floorno FROM roomstatus WHERE roomno = ?", (roomno,)
            )
            roomno = cursor.fetchone()

            if not roomno:
                self.show_confirmation_dialog(f"No details found for Mobile No {roomno}.")
                return

            # Unpack and populate the input fields
            roomcategory, roomtariff, floorno = roomno
            self.roomcategory_input.text = roomcategory
            self.roomtariff_input.text = str(roomtariff)
            self.floorno_input.text = floorno
            
        except Exception as e:
            self.show_confirmation_dialog(f"Error: {e}")
        finally:
            conn.close()


    

    #============For Adding/Saving Records and Loading Records to Table and Selection of Row from table==================================

    def save_checkinn(self, *args):
        checkinnid=self.checkinnid_input.text.strip()
        mobileno=self.mobileno_input.text.strip()
        name=self.custname_input.text.strip()
        address=self.address_input.text.strip()
        idtype=self.idtype_input.text.strip()
        roomno=self.roomno_input.text.strip()
        roomcategory=self.roomcategory_input.text.strip()
        roomtariff=self.roomtariff_input.text.strip()
        floorno=self.floorno_input.text.strip()
        checkinndt=self.checkinndt_input.text.strip()
        
         
        # checkinnid ,mobileno ,custname ,address ,idtype ,roomno ,roomcategory , roomtariff ,floorno,checkinndt  
        if not all([checkinnid,mobileno,name,address,idtype,roomno,roomcategory,roomtariff,floorno,checkinndt]):
            self.show_confirmation_dialog("Please fill all fields ")
            return

        conn = sqlite3.connect("radision.db")
        cursor = conn.cursor()
        #floorid,floorno
        cursor.execute('''
            INSERT INTO checkinn (checkinnid ,mobileno ,custname ,address ,idtype ,roomno ,roomcategory , roomtariff ,floorno,checkinndt)
            VALUES (?, ?,?,?,?,?,?,?,?,?)
        ''', (checkinnid,mobileno,name,address,idtype,roomno,roomcategory,roomtariff,floorno,checkinndt))
        conn.commit()
        conn.close()
        self.show_confirmation_dialog("Customer Checkinn saved successfully!")
        self.reset_fields()
        self.load_checkinn_records_to_table()

    def load_checkinn_records_to_table(self):
        # checkinnid ,mobileno ,custname ,address ,idtype ,roomno ,roomcategory , roomtariff ,floorno,checkinndt  
        self.table.row_data = []  # Clear previous data
        conn = sqlite3.connect("radision.db")
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM checkinn ORDER BY checkinnid DESC")
        rows = cursor.fetchall()
        conn.close()
        self.table.row_data = [(str(r[0]), r[1],r[2],r[3],r[4],r[5],r[6],r[7],r[8],r[9]) for r in rows]

    def on_row_select(self, instance_table, instance_row):
        """Populate fields when a row is selected."""
        selected_row = instance_row.text
        for row in self.table.row_data:
            if row[0] == selected_row:
                self.checkinnid_input.text=row[0]
                self.mobileno_input.text=row[1]
                self.custname_input.text=str(row[2])
                self.address_input.text=row[3]
                self.idtype_input.text=row[4]
                self.roomno_input.text=row[5]
                self.roomcategory_input.text=row[6]
                self.roomtariff_input.text=str(row[7])
                self.floorno_input.text=row[8]
                self.checkinndt_input.text=row[9]
                break
    #============For Updating Records==================================
    def update_record(self, *args):
        checkinnid=self.checkinnid_input.text.strip()
        mobileno=self.mobileno_input.text.strip()
        name=self.custname_input.text.strip()
        address=self.address_input.text.strip()
        idtype=self.idtype_input.text.strip()
        roomno=self.roomno_input.text.strip()
        roomcategory=self.roomcategory_input.text.strip()
        roomtariff=self.roomtariff_input.text.strip()
        floorno=self.floorno_input.text.strip()
        checkinndt=self.checkinndt_input.text.strip()
       

        # Validation: Check for required fields
        if not all([checkinnid,mobileno,name,address,idtype,roomno,roomcategory,roomtariff,floorno,checkinndt]):
            self.show_confirmation_dialog("Please fill all fields!")
            return
        
        try:
            conn = sqlite3.connect("radision.db")
            cursor = conn.cursor()

            # Check if record exists before updating
            cursor.execute('SELECT 1 FROM checkinn WHERE checkinnid = ?', (checkinnid,))
            if not cursor.fetchone():
                self.show_confirmation_dialog(f"No record found with Customer ID {checkinnid}.")
                conn.close()
                return

            # Update the record
            # checkinnid ,mobileno ,custname ,address ,idtype ,roomno ,roomcategory , roomtariff ,floorno,checkinndt  
            cursor.execute('''
                UPDATE checkinn
                SET mobileno=?,
                custname =?,
                address=?,
                idtype=?,
                roomno=?,
                roomcategory=?,
                roomtariff=?,
                floorno=?,
                checkinndt=?
                WHERE checkinnid = ?
            ''', (mobileno,name,address,idtype,roomno,roomcategory,roomtariff,floorno,checkinndt,checkinnid))
            conn.commit()

            self.show_confirmation_dialog("Record updated successfully!")
        except sqlite3.Error as e:
            self.show_confirmation_dialog(f"Database error occurred: {e}")
        finally:
            conn.close()
            self.reset_fields()
            self.load_checkinn_records_to_table()
    #============For Deleting Records==================================

    def delete_record(self, *args):
        checkinnid=self.checkinnid_input.text.strip()
        mobileno=self.mobileno_input.text.strip()
        name=self.custname_input.text.strip()
        address=self.address_input.text.strip()
        idtype=self.idtype_input.text.strip()
        roomno=self.roomno_input.text.strip()
        roomcategory=self.roomcategory_input.text.strip()
        roomtariff=self.roomtariff_input.text.strip()
        floorno=self.floorno_input.text.strip()
        checkinndt=self.checkinndt_input.text.strip()
       

        # Validation: Check for required fields
        if not all([checkinnid,mobileno,name,address,idtype,roomno,roomcategory,roomtariff,floorno,checkinndt]):
            self.show_confirmation_dialog("Please fill all fields!")
            return
        
        conn = sqlite3.connect("radision.db")
        cursor = conn.cursor()
        cursor.execute('DELETE FROM checkinn WHERE checkinnid = ?', (checkinnid,))
        conn.commit()
        conn.close()
        self.show_confirmation_dialog(" Record deleted successfully!")
        self.reset_fields()
        self.load_checkinn_records_to_table()

    #============For Searcing Records==================================
    def search_checkinn_records(self, *args):
        """Search and filter employee records based on search input."""
        search_query = self.mobileno_input.text.strip()
       
        # Connect to the database
        conn = sqlite3.connect("radision.db")
        cursor = conn.cursor()

        if search_query :
            # checkinnid ,mobileno ,custname ,address ,idtype ,roomno ,roomcategory , roomtariff ,floorno,checkinndt 
            # Search by Name or Reg_No (case insensitive)
            cursor.execute('''
                SELECT checkinnid ,mobileno ,custname ,address ,idtype ,roomno ,roomcategory , roomtariff ,floorno,checkinndt 
                FROM checkinn
                WHERE LOWER(mobileno) LIKE ? OR LOWER(custname) LIKE ?
            ''', (f'%{search_query.lower()}%', f'%{search_query.lower()}%'))
        else:
            # Fetch all records if no search query
            cursor.execute('''
                SELECT checkinnid ,mobileno ,custname ,address ,idtype ,roomno ,roomcategory , roomtariff ,floorno,checkinndt 
                FROM checkinn
            ''')

        # Fetch data and close connection
        rows = cursor.fetchall()
        conn.close()
        self.load_checkinn_records_to_table()

        # Reload table data
        self.load_filtered_data_for_search(rows)

    def load_filtered_data_for_search(self, rows):
        """Reload the table with filtered employee data."""
        self.table.row_data = []  # Clear existing rows
    
        for row in rows:
            # checkinnid ,mobileno ,custname ,address ,idtype ,roomno ,roomcategory , roomtariff ,floorno,checkinndt 
            self.table.row_data.append((
                row[0],  # checkinnid
                row[1],  # mobileno
                row[2],  # custname
                row[3],  # address
                row[4],  # idtype
                row[5],  # roomno
                row[6],  # roomcategory
                row[7],  # roomtariff
                row[8],  # floorno
                row[9],  # checkinndt     
            ))

    #============For Clearing Fields after adding or saving==================================

    def clear_fields(self, *args):#For Clearing Fields 
        pass
    #============For setting Fields after adding or saving==================================

    def reset_fields(self, *args):
        """Reset all input fields, clear the search input, and reload the table with unfiltered data."""
         # checkinnid ,mobileno ,custname ,address ,idtype ,roomno ,roomcategory , roomtariff ,floorno,checkinndt 
        self.generate_checkinnid()
        self.generate_checkinn_date()
        self.mobileno_input.text = ""
        self.custname_input.text = "" 
        self.address_input.text = ""
        self.idtype_input.text = ""
        self.roomno_input.text = ""
        self.roomcategory_input.text = "" 
        self.roomtariff_input.text = ""
        self.floorno_input.text = ""
        
    
        # Fetch and reload all employee records into the table
        conn = sqlite3.connect("radision.db")
        cursor = conn.cursor()
    
        cursor.execute('''
            SELECT checkinnid ,mobileno ,custname ,address ,idtype ,roomno ,roomcategory , roomtariff ,floorno,checkinndt 
            FROM checkinn
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

class checkinnApp(MDApp):
    def build(self):
        self.theme_cls.theme_style = "Light"
        self.theme_cls.primary_palette = "Blue"
        return CheckinnScreen()

    

if __name__ == "__main__":
    checkinnApp().run()

