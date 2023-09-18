# Made by Dorato, Nollan, Sarmiento
import customtkinter as ctk
import tkinter as tk
from tkinter import ttk
import sqlite3
from tkinter import messagebox
import customtkinter as ctk

# Windows
root = ctk.CTk()
root.title("Boarding House Management System")
root.geometry("1366x768")
root.maxsize(1366, 768)
appearance = ctk.set_appearance_mode("dark")

# Main Frame
main_frame = ctk.CTkFrame(root, width=1366, height=768, fg_color="#1B2936")
main_frame.pack(fill="both")

dashboard_frame = ctk.CTkFrame(main_frame, width=1000, height=700, fg_color="#213440")
dashboard_frame.place(relx=0.23, rely=0.05)
tenant_frame = ctk.CTkFrame(main_frame, width=1000, height=700, fg_color="#213440")

room_assignment_frame = ctk.CTkFrame(
    main_frame, width=1000, height=700, fg_color="#213440"
)
bill_frame = ctk.CTkFrame(main_frame, width=1000, height=700, fg_color="#213440")

payment_history_frame = ctk.CTkFrame(
    main_frame, width=1000, height=700, fg_color="#213440"
)
# Greetings
greetings_label = ctk.CTkLabel(
    dashboard_frame,
    text="Bahay ni Kuya \n Boarding House Management System",
    height=200,
    width=200,
    fg_color="#336082",
    corner_radius=10,
    font=("Caprasimo", 30),
)
greetings_label.place(relx=0.2, rely=0.3)

# Sub main frames
tree_tenant_frame = ttk.Frame(tenant_frame)
tree_emergency_frame = ttk.Frame(tenant_frame)
tree_room_assignment_frame = ttk.Frame(room_assignment_frame)
tree_bill_frame = ttk.Frame(bill_frame)
tree_payment_history_frame = ttk.Frame(payment_history_frame)

# Scrollbars
treeview_scrollbar_1 = ttk.Scrollbar(tree_tenant_frame)
treeview_scrollbar_2 = ttk.Scrollbar(tree_emergency_frame)
treeview_scrollbar_3 = ttk.Scrollbar(tree_room_assignment_frame)
treeview_scrollbar_4 = ttk.Scrollbar(tree_bill_frame)
treeview_scrollbar_5 = ttk.Scrollbar(tree_payment_history_frame)

# Create Treeviews
treeview_tenant = ttk.Treeview(
    tree_tenant_frame, yscrollcommand=treeview_scrollbar_1.set
)
treeview_emergency = ttk.Treeview(
    tree_emergency_frame, yscrollcommand=treeview_scrollbar_2.set
)
treeview_room_assignment = ttk.Treeview(
    tree_room_assignment_frame, yscrollcommand=treeview_scrollbar_3.set
)
treeview_bills = ttk.Treeview(tree_bill_frame, yscrollcommand=treeview_scrollbar_4.set)
treeview_payment_history = ttk.Treeview(
    tree_payment_history_frame, yscrollcommand=treeview_scrollbar_5.set
)


# Queries
def tenant_query():
    # Clear the Treeview
    data = treeview_tenant.get_children()
    for record in data:
        treeview_tenant.delete(record)

    # Create a new database or connecct to one that exists
    conn = sqlite3.connect("boarding_house.db")

    # Create a cursor instance
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM tenants")
    records = cursor.fetchall()

    # Display Data
    global count
    count = 0
    for data in records:
        if count % 2 == 0:
            treeview_tenant.insert(
                parent="",
                index=tk.END,
                iid=count,
                values=(
                    data[0],
                    data[1],
                    data[2],
                    data[3],
                    data[4],
                    data[5],
                    data[6],
                    data[7],
                    data[8],
                ),
                tags=("evenrow",),
            )
        else:
            treeview_tenant.insert(
                parent="",
                index=tk.END,
                iid=count,
                values=(
                    data[0],
                    data[1],
                    data[2],
                    data[3],
                    data[4],
                    data[5],
                    data[6],
                    data[7],
                    data[8],
                ),
                tags=("oddrow",),
            )
        count = count + 1

    # Commit changes
    conn.commit()

    # Close our connection
    conn.close()


def emergency_contacts_query():
    # Clear the Treeview
    data = treeview_emergency.get_children()
    for record in data:
        treeview_emergency.delete(record)

    # Create a new database or connecct to one that exists
    conn = sqlite3.connect("boarding_house.db")

    # Create a cursor instance
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM emergency_contact")
    records = cursor.fetchall()

    # Display Data
    global count
    count = 0
    for data in records:
        if count % 2 == 0:
            treeview_emergency.insert(
                parent="",
                index=tk.END,
                iid=count,
                values=(
                    data[0],
                    data[1],
                    data[2],
                    data[3],
                    data[4],
                    data[5],
                    data[6],
                    data[7],
                ),
                tags=("evenrow",),
            )
        else:
            treeview_emergency.insert(
                parent="",
                index=tk.END,
                iid=count,
                values=(
                    data[0],
                    data[1],
                    data[2],
                    data[3],
                    data[4],
                    data[5],
                    data[6],
                    data[7],
                ),
                tags=("oddrow",),
            )
        count = count + 1

    # Commit changes
    conn.commit()

    # Close our connection
    conn.close()


def room_assignment_query():
    # Clear the Treeview
    data = treeview_room_assignment.get_children()
    for record in data:
        treeview_room_assignment.delete(record)

    # Create a new database or connecct to one that exists
    conn = sqlite3.connect("boarding_house.db")

    # Create a cursor instance
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM room")
    records = cursor.fetchall()

    # Display Data
    global count
    count = 0
    for data in records:
        if count % 2 == 0:
            treeview_room_assignment.insert(
                parent="",
                index=tk.END,
                iid=count,
                values=(
                    data[0],
                    data[1],
                    data[2],
                    data[3],
                    data[4],
                    data[5],
                ),
                tags=("evenrow",),
            )
        else:
            treeview_room_assignment.insert(
                parent="",
                index=tk.END,
                iid=count,
                values=(
                    data[0],
                    data[1],
                    data[2],
                    data[3],
                    data[4],
                    data[5],
                ),
                tags=("oddrow",),
            )
        count = count + 1

    # Commit changes
    conn.commit()

    # Close our connection
    conn.close()


def bill_query():
    # Clear the Treeview
    data = treeview_bills.get_children()
    for record in data:
        treeview_bills.delete(record)

    # Create a new database or connecct to one that exists
    conn = sqlite3.connect("boarding_house.db")

    # Create a cursor instance
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM bills")
    records = cursor.fetchall()

    # Display Data
    global count
    count = 0
    for data in records:
        if count % 2 == 0:
            treeview_bills.insert(
                parent="",
                index=tk.END,
                iid=count,
                values=(
                    data[0],
                    data[1],
                    data[2],
                    data[3],
                    data[4],
                    data[5],
                    data[6],
                    data[7],
                ),
                tags=("evenrow",),
            )
        else:
            treeview_bills.insert(
                parent="",
                index=tk.END,
                iid=count,
                values=(
                    data[0],
                    data[1],
                    data[2],
                    data[3],
                    data[4],
                    data[5],
                    data[6],
                    data[7],
                ),
                tags=("oddrow",),
            )
        count = count + 1

    # Commit changes
    conn.commit()

    # Close our connection
    conn.close()


def payment_history_query():
    # Clear the Treeview
    data = treeview_payment_history.get_children()
    for record in data:
        treeview_payment_history.delete(record)

    # Create a new database or connecct to one that exists
    conn = sqlite3.connect("boarding_house.db")

    # Create a cursor instance
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM payment")
    records = cursor.fetchall()

    # Display Data
    global count
    count = 0
    for data in records:
        if count % 2 == 0:
            treeview_payment_history.insert(
                parent="",
                index=tk.END,
                iid=count,
                values=(
                    data[0],
                    data[1],
                    data[2],
                    data[3],
                    data[4],
                    data[5],
                    data[6],
                    data[7],
                ),
                tags=("evenrow",),
            )
        else:
            treeview_payment_history.insert(
                parent="",
                index=tk.END,
                iid=count,
                values=(
                    data[0],
                    data[1],
                    data[2],
                    data[3],
                    data[4],
                    data[5],
                    data[6],
                    data[7],
                ),
                tags=("oddrow",),
            )
        count = count + 1

    # Commit changes
    conn.commit()

    # Close our connection
    conn.close()


# Create the tables
def create_tables():
    # Database
    # Create a new database or connecct to one that exists
    conn = sqlite3.connect("boarding_house.db")

    # Create a cursor instance
    cursor = conn.cursor()

    # Create Tables
    cursor.execute(
        """ CREATE TABLE if not exists "tenants" (
	"Tenant_ID"	TEXT,
	"Tenant_Name"	TEXT,
	"Age"	INTEGER,
	"Gender"	TEXT,
	"Email"	TEXT,
	"Permanent_address"	TEXT,
	"Occupation"	TEXT,
	"Contact_number"	TEXT,
	"Number_of_EDevices"	TEXT,
	PRIMARY KEY("Tenant_ID")
    );
        """
    )

    cursor.execute(
        """ CREATE TABLE if not EXISTS "room" (
	"Room_ID"	TEXT,
	"Tenant_ID"	TEXT,
	"Rental_amount"	INTEGER,
	"Rent_date"	TEXT,
	"Due_date"	TEXT,
	"Electric_meter_number"	TEXT,
	FOREIGN KEY("Tenant_ID") REFERENCES "tenants"("Tenant_ID"),
	PRIMARY KEY("Room_ID")
    );
        """
    )

    cursor.execute(
        """ CREATE TABLE if not exists "emergency_contact" (
	"EC_Name"	TEXT,
	"Age"	INTEGER,
	"Sex"	TEXT,
	"Relationship"	TEXT,
	"Phone_number"	TEXT,
	"Email"	TEXT,
	"Address"	TEXT,
	"Tenant_ID"	TEXT,
	FOREIGN KEY("Tenant_ID") REFERENCES "tenants"("Tenant_ID")
    );
        """
    )

    cursor.execute(
        """ CREATE TABLE if not EXISTS "bills" (
	"Bill_ID"	INTEGER,
	"Room_ID"	TEXT,
	"Tenant_ID"	TEXT,
	"Bill_Name"	TEXT,
	"Previous_consumption"	TEXT,
	"Current_consumption"	TEXT,
	"Rate"	TEXT,
	"Cost"	INTEGER,
	FOREIGN KEY("Room_ID") REFERENCES "room"("Room_ID"),
	FOREIGN KEY("Tenant_ID") REFERENCES "tenants"("Tenant_ID"),
	PRIMARY KEY("Bill_ID" AUTOINCREMENT)
    );
        """
    )

    cursor.execute(
        """ CREATE TABLE if not EXISTS "payment" (
	"Payment_ID"	TEXT,
	"Room_ID"	TEXT,
	"Tenant_ID"	TEXT,
	"Payment_Name"	TEXT,
	"Payment_date"	TEXT,
	"Payment_amount"	INTEGER,
	"Payment_method"	TEXT,
	"Status"	TEXT,
	FOREIGN KEY("Tenant_ID") REFERENCES "tenants"("Tenant_ID"),
	FOREIGN KEY("Room_ID") REFERENCES "room"("Room_ID"),
	PRIMARY KEY("Payment_ID")
    );
        """
    )

    # Commit changes
    conn.commit()
    # Close oour connection
    conn.close()


# Treeview Functions
def tenant_treeview():
    global treeview_scrollbar_1
    # Tree tenant frame
    tree_tenant_frame.place(relx=0.01, rely=0.2, width=1040)

    # Scrollabar
    treeview_scrollbar_1.pack(side="right", fill="y")

    # Display Treeview
    treeview_tenant.pack(side="left")

    # Configure the Scrollbar
    treeview_scrollbar_1.config(command=treeview_tenant.yview)

    # Define our columns
    fieldnames = [
        "Tenant_ID",
        "Tenant_Name",
        "Age",
        "Gender",
        "Email",
        "Permanent_address",
        "Occupation",
        "Contact_number",
        "Number_of_EDevices",
    ]
    treeview_tenant["columns"] = fieldnames

    # Format our columns
    treeview_tenant.column("#0", stretch="NO", width=0)
    treeview_tenant.column("Tenant_ID", anchor="center", width=85)
    treeview_tenant.column("Tenant_Name", anchor="w", width=150)
    treeview_tenant.column("Age", anchor="center", width=30)
    treeview_tenant.column("Gender", anchor="center", width=50)
    treeview_tenant.column("Email", anchor="w", width=200)
    treeview_tenant.column("Permanent_address", anchor="w", width=200)
    treeview_tenant.column("Occupation", anchor="center", width=150)
    treeview_tenant.column("Contact_number", anchor="center", width=100)
    treeview_tenant.column("Number_of_EDevices", anchor="center", width=50)

    # Format our headings
    treeview_tenant.heading("#0", text="", anchor="w")
    treeview_tenant.heading("Tenant_ID", text="Tenant_ID", anchor="center")
    treeview_tenant.heading("Tenant_Name", text="Tenant_Name", anchor="center")
    treeview_tenant.heading("Age", text="Age", anchor="center")
    treeview_tenant.heading("Gender", text="Gender", anchor="center")
    treeview_tenant.heading("Email", text="Email", anchor="center")
    treeview_tenant.heading(
        "Permanent_address", text="Permanent_address", anchor="center"
    )
    treeview_tenant.heading("Occupation", text="Occupation", anchor="center")
    treeview_tenant.heading("Contact_number", text="Contact_number", anchor="center")
    treeview_tenant.heading("Number_of_EDevices", text="Devices", anchor="center")
    # Create Striped Row Tags
    treeview_tenant.tag_configure("oddrow", background="white")
    treeview_tenant.tag_configure("evenrow", background="lightblue")


def emergency_contact_treeview():
    # Tree tenant frame
    tree_emergency_frame.place(relx=0.03, rely=0.65, width=1000)

    # Scrollabar
    treeview_scrollbar_2.pack(side="right", fill="y")

    # Display Treeview
    treeview_emergency.pack(side="left")

    # Configure the Scrollbar
    treeview_scrollbar_2.config(command=treeview_emergency.yview)

    # Define our columns
    fieldnames = [
        "EC_Name",
        "Age",
        "Sex",
        "Relationship",
        "Phone_Number",
        "Email",
        "Address",
        "Tenant_ID",
    ]
    treeview_emergency["columns"] = fieldnames

    # Format our columns
    treeview_emergency.column("#0", stretch="NO", width=0)
    treeview_emergency.column("EC_Name", anchor="center", width=120)
    treeview_emergency.column("Age", anchor="center", width=40)
    treeview_emergency.column("Sex", anchor="center", width=50)
    treeview_emergency.column("Relationship", anchor="center", width=80)
    treeview_emergency.column("Phone_Number", anchor="center", width=120)
    treeview_emergency.column("Email", anchor="center", width=150)
    treeview_emergency.column("Address", anchor="w", width=300)
    treeview_emergency.column("Tenant_ID", anchor="center", width=120)

    # Format our headings

    treeview_emergency.heading("#0", text="", anchor="w")
    treeview_emergency.heading("EC_Name", text="Name", anchor="center")
    treeview_emergency.heading("Age", text="Age", anchor="center")
    treeview_emergency.heading("Sex", text="Sex", anchor="center")
    treeview_emergency.heading("Relationship", text="Relationship", anchor="center")
    treeview_emergency.heading("Phone_Number", text="Phone_Number", anchor="center")
    treeview_emergency.heading("Email", text="Email", anchor="center")
    treeview_emergency.heading("Address", text="Address", anchor="center")
    treeview_emergency.heading("Tenant_ID", text="Tenant_ID", anchor="center")

    # Create Striped Row Tags
    treeview_emergency.tag_configure("oddrow", background="white")
    treeview_emergency.tag_configure("evenrow", background="lightblue")


def room_assignment_treeview():
    # Tree tenant frame
    tree_room_assignment_frame.place(relx=0.01, rely=0.2, width=1000, height=350)

    # Scrollabar
    treeview_scrollbar_3.pack(side="right", fill="y")

    # Display Treeview
    treeview_room_assignment.pack(side="left", fill="both")

    # Configure the Scrollbar
    treeview_scrollbar_3.config(command=treeview_room_assignment.yview)

    # Define our columns
    fieldnames = [
        "Room_ID",
        "Tenant_ID",
        "Rental_amount",
        "Rent_date",
        "Due_date",
        "Electric_meter_number",
    ]
    treeview_room_assignment["columns"] = fieldnames

    # Format our columns
    treeview_room_assignment.column("#0", stretch="NO", width=0)
    treeview_room_assignment.column("Room_ID", anchor="center", width=100)
    treeview_room_assignment.column("Tenant_ID", anchor="center", width=150)
    treeview_room_assignment.column("Rental_amount", anchor="center", width=175)
    treeview_room_assignment.column("Rent_date", anchor="center", width=175)
    treeview_room_assignment.column("Due_date", anchor="center", width=150)
    treeview_room_assignment.column("Electric_meter_number", anchor="center", width=250)

    # Format our headings

    treeview_room_assignment.heading("#0", text="", anchor="w")
    treeview_room_assignment.heading("Room_ID", text="Room_ID", anchor="center")
    treeview_room_assignment.heading("Tenant_ID", text="Tenant_ID", anchor="center")
    treeview_room_assignment.heading(
        "Rental_amount", text="Rental_amount", anchor="center"
    )
    treeview_room_assignment.heading("Rent_date", text="Rent_date", anchor="center")
    treeview_room_assignment.heading("Due_date", text="Due_date", anchor="center")
    treeview_room_assignment.heading(
        "Electric_meter_number", text="Electric_meter_number", anchor="center"
    )

    # Create Striped Row Tags
    treeview_room_assignment.tag_configure("oddrow", background="white")
    treeview_room_assignment.tag_configure("evenrow", background="lightblue")


def bills_treeview():
    # Tree tenant frame
    tree_bill_frame.place(relx=0.01, rely=0.2, width=1000, height=500)

    # Scrollabar
    treeview_scrollbar_4.pack(side="right", fill="y")

    # Display Treeview
    treeview_bills.pack(side="left", fill="both")

    # Configure the Scrollbar
    treeview_scrollbar_4.config(command=treeview_bills.yview)

    # Define our columns
    fieldnames = [
        "Bill_ID",
        "Room_ID",
        "Tenant_ID",
        "Bill_Name",
        "Previous_Consumption",
        "Current_Consumption",
        "Rate",
        "Cost",
    ]
    treeview_bills["columns"] = fieldnames

    # Format our columns
    treeview_bills.column("#0", stretch="NO", width=0)
    treeview_bills.column("Bill_ID", anchor="center", width=110)
    treeview_bills.column("Room_ID", anchor="center", width=60)
    treeview_bills.column("Tenant_ID", anchor="center", width=150)
    treeview_bills.column("Bill_Name", anchor="center", width=150)
    treeview_bills.column("Previous_Consumption", anchor="center", width=150)
    treeview_bills.column("Current_Consumption", anchor="center", width=150)
    treeview_bills.column("Rate", anchor="center", width=80)
    treeview_bills.column("Cost", anchor="center", width=140)

    # Format our headings
    treeview_bills.heading("#0", text="", anchor="w")
    treeview_bills.heading("Bill_ID", text="Bill_ID", anchor="center")
    treeview_bills.heading("Room_ID", text="Room_ID", anchor="center")
    treeview_bills.heading("Tenant_ID", text="Tenant_ID", anchor="center")
    treeview_bills.heading("Bill_Name", text="Bill_Name", anchor="center")
    treeview_bills.heading(
        "Previous_Consumption", text="Previous_Consumption", anchor="center"
    )
    treeview_bills.heading(
        "Current_Consumption", text="Current_Consumptiont", anchor="center"
    )
    treeview_bills.heading("Rate", text="Rate", anchor="center")
    treeview_bills.heading("Cost", text="Cost", anchor="center")

    # Create Striped Row Tags
    treeview_bills.tag_configure("oddrow", background="white")
    treeview_bills.tag_configure("evenrow", background="lightblue")


def payment_history_treeview():
    # Tree tenant frame
    tree_payment_history_frame.place(relx=0.01, rely=0.2, width=1000, height=500)

    # Scrollabar
    treeview_scrollbar_5.pack(side="right", fill="y")

    # Create Treeview
    treeview_payment_history.pack(side="left", fill="both")

    # Configure the Scrollbar
    treeview_scrollbar_5.config(command=treeview_payment_history.yview)

    # Define our columns
    fieldnames = [
        "Payment_ID",
        "Room_ID",
        "Tenant_ID",
        "Payment_Name",
        "Payment_date",
        "Payment_amount",
        "Payment_method",
        "Status",
    ]
    treeview_payment_history["columns"] = fieldnames

    # Format our columns
    treeview_payment_history.column("#0", stretch="NO", width=0)
    treeview_payment_history.column("Payment_ID", anchor="center", width=110)
    treeview_payment_history.column("Room_ID", anchor="center", width=60)
    treeview_payment_history.column("Tenant_ID", anchor="center", width=150)
    treeview_payment_history.column("Payment_Name", anchor="center", width=150)
    treeview_payment_history.column("Payment_date", anchor="center", width=130)
    treeview_payment_history.column("Payment_amount", anchor="center", width=125)
    treeview_payment_history.column("Payment_method", anchor="center", width=125)
    treeview_payment_history.column("Status", anchor="center", width=128)
    treeview_payment_history.column("Payment_method", anchor="center", width=125)

    # Format our headings
    treeview_payment_history.heading("#0", text="", anchor="w")
    treeview_payment_history.heading("Payment_ID", text="Payment_ID", anchor="center")
    treeview_payment_history.heading("Room_ID", text="Room_ID", anchor="center")
    treeview_payment_history.heading("Tenant_ID", text="Tenant Name", anchor="center")
    treeview_payment_history.heading(
        "Payment_Name", text="Payment Name", anchor="center"
    )
    treeview_payment_history.heading(
        "Payment_date", text="Payment Date", anchor="center"
    )
    treeview_payment_history.heading(
        "Payment_amount", text="Payment Amount", anchor="center"
    )
    treeview_payment_history.heading(
        "Payment_method", text="Payment Method", anchor="center"
    )
    treeview_payment_history.heading("Status", text="Status", anchor="center")

    # Create Striped Row Tags
    treeview_payment_history.tag_configure("oddrow", background="white")
    treeview_payment_history.tag_configure("evenrow", background="lightblue")


# Checker whether there is a tenant or not in the room
def tenant_checker(selected=None):
    # Create a new database or connecct to one that exists
    conn = sqlite3.connect("boarding_house.db")

    # Create a cursor instance
    cursor = conn.cursor()

    cursor.execute(
        """SELECT room.Tenant_ID, tenants.Tenant_ID, count(*) as rented
        FROM room
        INNER JOIN tenants
        ON room.Tenant_ID = tenants.Tenant_ID
        GROUP by room.Tenant_ID"""
    )

    result = cursor.fetchall()
    print(result)
    for room in result:
        t_id, _, count = room
        if t_id == selected and count != 0:
            return False

    return True


# Checker whether foreign key in tables is empty
def strings_checker(user_input=None):
    if user_input == "":
        return False
    else:
        return True


# Verifier for unique ID
def unique_tenant_id_verifier(id_verifier=None):
    # Create a new database or connect to one that exists
    conn = sqlite3.connect("boarding_house.db")
    # Create a cursor instance
    cursor = conn.cursor()

    # Adding New Student
    cursor.execute(
        "SELECT COUNT(*) FROM tenants WHERE Tenant_ID like ?", ((id_verifier,))
    )
    result = cursor.fetchone()
    print(result)
    for data in result:
        if data != 0:
            return False

    return True


def unique_room_id_verifier(id_verifier=None):
    # Create a new database or connect to one that exists
    conn = sqlite3.connect("boarding_house.db")
    # Create a cursor instance
    cursor = conn.cursor()

    # Adding New Student
    cursor.execute("SELECT COUNT(*) FROM room WHERE Room_ID like ?", ((id_verifier,)))
    result = cursor.fetchone()
    print(result)
    for data in result:
        if data != 0:
            return False

    return True


def unique_bill_id_verifier(id_verifier=None):
    # Create a new database or connect to one that exists
    conn = sqlite3.connect("boarding_house.db")
    # Create a cursor instance
    cursor = conn.cursor()

    # Adding New Student
    cursor.execute("SELECT COUNT(*) FROM bills WHERE Bill_ID like ?", ((id_verifier,)))
    result = cursor.fetchone()
    print(result)
    for data in result:
        if data != 0:
            return False

    return True


def unique_payment_id_verifier(id_verifier=None):
    # Create a new database or connect to one that exists
    conn = sqlite3.connect("boarding_house.db")
    # Create a cursor instance
    cursor = conn.cursor()

    # Adding New Student
    cursor.execute(
        "SELECT COUNT(*) FROM payment WHERE Payment_ID like ?", ((id_verifier,))
    )
    result = cursor.fetchone()
    print(result)
    for data in result:
        if data != 0:
            return False

    return True


# Tenant Functions
def add_new_tenant():
    # Create a new database or connect to one that exists
    conn = sqlite3.connect("boarding_house.db")
    # Create a cursor instance
    cursor = conn.cursor()
    id_to_verify = tenant_id_entry.get()
    if unique_tenant_id_verifier(id_to_verify):
        # Adding New Tenant Info
        cursor.execute(
            "INSERT INTO tenants VALUES (:Tenant_ID, :Tenant_Name, :Age, :Gender, :Email, :Permanent_address, :Occupation, :Contact_number, :Number_of_EDevices )",
            {
                "Tenant_ID": tenant_id_entry.get(),
                "Tenant_Name": tenant_name_entry.get(),
                "Age": age_entry.get(),
                "Gender": gender_entry.get(),
                "Email": email_entry.get(),
                "Permanent_address": address_entry.get(),
                "Occupation": occupation_entry.get(),
                "Contact_number": contact_number_entry.get(),
                "Number_of_EDevices": number_of_edevices_entry.get(),
            },
        )

        # Commit changes
        conn.commit()

        # Close our connection
        conn.close()

        # Clear Entry Boxes
        clear_entries_tenants()

        # Clear the Treeview Table
        treeview_tenant.delete(*treeview_tenant.get_children())

        # Run the query_database again
        tenant_query()
        messagebox.showinfo("Added", "Tenant info added successfully.")
    else:
        messagebox.showinfo("Notice", "Please enter a unique ID.")


def delete_tenant():
    response = messagebox.askyesno(
        "WARNING!",
        "Are you sure you want to delete the data from the table?",
    )
    if response == 1:
        # Designate selections
        selected = treeview_tenant.selection()

        # Create a list of IDs to delete
        ids_to_delete = []

        # Loop through the data from the treeview
        for ids in selected:
            ids_to_delete.append(treeview_tenant.item(ids, "values")[0])

        # Delete from Treeview
        for record in selected:
            treeview_tenant.delete(record)

        # Create a new database or connect to one that exists
        conn = sqlite3.connect("boarding_house.db")
        # Create a cursor instance
        cursor = conn.cursor()

        # Delete Selected Tenant Info
        cursor.executemany(
            "DELETE FROM tenants WHERE Tenant_ID = ?", [(a,) for a in ids_to_delete]
        )
        cursor.executemany(
            "DELETE FROM emergency_contact WHERE Tenant_ID = ?",
            [(a,) for a in ids_to_delete],
        )

        # Commit changes
        conn.commit()

        # Close our connection
        conn.close()

        # Add a little message box for fun
        messagebox.showinfo("Deleted!", "Tenant Info Has Been Deleted!")
        tenant_query()
        emergency_contacts_query()


def update_tenant_info():
    # Grab record numbers
    selected = treeview_tenant.focus()

    # Update Record
    treeview_tenant.item(
        selected,
        text="",
        values=(
            tenant_id_entry.get(),
            tenant_name_entry.get(),
            age_entry.get(),
            gender_entry.get(),
            email_entry.get(),
            address_entry.get(),
            occupation_entry.get(),
            contact_number_entry.get(),
            number_of_edevices_entry.get(),
        ),
    )
    # Update data to the database
    # Create a new database or connect to one that exists
    conn = sqlite3.connect("boarding_house.db")

    # Create a cursor instance
    cursor = conn.cursor()

    cursor.execute(
        """UPDATE tenants SET
                   Tenant_Name = :Tenant_Name,
                   Age = :Age,
                   Gender = :Gender,
                   Email = :Email,
                   Permanent_address = :Permanent_address,
                   Occupation = :Occupation,
                   Contact_number = :Contact_number,
                   Number_of_EDevices = :Number_of_EDevices
                   
                   WHERE Tenant_ID = :Tenant_ID""",
        {
            "Tenant_Name": tenant_name_entry.get(),
            "Age": age_entry.get(),
            "Gender": gender_entry.get(),
            "Email": email_entry.get(),
            "Permanent_address": address_entry.get(),
            "Occupation": occupation_entry.get(),
            "Contact_number": contact_number_entry.get(),
            "Number_of_EDevices": number_of_edevices_entry.get(),
            "Tenant_ID": tenant_id_entry.get(),
        },
    )

    # Commit changes
    conn.commit()

    # Close our connection
    conn.close()
    # Clear Entry Boxes
    clear_entries_tenants()
    # Add a little message box for fun
    messagebox.showinfo("Updated!", "Tenant Info has been updated!")


def search_tenant_id():
    lookup_records = search_tenant_entry.get()

    # Clear the Treeview
    data = treeview_tenant.get_children()
    for record in data:
        treeview_tenant.delete(record)

    # Create a new database or connecct to one that exists
    conn = sqlite3.connect("boarding_house.db")

    # Create a cursor instance
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM tenants WHERE Tenant_ID like ?", ((lookup_records,)))
    records = cursor.fetchall()
    if records:
        messagebox.showinfo("Success", "We have found the data.")
        # Display Data
        global count
        count = 0
        for data in records:
            if count % 2 == 0:
                treeview_tenant.insert(
                    parent="",
                    index=tk.END,
                    iid=count,
                    values=(
                        data[0],
                        data[1],
                        data[2],
                        data[3],
                        data[4],
                        data[5],
                        data[6],
                        data[7],
                        data[8],
                    ),
                    tags=("evenrow",),
                )
            else:
                treeview_tenant.insert(
                    parent="",
                    index=tk.END,
                    iid=count,
                    values=(
                        data[0],
                        data[1],
                        data[2],
                        data[3],
                        data[4],
                        data[5],
                        data[6],
                        data[7],
                        data[8],
                    ),
                    tags=("oddrow",),
                )
            count = count + 1

        # Commit changes
        conn.commit()

        # Close our connection
        conn.close()
    else:
        messagebox.showinfo(
            "Notice!", "Unfortunately, your data is not found in the database."
        )
        tenant_query()


# EC Tenant Functions
def add_ec_tenant_info():
    # Create a new database or connect to one that exists
    conn = sqlite3.connect("boarding_house.db")
    # Create a cursor instance
    cursor = conn.cursor()

    checker = tenants_id_entry.get()
    print(checker)
    if strings_checker(checker):
        print(strings_checker(checker))
        # Adding New EC_Tenant Information
        cursor.execute(
            "INSERT INTO emergency_contact VALUES (:EC_Name, :Age, :Sex, :Relationship, :Phone_Number, :Email, :Address, :Tenant_ID )",
            {
                "EC_Name": ec_tenant_name_entry.get(),
                "Age": ec_age_entry.get(),
                "Sex": ec_sex_entry.get(),
                "Relationship": ec_relationship_entry.get(),
                "Phone_Number": ec_contact_number_entry.get(),
                "Email": ec_email_entry.get(),
                "Address": ec_address_entry.get(),
                "Tenant_ID": tenants_id_entry.get(),
            },
        )

        # Commit changes
        conn.commit()

        # Close our connection
        conn.close()

        # Clear Entry Boxes
        clear_entries_ec_tenants()

        # Clear the Treeview Table
        treeview_emergency.delete(*treeview_emergency.get_children())

        # Run the query_database again
        emergency_contacts_query()
        messagebox.showinfo("Added", "EC_Tenant info added successfully.")
    else:
        messagebox.showinfo(
            "Error.",
            "Please select the appropriate tenant for their emergency contact.",
        )


def delete_ec_tenant_info():
    response = messagebox.askyesno(
        "WARNING!",
        "Are you sure you want to delete the data from the table?",
    )
    if response == 1:
        # Designate selections
        selected = treeview_emergency.selection()

        # Create a list of IDs to delete
        ec_name_to_delete = []

        # Loop through the data from the treeview
        for names in selected:
            ec_name_to_delete.append(treeview_emergency.item(names, "values")[0])

        # Delete from Treeview
        for record in selected:
            treeview_emergency.delete(record)

        # Create a new database or connect to one that exists
        conn = sqlite3.connect("boarding_house.db")
        # Create a cursor instance
        cursor = conn.cursor()

        # Delete Selected Student Info
        cursor.executemany(
            "DELETE FROM emergency_contact WHERE EC_Name = ?",
            [(a,) for a in ec_name_to_delete],
        )

        # Commit changes
        conn.commit()

        # Close our connection
        conn.close()

        # Add a little message box for fun
        messagebox.showinfo("Deleted!", "EC_Tenant Info Has Been Deleted!")


def update_ec_tenant_info():
    # Grab record numbers
    selected = treeview_emergency.focus()
    # Update Record
    treeview_emergency.item(
        selected,
        text="",
        values=(
            ec_tenant_name_entry.get(),
            ec_age_entry.get(),
            ec_sex_entry.get(),
            ec_relationship_entry.get(),
            ec_contact_number_entry.get(),
            ec_email_entry.get(),
            ec_address_entry.get(),
            update_tenants_id_entry.get(),
        ),
    )
    # Update data to the database
    # Create a new database or connect to one that exists
    conn = sqlite3.connect("boarding_house.db")

    # Create a cursor instance
    cursor = conn.cursor()

    cursor.execute(
        """UPDATE emergency_contact SET
                   EC_Name = :EC_Name,
                   Age = :Age,
                   Sex = :Sex,
                   Relationship = :Relationship,
                   Phone_number = :Phone_number,
                   Email = :Email,
                   Address = :Address
                   
                   WHERE Tenant_ID = :Tenant_ID""",
        {
            "EC_Name": ec_tenant_name_entry.get(),
            "Age": ec_age_entry.get(),
            "Sex": ec_sex_entry.get(),
            "Relationship": ec_relationship_entry.get(),
            "Phone_number": ec_contact_number_entry.get(),
            "Email": ec_email_entry.get(),
            "Address": ec_address_entry.get(),
            "Tenant_ID": update_tenants_id_entry.get(),
        },
    )

    # Commit changes
    conn.commit()

    # Close our connection
    conn.close()
    # Clear Entry Boxes
    clear_entries_ec_tenants()
    # Add a little message box for fun
    messagebox.showinfo("Updated!", "EC_Tenant Info has been updated!")


def search_ec_tenant_info():
    lookup_records = search_ETenant_entry.get()

    # Clear the Treeview
    data = treeview_emergency.get_children()
    for record in data:
        treeview_emergency.delete(record)

    # Create a new database or connecct to one that exists
    conn = sqlite3.connect("boarding_house.db")

    # Create a cursor instance
    cursor = conn.cursor()

    cursor.execute(
        "SELECT * FROM emergency_contact WHERE Tenant_ID like ?", ((lookup_records,))
    )
    records = cursor.fetchall()
    if records:
        messagebox.showinfo("Success", "We have found the data.")
        # Display Data
        global count
        count = 0
        for data in records:
            if count % 2 == 0:
                treeview_emergency.insert(
                    parent="",
                    index=tk.END,
                    iid=count,
                    values=(
                        data[0],
                        data[1],
                        data[2],
                        data[3],
                        data[4],
                        data[5],
                        data[6],
                        data[7],
                    ),
                    tags=("evenrow",),
                )
            else:
                treeview_emergency.insert(
                    parent="",
                    index=tk.END,
                    iid=count,
                    values=(
                        data[0],
                        data[1],
                        data[2],
                        data[3],
                        data[4],
                        data[5],
                        data[6],
                        data[7],
                    ),
                    tags=("oddrow",),
                )
            count = count + 1

        # Commit changes
        conn.commit()

        # Close our connection
        conn.close()
    else:
        messagebox.showinfo(
            "Notice!", "Unfortunately, your data is not found in the database."
        )
        emergency_contacts_query()


# Room Functions
def add_room_info():
    # Create a new database or connect to one that exists
    conn = sqlite3.connect("boarding_house.db")
    # Create a cursor instance
    cursor = conn.cursor()
    id_to_verify = room_ID_entry.get()
    if unique_room_id_verifier(id_to_verify):
        # Adding New Room Information
        cursor.execute(
            "INSERT INTO room VALUES (:Room_ID, :Tenant_ID, :Rental_amount, :Rent_Date, :Due_Date, :Electric_meter_number )",
            {
                "Room_ID": room_ID_entry.get(),
                "Tenant_ID": room_tenant_entry.get(),
                "Rental_amount": rental_amount_entry.get(),
                "Rent_Date": rent_date_entry.get(),
                "Due_Date": due_date_entry.get(),
                "Electric_meter_number": electric_meter_number_entry.get(),
            },
        )

        # Commit changes
        conn.commit()

        # Close our connection
        conn.close()

        # Clear Entry Boxes
        clear_room_entries()

        # Clear the Treeview Table
        treeview_room_assignment.delete(*treeview_room_assignment.get_children())

        # Run the query_database again
        room_assignment_query()
        messagebox.showinfo("Added", "Room info added successfully.")
    else:
        messagebox.showinfo("Notice", "Please enter a unique ID.")


def delete_room_info():
    response = messagebox.askyesno(
        "WARNING!",
        "Are you sure you want to delete the data from the table?",
    )
    if response == 1:
        # Designate selections
        selected = treeview_room_assignment.selection()
        for data in selected:
            room_id_to_delete = treeview_room_assignment.item(data, "values")[1]
        if tenant_checker(room_id_to_delete):
            # Create a list of IDs to delete
            ids_name_to_delete = []

            # Loop through the data from the treeview
            for ids in selected:
                ids_name_to_delete.append(
                    treeview_room_assignment.item(ids, "values")[0]
                )

            # Delete from Treeview
            for record in selected:
                treeview_room_assignment.delete(record)

            # Create a new database or connect to one that exists
            conn = sqlite3.connect("boarding_house.db")
            # Create a cursor instance
            cursor = conn.cursor()

            # Delete Selected Student Info
            cursor.executemany(
                "DELETE FROM room WHERE Room_ID = ?",
                [(a,) for a in ids_name_to_delete],
            )

            # Commit changes
            conn.commit()

            # Close our connection
            conn.close()

            # Add a little message box for fun
            messagebox.showinfo("Deleted!", "Room Info Has Been Deleted!")
        else:
            messagebox.showinfo(
                "Delete Cancelled.", "Cannot delete the room since it is occupied."
            )


def update_room_info():
    # Grab record numbers
    selected = treeview_room_assignment.focus()
    # Update Record
    treeview_room_assignment.item(
        selected,
        text="",
        values=(
            room_ID_entry.get(),
            room_tenant_entry.get(),
            rental_amount_entry.get(),
            rent_date_entry.get(),
            due_date_entry.get(),
            electric_meter_number_entry.get(),
        ),
    )
    # Update data to the database
    # Create a new database or connect to one that exists
    conn = sqlite3.connect("boarding_house.db")

    # Create a cursor instance
    cursor = conn.cursor()

    cursor.execute(
        """UPDATE room SET
                   Tenant_ID = :Tenant_ID,
                   Rental_amount = :Rental_amount,
                   Rent_Date = :Rent_Date,
                   Due_Date = :Due_Date,
                   Electric_meter_number = :Electric_meter_number
                   
                   WHERE Room_ID = :Room_ID""",
        {
            "Tenant_ID": room_tenant_entry.get(),
            "Rental_amount": rental_amount_entry.get(),
            "Rent_Date": rent_date_entry.get(),
            "Due_Date": due_date_entry.get(),
            "Electric_meter_number": electric_meter_number_entry.get(),
            "Room_ID": room_ID_entry.get(),
        },
    )

    # Commit changes
    conn.commit()

    # Close our connection
    conn.close()
    # Clear Entry Boxes
    clear_room_entries()
    # Add a little message box for fun
    messagebox.showinfo("Updated!", "Room Info has been updated!")


def search_room_info():
    lookup_records = search_room_entry.get()

    # Clear the Treeview
    data = treeview_room_assignment.get_children()
    for record in data:
        treeview_room_assignment.delete(record)

    # Create a new database or connecct to one that exists
    conn = sqlite3.connect("boarding_house.db")

    # Create a cursor instance
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM room WHERE Room_ID like ?", ((lookup_records,)))
    records = cursor.fetchall()
    if records:
        messagebox.showinfo("Success", "We have found the data.")
        # Display Data
        global count
        count = 0
        for data in records:
            if count % 2 == 0:
                treeview_room_assignment.insert(
                    parent="",
                    index=tk.END,
                    iid=count,
                    values=(
                        data[0],
                        data[1],
                        data[2],
                        data[3],
                        data[4],
                        data[5],
                    ),
                    tags=("evenrow",),
                )
            else:
                treeview_room_assignment.insert(
                    parent="",
                    index=tk.END,
                    iid=count,
                    values=(
                        data[0],
                        data[1],
                        data[2],
                        data[3],
                        data[4],
                        data[5],
                    ),
                    tags=("oddrow",),
                )
            count = count + 1

        # Commit changes
        conn.commit()

        # Close our connection
        conn.close()
    else:
        messagebox.showinfo(
            "Notice!", "Unfortunately, your data is not found in the database."
        )
        room_assignment_query()


# Bills Functions
def add_bills_info():
    # Create a new database or connect to one that exists
    conn = sqlite3.connect("boarding_house.db")
    # Create a cursor instance
    cursor = conn.cursor()

    checking_string1 = room_id_entry.get()
    checking_string2 = tenant_ID_entry.get()
    id_to_verify = bill_id_entry.get()
    if (
        unique_bill_id_verifier(id_to_verify)
        and strings_checker(checking_string1)
        and strings_checker(checking_string2)
    ):
        # Adding New Bill Information
        cursor.execute(
            "INSERT INTO bills VALUES (:Bill_ID, :Room_ID, :Tenant_ID, :Bill_Name, :Previous_consumption, :Current_consumption, :Rate, :Cost )",
            {
                "Bill_ID": bill_id_entry.get(),
                "Room_ID": room_id_entry.get(),
                "Tenant_ID": tenant_ID_entry.get(),
                "Bill_Name": bill_name_entry.get(),
                "Previous_consumption": prev_entry.get(),
                "Current_consumption": current_entry.get(),
                "Rate": rate_entry.get(),
                "Cost": cost_entry.get(),
            },
        )

        # Commit changes
        conn.commit()

        # Close our connection
        conn.close()

        # Clear the Treeview Table
        treeview_bills.delete(*treeview_bills.get_children())

        # Run the query_database again
        bill_query()
        messagebox.showinfo("Added", "Bill info added successfully.")
    else:
        messagebox.showinfo(
            "Notice", "Please enter a unique ID or enter the appropriate IDs."
        )


def delete_bills_info():
    response = messagebox.askyesno(
        "WARNING!",
        "Are you sure you want to delete the data from the table?",
    )
    if response == 1:
        # Designate selections
        selected = treeview_bills.selection()

        # Create a list of IDs to delete
        ids_to_delete = []

        # Loop through the data from the treeview
        for ids in selected:
            ids_to_delete.append(treeview_bills.item(ids, "values")[0])

        # Delete from Treeview
        for record in selected:
            treeview_bills.delete(record)

        # Create a new database or connect to one that exists
        conn = sqlite3.connect("boarding_house.db")
        # Create a cursor instance
        cursor = conn.cursor()

        # Delete Selected Student Info
        cursor.executemany(
            "DELETE FROM bills WHERE Bill_ID = ?",
            [(a,) for a in ids_to_delete],
        )

        # Commit changes
        conn.commit()

        # Close our connection
        conn.close()

        # Add a little message box for fun
        messagebox.showinfo("Deleted!", "Bill Info Has Been Deleted!")


def update_bills_info():
    # Grab record numbers
    selected = treeview_bills.focus()
    # Update Record
    treeview_bills.item(
        selected,
        text="",
        values=(
            bill_id_entry.get(),
            update_room_id_entry.get(),
            update_tenant_ID_entry.get(),
            bill_name_entry.get(),
            prev_entry.get(),
            current_entry.get(),
            rate_entry.get(),
            cost_entry.get(),
        ),
    )
    # Update data to the database
    # Create a new database or connect to one that exists
    conn = sqlite3.connect("boarding_house.db")

    # Create a cursor instance
    cursor = conn.cursor()

    cursor.execute(
        """UPDATE bills SET
                Room_ID = :Room_ID,
                Tenant_ID = :Tenant_ID,
                Bill_Name = :Bill_Name,
                Previous_consumption = :Previous_consumption,
                Current_consumption = :Current_consumption,
                Rate = :Rate,
                Cost = :Cost
                    
                WHERE Bill_ID = :Bill_ID""",
        {
            "Room_ID": update_room_id_entry.get(),
            "Tenant_ID": update_tenant_ID_entry.get(),
            "Bill_Name": bill_name_entry.get(),
            "Previous_consumption": prev_entry.get(),
            "Current_consumption": current_entry.get(),
            "Rate": rate_entry.get(),
            "Cost": cost_entry.get(),
            "Bill_ID": bill_id_entry.get(),
        },
    )

    # Commit changes
    conn.commit()

    # Close our connection
    conn.close()
    # Clear Entry Boxes
    clear_bills_entries()
    # Add a little message box for fun
    messagebox.showinfo("Updated!", "Bill Info has been updated!")


def search_bills_info():
    lookup_records = search_bill_entry.get()

    # Clear the Treeview
    data = treeview_bills.get_children()
    for record in data:
        treeview_bills.delete(record)

    # Create a new database or connecct to one that exists
    conn = sqlite3.connect("boarding_house.db")

    # Create a cursor instance
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM bills WHERE Bill_ID like ?", ((lookup_records,)))
    records = cursor.fetchall()
    if records:
        messagebox.showinfo("Success", "We have found the data.")
        # Display Data
        global count
        count = 0
        for data in records:
            if count % 2 == 0:
                treeview_bills.insert(
                    parent="",
                    index=tk.END,
                    iid=count,
                    values=(
                        data[0],
                        data[1],
                        data[2],
                        data[3],
                        data[4],
                        data[5],
                        data[6],
                        data[7],
                    ),
                    tags=("evenrow",),
                )
            else:
                treeview_bills.insert(
                    parent="",
                    index=tk.END,
                    iid=count,
                    values=(
                        data[0],
                        data[1],
                        data[2],
                        data[3],
                        data[4],
                        data[5],
                        data[6],
                        data[7],
                    ),
                    tags=("oddrow",),
                )
            count = count + 1

        # Commit changes
        conn.commit()

        # Close our connection
        conn.close()
    else:
        messagebox.showinfo(
            "Notice!", "Unfortunately, your data is not found in the database."
        )
        bill_query()


# Payment Functions
def add_payment_info():
    # Create a new database or connect to one that exists
    conn = sqlite3.connect("boarding_house.db")
    # Create a cursor instance
    cursor = conn.cursor()
    id_to_verify = payment_ID_entry.get()
    checking_string1 = room_ids_entry.get()
    checking_string2 = tenant_ids_entry.get()
    if (
        unique_payment_id_verifier(id_to_verify)
        and strings_checker(checking_string1)
        and strings_checker(checking_string2)
    ):
        # Adding New Payment Information
        cursor.execute(
            "INSERT INTO payment VALUES (:Payment_ID, :Room_ID, :Tenant_ID, :Payment_Name, :Payment_date, :Payment_amount, :Payment_method, :Status )",
            {
                "Payment_ID": payment_ID_entry.get(),
                "Room_ID": room_ids_entry.get(),
                "Tenant_ID": tenant_ids_entry.get(),
                "Payment_Name": payment_name_entry.get(),
                "Payment_date": payment_date_entry.get(),
                "Payment_amount": payment_amount_entry.get(),
                "Payment_method": payment_method_entry.get(),
                "Status": status_entry.get(),
            },
        )

        # Commit changes
        conn.commit()

        # Close our connection
        conn.close()

        # Clear the Treeview Table
        treeview_emergency.delete(*treeview_emergency.get_children())

        # Run the query_database again
        payment_history_query()
        messagebox.showinfo("Added", "Payment info added successfully.")
    else:
        messagebox.showinfo("Notice", "Please enter a unique ID.")


def delete_payment_info():
    response = messagebox.askyesno(
        "WARNING!",
        "Are you sure you want to delete the data from the table?",
    )
    if response == 1:
        # Designate selections
        selected = treeview_payment_history.selection()

        # Create a list of IDs to delete
        ids_to_delete = []

        # Loop through the data from the treeview
        for names in selected:
            ids_to_delete.append(treeview_payment_history.item(names, "values")[0])

        # Delete from Treeview
        for record in selected:
            treeview_payment_history.delete(record)

        # Create a new database or connect to one that exists
        conn = sqlite3.connect("boarding_house.db")
        # Create a cursor instance
        cursor = conn.cursor()

        # Delete Selected Student Info
        cursor.executemany(
            "DELETE FROM payment WHERE Payment_ID = ?",
            [(a,) for a in ids_to_delete],
        )

        # Commit changes
        conn.commit()

        # Close our connection
        conn.close()

        # Add a little message box for fun
        messagebox.showinfo("Deleted!", "Payment Info Has Been Deleted!")


def update_payment_info():
    # Grab record numbers
    selected = treeview_payment_history.focus()
    # Update Record
    treeview_payment_history.item(
        selected,
        text="",
        values=(
            payment_ID_entry.get(),
            room_ids_entry.get(),
            tenant_ids_entry.get(),
            payment_name_entry.get(),
            payment_date_entry.get(),
            payment_amount_entry.get(),
            payment_method_entry.get(),
            status_entry.get(),
        ),
    )
    # Update data to the database
    # Create a new database or connect to one that exists
    conn = sqlite3.connect("boarding_house.db")

    # Create a cursor instance
    cursor = conn.cursor()

    cursor.execute(
        """UPDATE payment SET
                   Room_ID = :Room_ID,
                   Tenant_ID = :Tenant_ID,
                   Payment_Name = :Payment_Name,
                   Payment_date = :Payment_date,
                   Payment_amount = :Payment_amount,
                   Payment_method = :Payment_method,
                   Status = :Status
                   
                   WHERE Payment_ID = :Payment_ID""",
        {
            "Room_ID": room_ids_entry.get(),
            "Tenant_ID": tenant_ids_entry.get(),
            "Payment_Name": payment_name_entry.get(),
            "Payment_date": payment_date_entry.get(),
            "Payment_amount": payment_amount_entry.get(),
            "Payment_method": payment_method_entry.get(),
            "Status": status_entry.get(),
            "Payment_ID": payment_ID_entry.get(),
        },
    )

    # Commit changes
    conn.commit()

    # Close our connection
    conn.close()
    # Clear Entry Boxes
    clear_payment_entries()
    # Add a little message box for fun
    messagebox.showinfo("Updated!", "Payment Info has been updated!")


def search_payment_info():
    lookup_records = search_payment_entry.get()

    # Clear the Treeview
    data = treeview_payment_history.get_children()
    for record in data:
        treeview_payment_history.delete(record)

    # Create a new database or connecct to one that exists
    conn = sqlite3.connect("boarding_house.db")

    # Create a cursor instance
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM payment WHERE Payment_ID like ?", ((lookup_records,)))
    records = cursor.fetchall()
    if records:
        messagebox.showinfo("Success", "We have found the data.")
        # Display Data
        global count
        count = 0
        for data in records:
            if count % 2 == 0:
                treeview_payment_history.insert(
                    parent="",
                    index=tk.END,
                    iid=count,
                    values=(
                        data[0],
                        data[1],
                        data[2],
                        data[3],
                        data[4],
                        data[5],
                        data[6],
                        data[7],
                    ),
                    tags=("evenrow",),
                )
            else:
                treeview_payment_history.insert(
                    parent="",
                    index=tk.END,
                    iid=count,
                    values=(
                        data[0],
                        data[1],
                        data[2],
                        data[3],
                        data[4],
                        data[5],
                        data[6],
                        data[7],
                    ),
                    tags=("oddrow",),
                )
            count = count + 1

        # Commit changes
        conn.commit()

        # Close our connection
        conn.close()
    else:
        messagebox.showinfo(
            "Notice!", "Unfortunately, your data is not found in the database."
        )
        payment_history_query()


# Widgets for Add and Update Tenants
def add_tenant_widget():
    global tenant_id_entry, tenant_name_entry, age_entry, gender_entry, email_entry, address_entry, occupation_entry, contact_number_entry, number_of_edevices_entry, adding_tenant
    # Windows
    adding_tenant = tk.Toplevel(tenant_frame)
    adding_tenant.title("Add Tenant")
    adding_tenant.geometry("1000x600")
    adding_tenant.maxsize(1000, 600)

    # Create Label Frame
    add_entry_frames = ttk.LabelFrame(adding_tenant, text="Add Entries")
    add_entry_frames.place(relx=0.01, rely=0.02, width=900, height=400)

    # Entry Box and Buttons
    # Add Tenants Entry Boxes and Labels
    tenant_id_label = ctk.CTkLabel(
        add_entry_frames,
        text="Tenant_ID",
        height=30,
        width=150,
        fg_color="#336082",
        corner_radius=10,
        font=("Montserrat Bold", 12),
        justify="left",
    )
    tenant_id_label.grid(row=0, column=0, padx=10, pady=10)
    tenant_id_entry = ctk.CTkEntry(add_entry_frames, font=("Helvetica", 12))
    tenant_id_entry.grid(row=0, column=1, padx=10, pady=10)

    tenant_name_label = ctk.CTkLabel(
        add_entry_frames,
        text="Name",
        height=30,
        width=150,
        fg_color="#336082",
        corner_radius=10,
        font=("Montserrat Bold", 12),
        justify="left",
    )
    tenant_name_label.grid(row=0, column=2, padx=10, pady=10)
    tenant_name_entry = ctk.CTkEntry(add_entry_frames, font=("Helvetica", 12))
    tenant_name_entry.grid(row=0, column=3, padx=10, pady=10)

    age_label = ctk.CTkLabel(
        add_entry_frames,
        text="Age",
        height=30,
        width=150,
        fg_color="#336082",
        corner_radius=10,
        font=("Montserrat Bold", 12),
        justify="left",
    )
    age_label.grid(row=1, column=0, padx=10, pady=10)
    age_entry = ctk.CTkEntry(add_entry_frames, font=("Helvetica", 12))
    age_entry.grid(row=1, column=1, padx=10, pady=10)

    gender_label = ctk.CTkLabel(
        add_entry_frames,
        text="Gender",
        height=30,
        width=150,
        fg_color="#336082",
        corner_radius=10,
        font=("Montserrat Bold", 12),
        justify="left",
    )
    gender_label.grid(row=1, column=2, padx=10, pady=10)

    gender_choices = ["Male", "Female", "Others"]
    gender_entry = ctk.CTkComboBox(
        add_entry_frames,
        font=("Helvetica", 12),
        height=30,
        width=140,
        values=gender_choices,
        button_hover_color="#F2E6D0",
        dropdown_hover_color="#BFAE99",
    )
    gender_entry.set("Select Gender")
    gender_entry.grid(row=1, column=3, padx=10, pady=10)

    email_label = ctk.CTkLabel(
        add_entry_frames,
        text="Email Address",
        height=30,
        width=150,
        fg_color="#336082",
        corner_radius=10,
        font=("Montserrat Bold", 12),
        justify="left",
    )
    email_label.grid(row=2, column=0, padx=10, pady=10)
    email_entry = ctk.CTkEntry(add_entry_frames, font=("Helvetica", 12))
    email_entry.grid(row=2, column=1, padx=10, pady=10)

    address_label = ctk.CTkLabel(
        add_entry_frames,
        text="Permanent Address",
        height=30,
        width=150,
        fg_color="#336082",
        corner_radius=10,
        font=("Montserrat Bold", 12),
        justify="left",
    )
    address_label.grid(row=2, column=2, padx=10, pady=10)
    address_entry = ctk.CTkEntry(add_entry_frames, font=("Helvetica", 12))
    address_entry.grid(row=2, column=3, padx=10, pady=10)

    occupation_label = ctk.CTkLabel(
        add_entry_frames,
        text="Occupation",
        height=30,
        width=150,
        fg_color="#336082",
        corner_radius=10,
        font=("Montserrat Bold", 12),
        justify="left",
    )
    occupation_label.grid(row=3, column=0, padx=10, pady=10)
    occupation_entry = ctk.CTkEntry(add_entry_frames, font=("Helvetica", 12))
    occupation_entry.grid(row=3, column=1, padx=10, pady=10)

    contact_number_label = ctk.CTkLabel(
        add_entry_frames,
        text="Contact Number",
        height=30,
        width=150,
        fg_color="#336082",
        corner_radius=10,
        font=("Montserrat Bold", 12),
        justify="left",
    )
    contact_number_label.grid(row=3, column=2, padx=10, pady=10)
    contact_number_entry = ctk.CTkEntry(add_entry_frames, font=("Helvetica", 12))
    contact_number_entry.grid(row=3, column=3, padx=10, pady=10)

    number_of_edevices_label = ctk.CTkLabel(
        add_entry_frames,
        text="No. of Edevices",
        height=30,
        width=150,
        fg_color="#336082",
        corner_radius=10,
        font=("Montserrat Bold", 12),
        justify="left",
    )
    number_of_edevices_label.grid(row=4, column=0, padx=10, pady=10)
    number_of_edevices_entry = ctk.CTkEntry(add_entry_frames, font=("Helvetica", 12))
    number_of_edevices_entry.grid(row=4, column=1, padx=10, pady=10)

    # Add Button after input
    add_btn = ctk.CTkButton(
        adding_tenant,
        text="Add Tenant",
        height=30,
        width=100,
        corner_radius=10,
        fg_color="#336082",
        font=("Montserrat Bold", 12),
        command=add_new_tenant,
    )
    add_btn.place(relx=0.78, rely=0.70)

    # Button for clearing entries
    clear_entry_button = ctk.CTkButton(
        adding_tenant,
        text="Clear Entries",
        height=30,
        width=100,
        corner_radius=10,
        fg_color="#336082",
        font=("Montserrat Bold", 12),
        command=clear_entries_tenants,
    )
    clear_entry_button.place(relx=0.65, rely=0.70)


def update_tenant_widget():
    global tenant_id_entry, tenant_name_entry, age_entry, gender_entry, email_entry, address_entry, occupation_entry, contact_number_entry, number_of_edevices_entry, updating_tenant
    # Windows
    updating_tenant = tk.Toplevel(tenant_frame)
    updating_tenant.title("Update Tenant")
    updating_tenant.geometry("1000x600")
    updating_tenant.maxsize(1000, 600)

    # Create Label Frame
    update_entry_frames = ttk.LabelFrame(updating_tenant, text="Update Entries")
    update_entry_frames.place(relx=0.01, rely=0.02, width=900, height=400)

    # Entry Box and Buttons
    # Update Tenants Entry Boxes and Labels
    tenant_id_label = ctk.CTkLabel(
        update_entry_frames,
        text="Tenant_ID",
        height=30,
        width=150,
        fg_color="#336082",
        corner_radius=10,
        font=("Montserrat Bold", 12),
        justify="left",
    )
    tenant_id_label.grid(row=0, column=0, padx=10, pady=10)
    tenant_id_entry = ctk.CTkEntry(update_entry_frames, font=("Helvetica", 12))
    tenant_id_entry.grid(row=0, column=1, padx=10, pady=10)

    tenant_name_label = ctk.CTkLabel(
        update_entry_frames,
        text="Name",
        height=30,
        width=150,
        fg_color="#336082",
        corner_radius=10,
        font=("Montserrat Bold", 12),
        justify="left",
    )
    tenant_name_label.grid(row=0, column=2, padx=10, pady=10)
    tenant_name_entry = ctk.CTkEntry(update_entry_frames, font=("Helvetica", 12))
    tenant_name_entry.grid(row=0, column=3, padx=10, pady=10)

    age_label = ctk.CTkLabel(
        update_entry_frames,
        text="Age",
        height=30,
        width=150,
        fg_color="#336082",
        corner_radius=10,
        font=("Montserrat Bold", 12),
        justify="left",
    )
    age_label.grid(row=1, column=0, padx=10, pady=10)
    age_entry = ctk.CTkEntry(update_entry_frames, font=("Helvetica", 12))
    age_entry.grid(row=1, column=1, padx=10, pady=10)

    gender_label = ctk.CTkLabel(
        update_entry_frames,
        text="Gender",
        height=30,
        width=150,
        fg_color="#336082",
        corner_radius=10,
        font=("Montserrat Bold", 12),
        justify="left",
    )
    gender_label.grid(row=1, column=2, padx=10, pady=10)

    gender_choices = ["Male", "Female", "Others"]
    gender_entry = ctk.CTkComboBox(
        update_entry_frames,
        font=("Helvetica", 12),
        height=30,
        width=140,
        values=gender_choices,
        button_hover_color="#F2E6D0",
        dropdown_hover_color="#BFAE99",
    )
    gender_entry.set("Select Gender")
    gender_entry.grid(row=1, column=3, padx=10, pady=10)

    email_label = ctk.CTkLabel(
        update_entry_frames,
        text="Email Address",
        height=30,
        width=150,
        fg_color="#336082",
        corner_radius=10,
        font=("Montserrat Bold", 12),
        justify="left",
    )
    email_label.grid(row=2, column=0, padx=10, pady=10)
    email_entry = ctk.CTkEntry(update_entry_frames, font=("Helvetica", 12))
    email_entry.grid(row=2, column=1, padx=10, pady=10)

    address_label = ctk.CTkLabel(
        update_entry_frames,
        text="Permanent Address",
        height=30,
        width=150,
        fg_color="#336082",
        corner_radius=10,
        font=("Montserrat Bold", 12),
        justify="left",
    )
    address_label.grid(row=2, column=2, padx=10, pady=10)
    address_entry = ctk.CTkEntry(update_entry_frames, font=("Helvetica", 12))
    address_entry.grid(row=2, column=3, padx=10, pady=10)

    occupation_label = ctk.CTkLabel(
        update_entry_frames,
        text="Occupation",
        height=30,
        width=150,
        fg_color="#336082",
        corner_radius=10,
        font=("Montserrat Bold", 12),
        justify="left",
    )
    occupation_label.grid(row=3, column=0, padx=10, pady=10)
    occupation_entry = ctk.CTkEntry(update_entry_frames, font=("Helvetica", 12))
    occupation_entry.grid(row=3, column=1, padx=10, pady=10)

    contact_number_label = ctk.CTkLabel(
        update_entry_frames,
        text="Contact Number",
        height=30,
        width=150,
        fg_color="#336082",
        corner_radius=10,
        font=("Montserrat Bold", 12),
        justify="left",
    )
    contact_number_label.grid(row=3, column=2, padx=10, pady=10)
    contact_number_entry = ctk.CTkEntry(update_entry_frames, font=("Helvetica", 12))
    contact_number_entry.grid(row=3, column=3, padx=10, pady=10)

    number_of_edevices_label = ctk.CTkLabel(
        update_entry_frames,
        text="No. of Edevices",
        height=30,
        width=150,
        fg_color="#336082",
        corner_radius=10,
        font=("Montserrat Bold", 12),
        justify="left",
    )
    number_of_edevices_label.grid(row=4, column=0, padx=10, pady=10)
    number_of_edevices_entry = ctk.CTkEntry(update_entry_frames, font=("Helvetica", 12))
    number_of_edevices_entry.grid(row=4, column=1, padx=10, pady=10)

    # Update Button after input
    update_btn = ctk.CTkButton(
        updating_tenant,
        text="Update Info",
        height=30,
        width=100,
        corner_radius=10,
        fg_color="#336082",
        font=("Montserrat Bold", 12),
        command=update_tenant_info,
    )
    update_btn.place(relx=0.78, rely=0.70)

    # Button for clearing entries
    clear_entry_button = ctk.CTkButton(
        updating_tenant,
        text="Clear Entries",
        height=30,
        width=100,
        corner_radius=10,
        fg_color="#336082",
        font=("Montserrat Bold", 12),
        command=clear_entries_tenants,
    )
    clear_entry_button.place(relx=0.65, rely=0.70)


# Widgets for Add and Update Emergency Contacts of Tenants
def add_ec_tenant_widget():
    global ec_tenant_name_entry, ec_age_entry, ec_sex_entry, ec_relationship_entry, ec_contact_number_entry, ec_email_entry, ec_address_entry, tenants_id_entry, adding_etenant
    # Windows
    adding_etenant = tk.Toplevel(tenant_frame)
    adding_etenant.title("Add EC_Tenant")
    adding_etenant.geometry("1000x600")
    adding_etenant.maxsize(1000, 600)

    # Create Label Frame
    add_entry_frames = ttk.LabelFrame(adding_etenant, text="Add Entries")
    add_entry_frames.place(relx=0.01, rely=0.02, width=900, height=400)

    # Entry Box and Buttons
    # Add EC Tenant Entry Boxes and Labels
    ec_tenant_name_label = ctk.CTkLabel(
        add_entry_frames,
        text="EC_Name",
        height=30,
        width=150,
        fg_color="#336082",
        corner_radius=10,
        font=("Montserrat Bold", 12),
        justify="left",
    )
    ec_tenant_name_label.grid(row=0, column=0, padx=10, pady=10)
    ec_tenant_name_entry = ctk.CTkEntry(add_entry_frames, font=("Helvetica", 12))
    ec_tenant_name_entry.grid(row=0, column=1, padx=10, pady=10)

    ec_age_label = ctk.CTkLabel(
        add_entry_frames,
        text="Age",
        height=30,
        width=150,
        fg_color="#336082",
        corner_radius=10,
        font=("Montserrat Bold", 12),
        justify="left",
    )
    ec_age_label.grid(row=0, column=2, padx=10, pady=10)
    ec_age_entry = ctk.CTkEntry(add_entry_frames, font=("Helvetica", 12))
    ec_age_entry.grid(row=0, column=3, padx=10, pady=10)

    ec_sex_label = ctk.CTkLabel(
        add_entry_frames,
        text="Sex",
        height=30,
        width=150,
        fg_color="#336082",
        corner_radius=10,
        font=("Montserrat Bold", 12),
        justify="left",
    )
    ec_sex_label.grid(row=1, column=0, padx=10, pady=10)

    sex_choices = ["Male", "Female"]
    ec_sex_entry = ctk.CTkComboBox(
        add_entry_frames,
        font=("Helvetica", 12),
        height=30,
        width=140,
        values=sex_choices,
        button_hover_color="#F2E6D0",
        dropdown_hover_color="#BFAE99",
    )
    ec_sex_entry.set("Select Sex")
    ec_sex_entry.grid(row=1, column=1, padx=10, pady=10)

    ec_relationship_label = ctk.CTkLabel(
        add_entry_frames,
        text="Relationship",
        height=30,
        width=150,
        fg_color="#336082",
        corner_radius=10,
        font=("Montserrat Bold", 12),
        justify="left",
    )
    ec_relationship_label.grid(row=1, column=2, padx=10, pady=10)
    ec_relationship_entry = ctk.CTkEntry(add_entry_frames, font=("Helvetica", 12))
    ec_relationship_entry.grid(row=1, column=3, padx=10, pady=10)

    ec_contact_number_label = ctk.CTkLabel(
        add_entry_frames,
        text="Contact Number",
        height=30,
        width=150,
        fg_color="#336082",
        corner_radius=10,
        font=("Montserrat Bold", 12),
        justify="left",
    )
    ec_contact_number_label.grid(row=2, column=0, padx=10, pady=10)
    ec_contact_number_entry = ctk.CTkEntry(add_entry_frames, font=("Helvetica", 12))
    ec_contact_number_entry.grid(row=2, column=1, padx=10, pady=10)

    ec_email_label = ctk.CTkLabel(
        add_entry_frames,
        text="Email Address",
        height=30,
        width=150,
        fg_color="#336082",
        corner_radius=10,
        font=("Montserrat Bold", 12),
        justify="left",
    )
    ec_email_label.grid(row=2, column=2, padx=10, pady=10)
    ec_email_entry = ctk.CTkEntry(add_entry_frames, font=("Helvetica", 12))
    ec_email_entry.grid(row=2, column=3, padx=10, pady=10)

    ec_address_label = ctk.CTkLabel(
        add_entry_frames,
        text="Permanent Address",
        height=30,
        width=150,
        fg_color="#336082",
        corner_radius=10,
        font=("Montserrat Bold", 12),
        justify="left",
    )
    ec_address_label.grid(row=3, column=0, padx=10, pady=10)
    ec_address_entry = ctk.CTkEntry(add_entry_frames, font=("Helvetica", 12))
    ec_address_entry.grid(row=3, column=1, padx=10, pady=10)

    tenants_id_label = ctk.CTkLabel(
        add_entry_frames,
        text="Tenant_ID",
        height=30,
        width=150,
        fg_color="#336082",
        corner_radius=10,
        font=("Montserrat Bold", 12),
        justify="left",
    )
    tenants_id_label.grid(row=3, column=2, padx=10, pady=10)

    # Create a new database or connect to one that exists
    conn = sqlite3.connect("boarding_house.db")
    # Create a cursor instance
    cursor = conn.cursor()

    cursor.execute("SELECT Tenant_ID from tenants")

    results = cursor.fetchall()
    # List containing the IDs of Tenant
    ids_of_tenants = []
    for ids in results:
        ids_of_tenants.append(ids[0])

    tenants_id_entry = ctk.CTkComboBox(
        add_entry_frames,
        font=("Helvetica", 12),
        height=30,
        width=140,
        values=ids_of_tenants,
        button_hover_color="#F2E6D0",
        dropdown_hover_color="#BFAE99",
    )
    tenants_id_entry.set("")
    tenants_id_entry.grid(row=3, column=3, padx=10, pady=10)

    # Add Button after input
    add_btn = ctk.CTkButton(
        adding_etenant,
        text="Add ETenant",
        height=30,
        width=100,
        corner_radius=10,
        fg_color="#336082",
        font=("Montserrat Bold", 12),
        command=add_ec_tenant_info,
    )
    add_btn.place(relx=0.78, rely=0.70)

    # Button for clearing entries
    clear_entry_button = ctk.CTkButton(
        adding_etenant,
        text="Clear Entries",
        height=30,
        width=100,
        corner_radius=10,
        fg_color="#336082",
        font=("Montserrat Bold", 12),
        command=clear_entries_ec_tenants,
    )
    clear_entry_button.place(relx=0.65, rely=0.70)


def update_ec_tenant_widget():
    global ec_tenant_name_entry, ec_age_entry, ec_sex_entry, ec_relationship_entry, ec_contact_number_entry, ec_email_entry, ec_address_entry, update_tenants_id_entry
    # Windows
    updating_etenant = tk.Toplevel(tenant_frame)
    updating_etenant.title("Update Tenant")
    updating_etenant.geometry("1000x600")
    updating_etenant.maxsize(1000, 600)

    # Create Label Frame
    update_entry_frames = ttk.LabelFrame(updating_etenant, text="Update Entries")
    update_entry_frames.place(relx=0.01, rely=0.02, width=900, height=400)

    # Entry Box and Buttons
    # Add EC Tenant Entry Boxes and Labels
    ec_tenant_name_label = ctk.CTkLabel(
        update_entry_frames,
        text="EC_Name",
        height=30,
        width=150,
        fg_color="#336082",
        corner_radius=10,
        font=("Montserrat Bold", 12),
        justify="left",
    )
    ec_tenant_name_label.grid(row=0, column=0, padx=10, pady=10)
    ec_tenant_name_entry = ctk.CTkEntry(update_entry_frames, font=("Helvetica", 12))
    ec_tenant_name_entry.grid(row=0, column=1, padx=10, pady=10)

    ec_age_label = ctk.CTkLabel(
        update_entry_frames,
        text="Age",
        height=30,
        width=150,
        fg_color="#336082",
        corner_radius=10,
        font=("Montserrat Bold", 12),
        justify="left",
    )
    ec_age_label.grid(row=0, column=2, padx=10, pady=10)
    ec_age_entry = ctk.CTkEntry(update_entry_frames, font=("Helvetica", 12))
    ec_age_entry.grid(row=0, column=3, padx=10, pady=10)

    ec_sex_label = ctk.CTkLabel(
        update_entry_frames,
        text="Sex",
        height=30,
        width=150,
        fg_color="#336082",
        corner_radius=10,
        font=("Montserrat Bold", 12),
        justify="left",
    )
    ec_sex_label.grid(row=1, column=0, padx=10, pady=10)
    sex_choices = ["Male", "Female"]
    ec_sex_entry = ctk.CTkComboBox(
        update_entry_frames,
        font=("Helvetica", 12),
        height=30,
        width=140,
        values=sex_choices,
        button_hover_color="#F2E6D0",
        dropdown_hover_color="#BFAE99",
    )
    ec_sex_entry.set("Select Sex")
    ec_sex_entry.grid(row=1, column=1, padx=10, pady=10)

    ec_relationship_label = ctk.CTkLabel(
        update_entry_frames,
        text="Relationship",
        height=30,
        width=150,
        fg_color="#336082",
        corner_radius=10,
        font=("Montserrat Bold", 12),
        justify="left",
    )
    ec_relationship_label.grid(row=1, column=2, padx=10, pady=10)
    ec_relationship_entry = ctk.CTkEntry(update_entry_frames, font=("Helvetica", 12))
    ec_relationship_entry.grid(row=1, column=3, padx=10, pady=10)

    ec_contact_number_label = ctk.CTkLabel(
        update_entry_frames,
        text="Contact Number",
        height=30,
        width=150,
        fg_color="#336082",
        corner_radius=10,
        font=("Montserrat Bold", 12),
        justify="left",
    )
    ec_contact_number_label.grid(row=2, column=0, padx=10, pady=10)
    ec_contact_number_entry = ctk.CTkEntry(update_entry_frames, font=("Helvetica", 12))
    ec_contact_number_entry.grid(row=2, column=1, padx=10, pady=10)

    ec_email_label = ctk.CTkLabel(
        update_entry_frames,
        text="Email Address",
        height=30,
        width=150,
        fg_color="#336082",
        corner_radius=10,
        font=("Montserrat Bold", 12),
        justify="left",
    )
    ec_email_label.grid(row=2, column=2, padx=10, pady=10)
    ec_email_entry = ctk.CTkEntry(update_entry_frames, font=("Helvetica", 12))
    ec_email_entry.grid(row=2, column=3, padx=10, pady=10)

    ec_address_label = ctk.CTkLabel(
        update_entry_frames,
        text="Permanent Address",
        height=30,
        width=150,
        fg_color="#336082",
        corner_radius=10,
        font=("Montserrat Bold", 12),
        justify="left",
    )
    ec_address_label.grid(row=3, column=0, padx=10, pady=10)
    ec_address_entry = ctk.CTkEntry(update_entry_frames, font=("Helvetica", 12))
    ec_address_entry.grid(row=3, column=1, padx=10, pady=10)

    tenants_id_label = ctk.CTkLabel(
        update_entry_frames,
        text="Tenant_ID",
        height=30,
        width=150,
        fg_color="#336082",
        corner_radius=10,
        font=("Montserrat Bold", 12),
        justify="left",
    )
    tenants_id_label.grid(row=3, column=2, padx=10, pady=10)
    # Create a new database or connect to one that exists
    conn = sqlite3.connect("boarding_house.db")
    # Create a cursor instance
    cursor = conn.cursor()

    cursor.execute("SELECT Tenant_ID from tenants")

    results = cursor.fetchall()
    # List containing the IDs of Tenant
    ids_of_tenants = []
    for ids in results:
        ids_of_tenants.append(ids[0])

    update_tenants_id_entry = ctk.CTkEntry(update_entry_frames, font=("Helvetica", 12))
    update_tenants_id_entry.grid(row=3, column=3, padx=10, pady=10)

    # Update Button after input
    update_btn = ctk.CTkButton(
        updating_etenant,
        text="Update Info",
        height=30,
        width=100,
        corner_radius=10,
        fg_color="#336082",
        font=("Montserrat Bold", 12),
        command=update_ec_tenant_info,
    )
    update_btn.place(relx=0.78, rely=0.70)

    # Button for clearing entries
    clear_entry_button = ctk.CTkButton(
        updating_etenant,
        text="Clear Entries",
        height=30,
        width=100,
        corner_radius=10,
        fg_color="#336082",
        font=("Montserrat Bold", 12),
        command=clear_entries_ec_tenants,
    )
    clear_entry_button.place(relx=0.65, rely=0.70)


# Widgets for Add and Update Rooms
def add_room_widget():
    global room_ID_entry, room_tenant_entry, rental_amount_entry, rent_date_entry, due_date_entry, electric_meter_number_entry, add_room
    # Windows
    add_room = tk.Toplevel(room_assignment_frame)
    add_room.title("Add Rooms")
    add_room.geometry("1000x600")
    add_room.maxsize(1000, 600)

    # Create Label Frame
    add_entry_frames = ttk.LabelFrame(add_room, text="Add Entries")
    add_entry_frames.place(relx=0.01, rely=0.02, width=900, height=400)

    # Entry Box and Buttons
    # Add Room Entry Boxes and Labels
    room_ID_label = ctk.CTkLabel(
        add_entry_frames,
        text="Room_ID",
        height=30,
        width=150,
        fg_color="#336082",
        corner_radius=10,
        font=("Montserrat Bold", 12),
        justify="left",
    )
    room_ID_label.grid(row=0, column=0, padx=10, pady=10)
    room_ID_entry = ctk.CTkEntry(add_entry_frames, font=("Helvetica", 12))
    room_ID_entry.grid(row=0, column=1, padx=10, pady=10)

    room_tenant_label = ctk.CTkLabel(
        add_entry_frames,
        text="Tenant_ID",
        height=30,
        width=150,
        fg_color="#336082",
        corner_radius=10,
        font=("Montserrat Bold", 12),
        justify="left",
    )
    room_tenant_label.grid(row=0, column=2, padx=10, pady=10)

    # Create a new database or connect to one that exists
    conn = sqlite3.connect("boarding_house.db")
    # Create a cursor instance
    cursor = conn.cursor()

    cursor.execute("SELECT Tenant_ID from tenants")

    results = cursor.fetchall()
    # List containing the IDs of Tenant
    ids_of_tenants = []
    for ids in results:
        ids_of_tenants.append(ids[0])
    room_tenant_entry = ctk.CTkComboBox(
        add_entry_frames,
        font=("Helvetica", 12),
        height=30,
        width=140,
        values=ids_of_tenants,
        button_hover_color="#F2E6D0",
        dropdown_hover_color="#BFAE99",
    )
    room_tenant_entry.set("")
    room_tenant_entry.grid(row=0, column=3, padx=10, pady=10)

    rental_amount_label = ctk.CTkLabel(
        add_entry_frames,
        text="Rental_Amount",
        height=30,
        width=150,
        fg_color="#336082",
        corner_radius=10,
        font=("Montserrat Bold", 12),
        justify="left",
    )
    rental_amount_label.grid(row=1, column=0, padx=10, pady=10)
    rental_amount_entry = ctk.CTkEntry(add_entry_frames, font=("Helvetica", 12))
    rental_amount_entry.grid(row=1, column=1, padx=10, pady=10)

    rent_date_label = ctk.CTkLabel(
        add_entry_frames,
        text="Rent Date",
        height=30,
        width=150,
        fg_color="#336082",
        corner_radius=10,
        font=("Montserrat Bold", 12),
        justify="left",
    )
    rent_date_label.grid(row=1, column=2, padx=10, pady=10)
    rent_date_entry = ctk.CTkEntry(add_entry_frames, font=("Helvetica", 12))
    rent_date_entry.grid(row=1, column=3, padx=10, pady=10)

    due_date_label = ctk.CTkLabel(
        add_entry_frames,
        text="Due Date",
        height=30,
        width=150,
        fg_color="#336082",
        corner_radius=10,
        font=("Montserrat Bold", 12),
        justify="left",
    )
    due_date_label.grid(row=2, column=0, padx=10, pady=10)
    due_date_entry = ctk.CTkEntry(add_entry_frames, font=("Helvetica", 12))
    due_date_entry.grid(row=2, column=1, padx=10, pady=10)

    electric_meter_number_label = ctk.CTkLabel(
        add_entry_frames,
        text="Electric Meter Number",
        height=30,
        width=150,
        fg_color="#336082",
        corner_radius=10,
        font=("Montserrat Bold", 12),
        justify="left",
    )
    electric_meter_number_label.grid(row=2, column=2, padx=10, pady=10)
    electric_meter_number_entry = ctk.CTkEntry(add_entry_frames, font=("Helvetica", 12))
    electric_meter_number_entry.grid(row=2, column=3, padx=10, pady=10)

    # Add Button after input
    add_btn = ctk.CTkButton(
        add_room,
        text="Add Room",
        height=30,
        width=100,
        corner_radius=10,
        fg_color="#336082",
        font=("Montserrat Bold", 12),
        command=add_room_info,
    )
    add_btn.place(relx=0.78, rely=0.70)

    # Button for clearing entries
    clear_entry_button = ctk.CTkButton(
        add_room,
        text="Clear Entries",
        height=30,
        width=100,
        corner_radius=10,
        fg_color="#336082",
        font=("Montserrat Bold", 12),
        command=clear_room_entries,
    )
    clear_entry_button.place(relx=0.65, rely=0.70)


def update_room_widget():
    global room_ID_entry, room_tenant_entry, rental_amount_entry, rent_date_entry, due_date_entry, electric_meter_number_entry, update_room
    # Windows
    update_room = tk.Toplevel(room_assignment_frame)
    update_room.title("Update Room")
    update_room.geometry("1000x600")
    update_room.maxsize(1000, 600)

    # Create Label Frame
    update_entry_frames = ttk.LabelFrame(update_room, text="Update Entries")
    update_entry_frames.place(relx=0.01, rely=0.02, width=900, height=400)

    # Entry Box and Buttons
    # Add Room Entry Boxes and Labels
    room_ID_label = ctk.CTkLabel(
        update_entry_frames,
        text="Room_ID",
        height=30,
        width=150,
        fg_color="#336082",
        corner_radius=10,
        font=("Montserrat Bold", 12),
        justify="left",
    )
    room_ID_label.grid(row=0, column=0, padx=10, pady=10)
    room_ID_entry = ctk.CTkEntry(update_entry_frames, font=("Helvetica", 12))
    room_ID_entry.grid(row=0, column=1, padx=10, pady=10)

    room_tenant_label = ctk.CTkLabel(
        update_entry_frames,
        text="Tenant_ID",
        height=30,
        width=150,
        fg_color="#336082",
        corner_radius=10,
        font=("Montserrat Bold", 12),
        justify="left",
    )
    room_tenant_label.grid(row=0, column=2, padx=10, pady=10)

    # Create a new database or connect to one that exists
    conn = sqlite3.connect("boarding_house.db")
    # Create a cursor instance
    cursor = conn.cursor()

    cursor.execute("SELECT Tenant_ID from tenants")

    results = cursor.fetchall()
    # List containing the IDs of Tenant
    ids_of_tenants = []
    for ids in results:
        ids_of_tenants.append(ids[0])
    room_tenant_entry = ctk.CTkComboBox(
        update_entry_frames,
        font=("Helvetica", 12),
        height=30,
        width=140,
        values=ids_of_tenants,
        button_hover_color="#F2E6D0",
        dropdown_hover_color="#BFAE99",
    )
    room_tenant_entry.set("")
    room_tenant_entry.grid(row=0, column=3, padx=10, pady=10)

    rental_amount_label = ctk.CTkLabel(
        update_entry_frames,
        text="Rental_Amount",
        height=30,
        width=150,
        fg_color="#336082",
        corner_radius=10,
        font=("Montserrat Bold", 12),
        justify="left",
    )
    rental_amount_label.grid(row=1, column=0, padx=10, pady=10)
    rental_amount_entry = ctk.CTkEntry(update_entry_frames, font=("Helvetica", 12))
    rental_amount_entry.grid(row=1, column=1, padx=10, pady=10)

    rent_date_label = ctk.CTkLabel(
        update_entry_frames,
        text="Rent Date",
        height=30,
        width=150,
        fg_color="#336082",
        corner_radius=10,
        font=("Montserrat Bold", 12),
        justify="left",
    )
    rent_date_label.grid(row=1, column=2, padx=10, pady=10)
    rent_date_entry = ctk.CTkEntry(update_entry_frames, font=("Helvetica", 12))
    rent_date_entry.grid(row=1, column=3, padx=10, pady=10)

    due_date_label = ctk.CTkLabel(
        update_entry_frames,
        text="Due Date",
        height=30,
        width=150,
        fg_color="#336082",
        corner_radius=10,
        font=("Montserrat Bold", 12),
        justify="left",
    )
    due_date_label.grid(row=2, column=0, padx=10, pady=10)
    due_date_entry = ctk.CTkEntry(update_entry_frames, font=("Helvetica", 12))
    due_date_entry.grid(row=2, column=1, padx=10, pady=10)

    electric_meter_number_label = ctk.CTkLabel(
        update_entry_frames,
        text="Electric Meter Number",
        height=30,
        width=150,
        fg_color="#336082",
        corner_radius=10,
        font=("Montserrat Bold", 12),
        justify="left",
    )
    electric_meter_number_label.grid(row=2, column=2, padx=10, pady=10)
    electric_meter_number_entry = ctk.CTkEntry(
        update_entry_frames, font=("Helvetica", 12)
    )
    electric_meter_number_entry.grid(row=2, column=3, padx=10, pady=10)

    # Update Button after input
    update_btn = ctk.CTkButton(
        update_room,
        text="Update Info",
        height=30,
        width=100,
        corner_radius=10,
        fg_color="#336082",
        font=("Montserrat Bold", 12),
        command=update_room_info,
    )
    update_btn.place(relx=0.78, rely=0.70)

    # Button for clearing entries
    clear_entry_button = ctk.CTkButton(
        update_room,
        text="Clear Entries",
        height=30,
        width=100,
        corner_radius=10,
        fg_color="#336082",
        font=("Montserrat Bold", 12),
        command=clear_room_entries,
    )
    clear_entry_button.place(relx=0.65, rely=0.70)


# Clear Entries in the Combobox
def clear_combobox():
    tenant_ID_entry.configure(values="")


# Widgets for Add and Update Bills
def my_upd(*args):
    # Create a new database or connect to one that exists
    conn = sqlite3.connect("boarding_house.db")
    # Create a cursor instance
    cursor = conn.cursor()
    tenant_ID_entry.set("")
    query = "SELECT Tenant_ID from room WHERE Room_ID ='" + text.get() + "'"
    cursor.execute(query)
    result = cursor.fetchall()
    for ids in result:
        ids_of_tenants.append(ids[0])
    tenant_ID_entry.configure(values=ids_of_tenants)


def add_bills_widget():
    global bill_id_entry, room_id_entry, tenant_ID_entry, bill_name_entry, prev_entry, current_entry, rate_entry, cost_entry, text, ids_of_tenants
    # Windows
    add_bills = tk.Toplevel(bill_frame)
    add_bills.title("Add Bills")
    add_bills.geometry("1000x600")
    add_bills.maxsize(1000, 600)

    # Create Label Frame
    add_entry_frames = ttk.LabelFrame(add_bills, text="Add Entries")
    add_entry_frames.place(relx=0.01, rely=0.02, width=900, height=400)

    # Entry Box and Buttons
    # Add EC Tenant Entry Boxes and Labels
    bill_id_label = ctk.CTkLabel(
        add_entry_frames,
        text="Bill_ID",
        height=30,
        width=150,
        fg_color="#336082",
        corner_radius=10,
        font=("Montserrat Bold", 12),
        justify="left",
    )
    bill_id_label.grid(row=0, column=0, padx=10, pady=10)
    bill_id_entry = ctk.CTkEntry(add_entry_frames, font=("Helvetica", 12))
    bill_id_entry.grid(row=0, column=1, padx=10, pady=10)

    room_id_label = ctk.CTkLabel(
        add_entry_frames,
        text="Room_ID",
        height=30,
        width=150,
        fg_color="#336082",
        corner_radius=10,
        font=("Montserrat Bold", 12),
        justify="left",
    )
    room_id_label.grid(row=0, column=2, padx=10, pady=10)

    # Create a new database or connect to one that exists
    conn = sqlite3.connect("boarding_house.db")
    # Create a cursor instance
    cursor = conn.cursor()

    cursor.execute("SELECT Room_ID from room")

    results = cursor.fetchall()
    # List containing the Room IDs
    ids_of_rooms = []
    for ids in results:
        ids_of_rooms.append(ids[0])

    # For linking
    ids_of_tenants = []
    text = tk.StringVar()
    text.trace("w", my_upd)
    room_id_entry = ctk.CTkComboBox(
        add_entry_frames,
        font=("Helvetica", 12),
        height=30,
        width=140,
        values=ids_of_rooms,
        button_hover_color="#F2E6D0",
        dropdown_hover_color="#BFAE99",
        variable=text,
    )
    room_id_entry.set("")
    room_id_entry.grid(row=0, column=3, padx=10, pady=10)

    tenant_ID_label = ctk.CTkLabel(
        add_entry_frames,
        text="Tenant_ID",
        height=30,
        width=150,
        fg_color="#336082",
        corner_radius=10,
        font=("Montserrat Bold", 12),
        justify="left",
    )
    tenant_ID_label.grid(row=1, column=0, padx=10, pady=10)

    tenant_ID_entry = ctk.CTkComboBox(
        add_entry_frames,
        font=("Helvetica", 12),
        height=30,
        width=140,
        values=ids_of_tenants,
        button_hover_color="#F2E6D0",
        dropdown_hover_color="#BFAE99",
    )
    tenant_ID_entry.set("")
    tenant_ID_entry.grid(row=1, column=1, padx=10, pady=10)

    bill_name_label = ctk.CTkLabel(
        add_entry_frames,
        text="Bill Name",
        height=30,
        width=150,
        fg_color="#336082",
        corner_radius=10,
        font=("Montserrat Bold", 12),
        justify="left",
    )
    bill_name_label.grid(row=1, column=2, padx=10, pady=10)
    bill_name_entry = ctk.CTkEntry(add_entry_frames, font=("Helvetica", 12))
    bill_name_entry.grid(row=1, column=3, padx=10, pady=10)

    prev_label = ctk.CTkLabel(
        add_entry_frames,
        text="Previous_consumption",
        height=30,
        width=150,
        fg_color="#336082",
        corner_radius=10,
        font=("Montserrat Bold", 12),
        justify="left",
    )
    prev_label.grid(row=2, column=0, padx=10, pady=10)
    prev_entry = ctk.CTkEntry(add_entry_frames, font=("Helvetica", 12))
    prev_entry.grid(row=2, column=1, padx=10, pady=10)

    current_label = ctk.CTkLabel(
        add_entry_frames,
        text="Current_consumption",
        height=30,
        width=150,
        fg_color="#336082",
        corner_radius=10,
        font=("Montserrat Bold", 12),
        justify="left",
    )
    current_label.grid(row=2, column=2, padx=10, pady=10)
    current_entry = ctk.CTkEntry(add_entry_frames, font=("Helvetica", 12))
    current_entry.grid(row=2, column=3, padx=10, pady=10)

    rate_label = ctk.CTkLabel(
        add_entry_frames,
        text="Rate",
        height=30,
        width=150,
        fg_color="#336082",
        corner_radius=10,
        font=("Montserrat Bold", 12),
        justify="left",
    )
    rate_label.grid(row=3, column=0, padx=10, pady=10)
    rate_entry = ctk.CTkEntry(add_entry_frames, font=("Helvetica", 12))
    rate_entry.grid(row=3, column=1, padx=10, pady=10)

    cost_label = ctk.CTkLabel(
        add_entry_frames,
        text="Cost",
        height=30,
        width=150,
        fg_color="#336082",
        corner_radius=10,
        font=("Montserrat Bold", 12),
        justify="left",
    )
    cost_label.grid(row=3, column=2, padx=10, pady=10)
    cost_entry = ctk.CTkEntry(add_entry_frames, font=("Helvetica", 12))
    cost_entry.grid(row=3, column=3, padx=10, pady=10)

    # Add Button after input
    add_btn = ctk.CTkButton(
        add_bills,
        text="Add Bills",
        height=30,
        width=100,
        corner_radius=10,
        fg_color="#336082",
        font=("Montserrat Bold", 12),
        command=add_bills_info,
    )
    add_btn.place(relx=0.78, rely=0.70)

    # Button for clearing entries
    clear_entry_button = ctk.CTkButton(
        add_bills,
        text="Clear Entries",
        height=30,
        width=100,
        corner_radius=10,
        fg_color="#336082",
        font=("Montserrat Bold", 12),
        command=clear_bills_entries,
    )
    clear_entry_button.place(relx=0.65, rely=0.70)


def update_bills_widget():
    global bill_id_entry, update_room_id_entry, update_tenant_ID_entry, bill_name_entry, prev_entry, current_entry, rate_entry, cost_entry
    # Windows
    update_bills = tk.Toplevel(bill_frame)
    update_bills.title("Update Bills")
    update_bills.geometry("1000x600")
    update_bills.maxsize(1000, 600)

    # Create Label Frame
    update_entry_frames = ttk.LabelFrame(update_bills, text="Update Entries")
    update_entry_frames.place(relx=0.01, rely=0.02, width=900, height=400)

    # Entry Box and Buttons
    # Update Bills Entry Boxes and Labels
    bill_id_label = ctk.CTkLabel(
        update_entry_frames,
        text="Bill_ID",
        height=30,
        width=150,
        fg_color="#336082",
        corner_radius=10,
        font=("Montserrat Bold", 12),
        justify="left",
    )
    bill_id_label.grid(row=0, column=0, padx=10, pady=10)
    bill_id_entry = ctk.CTkEntry(update_entry_frames, font=("Helvetica", 12))
    bill_id_entry.grid(row=0, column=1, padx=10, pady=10)

    room_id_label = ctk.CTkLabel(
        update_entry_frames,
        text="Room_ID",
        height=30,
        width=150,
        fg_color="#336082",
        corner_radius=10,
        font=("Montserrat Bold", 12),
        justify="left",
    )
    room_id_label.grid(row=0, column=2, padx=10, pady=10)

    update_room_id_entry = ctk.CTkEntry(update_entry_frames, font=("Helvetica", 12))
    update_room_id_entry.grid(row=0, column=3, padx=10, pady=10)

    tenant_ID_label = ctk.CTkLabel(
        update_entry_frames,
        text="Tenant_ID",
        height=30,
        width=150,
        fg_color="#336082",
        corner_radius=10,
        font=("Montserrat Bold", 12),
        justify="left",
    )
    tenant_ID_label.grid(row=1, column=0, padx=10, pady=10)

    update_tenant_ID_entry = ctk.CTkEntry(update_entry_frames, font=("Helvetica", 12))
    update_tenant_ID_entry.grid(row=1, column=1, padx=10, pady=10)

    bill_name_label = ctk.CTkLabel(
        update_entry_frames,
        text="Bill Name",
        height=30,
        width=150,
        fg_color="#336082",
        corner_radius=10,
        font=("Montserrat Bold", 12),
        justify="left",
    )
    bill_name_label.grid(row=1, column=2, padx=10, pady=10)
    bill_name_entry = ctk.CTkEntry(update_entry_frames, font=("Helvetica", 12))
    bill_name_entry.grid(row=1, column=3, padx=10, pady=10)

    prev_label = ctk.CTkLabel(
        update_entry_frames,
        text="Previous_consumption",
        height=30,
        width=150,
        fg_color="#336082",
        corner_radius=10,
        font=("Montserrat Bold", 12),
        justify="left",
    )
    prev_label.grid(row=2, column=0, padx=10, pady=10)
    prev_entry = ctk.CTkEntry(update_entry_frames, font=("Helvetica", 12))
    prev_entry.grid(row=2, column=1, padx=10, pady=10)

    current_label = ctk.CTkLabel(
        update_entry_frames,
        text="Current_consumption",
        height=30,
        width=150,
        fg_color="#336082",
        corner_radius=10,
        font=("Montserrat Bold", 12),
        justify="left",
    )
    current_label.grid(row=2, column=2, padx=10, pady=10)
    current_entry = ctk.CTkEntry(update_entry_frames, font=("Helvetica", 12))
    current_entry.grid(row=2, column=3, padx=10, pady=10)

    rate_label = ctk.CTkLabel(
        update_entry_frames,
        text="Rate",
        height=30,
        width=150,
        fg_color="#336082",
        corner_radius=10,
        font=("Montserrat Bold", 12),
        justify="left",
    )
    rate_label.grid(row=3, column=0, padx=10, pady=10)
    rate_entry = ctk.CTkEntry(update_entry_frames, font=("Helvetica", 12))
    rate_entry.grid(row=3, column=1, padx=10, pady=10)

    cost_label = ctk.CTkLabel(
        update_entry_frames,
        text="Cost",
        height=30,
        width=150,
        fg_color="#336082",
        corner_radius=10,
        font=("Montserrat Bold", 12),
        justify="left",
    )
    cost_label.grid(row=3, column=2, padx=10, pady=10)
    cost_entry = ctk.CTkEntry(update_entry_frames, font=("Helvetica", 12))
    cost_entry.grid(row=3, column=3, padx=10, pady=10)

    # Update Button after input
    update_btn = ctk.CTkButton(
        update_bills,
        text="Update Info",
        height=30,
        width=100,
        corner_radius=10,
        fg_color="#336082",
        font=("Montserrat Bold", 12),
        command=update_bills_info,
    )
    update_btn.place(relx=0.78, rely=0.70)

    # Button for clearing entries
    clear_entry_button = ctk.CTkButton(
        update_bills,
        text="Clear Entries",
        height=30,
        width=100,
        corner_radius=10,
        fg_color="#336082",
        font=("Montserrat Bold", 12),
        command=clear_bills_entries,
    )
    clear_entry_button.place(relx=0.65, rely=0.70)


# Link for Combobox in Payment
def my_upd2(*args):
    # Create a new database or connect to one that exists
    conn = sqlite3.connect("boarding_house.db")
    # Create a cursor instance
    cursor = conn.cursor()
    tenant_ids_entry.set("")
    query = "SELECT Tenant_ID from room WHERE Room_ID ='" + text_2.get() + "'"
    cursor.execute(query)
    result = cursor.fetchall()
    for ids in result:
        ids_of_tenants_2.append(ids[0])
    tenant_ids_entry.configure(values=ids_of_tenants_2)


# Widgets for Add and Update Payment
def add_payment_widget():
    global payment_ID_entry, room_ids_entry, tenant_ids_entry, payment_name_entry, payment_date_entry, payment_amount_entry, payment_method_entry, status_entry, ids_of_tenants_2, text_2
    # Windows
    add_payment = tk.Toplevel(payment_history_frame)
    add_payment.title("Add Payment")
    add_payment.geometry("1000x600")
    add_payment.maxsize(1000, 600)

    # Create Label Frame
    add_entry_frames = ttk.LabelFrame(add_payment, text="Add Entries")
    add_entry_frames.place(relx=0.01, rely=0.02, width=900, height=400)

    # Entry Box and Buttons
    # Add Payment Entry Boxes and Labels
    payment_ID_label = ctk.CTkLabel(
        add_entry_frames,
        text="Payment_ID",
        height=30,
        width=150,
        fg_color="#336082",
        corner_radius=10,
        font=("Montserrat Bold", 12),
        justify="left",
    )
    payment_ID_label.grid(row=0, column=0, padx=10, pady=10)
    payment_ID_entry = ctk.CTkEntry(add_entry_frames, font=("Helvetica", 12))
    payment_ID_entry.grid(row=0, column=1, padx=10, pady=10)

    room_ids_label = ctk.CTkLabel(
        add_entry_frames,
        text="Room_ID",
        height=30,
        width=150,
        fg_color="#336082",
        corner_radius=10,
        font=("Montserrat Bold", 12),
        justify="left",
    )
    room_ids_label.grid(row=0, column=2, padx=10, pady=10)

    # Linker
    text_2 = tk.StringVar()
    text_2.trace("w", my_upd2)

    # List containing the IDs of Tenant
    ids_of_tenants_2 = []

    # Create a new database or connect to one that exists
    conn = sqlite3.connect("boarding_house.db")
    # Create a cursor instance
    cursor = conn.cursor()

    cursor.execute("SELECT Room_ID from room")

    results = cursor.fetchall()
    # List containing the Room_IDs
    ids_of_rooms = []
    for ids in results:
        ids_of_rooms.append(ids[0])

    room_ids_entry = ctk.CTkComboBox(
        add_entry_frames,
        font=("Helvetica", 12),
        height=30,
        width=140,
        values=ids_of_rooms,
        button_hover_color="#F2E6D0",
        dropdown_hover_color="#BFAE99",
        variable=text_2,
    )
    room_ids_entry.set("")
    room_ids_entry.grid(row=0, column=3, padx=10, pady=10)

    tenant_ids_label = ctk.CTkLabel(
        add_entry_frames,
        text="Tenant_ID",
        height=30,
        width=150,
        fg_color="#336082",
        corner_radius=10,
        font=("Montserrat Bold", 12),
        justify="left",
    )
    tenant_ids_label.grid(row=1, column=0, padx=10, pady=10)

    tenant_ids_entry = ctk.CTkComboBox(
        add_entry_frames,
        font=("Helvetica", 12),
        height=30,
        width=140,
        values=ids_of_tenants_2,
        button_hover_color="#F2E6D0",
        dropdown_hover_color="#BFAE99",
    )
    tenant_ids_entry.set("")
    tenant_ids_entry.grid(row=1, column=1, padx=10, pady=10)

    payment_name_label = ctk.CTkLabel(
        add_entry_frames,
        text="Payment Name",
        height=30,
        width=150,
        fg_color="#336082",
        corner_radius=10,
        font=("Montserrat Bold", 12),
        justify="left",
    )
    payment_name_label.grid(row=1, column=2, padx=10, pady=10)

    payment_name_choices = ["Devices", "Electricity", "Rental Payment"]

    payment_name_entry = ctk.CTkComboBox(
        add_entry_frames,
        font=("Helvetica", 12),
        height=30,
        width=140,
        values=payment_name_choices,
        button_hover_color="#F2E6D0",
        dropdown_hover_color="#BFAE99",
    )
    payment_name_entry.set("Select Payment Name")
    payment_name_entry.grid(row=1, column=3, padx=10, pady=10)

    payment_date_label = ctk.CTkLabel(
        add_entry_frames,
        text="Payment Date",
        height=30,
        width=150,
        fg_color="#336082",
        corner_radius=10,
        font=("Montserrat Bold", 12),
        justify="left",
    )
    payment_date_label.grid(row=2, column=0, padx=10, pady=10)
    payment_date_entry = ctk.CTkEntry(add_entry_frames, font=("Helvetica", 12))
    payment_date_entry.grid(row=2, column=1, padx=10, pady=10)

    payment_amount_label = ctk.CTkLabel(
        add_entry_frames,
        text="Payment Amount",
        height=30,
        width=150,
        fg_color="#336082",
        corner_radius=10,
        font=("Montserrat Bold", 12),
        justify="left",
    )
    payment_amount_label.grid(row=2, column=2, padx=10, pady=10)
    payment_amount_entry = ctk.CTkEntry(add_entry_frames, font=("Helvetica", 12))
    payment_amount_entry.grid(row=2, column=3, padx=10, pady=10)

    payment_method_label = ctk.CTkLabel(
        add_entry_frames,
        text="Payment Method",
        height=30,
        width=150,
        fg_color="#336082",
        corner_radius=10,
        font=("Montserrat Bold", 12),
        justify="left",
    )
    payment_method_label.grid(row=3, column=0, padx=10, pady=10)

    payment_method_choices = ["Door-to-door", "GCash", "Palawan Pawnshop", "Others"]
    payment_method_entry = ctk.CTkComboBox(
        add_entry_frames,
        font=("Helvetica", 12),
        height=30,
        width=140,
        values=payment_method_choices,
        button_hover_color="#F2E6D0",
        dropdown_hover_color="#BFAE99",
    )
    payment_method_entry.set("Select payment method")
    payment_method_entry.grid(row=3, column=1, padx=10, pady=10)

    status_label = ctk.CTkLabel(
        add_entry_frames,
        text="Status",
        height=30,
        width=150,
        fg_color="#336082",
        corner_radius=10,
        font=("Montserrat Bold", 12),
        justify="left",
    )
    status_label.grid(row=3, column=2, padx=10, pady=10)

    status_choices = ["Paid", "Unpaid", "Partially paid"]
    status_entry = ctk.CTkComboBox(
        add_entry_frames,
        font=("Helvetica", 12),
        height=30,
        width=140,
        values=status_choices,
        button_hover_color="#F2E6D0",
        dropdown_hover_color="#BFAE99",
    )
    status_entry.set("Select Status")
    status_entry.grid(row=3, column=3, padx=10, pady=10)

    # Add Button after input
    add_btn = ctk.CTkButton(
        add_payment,
        text="Add Payment",
        height=30,
        width=100,
        corner_radius=10,
        fg_color="#336082",
        font=("Montserrat Bold", 12),
        command=add_payment_info,
    )
    add_btn.place(relx=0.78, rely=0.70)

    # Button for clearing entries
    clear_entry_button = ctk.CTkButton(
        add_payment,
        text="Clear Entries",
        height=30,
        width=100,
        corner_radius=10,
        fg_color="#336082",
        font=("Montserrat Bold", 12),
        command=clear_payment_entries,
    )
    clear_entry_button.place(relx=0.65, rely=0.70)


def update_payment_widget():
    global payment_ID_entry, room_ids_entry, tenant_ids_entry, payment_name_entry, payment_date_entry, payment_amount_entry, payment_method_entry, status_entry
    # Windows
    update_payment = tk.Toplevel(payment_history_frame)
    update_payment.title("Update Payment")
    update_payment.geometry("1000x600")
    update_payment.maxsize(1000, 600)

    # Create Label Frame
    update_entry_frames = ttk.LabelFrame(update_payment, text="Update Entries")
    update_entry_frames.place(relx=0.01, rely=0.02, width=900, height=400)

    # Entry Box and Buttons
    # Update Payment Entry Boxes and Labels
    payment_ID_label = ctk.CTkLabel(
        update_entry_frames,
        text="Payment_ID",
        height=30,
        width=150,
        fg_color="#336082",
        corner_radius=10,
        font=("Montserrat Bold", 12),
        justify="left",
    )
    payment_ID_label.grid(row=0, column=0, padx=10, pady=10)
    payment_ID_entry = ctk.CTkEntry(update_entry_frames, font=("Helvetica", 12))
    payment_ID_entry.grid(row=0, column=1, padx=10, pady=10)

    room_ids_label = ctk.CTkLabel(
        update_entry_frames,
        text="Room_ID",
        height=30,
        width=150,
        fg_color="#336082",
        corner_radius=10,
        font=("Montserrat Bold", 12),
        justify="left",
    )
    room_ids_label.grid(row=0, column=2, padx=10, pady=10)

    room_ids_entry = ctk.CTkEntry(update_entry_frames, font=("Helvetica", 12))
    room_ids_entry.grid(row=0, column=3, padx=10, pady=10)

    tenant_ids_label = ctk.CTkLabel(
        update_entry_frames,
        text="Tenant_ID",
        height=30,
        width=150,
        fg_color="#336082",
        corner_radius=10,
        font=("Montserrat Bold", 12),
        justify="left",
    )
    tenant_ids_label.grid(row=1, column=0, padx=10, pady=10)

    tenant_ids_entry = ctk.CTkEntry(update_entry_frames, font=("Helvetica", 12))
    tenant_ids_entry.grid(row=1, column=1, padx=10, pady=10)

    payment_name_label = ctk.CTkLabel(
        update_entry_frames,
        text="Payment Name",
        height=30,
        width=150,
        fg_color="#336082",
        corner_radius=10,
        font=("Montserrat Bold", 12),
        justify="left",
    )
    payment_name_label.grid(row=1, column=2, padx=10, pady=10)

    payment_name_choices = ["Devices", "Electricity", "Rental Payment"]
    payment_name_entry = ctk.CTkComboBox(
        update_entry_frames,
        font=("Helvetica", 12),
        height=30,
        width=140,
        values=payment_name_choices,
        button_hover_color="#F2E6D0",
        dropdown_hover_color="#BFAE99",
    )
    payment_name_entry.set("Select Payment Name")
    payment_name_entry.grid(row=1, column=3, padx=10, pady=10)

    payment_date_label = ctk.CTkLabel(
        update_entry_frames,
        text="Payment Date",
        height=30,
        width=150,
        fg_color="#336082",
        corner_radius=10,
        font=("Montserrat Bold", 12),
        justify="left",
    )
    payment_date_label.grid(row=2, column=0, padx=10, pady=10)
    payment_date_entry = ctk.CTkEntry(update_entry_frames, font=("Helvetica", 12))
    payment_date_entry.grid(row=2, column=1, padx=10, pady=10)

    payment_amount_label = ctk.CTkLabel(
        update_entry_frames,
        text="Payment Amount",
        height=30,
        width=150,
        fg_color="#336082",
        corner_radius=10,
        font=("Montserrat Bold", 12),
        justify="left",
    )
    payment_amount_label.grid(row=2, column=2, padx=10, pady=10)
    payment_amount_entry = ctk.CTkEntry(update_entry_frames, font=("Helvetica", 12))
    payment_amount_entry.grid(row=2, column=3, padx=10, pady=10)

    payment_method_label = ctk.CTkLabel(
        update_entry_frames,
        text="Payment Method",
        height=30,
        width=150,
        fg_color="#336082",
        corner_radius=10,
        font=("Montserrat Bold", 12),
        justify="left",
    )
    payment_method_label.grid(row=3, column=0, padx=10, pady=10)
    payment_method_choices = ["Door-to-door", "GCash", "Palawan Pawnshop", "Others"]
    payment_method_entry = ctk.CTkComboBox(
        update_entry_frames,
        font=("Helvetica", 12),
        height=30,
        width=140,
        values=payment_method_choices,
        button_hover_color="#F2E6D0",
        dropdown_hover_color="#BFAE99",
    )
    payment_method_entry.set("Select payment method")
    payment_method_entry.grid(row=3, column=1, padx=10, pady=10)

    status_label = ctk.CTkLabel(
        update_entry_frames,
        text="Status",
        height=30,
        width=150,
        fg_color="#336082",
        corner_radius=10,
        font=("Montserrat Bold", 12),
        justify="left",
    )
    status_label.grid(row=3, column=2, padx=10, pady=10)
    status_choices = ["Paid", "Unpaid", "Partially paid"]
    status_entry = ctk.CTkComboBox(
        update_entry_frames,
        font=("Helvetica", 12),
        height=30,
        width=140,
        values=status_choices,
        button_hover_color="#F2E6D0",
        dropdown_hover_color="#BFAE99",
    )
    status_entry.set("Select Status")
    status_entry.grid(row=3, column=3, padx=10, pady=10)

    # Update Button after input
    update_btn = ctk.CTkButton(
        update_payment,
        text="Update Info",
        height=30,
        width=100,
        corner_radius=10,
        fg_color="#336082",
        font=("Montserrat Bold", 12),
        command=update_payment_info,
    )
    update_btn.place(relx=0.78, rely=0.70)

    # Button for clearing entries
    clear_entry_button = ctk.CTkButton(
        update_payment,
        text="Clear Entries",
        height=30,
        width=100,
        corner_radius=10,
        fg_color="#336082",
        font=("Montserrat Bold", 12),
        command=clear_payment_entries,
    )
    clear_entry_button.place(relx=0.65, rely=0.70)


# Selection for Bind Treeview
def selected_tenant(event):
    tenant_id_entry.delete(0, "end")
    tenant_name_entry.delete(0, "end")
    age_entry.delete(0, "end")
    email_entry.delete(0, "end")
    address_entry.delete(0, "end")
    occupation_entry.delete(0, "end")
    contact_number_entry.delete(0, "end")
    number_of_edevices_entry.delete(0, "end")

    # Grab record number
    selected = treeview_tenant.focus()
    # Grab record values
    values = treeview_tenant.item(selected, "values")

    # Output/Display to entry Boxes
    tenant_id_entry.insert(0, values[0])
    tenant_name_entry.insert(0, values[1])
    age_entry.insert(0, values[2])
    email_entry.insert(0, values[4])
    address_entry.insert(0, values[5])
    occupation_entry.insert(0, values[6])
    contact_number_entry.insert(0, values[7])
    number_of_edevices_entry.insert(0, values[8])


# Selection for ECTenants
def selected_ectenant(event):
    ec_tenant_name_entry.delete(0, "end")
    ec_age_entry.delete(0, "end")
    ec_relationship_entry.delete(0, "end")
    ec_contact_number_entry.delete(0, "end")
    ec_email_entry.delete(0, "end")
    ec_address_entry.delete(0, "end")
    update_tenants_id_entry.delete(0, "end")

    # Grab record number
    selected = treeview_emergency.focus()
    # Grab record values
    values = treeview_emergency.item(selected, "values")

    # Output/Display to entry Boxes
    ec_tenant_name_entry.insert(0, values[0])
    ec_age_entry.insert(0, values[1])
    ec_relationship_entry.insert(0, values[3])
    ec_contact_number_entry.insert(0, values[4])
    ec_email_entry.insert(0, values[5])
    ec_address_entry.insert(0, values[6])
    update_tenants_id_entry.insert(0, values[7])


# Selection for Rooms
def selected_room(event):
    room_ID_entry.delete(0, "end")
    rental_amount_entry.delete(0, "end")
    rent_date_entry.delete(0, "end")
    due_date_entry.delete(0, "end")
    electric_meter_number_entry.delete(0, "end")

    # Grab record number
    selected = treeview_room_assignment.focus()
    # Grab record values
    values = treeview_room_assignment.item(selected, "values")

    # Output/Display to entry Boxes
    room_ID_entry.insert(0, values[0])
    rental_amount_entry.insert(0, values[2])
    rent_date_entry.insert(0, values[3])
    due_date_entry.insert(0, values[4])
    electric_meter_number_entry.insert(0, values[5])


# Selection for Bills
def selected_bills(event):
    bill_id_entry.delete(0, "end")
    update_room_id_entry.delete(0, "end")
    update_tenant_ID_entry.delete(0, "end")
    bill_name_entry.delete(0, "end")
    prev_entry.delete(0, "end")
    current_entry.delete(0, "end")
    rate_entry.delete(0, "end")
    cost_entry.delete(0, "end")

    # Grab record number
    selected = treeview_bills.focus()
    # Grab record values
    values = treeview_bills.item(selected, "values")

    # Output/Display to entry Boxes
    bill_id_entry.insert(0, values[0])
    update_room_id_entry.insert(0, values[1])
    update_tenant_ID_entry.insert(0, values[2])
    bill_name_entry.insert(0, values[3])
    prev_entry.insert(0, values[4])
    current_entry.insert(0, values[5])
    rate_entry.insert(0, values[6])
    cost_entry.insert(0, values[7])


# Selection for Payments
def selected_payment(event):
    payment_ID_entry.delete(0, "end")
    room_ids_entry.delete(0, "end")
    tenant_ids_entry.delete(0, "end")
    payment_date_entry.delete(0, "end")
    payment_amount_entry.delete(0, "end")

    # Grab record number
    selected = treeview_payment_history.focus()
    # Grab record values
    values = treeview_payment_history.item(selected, "values")

    # Output/Display to entry Boxes
    payment_ID_entry.insert(0, values[0])
    room_ids_entry.insert(0, values[1])
    tenant_ids_entry.insert(0, values[2])
    payment_date_entry.insert(0, values[4])
    payment_amount_entry.insert(0, values[5])


# Clear Entries in the Entry boxes of Tenants
def clear_entries_tenants():
    tenant_id_entry.delete(0, "end")
    tenant_name_entry.delete(0, "end")
    age_entry.delete(0, "end")
    email_entry.delete(0, "end")
    address_entry.delete(0, "end")
    occupation_entry.delete(0, "end")
    contact_number_entry.delete(0, "end")
    number_of_edevices_entry.delete(0, "end")


# Clear Entries in the Entry boxes of EC_Tenants
def clear_entries_ec_tenants():
    ec_tenant_name_entry.delete(0, "end")
    ec_age_entry.delete(0, "end")
    ec_relationship_entry.delete(0, "end")
    ec_contact_number_entry.delete(0, "end")
    ec_email_entry.delete(0, "end")
    ec_address_entry.delete(0, "end")


# Clear Entries in the Entry Boxes of Rooms
def clear_room_entries():
    room_ID_entry.delete(0, "end")
    rental_amount_entry.delete(0, "end")
    rent_date_entry.delete(0, "end")
    due_date_entry.delete(0, "end")
    electric_meter_number_entry.delete(0, "end")


# Clear Entries in the Entry Boxes of Bills
def clear_bills_entries():
    bill_id_entry.delete(0, "end")
    update_room_id_entry.delete(0, "end")
    update_tenant_ID_entry.delete(0, "end")
    bill_name_entry.delete(0, "end")
    prev_entry.delete(0, "end")
    current_entry.delete(0, "end")
    rate_entry.delete(0, "end")
    cost_entry.delete(0, "end")


# Clear Entries in the Entry Boxes of Payments
def clear_payment_entries():
    payment_ID_entry.delete(0, "end")
    payment_date_entry.delete(0, "end")
    payment_amount_entry.delete(0, "end")


# Functions
def dashboard_function():
    global greetings_label
    greetings_label.destroy()
    tenant_frame.place_forget()
    room_assignment_frame.place_forget()
    bill_frame.place_forget()
    payment_history_frame.place_forget()
    dashboard_frame.place(relx=0.23, rely=0.05)

    # Labels
    dashboard_label = ctk.CTkLabel(
        dashboard_frame,
        text="Dashboard",
        height=40,
        width=150,
        fg_color="#336082",
        corner_radius=10,
        font=("Montserrat Bold", 12),
        justify="left",
    )
    dashboard_label.place(relx=0.01, rely=0.05)

    # Connect to sqlite database
    conn = sqlite3.connect("boarding_house.db")
    cur = conn.cursor()

    cur.execute("SELECT COUNT(*) FROM tenants")
    results = cur.fetchone()
    total_tenants = results[0]
    number_of_tenants_label = ctk.CTkLabel(
        dashboard_frame,
        text=f"{total_tenants}\n Number of Tenants",
        textvariable="",
        height=100,
        width=300,
        fg_color="#336082",
        corner_radius=10,
        font=("Montserrat Bold", 12),
        justify="center",
    )

    # Connect to sqlite database
    conn = sqlite3.connect("boarding_house.db")
    cur = conn.cursor()

    cur.execute("SELECT COUNT(*) FROM room")
    results = cur.fetchone()
    total_rooms = results[0]
    number_of_rooms_label = ctk.CTkLabel(
        dashboard_frame,
        text=f"{total_rooms}\n Number of Rooms",
        textvariable="",
        height=100,
        width=300,
        fg_color="#336082",
        corner_radius=10,
        font=("Montserrat Bold", 12),
        justify="center",
    )

    total_bill_label = ctk.CTkLabel(
        dashboard_frame,
        text="Bills",
        textvariable="₱",
        height=100,
        width=300,
        fg_color="#336082",
        corner_radius=10,
        font=("Montserrat Bold", 12),
        justify="center",
    )

    payment_history_label = ctk.CTkLabel(
        dashboard_frame,
        text="Payment History",
        textvariable="",
        height=100,
        width=300,
        fg_color="#336082",
        corner_radius=10,
        font=("Montserrat Bold", 12),
        justify="center",
    )

    # Buttons
    number_of_tenants_info_button = ctk.CTkButton(
        dashboard_frame,
        text="More info",
        height=30,
        width=300,
        corner_radius=0,
        fg_color="#242D40",
        font=("Montserrat Bold", 12),
        command=tenant_profile_function,
    )
    number_of_rooms_info_button = ctk.CTkButton(
        dashboard_frame,
        text="More info",
        height=30,
        width=300,
        corner_radius=0,
        fg_color="#242D40",
        font=("Montserrat Bold", 12),
        command=room_assignment_function,
    )

    total_bill_button = ctk.CTkButton(
        dashboard_frame,
        text="More info",
        height=30,
        width=300,
        corner_radius=0,
        fg_color="#242D40",
        font=("Montserrat Bold", 12),
        command=bills_function,
    )
    payment_history_button = ctk.CTkButton(
        dashboard_frame,
        text="More info",
        height=30,
        width=300,
        corner_radius=0,
        fg_color="#242D40",
        font=("Montserrat Bold", 12),
        command=payment_history_function,
    )

    # Commit changes
    conn.commit()

    # Close our connection
    conn.close()

    # Display the labels and buttons
    number_of_tenants_label.place(relx=0.01, rely=0.15)
    number_of_rooms_label.place(relx=0.35, rely=0.15)
    total_bill_label.place(relx=0.69, rely=0.15)
    payment_history_label.place(relx=0.01, rely=0.35)

    number_of_tenants_info_button.place(relx=0.01, rely=0.26)
    number_of_rooms_info_button.place(relx=0.35, rely=0.26)
    total_bill_button.place(relx=0.69, rely=0.26)
    payment_history_button.place(relx=0.01, rely=0.46)


def tenant_profile_function():
    global greetings_label, search_tenant_entry, search_ETenant_entry
    greetings_label.destroy()
    dashboard_frame.place_forget()
    room_assignment_frame.place_forget()
    bill_frame.place_forget()
    payment_history_frame.place_forget()
    tenant_frame.place(relx=0.23, rely=0.05)

    # Labels
    tenant_profile_label = ctk.CTkLabel(
        tenant_frame,
        text="Tenant Profile",
        height=40,
        width=150,
        fg_color="#336082",
        corner_radius=10,
        font=("Montserrat Bold", 12),
        justify="left",
    )
    tenant_profile_label.place(relx=0.01, rely=0.05)

    # Add Tenant Button
    add_tenant_button = ctk.CTkButton(
        tenant_frame,
        text="Add Tenant Profile",
        height=30,
        width=100,
        corner_radius=10,
        fg_color="#336082",
        font=("Montserrat Bold", 12),
        command=add_tenant_widget,
    )
    add_tenant_button.place(relx=0.01, rely=0.15)

    # Search Entry and Button
    search_tenant_entry = ctk.CTkEntry(
        tenant_frame,
        width=200,
        height=30,
        corner_radius=5,
        fg_color="#F2E6D0",
        placeholder_text="Enter Tenant ID",
        placeholder_text_color="#BFAE99",
        text_color="#3e637a",
        font=("Montserrat Bold", 12),
    )
    search_tenant_entry.place(relx=0.155, rely=0.15)
    search_button = ctk.CTkButton(
        tenant_frame,
        text="Search Tenant ID",
        height=30,
        width=100,
        corner_radius=10,
        fg_color="#336082",
        font=("Montserrat Bold", 12),
        command=search_tenant_id,
    )
    search_button.place(relx=0.36, rely=0.15)

    # Delete Tenant Button
    delete_button = ctk.CTkButton(
        tenant_frame,
        text="Delete Tenant",
        height=30,
        width=122,
        corner_radius=10,
        fg_color="#336082",
        font=("Montserrat Bold", 12),
        command=delete_tenant,
    )
    delete_button.place(relx=0.85, rely=0.30)

    # Update Tenant Button
    update_button = ctk.CTkButton(
        tenant_frame,
        text="Update Tenant",
        height=30,
        width=122,
        corner_radius=10,
        fg_color="#336082",
        font=("Montserrat Bold", 12),
        command=update_tenant_widget,
    )
    update_button.place(relx=0.85, rely=0.25)

    # Display Tenant Button
    display_button = ctk.CTkButton(
        tenant_frame,
        text="Display Tenant",
        height=30,
        width=122,
        corner_radius=10,
        fg_color="#336082",
        font=("Montserrat Bold", 12),
        command=tenant_query,
    )
    display_button.place(relx=0.85, rely=0.2)

    # Emergency Contact Buttons
    # Labels
    Etenant_profile_label = ctk.CTkLabel(
        tenant_frame,
        text="Emergency Contact Profile",
        height=40,
        width=150,
        fg_color="#336082",
        corner_radius=10,
        font=("Montserrat Bold", 12),
        justify="left",
    )
    Etenant_profile_label.place(relx=0.01, rely=0.50)
    # Add ETenant Button
    add_Etenant_button = ctk.CTkButton(
        tenant_frame,
        text="Add ETenant Profile",
        height=30,
        width=100,
        corner_radius=10,
        fg_color="#336082",
        font=("Montserrat Bold", 12),
        command=add_ec_tenant_widget,
    )
    add_Etenant_button.place(relx=0.01, rely=0.6)

    # Search Entry and Button
    search_ETenant_entry = ctk.CTkEntry(
        tenant_frame,
        width=200,
        height=30,
        corner_radius=5,
        fg_color="#F2E6D0",
        placeholder_text="Enter ETenant ID",
        placeholder_text_color="#BFAE99",
        text_color="#3e637a",
        font=("Montserrat Bold", 12),
    )
    search_ETenant_entry.place(relx=0.17, rely=0.6)
    search_Etenant_button = ctk.CTkButton(
        tenant_frame,
        text="Search ETenant ID",
        height=30,
        width=100,
        corner_radius=10,
        fg_color="#336082",
        font=("Montserrat Bold", 12),
        command=search_ec_tenant_info,
    )
    search_Etenant_button.place(relx=0.375, rely=0.6)

    # Delete ETenant Button
    delete_Etenant_button = ctk.CTkButton(
        tenant_frame,
        text="Delete ETenant",
        height=30,
        width=122,
        corner_radius=10,
        fg_color="#336082",
        font=("Montserrat Bold", 12),
        command=delete_ec_tenant_info,
    )
    delete_Etenant_button.place(relx=0.85, rely=0.75)

    # Update ETenant Button
    update_Etenant_button = ctk.CTkButton(
        tenant_frame,
        text="Update ETenant",
        height=30,
        width=115,
        corner_radius=10,
        fg_color="#336082",
        font=("Montserrat Bold", 12),
        command=update_ec_tenant_widget,
    )
    update_Etenant_button.place(relx=0.85, rely=0.70)

    # Display ETenant Button
    display_Etenant_button = ctk.CTkButton(
        tenant_frame,
        text="Display ETenant",
        height=30,
        width=122,
        corner_radius=10,
        fg_color="#336082",
        font=("Montserrat Bold", 12),
        command=emergency_contacts_query,
    )
    display_Etenant_button.place(relx=0.85, rely=0.65)

    # Treeview Display
    tenant_treeview()
    emergency_contact_treeview()


def room_assignment_function():
    global greetings_label, search_room_entry
    greetings_label.destroy()
    dashboard_frame.place_forget()
    bill_frame.place_forget()
    payment_history_frame.place_forget()
    tenant_frame.place_forget()
    room_assignment_frame.place(relx=0.23, rely=0.05)

    # Labels
    room_assignment_label = ctk.CTkLabel(
        room_assignment_frame,
        text="Room Assignment",
        height=40,
        width=150,
        fg_color="#336082",
        corner_radius=10,
        font=("Montserrat Bold", 12),
        justify="left",
    )
    room_assignment_label.place(relx=0.01, rely=0.05)

    # Add Room Button
    add_room_assignment_button = ctk.CTkButton(
        room_assignment_frame,
        text="Add Room",
        height=30,
        width=100,
        corner_radius=10,
        fg_color="#336082",
        font=("Montserrat Bold", 12),
        command=add_room_widget,
    )
    add_room_assignment_button.place(relx=0.01, rely=0.15)

    # Search Entry and Button
    search_room_entry = ctk.CTkEntry(
        room_assignment_frame,
        width=200,
        height=30,
        corner_radius=5,
        fg_color="#F2E6D0",
        placeholder_text="Enter Room ID",
        placeholder_text_color="#BFAE99",
        text_color="#3e637a",
        font=("Montserrat Bold", 12),
    )
    search_room_entry.place(relx=0.12, rely=0.15)
    search_room_button = ctk.CTkButton(
        room_assignment_frame,
        text="Search Room ID",
        height=30,
        width=100,
        corner_radius=10,
        fg_color="#336082",
        font=("Montserrat Bold", 12),
        command=search_room_info,
    )
    search_room_button.place(relx=0.325, rely=0.15)

    # Delete Room Button
    delete_button = ctk.CTkButton(
        room_assignment_frame,
        text="Delete Room",
        height=30,
        width=122,
        corner_radius=10,
        fg_color="#336082",
        font=("Montserrat Bold", 12),
        command=delete_room_info,
    )
    delete_button.place(relx=0.83, rely=0.30)

    # Update Room Button
    update_button = ctk.CTkButton(
        room_assignment_frame,
        text="Update Room",
        height=30,
        width=122,
        corner_radius=10,
        fg_color="#336082",
        font=("Montserrat Bold", 12),
        command=update_room_widget,
    )
    update_button.place(relx=0.83, rely=0.25)

    # Display Bills Button
    display_button = ctk.CTkButton(
        room_assignment_frame,
        text="Display Rooms",
        height=30,
        width=122,
        corner_radius=10,
        fg_color="#336082",
        font=("Montserrat Bold", 12),
        command=room_assignment_query,
    )
    display_button.place(relx=0.83, rely=0.2)

    # Treeview Display
    room_assignment_treeview()


def bills_function():
    global greetings_label, search_bill_entry
    greetings_label.destroy()
    dashboard_frame.place_forget()
    payment_history_frame.place_forget()
    tenant_frame.place_forget()
    room_assignment_frame.place_forget()
    bill_frame.place(relx=0.23, rely=0.05)

    # Labels
    bill_label = ctk.CTkLabel(
        bill_frame,
        text="Bills",
        height=40,
        width=150,
        fg_color="#336082",
        corner_radius=10,
        font=("Montserrat Bold", 12),
        justify="left",
    )
    bill_label.place(relx=0.01, rely=0.05)

    # Add Room Button
    bills_button = ctk.CTkButton(
        bill_frame,
        text="Add Bill",
        height=30,
        width=100,
        corner_radius=10,
        fg_color="#336082",
        font=("Montserrat Bold", 12),
        command=add_bills_widget,
    )
    bills_button.place(relx=0.01, rely=0.15)

    # Search Entry and Button
    search_bill_entry = ctk.CTkEntry(
        bill_frame,
        width=200,
        height=30,
        corner_radius=5,
        fg_color="#F2E6D0",
        placeholder_text="Enter Bill_ID",
        placeholder_text_color="#BFAE99",
        text_color="#3e637a",
        font=("Montserrat Bold", 12),
    )
    search_bill_entry.place(relx=0.12, rely=0.15)
    search_bill_button = ctk.CTkButton(
        bill_frame,
        text="Search Bill_ID",
        height=30,
        width=100,
        corner_radius=10,
        fg_color="#336082",
        font=("Montserrat Bold", 12),
        command=search_bills_info,
    )
    search_bill_button.place(relx=0.325, rely=0.15)

    # Delete Bill Button
    delete_bill_button = ctk.CTkButton(
        bill_frame,
        text="Delete Bill",
        height=30,
        width=122,
        corner_radius=10,
        fg_color="#336082",
        font=("Montserrat Bold", 12),
        command=delete_bills_info,
    )
    delete_bill_button.place(relx=0.82, rely=0.30)

    # Update Bill Button
    update_bill_button = ctk.CTkButton(
        bill_frame,
        text="Update Bill",
        height=30,
        width=122,
        corner_radius=10,
        fg_color="#336082",
        font=("Montserrat Bold", 12),
        command=update_bills_widget,
    )
    update_bill_button.place(relx=0.82, rely=0.25)

    # Display Bill Button
    display_bill_button = ctk.CTkButton(
        bill_frame,
        text="Display Bill",
        height=30,
        width=122,
        corner_radius=10,
        fg_color="#336082",
        font=("Montserrat Bold", 12),
        command=bill_query,
    )
    display_bill_button.place(relx=0.82, rely=0.20)

    # Display the Treeview
    bills_treeview()


def payment_history_function():
    global greetings_label, search_payment_entry
    greetings_label.destroy()
    dashboard_frame.place_forget()
    bill_frame.place_forget()
    tenant_frame.place_forget()
    room_assignment_frame.place_forget()
    payment_history_frame.place(relx=0.23, rely=0.05)
    # Labels
    payment_history_label = ctk.CTkLabel(
        payment_history_frame,
        text="Payment History",
        height=40,
        width=150,
        fg_color="#336082",
        corner_radius=10,
        font=("Montserrat Bold", 12),
        justify="left",
    )
    payment_history_label.place(relx=0.01, rely=0.05)

    # Add Payment Button
    add_payment_history_button = ctk.CTkButton(
        payment_history_frame,
        text="Add Payment",
        height=30,
        width=100,
        corner_radius=10,
        fg_color="#336082",
        font=("Montserrat Bold", 12),
        command=add_payment_widget,
    )
    add_payment_history_button.place(relx=0.01, rely=0.15)

    # Search Entry and Button
    search_payment_entry = ctk.CTkEntry(
        payment_history_frame,
        width=200,
        height=30,
        corner_radius=5,
        fg_color="#F2E6D0",
        placeholder_text="Enter Payment_ID",
        placeholder_text_color="#BFAE99",
        text_color="#3e637a",
        font=("Montserrat Bold", 12),
    )
    search_payment_entry.place(relx=0.12, rely=0.15)
    search_payment_button = ctk.CTkButton(
        payment_history_frame,
        text="Search Payment_ID",
        height=30,
        width=100,
        corner_radius=10,
        fg_color="#336082",
        font=("Montserrat Bold", 12),
        command=search_payment_info,
    )
    search_payment_button.place(relx=0.325, rely=0.15)

    # Delete Payment Button
    delete_payment_button = ctk.CTkButton(
        payment_history_frame,
        text="Delete Payment",
        height=30,
        width=128,
        corner_radius=10,
        fg_color="#336082",
        font=("Montserrat Bold", 12),
        command=delete_payment_info,
    )
    delete_payment_button.place(relx=0.82, rely=0.30)

    # Update Payment Button
    update_payment_button = ctk.CTkButton(
        payment_history_frame,
        text="Update Payment",
        height=30,
        width=115,
        corner_radius=10,
        fg_color="#336082",
        font=("Montserrat Bold", 12),
        command=update_payment_widget,
    )
    update_payment_button.place(relx=0.82, rely=0.25)

    # Display Payment Button
    display_payment_button = ctk.CTkButton(
        payment_history_frame,
        text="Display Payment",
        height=30,
        width=122,
        corner_radius=10,
        fg_color="#336082",
        font=("Montserrat Bold", 12),
        command=payment_history_query,
    )
    display_payment_button.place(relx=0.82, rely=0.20)

    payment_history_treeview()


def exit_function():
    response = messagebox.askyesno(
        "Notice!",
        "Are you sure you want to exit the app?",
    )
    if response == 1:
        root.destroy()


class SlidePanel(ctk.CTkFrame):
    def __init__(self, parent, start_pos, end_pos):
        super().__init__(master=parent, fg_color="#242D40")

        # General attributes
        self.start_pos = start_pos - 0.25
        self.end_pos = end_pos + 0.2
        self.width = abs(start_pos - end_pos)

        # Animation logic
        self.pos = self.start_pos
        self.in_start_pos = True

        # layout
        self.place(relx=self.start_pos, rely=0.05, relwidth=self.width, relheight=0.9)

    def animate(self):
        if self.in_start_pos:
            self.animate_forward()
        else:
            self.animate_backward()

    def animate_forward(self):
        if self.pos < self.end_pos:
            self.pos += 0.008
            self.place(relx=self.pos, rely=0.05, relwidth=self.width, relheight=0.9)
            self.after(15, self.animate_forward)
        else:
            self.in_start_pos = False

    def animate_backward(self):
        if self.pos > self.start_pos:
            self.pos -= 0.008
            self.place(relx=self.pos, rely=0.05, relwidth=self.width, relheight=0.9)
            self.after(15, self.animate_backward)
        else:
            self.in_start_pos = True


# Animated widget
animated_panel = SlidePanel(root, 0, -0.3)

# Main Buttons inside the Slide Panel
dashboard_button = ctk.CTkButton(
    animated_panel,
    text="Dashboard",
    height=30,
    width=150,
    corner_radius=5,
    font=("Montserrat Bold", 12),
    command=dashboard_function,
)
dashboard_button.place(relx=0.65, rely=0.2, anchor="center")
tenant_profile_button = ctk.CTkButton(
    animated_panel,
    text="Tenant Profile",
    height=30,
    width=150,
    corner_radius=5,
    font=("Montserrat Bold", 12),
    command=tenant_profile_function,
)
tenant_profile_button.place(relx=0.65, rely=0.3, anchor="center")
room_assignment_button = ctk.CTkButton(
    animated_panel,
    text="Room Assignment",
    height=30,
    width=150,
    corner_radius=5,
    font=("Montserrat Bold", 12),
    command=room_assignment_function,
)
room_assignment_button.place(relx=0.65, rely=0.4, anchor="center")
bills_button = ctk.CTkButton(
    animated_panel,
    text="Bills",
    height=30,
    width=150,
    corner_radius=5,
    font=("Montserrat Bold", 12),
    command=bills_function,
)
bills_button.place(relx=0.65, rely=0.5, anchor="center")
payment_history_button = ctk.CTkButton(
    animated_panel,
    text="Payment History",
    height=30,
    width=150,
    corner_radius=5,
    font=("Montserrat Bold", 12),
    command=payment_history_function,
)
payment_history_button.place(relx=0.65, rely=0.6, anchor="center")
exit_button = ctk.CTkButton(
    animated_panel,
    text="Exit",
    height=30,
    width=150,
    corner_radius=5,
    command=exit_function,
    font=("Montserrat Bold", 12),
)
exit_button.place(relx=0.65, rely=0.7, anchor="center")
# Button in the slide panel
button_x = 0.95
button = ctk.CTkButton(
    animated_panel, text="≡", command=animated_panel.animate, width=20
)
button.place(relx=button_x, rely=0.05, anchor="center")

# Running the query and creation of tables
create_tables()

# Run to pull data from the database on start
tenant_query()
emergency_contacts_query()
room_assignment_query()
bill_query()
payment_history_query()

# Bind Treeview
treeview_tenant.bind("<ButtonRelease-1>", selected_tenant)
treeview_emergency.bind("<ButtonRelease-1>", selected_ectenant)
treeview_room_assignment.bind("<ButtonRelease-1>", selected_room)
treeview_bills.bind("<ButtonRelease-1>", selected_bills)
treeview_payment_history.bind("<ButtonRelease-1>", selected_payment)

root.bind("<Escape>", lambda event: root.quit())
# Root
root.mainloop()
