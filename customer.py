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

class CustomerScreen(MDScreen):
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
        title_label = MDLabel(text="Customer Details",
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

        self.customerid_input = MDTextField(hint_text="Customer ID", disabled=True, size_hint_x=None, width=200)
        grid_layout.add_widget(self.customerid_input)
        self.mobileno_input = MDTextField(hint_text="Contact No", size_hint_x=None, width=200)
        grid_layout.add_widget(self.mobileno_input)
        self.customername_input = MDTextField(hint_text="Customer Name", size_hint_x=None, width=200)
        grid_layout.add_widget(self.customername_input)
        self.address_input = MDTextField(hint_text="Customer Address", size_hint_x=None, width=200)
        grid_layout.add_widget(self.address_input)
        self.idtype_input = MDTextField(hint_text="Customer ID_Type", size_hint_x=None, width=200)
        grid_layout.add_widget(self.idtype_input)

        main_layout.add_widget(grid_layout)

        #Button Layout
        btn_layout=MDBoxLayout(size_hint=(1, None), height=dp(50), spacing=10)
        btn_layout.md_bg_color = (1, 0.95, 0.85, 1)  # Light peach background

        add_button = MDRaisedButton(text="Add", on_release=self.save_customer)
        btn_layout.add_widget(add_button)
        update_button = MDRaisedButton(text="Update", on_release=self.update_record)
        btn_layout.add_widget(update_button)
        delete_button = MDRaisedButton(text="Delete", on_release=self.delete_record)
        btn_layout.add_widget(delete_button)
        search_button = MDRaisedButton(text="Search", on_release=self.search_customer_records)
        btn_layout.add_widget(search_button)
        reset_button = MDRaisedButton(text="Reset", on_release=self.reset_fields)
        btn_layout.add_widget(reset_button)
        fetchidtype_button = MDRaisedButton(text="Fetch Customer ID Type", on_release=self.populate_idtype)
        btn_layout.add_widget(fetchidtype_button)
        
        main_layout.add_widget(btn_layout)

        #Data Table for Displaying Records
        table_layout = MDBoxLayout( padding=10)
        table_layout.md_bg_color = (0.9, 1, 0.9, 1)  # Light green background
        self.table = MDDataTable(
            size_hint=(1, None),
            height=dp(420),
            column_data=[
                ("Customer_ID", dp(30)),
                ("Contact_No", dp(30)),
                ("Customer Name", dp(30)),
                ("Address", dp(50)),
                ("ID Type", dp(30)),
                
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
        self.generate_custid()
        self.load_customer_records_to_table()
        #Calling of Functions-1
        #Calling of Functions-2
        #Calling of Functions-3
        #Calling of Functions-4
        #Calling of Functions-5
        #Calling of Functions-6
        
    
    #============For Data Base , Autoid , Auto Registration No , Auto Current Date========================
    # custid , mobileno , name , address , idtype
    def initialize_database(self):
        """Initialize the database and create the class table if it does not exist."""
        conn = sqlite3.connect("radision.db")
        cursor = conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS customer (
                custid INTEGER PRIMARY KEY AUTOINCREMENT,
                mobileno TEXT NOT NULL ,
                name TEXT NOT NULL ,
                address TEXT NOT NULL ,
                idtype TEXT NOT NULL 
                
            )
        ''')
        conn.commit()
        conn.close()

    def generate_custid(self):
        """Generate the next class ID."""
        conn = sqlite3.connect("radision.db")
        cursor = conn.cursor()
        cursor.execute("SELECT MAX(custid) FROM customer")
        last_custid = cursor.fetchone()[0]
        self.customerid_input.text = str((last_custid or 0) + 1)
        conn.close()

    
    
    #============For Populating Data from Other Table==================================

    def populate_idtype(self, instance):
        conn = sqlite3.connect("radision.db")
        cursor = conn.cursor()
        try:
            cursor.execute("SELECT idtype FROM id order by idtype ASC")
            idtype = cursor.fetchall()

            if not idtype:
                self.show_confirmation_dialog("No category found in the database.")
                return

            menu_items = [
                {
                    "text": id[0],
                    "viewclass": "OneLineListItem",
                    "on_release": lambda x=id[0]: self.idtype_menu_callback(x),
                }
                for id in idtype
            ]

            self.menu = MDDropdownMenu(
                caller=self.idtype_input,
                items=menu_items,
                width_mult=4,
            )
            self.menu.open()
        except Exception as e:
            self.show_confirmation_dialog(f"Error: {e}")
        finally:
            conn.close()

    def idtype_menu_callback(self, selected_idtype):
        self.idtype_input.text = selected_idtype
        self.menu.dismiss()


    #============For Adding/Saving Records and Loading Records to Table and Selection of Row from table==================================

    def save_customer(self, *args):
        custid=self.customerid_input.text.strip()
        mobileno=self.mobileno_input.text.strip()
        name=self.customername_input.text.strip()
        address=self.address_input.text.strip()
        idtype=self.idtype_input.text.strip()
       
        
         
        # custid , mobileno , name , address , idtype
        if not all([custid,mobileno,name,address,idtype]):
            self.show_confirmation_dialog("Please fill all fields ")
            return

        conn = sqlite3.connect("radision.db")
        cursor = conn.cursor()
        #floorid,floorno
        cursor.execute('''
            INSERT INTO customer (custid,mobileno,name,address,idtype)
            VALUES (?, ?,?,?,?)
        ''', (custid,mobileno,name,address,idtype))
        conn.commit()
        conn.close()
        self.show_confirmation_dialog("Customer saved successfully!")
        self.reset_fields()
        self.load_customer_records_to_table()

    def load_customer_records_to_table(self):
         # custid , mobileno , name , address , idtype
        self.table.row_data = []  # Clear previous data
        conn = sqlite3.connect("radision.db")
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM customer ORDER BY custid DESC")
        rows = cursor.fetchall()
        conn.close()
        self.table.row_data = [(str(r[0]), r[1],r[2],r[3],r[4]) for r in rows]

    def on_row_select(self, instance_table, instance_row):
        """Populate fields when a row is selected."""
        selected_row = instance_row.text
        for row in self.table.row_data:
            if row[0] == selected_row:
                self.customerid_input.text=row[0]
                self.mobileno_input.text=row[1]
                self.customername_input.text=str(row[2])
                self.address_input.text=row[3]
                self.idtype_input.text=row[4]
                
                break
    #============For Updating Records==================================
    def update_record(self, *args):
        custid=self.customerid_input.text.strip()
        mobileno=self.mobileno_input.text.strip()
        name=self.customername_input.text.strip()
        address=self.address_input.text.strip()
        idtype=self.idtype_input.text.strip()
       

        # Validation: Check for required fields
        if not all([custid,mobileno,name,address,idtype]):
            self.show_confirmation_dialog("Please fill all fields!")
            return
        
        try:
            conn = sqlite3.connect("radision.db")
            cursor = conn.cursor()

            # Check if record exists before updating
            cursor.execute('SELECT 1 FROM customer WHERE custid = ?', (custid,))
            if not cursor.fetchone():
                self.show_confirmation_dialog(f"No record found with Customer ID {id}.")
                conn.close()
                return

            # Update the record
            # custid , mobileno , name , address , idtype
            cursor.execute('''
                UPDATE customer
                SET mobileno=?,
                name =?,
                address=?,
                idtype=?
                WHERE custid = ?
            ''', (mobileno,name,address,idtype,custid))
            conn.commit()

            self.show_confirmation_dialog("Record updated successfully!")
        except sqlite3.Error as e:
            self.show_confirmation_dialog(f"Database error occurred: {e}")
        finally:
            conn.close()
            self.reset_fields()
            self.load_customer_records_to_table()
    #============For Deleting Records==================================

    def delete_record(self, *args):
        custid=self.customerid_input.text.strip()
        mobileno=self.mobileno_input.text.strip()
        name=self.customername_input.text.strip()
        address=self.address_input.text.strip()
        idtype=self.idtype_input.text.strip()
       

        # Validation: Check for required fields
        if not all([custid,mobileno,name,address,idtype]):
            self.show_confirmation_dialog("Please fill all fields!")
            return
        
        conn = sqlite3.connect("radision.db")
        cursor = conn.cursor()
        cursor.execute('DELETE FROM customer WHERE custid = ?', (custid,))
        conn.commit()
        conn.close()
        self.show_confirmation_dialog(" Record deleted successfully!")
        self.reset_fields()
        self.load_customer_records_to_table()

    #============For Searcing Records==================================
    def search_customer_records(self, *args):
        """Search and filter employee records based on search input."""
        search_query = self.mobileno_input.text.strip()
       
        # Connect to the database
        conn = sqlite3.connect("radision.db")
        cursor = conn.cursor()

        if search_query :
            # custid , mobileno , name , address , idtype
            # Search by Name or Reg_No (case insensitive)
            cursor.execute('''
                SELECT custid , mobileno , name , address , idtype
                FROM customer
                WHERE LOWER(mobileno) LIKE ? OR LOWER(name) LIKE ?
            ''', (f'%{search_query.lower()}%', f'%{search_query.lower()}%'))
        else:
            # Fetch all records if no search query
            cursor.execute('''
                SELECT custid , mobileno , name , address , idtype
                FROM customer
            ''')

        # Fetch data and close connection
        rows = cursor.fetchall()
        conn.close()
        self.load_customer_records_to_table()

        # Reload table data
        self.load_filtered_data_for_search(rows)

    def load_filtered_data_for_search(self, rows):
        """Reload the table with filtered employee data."""
        self.table.row_data = []  # Clear existing rows
    
        for row in rows:
            # Append records to the table row_data
            self.table.row_data.append((
                row[0],  # custid
                row[1],  # mobileno
                row[2],  # name
                row[3],  # address
                row[4],  # idtype
                
                
            ))

    #============For Clearing Fields after adding or saving==================================

    def clear_fields(self, *args):#For Clearing Fields 
        pass
    #============For setting Fields after adding or saving==================================

    def reset_fields(self, *args):
        """Reset all input fields, clear the search input, and reload the table with unfiltered data."""
        # custid , mobileno , name , address , idtype
        self.generate_custid()
        self.mobileno_input.text = ""
        self.customername_input.text = ""  # This is your search input field
        self.address_input.text = ""
        self.idtype_input.text = ""
        
    
        # Fetch and reload all employee records into the table
        conn = sqlite3.connect("radision.db")
        cursor = conn.cursor()
    
        cursor.execute('''
            SELECT custid , mobileno , name , address , idtype
            FROM customer
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

class customerApp(MDApp):
    def build(self):
        self.theme_cls.theme_style = "Light"
        self.theme_cls.primary_palette = "Blue"
        return CustomerScreen()

    

if __name__ == "__main__":
    customerApp().run()

