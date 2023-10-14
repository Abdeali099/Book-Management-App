import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox
from tkinter import ttk
from tkcalendar import DateEntry
from PIL import Image, ImageTk
from datetime import date
import re


# <----- Variables -------> #

# Sample data store for books
input_books_data= []

pattern_real_number = re.compile(r"^\d+(\.\d+)?$")
pattern_natural_number = re.compile(r"^\d?$")

# Global variables for images and its data
book_cover_path = "./assets/byDefaultCover.jpg"
book_cover_data = []
default_book_cover = None
user_selected_cover = None

# Function to add a book to the data store
def add_book():
    # Add code to handle adding a book to the data store.
    # Retrieve data from the input fields and append it to the 'books' list.
    pass


# Function to update a book in the data store
def update_book():
    # Add code to handle updating a book in the data store.
    pass


# Function to delete a book from the data store
def delete_book():
    # Add code to handle deleting a book from the data store.
    pass


# Function to search for books based on criteria
def search_books():
    # Add code to search for books based on the selected criteria and search text.
    pass


# Function to populate the table with random data
def populate_table():
    global default_book_cover
    
    img = Image.open(book_cover_path)
    img = img.resize((80, 80), reducing_gap=Image.LANCZOS)  # Adjust the size as needed
    default_book_cover = ImageTk.PhotoImage(img)

    # Insert the rows into the table
    table_data.insert("", "end", iid=1, open=True, image=default_book_cover, values=("book_id", "book_name", "book_subject", "author_name", "publication", "date_of_publication", "book_price", "book_quantity", "total_cost"))
    
# <----------- Helper Functions | Functionality -----------> #

# def is_inputs_valid() -> bool:
#     global input_data

#     try:
#         new_id = int(entry_id.get())

#         input_data = [new_id, entry_hostname.get(), entry_brand.get(), entry_ram.get(),
#                       entry_flash.get()]

#         if '' in input_data:
#             messagebox.showerror('Error', 'Please provide proper inputs')
#             return False

#     except Exception as e:
#         print("Value error in selection : ", e)
#         messagebox.showerror('Error', 'Please provide proper inputs')
#         return False

#     return True

def get_input_data():
    global input_books_data, book_cover_data

    # Retrieve data from the input fields
    book_id = entry_book_id.get()
    book_name = entry_book_name.get()
    book_subject = entry_book_subject.get()
    author_name = entry_author_name.get()
    publication = entry_publication.get()

    date_of_publication = date_entry.get_date()

    book_price = price_spinbox.get()
    book_quantity = quantity_spinbox.get()
    total_cost = total_entry.get()

    input_books_data = [book_id, book_name, book_subject, author_name, publication, date_of_publication, book_price, book_quantity, total_cost]

    img_choosen = Image.open(book_cover_path)
    img_choosen = img_choosen.resize((80, 80), reducing_gap=Image.LANCZOS)
    user_selected_cover = ImageTk.PhotoImage(img_choosen)

    # Store the image data in a list or dictionary
    book_cover_data.append(user_selected_cover)

    # Insert data into the table
    table_data.insert("", "end", iid=book_id, open=True, image=user_selected_cover, values=input_books_data)
    

def set_book_cover(default=False):
    
    """
    -> Set book cover image to label. \n
    -> If default is False user have to choose path.
    """
    
    global book_cover_path
    
    if not default : 
        book_cover_path = filedialog.askopenfilename(filetypes=[("Image files", "*.jpg *.jpeg *.png")])

    if book_cover_path:
        img_cover = Image.open(book_cover_path)
        img_cover = img_cover.resize((150, 200), reducing_gap=Image.LANCZOS)
        img_cover = ImageTk.PhotoImage(img_cover)
        img_container.image = img_cover
        img_container['image'] = img_cover

def get_confirmation(msg="Are you sure , you want to proceed??"):
    
    """
    -> Custom message Confirmation window. \n
    -> Return 'True' if yes clicked , other wise 'False'
    """
    
    result = messagebox.askyesno("Confirmation", msg)
    return result
        
def clear_input_fields(confirmation=False):
    
    """
    -> This function clear the input fields and set initial value of some entries. \n
    -> Use also as "Cancel".
    """
    
    if confirmation :
        do_clear=get_confirmation("Are you sure to clear fields?")
        
        if not do_clear:
            return
        
    entry_book_id.delete(0, tk.END)
    entry_book_name.delete(0, tk.END)
    entry_book_subject.delete(0, tk.END)
    entry_author_name.delete(0, tk.END)
    entry_publication.delete(0, tk.END)
    
    date_entry.set_date(date.today())
    
    price_spinbox.delete(0,tk.END)  
    price_spinbox.insert(0, "0.00")
    
    quantity_spinbox.delete(0, tk.END)  
    quantity_spinbox.insert(0, "0")
    
    total_entry.config(state="normal")  
    total_entry.delete(0, tk.END)  
    total_entry.insert(0, "0.00")
    total_entry.config(state="readonly") 
    
    set_book_cover(default=True)
    
def calculate_total():
    
    """
    -> This function calls whenever price or quantity changes and calcluate total and set it.
    """
    
    try:
        # Get the values from the price and quantity spinboxes
        price_value_str =price_spinbox.get()
        quantity_value_str =quantity_spinbox.get()

        if pattern_real_number.fullmatch(price_value_str) and pattern_natural_number.fullmatch(quantity_value_str):
            
            price = float(price_spinbox.get())
            quantity = int(quantity_spinbox.get())

            # Calculate the total cost
            total_cost = price * quantity

            # Update the total cost entry field
            total_entry.config(state="normal")  # Enable editing
            total_entry.delete(0, "end")  # Clear previous value
            total_entry.insert(0, f"{total_cost:.2f}")  # Insert the new total cost
            total_entry.config(state="readonly")  # Disable editing

    except Exception as e :
        messagebox.showerror('Error', 'Provide proper value of price or quantity')
        print("Error in reading price | quantity : ",e)

# -------------------------- GUI Application -------------------------- #

# Create the main window
main_window = tk.Tk()
main_window.title("Book Management")

style = ttk.Style(main_window)
style.theme_use('clam')  

window_icon_image = tk.PhotoImage(file="./assets/BookStoreIcon.png")
main_window.iconphoto(False, window_icon_image)

# Configure the main window size and position
screen_width = main_window.winfo_screenwidth()
screen_height = main_window.winfo_screenheight()
main_window.state('zoomed')
main_window['background'] = '#165d95'

# Different types of font for different element
title_font = ("Arial", 24, "bold")
section_font = ("Fira Code", 12, "bold")
table_heading_font = ("Fira Code", 10, "bold")
label_font = ("Arial", 12, "bold")
button_font = ("Arial", 12, "bold")
text_filed_font = ("Fira Code", 12, "normal")

#  Title : Admin Panel
admin_label = tk.Label(main_window, text="Admin Panel", font=title_font, bg="#165d95", fg="white")
admin_label.place(x=screen_width / 2 - 100, y=20)

# ---- 1) First Frame  : Form ---- #

# Maintain Book section (Heading)
tk.Label(main_window, text="--- Maintain Book ---", font=section_font, bg="#165d95", fg="white").place(x=200, y=50)

# First Frame
form_frame = tk.Frame(main_window, width=screen_width - 400, height=300, bg="#60cb5f")
form_frame.place(x=200, y=80)

# Labels and Entry Widgets (Total : 6)
labels = ["Book ID", "Book Name", "Book Subject", "Author Name", "Publication", "Publication Date"]

# Label and Entry for Book ID
label_book_id = tk.Label(form_frame, text=labels[0], font=label_font, bg="#60cb5f", fg="black")
label_book_id.place(x=20, y=20)

entry_book_id = tk.Entry(form_frame, font=text_filed_font)
entry_book_id.place(x=180, y=20, width=300, height=30)

# Label and Entry for Book Name
label_book_name = tk.Label(form_frame, text=labels[1], font=label_font, bg="#60cb5f", fg="black")
label_book_name.place(x=20, y=70)

entry_book_name = tk.Entry(form_frame, font=text_filed_font)
entry_book_name.place(x=180, y=70, width=300, height=30)

# Label and Entry for Book Subject
label_book_subject = tk.Label(form_frame, text=labels[2], font=label_font, bg="#60cb5f", fg="black")
label_book_subject.place(x=500, y=20)

entry_book_subject = tk.Entry(form_frame, font=text_filed_font)
entry_book_subject.place(x=660, y=20, width=300, height=30)

# Label and Entry for Author Name
label_author_name = tk.Label(form_frame, text=labels[3], font=label_font, bg="#60cb5f", fg="black")
label_author_name.place(x=500, y=70)

entry_author_name = tk.Entry(form_frame, font=text_filed_font)
entry_author_name.place(x=660, y=70, width=300, height=30)

# Label and Entry for Publication
label_publication = tk.Label(form_frame, text=labels[4], font=label_font, bg="#60cb5f", fg="black")
entry_publication = tk.Entry(form_frame, font=text_filed_font)

label_publication.place(x=20, y=120)
entry_publication.place(x=180, y=120, width=300, height=30)

# Label and the DateEntry widget

label_date = tk.Label(form_frame, text=labels[5], font=label_font, bg="#60cb5f", fg="black")
label_date.place(x=500, y=120)

style.configure('my.DateEntry',fieldbackground='white',background='#165d95',foreground='black',arrowcolor='black')

# Create a separate DateEntry widget
date_entry = DateEntry(form_frame, style='my.DateEntry', selectmode='day',date_pattern="dd/mm/yyyy",font=text_filed_font)
date_entry.config(state="readonly")  # Disable editing
date_entry.place(x=660, y=120, width=300, height=30)

# <---- Price, Quantity, and Total (Total 3) ---->
price_label = tk.Label(form_frame, text="Book Price", font=label_font, bg="#60cb5f", fg="black")
price_label.place(x=20, y=170)
price_spinbox = tk.Spinbox(form_frame, from_=0, to=999999, width=8, command=calculate_total, font=text_filed_font)
price_spinbox.bind("<KeyRelease>", lambda event: calculate_total())
price_spinbox.place(x=120, y=170, height=30)
price_spinbox.delete(0, "end")  # Set initial price to 0
price_spinbox.insert(0, "0.00")

quantity_label = tk.Label(form_frame, text="Book Quantity", font=label_font, bg="#60cb5f", fg="black")
quantity_label.place(x=260, y=170)
quantity_spinbox = tk.Spinbox(form_frame, from_=0, to=999, width=8, command=calculate_total, font=text_filed_font)
quantity_spinbox.bind("<KeyRelease>", lambda event: calculate_total())
quantity_spinbox.place(x=390, y=170, height=30)
quantity_spinbox.delete(0, "end")  # Set initial quantity to 0
quantity_spinbox.insert(0, "0")

total_label = tk.Label(form_frame, text="Total Cost", font=label_font, bg="#60cb5f", fg="black")
total_label.place(x=500, y=170)
total_entry = tk.Entry(form_frame, font=text_filed_font)
total_entry.insert(0, "0.00")
total_entry.config(state="readonly")  # Disable editing
total_entry.place(x=660, y=170, width=300, height=30)

# Action Buttons (4 buttons)

add_btn_icon = tk.PhotoImage(file="./assets/addIcon.png")
add_button = tk.Button(form_frame, width=150, text="Add", image=add_btn_icon, compound=tk.LEFT, command=get_input_data,font=button_font, bg="#165d95", fg="white")

update_btn_icon = tk.PhotoImage(file="./assets/updateIcon.png")
update_button = tk.Button(form_frame, width=150, text="Update", image=update_btn_icon, compound=tk.LEFT, command=update_book, font=button_font, bg="#165d95", fg="white")

delete_btn_icon = tk.PhotoImage(file="./assets/deleteIcon.png")
delete_button = tk.Button(form_frame, width=150, text="Delete", image=delete_btn_icon, compound=tk.LEFT,command=delete_book, font=button_font, bg="#165d95",fg="white")

cancel_btn_icon = tk.PhotoImage(file="./assets/cancelIcon.png")
cancel_button = tk.Button(form_frame, width=150, text="Cancel", image=cancel_btn_icon, compound=tk.LEFT, command=lambda : clear_input_fields(confirmation=True),font=button_font, bg="#165d95",fg="white")

add_button.place(x=180, y=245, height=40)
update_button.place(x=360, y=245, height=40)
delete_button.place(x=540, y=245, height=40)
cancel_button.place(x=720, y=245, height=40)

# Cover selection and display area
img_container = tk.Label(form_frame, relief="solid", borderwidth=2)
img_container.place(x=990, y=20, width=150, height=200)

# set default cover image
set_book_cover(default=True)

# select cover Image Button
choose_cover_btn_icon = tk.PhotoImage(file="./assets/browseIcon.png")
choose_cover_btn = tk.Button(form_frame, width=150, text="Choose Cover", image=choose_cover_btn_icon, compound=tk.LEFT, command=set_book_cover, font=button_font, bg="#165d95", fg="white")
choose_cover_btn.place(x=980, y=250, height=35)

# ---- 2) Second Frame  : Filter frame ---- #

# Filter Book (Heading)
tk.Label(main_window, text="--- Filter Book ---", font=section_font, bg="#165d95", fg="white").place(x=200, y=410)

# Second Frame (Search | Filter)
filter_frame = tk.Frame(main_window, width=screen_width - 825, height=70, bg="#60cb5f")
filter_frame.place(x=400, y=440)

# Dropdown for search criteria
search_criteria = tk.StringVar()
search_criteria.set("Id")  # Default search criteria
search_dropdown = ttk.Combobox(filter_frame, textvariable=search_criteria, state="readonly", values=["Id", "Book Name", "Publication", "Book Subject"], font=label_font)
search_dropdown.place(x=20, y=20, width=150, height=30)

# Input field for search text
search_text = tk.Entry(filter_frame, font=text_filed_font)
search_text.place(x=185, y=20, width=300, height=30)

# Search Button
search_btn_icon = tk.PhotoImage(file="./assets/searchIcon.png")
search_button = tk.Button(filter_frame, text="Search", image=search_btn_icon,compound=tk.LEFT, command=search_books, font=button_font, bg="#165d95", fg="white")
search_button.place(x=500, y=20, width=250, height=30)

# ---- Third Frame  : Table frame ---- #

# Available Book (Heading)
tk.Label(main_window, text="--- Available Book ---", font=section_font, bg="#165d95", fg="white").place(x=100, y=540)

# Third Frame (Table)
table_frame = tk.Frame(main_window)
table_frame.place(x=100, y=570, width=screen_width - 200, height=250)
 
#  Create a Treeview widget to display the table
table_data = ttk.Treeview(table_frame, selectmode ='browse',height=3)  

# Defining of columns
columns =  ("Book ID", "Book Name", "Book Subject", "Author Name", "Publication", "Publication Date", "Book Price", "Book Quantity", "Total Cost")
table_data["columns"] = columns

# Defining heading
table_data['show'] = 'tree headings'

#  style for table 
style.configure('Treeview.Heading', background="#165d95",font=table_heading_font,foreground="white")
style.configure('Treeview',font=text_filed_font,rowheight=80)
table_data.tag_configure("even_row", background="white")  # or any other light color
table_data.tag_configure("odd_row", background="#a1bde8")  # or any other dark color

# initilaizing heading-column
table_data.heading("#0", text ="#") # Text of the column 
table_data.column("#0", width = 50, anchor ='center') # Width of column

for col in columns:
    table_data.heading(col, text=col)
    table_data.column(col, width=80,anchor=tk.CENTER)
    
# Add a vertical scrollbar
table_scrollbar = ttk.Scrollbar(table_frame, orient="vertical", command=table_data.yview)
table_data.configure(yscrollcommand=table_scrollbar.set)
table_scrollbar.pack(side="right", fill="y")

table_data.pack(fill="both", expand=True)

# Populate the table with random data
populate_table()

main_window.mainloop()
