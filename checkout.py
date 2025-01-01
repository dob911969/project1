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
        
        main_layout = MDBoxLayout(orientation="vertical", padding=10, spacing=10)

        #title layout

        # Title layout with the school logo, label, and wall clock
        title_layout = MDBoxLayout(orientation="horizontal", size_hint_y=None, height=dp(70), spacing=10, padding=10)
        title_layout.md_bg_color = (0.9, 0.9, 0.9, 1)  # Light gray background

        logo = Image(source="C:/KIVYMD_PROJECTS/DHARMAGATPUR_SCHOOL/logo and signature/school_logo.png",
                     size_hint=(None, None), size=(70, 70))
        title_label = MDLabel(text="CheckOut",
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

        self.checkoutid_input = MDTextField(hint_text="Checkout ID", disabled=True, size_hint_x=None, width=200)
        grid_layout.add_widget(self.checkoutid_input)
        self.mobileno_input = MDTextField(hint_text="Mobile No", size_hint_x=None, width=200)
        grid_layout.add_widget(self.mobileno_input)
        self.custname_input = MDTextField(hint_text="Name", size_hint_x=None, width=200)
        grid_layout.add_widget(self.custname_input)
        self.address_input = MDTextField(hint_text="Address", size_hint_x=None, width=200)
        grid_layout.add_widget(self.address_input)
        self.roomno_input = MDTextField(hint_text="Room No", size_hint_x=None, width=200)
        grid_layout.add_widget(self.roomno_input)
        self.roomcategory_input = MDTextField(hint_text="Category", size_hint_x=None, width=200)
        grid_layout.add_widget(self.roomcategory_input)
        self.roomtariff_input = MDTextField(hint_text="Tariff", size_hint_x=None, width=200)
        grid_layout.add_widget(self.roomtariff_input)
        self.checkinndt_input = MDTextField(hint_text="Checkinn_Dt", size_hint_x=None, width=200)
        grid_layout.add_widget(self.checkinndt_input)
        self.checkoutdt_input = MDTextField(hint_text="Checkout_Dt", size_hint_x=None, width=200)
        grid_layout.add_widget(self.checkoutdt_input)
        self.daysstayed_input = MDTextField(hint_text="Days Stayed", size_hint_x=None, width=200)
        grid_layout.add_widget(self.daysstayed_input)
        self.gstrate_input = MDTextField(hint_text="GST_Rate", size_hint_x=None, width=200)
        grid_layout.add_widget(self.gstrate_input)
        self.strate_input = MDTextField(hint_text="ST_Rate", size_hint_x=None, width=200)
        grid_layout.add_widget(self.strate_input)
        self.gstamt_input = MDTextField(hint_text="GST_Amt", size_hint_x=None, width=200)
        grid_layout.add_widget(self.gstamt_input)
        self.stamt_input = MDTextField(hint_text="ST_Amt", size_hint_x=None, width=200)
        grid_layout.add_widget(self.stamt_input)
        self.totalbill_input = MDTextField(hint_text="Total Bill", size_hint_x=None, width=200)
        grid_layout.add_widget(self.totalbill_input)
        
        main_layout.add_widget(grid_layout)

        #Button Layout
        btn_layout=MDBoxLayout(size_hint=(1, None), height=dp(50), spacing=10)
        btn_layout.md_bg_color = (1, 0.95, 0.85, 1)  # Light peach background

        add_button = MDRaisedButton(text="Add",on_release=self.save_checkout)
        btn_layout.add_widget(add_button)
        update_button = MDRaisedButton(text="Update")
        btn_layout.add_widget(update_button)
        delete_button = MDRaisedButton(text="Delete")
        btn_layout.add_widget(delete_button)
        search_button = MDRaisedButton(text="Search")
        btn_layout.add_widget(search_button)
        reset_button = MDRaisedButton(text="Reset")
        btn_layout.add_widget(reset_button)
        fetchmobileno_button = MDRaisedButton(text="Fetch Customer Mobile No",on_release=self.populate_mobileno)
        btn_layout.add_widget(fetchmobileno_button)
        
        main_layout.add_widget(btn_layout)

        #Data Table for Displaying Records
        table_layout = MDBoxLayout( padding=10)
        table_layout.md_bg_color = (0.9, 1, 0.9, 1)  # Light green background
        self.table = MDDataTable(
            size_hint=(1, None),
            height=dp(420),
            column_data=[
                ("ID", dp(15)),
                ("Mobile No", dp(20)),
                ("Name", dp(20)),
                ("Address", dp(25)),
                ("Room No", dp(20)),
                ("Category", dp(20)),
                ("Tariff", dp(20)),
                ("Inn_Dt", dp(20)),
                ("Out_Dt", dp(20)),
                ("Days Stayed", dp(20)),
                ("GST_Rate", dp(20)),
                ("ST_Rate", dp(20)),
                ("GST_Amt", dp(20)),
                ("ST_Amt", dp(20)),
                ("Total Bill", dp(30)),
                
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
        self.generate_checkoutid()
        self.generate_checkout_date()
        self.load_checkout_records_to_table()
        #Calling of Functions-1
        #Calling of Functions-2
        #Calling of Functions-3
        #Calling of Functions-4
        #Calling of Functions-5
        #Calling of Functions-6
        
    
    #============For Data Base , Autoid , Auto Registration No , Auto Current Date========================
    # checkoutid,mobileno,custname,address,roomno,roomcategory,roomtariff,checkinndt,checkoutdt,daysstayed,gstrate,strate,gstamt,stamt,totalbill
    def initialize_database(self):
        """Initialize the database and create the checkout table if it does not exist."""
        conn = sqlite3.connect("radision.db")
        cursor = conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS checkout (
                checkoutid INTEGER PRIMARY KEY AUTOINCREMENT,
                mobileno TEXT NOT NULL ,
                custname TEXT NOT NULL ,
                address TEXT NOT NULL ,
                roomno TEXT NOT NULL,
                roomcategory TEXT NOT NULL,
                roomtariff REAL NOT NULL,
                checkinndt TEXT NOT NULL,
                checkoutdt TEXT NOT NULL,
                daysstayed INTEGER NOT NULL,
                gstrate REAL NOT NULL,
                strate REAL NOT NULL,
                gstamt REAL NOT NULL,
                stamt REAL NOT NULL,
                totalbill REAL NOT NULL 
                
            )
        ''')
        conn.commit()
        conn.close()

    def generate_checkoutid(self):
        """Generate the next class ID."""
        conn = sqlite3.connect("radision.db")
        cursor = conn.cursor()
        cursor.execute("SELECT MAX(checkoutid) FROM checkout")
        last_checkoutid = cursor.fetchone()[0]
        self.checkoutid_input.text = str((last_checkoutid or 0) + 1)
        conn.close()

    
    def generate_checkout_date(self):
        """Set the current date in the date input field."""
        self.checkoutdt_input.text = datetime.now().strftime("%Y-%m-%d")

    
    #============For Populating Data from Other Table==================================

    def populate_mobileno(self, instance):
        conn = sqlite3.connect("radision.db")
        cursor = conn.cursor()
        try:
            cursor.execute("SELECT mobileno FROM checkinn ")
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
        self.fetch_checkinn_details(selected_mobileno)
        self.menu.dismiss()

    def fetch_checkinn_details(self, mobileno):
        conn = sqlite3.connect("radision.db")
        cursor = conn.cursor()
        try:
            cursor.execute(
                "SELECT custname, address,roomno , roomcategory , roomtariff , checkinndt FROM checkinn WHERE mobileno = ?", (mobileno,)
            )
            checkinn = cursor.fetchone()

            if not checkinn:
                self.show_confirmation_dialog(f"No details found for Mobile No {mobileno}.")
                return

            # Unpack and populate the input fields
            custname, address,roomno,roomcategory,roomtariff,checkinndt= checkinn
            self.custname_input.text = custname
            self.address_input.text = address
            self.roomno_input.text = roomno
            self.roomcategory_input.text = roomcategory
            self.roomtariff_input.text = str(roomtariff)
            self.checkinndt_input.text = checkinndt
            
        except Exception as e:
            self.show_confirmation_dialog(f"Error: {e}")
        finally:
            conn.close()
    #============For Adding/Saving Records and Loading Records to Table and Selection of Row from table==================================

    def save_checkout(self, *args):
        checkoutid=self.checkoutid_input.text.strip()
        mobileno=self.mobileno_input.text.strip()
        name=self.custname_input.text.strip()
        address=self.address_input.text.strip()
        roomno=self.roomno_input.text.strip()
        roomcategory=self.roomcategory_input.text.strip()
        roomtariff=self.roomtariff_input.text.strip()
        checkinndt=self.checkinndt_input.text.strip()
        checkoutdt=self.checkoutdt_input.text.strip()
        #daysstayed=self.daysstayed_input.text.strip()
        gstrate=self.gstrate_input.text.strip()
        strate=self.strate_input.text.strip()
        #gstamt=self.gstamt_input.text.strip()
        #stamt=self.stamt_input.text.strip()
        #totalbill=self.totalbill_input.text.strip()

        #==============Input Calculation===============
        if not all([checkoutid,mobileno,name,address,roomno,roomcategory,roomtariff,checkinndt,checkoutdt,gstrate , strate]):
            self.show_confirmation_dialog("Please fill all fields ")
            return
        
        checkin_date = datetime.strptime(checkinndt, "%Y-%m-%d")
        checkout_date = datetime.strptime(checkoutdt, "%Y-%m-%d")
        daysstayed=(checkout_date-checkin_date).days

        if daysstayed < 0:
                self.show_confirmation_dialog("Checkout date must be after check-in date.")
                return
        
        roomtariff=float(roomtariff)
        gstrate=float(gstrate)
        strate=float(strate)

        
        gstamt=round(daysstayed*roomtariff*gstrate/100,2)
        stamt=round(daysstayed*roomtariff*strate/100,2)
        totalbill=round(daysstayed*roomtariff+gstamt+stamt,2)

        self.daysstayed_input.text = str(daysstayed)
        self.gstamt_input.text=str(gstamt)
        self.stamt_input.text=str(stamt)
        self.totalbill_input.text=str(totalbill)

        # checkoutid,mobileno,custname,address,roomno,roomcategory,roomtariff,checkinndt,checkoutdt,daysstayed,gstrate,strate,gstamt,stamt,totalbill
        

        conn = sqlite3.connect("radision.db")
        cursor = conn.cursor()
        #floorid,floorno
        cursor.execute('''
            INSERT INTO checkout (checkoutid,mobileno,custname,address,roomno,roomcategory,roomtariff,checkinndt,checkoutdt,daysstayed,gstrate,strate,gstamt,stamt,totalbill)
            VALUES (?, ?,?,?,?,?,?,?,?,?,?,?,?,?,?)
        ''', (checkoutid,mobileno,name,address,roomno,roomcategory,roomtariff,checkinndt,checkoutdt,daysstayed,gstrate,strate,gstamt,stamt,totalbill))
        conn.commit()
        conn.close()
        self.show_confirmation_dialog("Customer Checkout saved successfully!")
        #self.reset_fields()
        self.load_checkout_records_to_table()
    def load_checkout_records_to_table(self):
        # checkoutid,mobileno,custname,address,roomno,roomcategory,roomtariff,checkinndt,checkoutdt,daysstayed,gstrate,strate,gstamt,stamt,totalbill
        self.table.row_data = []  # Clear previous data
        conn = sqlite3.connect("radision.db")
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM checkout ORDER BY checkoutid DESC")
        rows = cursor.fetchall()
        conn.close()
        self.table.row_data = [(str(r[0]), r[1],r[2],r[3],r[4],r[5],r[6],r[7],r[8],r[9],r[10],r[11],r[12],r[13],r[14]) for r in rows]
    
    def on_row_select(self, instance_table, instance_row):
        """Populate fields when a row is selected."""
        selected_row = instance_row.text
        for row in self.table.row_data:
            if row[0] == selected_row:
                self.checkoutid_input.text=row[0]
                self.mobileno_input.text=row[1]
                self.custname_input.text=str(row[2])
                self.address_input.text=row[3]
                self.roomno_input.text=row[4]
                self.roomcategory_input.text=row[5]
                self.roomtariff_input.text=str(row[6])
                self.checkinndt_input.text=row[7]
                self.checkoutdt_input.text=row[8]
                self.daysstayed_input.text=str(row[9])
                self.gstrate_input.text=str(row[10])
                self.strate_input.text=str(row[11])
                self.gstamt_input.text=str(row[12])
                self.stamt_input.text=str(row[13])
                self.totalbill_input.text=str(row[14])

                break
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

