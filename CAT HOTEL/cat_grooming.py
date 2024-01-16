import tkinter as tk
from tkcalendar import Calendar
from tkinter import CENTER, Label, messagebox
import mysql.connector


# Connect to my MySQL database
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",

)

# creating cursor object to execute SQL queries
mycursor = mydb.cursor()

# Function to handle the calculation and database saving
def collect_data():
    grooming_type = package_var.get()
    quantity = int(period_spinbox.get())
    appointment_date= my_label.cget("text")
   
    
    #  Defining the prices from the User selections
    prices = {
        "Aromatic salt Bath": 139,
        "Oatmeal Scrub": 129,
        "Collagen Essence Bath": 98,
        "Royal Splash": 129
  
    }
    
    # Calculating the total price. Which derived from the selection (Type, Period).
    total_price = (prices[grooming_type] * quantity)
    
    # Inserting data to the database,  3 attributes. 
    sql = "INSERT INTO package (grooming_type, quantity_cat, date_appointment) VALUES (%s, %s, %s)"
    val = (grooming_type, quantity, appointment_date)
    mycursor.execute(sql, val)
    mydb.commit()

#implement the deletion
def delete_data():
    pass



# Your Main window, You need to have the title, geometry (MUST)
root = tk.Tk()
root.title("Cat Grooming")
root.geometry('800x700')

# Set the background color
root.configure(bg='#3C565B')

# Page Title
label = tk.Label(root, text='Grooming Your Cat ^_^', font=("Times New Roman", 18, "bold"), bg='#3C565B', fg='white')
label.grid(row=0, column= 3, pady=20)

# Prices List by using textbox
prices_text1 = tk.Text(root, height=8, width=20, font= ("Georgia", 12), borderwidth=2, relief="sunken", bg= '#B0CFDE')
prices_text1.grid(row=1, column=1, padx=8, pady=(20, 20))

prices_text2 = tk.Text(root, height=8, width=20, font=("Georgia", 12), borderwidth=2, relief="sunken", bg= '#B0CFDE')
prices_text2.grid(row=2, column=1, padx=8, pady=(20, 20))


# The defined list by using pricebox

prices_text1.insert(tk.END,"\n")
prices_text2.insert(tk.END,"\n")
prices_text1.insert(tk.END, "Wellness Cat Spa :\n")
prices_text1.insert(tk.END, "Aromatic Salt Bath \nPrice: RM 139\n\n")
prices_text1.insert(tk.END, "Oatmeal Scrub \nPrice: RM129\n\n")

prices_text2.insert(tk.END, "Beauty Cat Spa :\n")
prices_text2.insert(tk.END, "Collagen Essence Bath \nPrice: RM 98\n\n")
prices_text2.insert(tk.END, "Royal Splash \nPrice: RM128\n\n")

# Configure tags for center alignment
prices_text1.tag_configure("center", justify='center')
prices_text2.tag_configure("center", justify='center')

# Center the text in the Text widgets
def center_text(text_widget):
    text_widget.tag_add("center", "1.0", "end")

center_text(prices_text1)
center_text(prices_text2)

prices_text1.configure(state='disabled')
prices_text2.configure(state='disabled')

choose_frame = tk.Frame(root)
choose_frame.grid(row=1, column=4, padx=20)
choose_frame.configure(bg='#3C565B')

# Trip Type Dropdown (Label)
period_label = tk.Label(choose_frame, text="Choose Your Grooming Type")
period_label.grid(pady=10)

# Trip Type Dropdown
package_var = tk.StringVar(choose_frame)
package_var.set("Select Your Grooming Type")  # Default value before your selection
trip_dropdown = tk.OptionMenu(choose_frame, package_var, "Aromatic Salt Bath", " Oatmeal Scrub", "Collagen Essence Bath", "Royal Splash" )
trip_dropdown.grid(pady=10)


# Packs Entry. Label and user can insert data thru entry
quantity_label = tk.Label(choose_frame, text="Enter Quantity:")
quantity_label.grid()
period_spinbox = tk.Spinbox(choose_frame, from_=1, to=4)  # Adjust the range as needed
period_spinbox.grid()

choose_frame1 = tk.Frame(root)
choose_frame1.grid(row=2, column=4, padx=20)

def grab_date():
    my_label.config(text=cal.get.date())

my_button = tk.Label (choose_frame1, text="Choose your Appointment Date")
my_button.grid(row=1, column=4, pady=10)

my_label= Label(root, text="")
my_label.grid(pady=10)


cal = Calendar(choose_frame1, selectmode="day", year=2024, month=1, day=15 )
cal.grid(row=2, column=4)


#Save button
save_button = tk.Button(root,text='BOOKKKKK', font=("Times New Romans",10), relief="raised", command = collect_data)
save_button.grid(row=3, column=3, ipadx=10, ipady=10)


#delete button 
delete_button = tk.Button(root, text="Delete Record", command=delete_data, bg='#FF6347', fg='white')  # Tomato color
delete_button.grid(row=6, column=3, pady=10)


def update_grooming(self):
    # Access entry fields using class attributes
        grooming_type = self.entry_grooming_type.get()
        quantity_cat = self.entry_quantity_cat.get()
        date_appointment = self.entry_date_appointment.get()
        

        if not  grooming_type or not quantity_cat or not date_appointment :
            messagebox.showwarning("Error", "Please fill in all fields.")
        else:
            # Connect to MySQL
            mydb = mysql.connector.connect(
                host="localhost",
                user="self",
                password="",
                database="cat_hotel"
            )

            # Create a cursor object to interact with the database
            cursor = mydb.cursor()

            # Update grooming information in the database
            sql = "UPDATE `grooming` SET grooming_type = %s, quantity_cat = %s, date_appointment = %s, WHERE grooming_id = %s"
            data = (grooming_type , quantity_cat, date_appointment, self.grooming_id)

            try:
                cursor.execute(sql, data)
                mydb.commit()
                messagebox.showinfo("Booking Detail Update", "Update successful!")
            except Exception as e:
                messagebox.showerror("Error", f"Error during update: {str(e)}")
            finally:
                # Close the cursor and database connection
                cursor.close()
                mydb.close()

# Create update button
update_button = tk.Button(root, text="Update", command=update_grooming)
update_button.grid(row=5, column=3, pady=10)



root.mainloop()