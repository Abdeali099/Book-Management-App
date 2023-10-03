import tkinter as tk
from tkinter import filedialog
from tkinter import ttk
from tkcalendar import DateEntry
from PIL import Image, ImageTk
import re
import random
import string

# Sample data store for books
books = []


def choose_cover():
    file_path = filedialog.askopenfilename(filetypes=[("Image files", "*.jpg *.jpeg *.png")])
    
    if file_path:
        img_cover = Image.open(file_path)
        img_cover = img_cover.resize((150, 200), reducing_gap=Image.LANCZOS)
        img_cover = ImageTk.PhotoImage(img_cover)
        img_container.image = img_cover
        img_container['image'] = img_cover


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
    for _ in range(5):
        book_id = ''.join(random.choices(string.ascii_uppercase + string.digits, k=5))
        book_name = ''.join(random.choices(string.ascii_letters, k=10))
        book_subject = ''.join(random.choices(string.ascii_letters, k=8))
        author_name = ''.join(random.choices(string.ascii_letters, k=8))
        publication = ''.join(random.choices(string.ascii_letters, k=8))
        date_of_publication = f"{random.randint(2000, 2022)}-{random.randint(1, 12)}-{random.randint(1, 28)}"
        book_price = 0  # Set initial price to 0
        book_quantity = 0  # Set initial quantity to 0
        total_cost = book_price * book_quantity

        table.insert("", "end", values=(book_id, book_name, book_subject, author_name, publication,
                                        date_of_publication, book_price, book_quantity, total_cost))


def cancel():
    # Add code to clear the input fields.
    pass


# Function to calculate the total price
def calculate_total():
    # Get the values from the price and quantity spinboxes
    pattern = re.compile(r"^/d+(/./d+)?$")

    price_value_str = price_spinbox.get()
    quantity_value_str = quantity_spinbox.get()

    if pattern.fullmatch(price_value_str) and pattern.fullmatch(quantity_value_str):
        price = float(price_spinbox.get())
        quantity = int(quantity_spinbox.get())

        # Calculate the total cost
        total_cost = price * quantity

        # Update the total cost entry field
        total_entry.config(state="normal")  # Enable editing
        total_entry.delete(0, "end")  # Clear previous value
        total_entry.insert(0, f"{total_cost:.2f}")  # Insert the new total cost
        total_entry.config(state="readonly")  # Disable editing


# -------------------------- GUI Application -------------------------- #

# Create the main window
main_window = tk.Tk()
main_window.title("Book Management")

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
labels = ["Book ID", "Book Name", "Book Subject", "Author Name", "Publication", "Date of Publication"]

style = ttk.Style(form_frame)
style.theme_use('clam')  # Theme to be changed # alt , classic, clam

style.configure('my.DateEntry',
                fieldbackground='white',
                background='dark green',
                foreground='dark blue',
                arrowcolor='black',
                )

# Create a separate DateEntry widget
date_entry_var = tk.StringVar()  # declaring string variable
date_entry = DateEntry(form_frame, style='my.DateEntry', selectmode='day', textvariable=date_entry_var,
                       date_pattern="dd/mm/yyyy")

# Label and Entry for Book ID
label_book_id = tk.Label(form_frame, text=labels[0], font=label_font, bg="#60cb5f", fg="black")
entry_book_id = tk.Entry(form_frame, font=text_filed_font)

# Label and Entry for Book Name
label_book_name = tk.Label(form_frame, text=labels[1], font=label_font, bg="#60cb5f", fg="black")
entry_book_name = tk.Entry(form_frame, font=text_filed_font)

# Label and Entry for Book Subject
label_book_subject = tk.Label(form_frame, text=labels[2], font=label_font, bg="#60cb5f", fg="black")
entry_book_subject = tk.Entry(form_frame, font=text_filed_font)

# Label and Entry for Author Name
label_author_name = tk.Label(form_frame, text=labels[3], font=label_font, bg="#60cb5f", fg="black")
entry_author_name = tk.Entry(form_frame, font=text_filed_font)

# Label and Entry for Publication
label_publication = tk.Label(form_frame, text=labels[4], font=label_font, bg="#60cb5f", fg="black")
entry_publication = tk.Entry(form_frame, font=text_filed_font)

# Place labels and entries
label_book_id.place(x=20, y=20)
entry_book_id.place(x=180, y=20, width=300, height=30)

label_book_name.place(x=20, y=70)
entry_book_name.place(x=180, y=70, width=300, height=30)

label_book_subject.place(x=500, y=20)
entry_book_subject.place(x=660, y=20, width=300, height=30)

label_author_name.place(x=500, y=70)
entry_author_name.place(x=660, y=70, width=300, height=30)

label_publication.place(x=20, y=120)
entry_publication.place(x=180, y=120, width=300, height=30)

# Place the DateEntry widget
date_entry.place(x=660, y=120, width=300, height=30)

# Price, Quantity, and Total (Total 3)
price_label = tk.Label(form_frame, text="Book Price", font=label_font, bg="#60cb5f", fg="black")
price_label.place(x=20, y=170)
price_spinbox = tk.Spinbox(form_frame, from_=0, to=999999, width=8, command=calculate_total, font=text_filed_font)
price_spinbox.bind("<KeyRelease>", lambda event: calculate_total())
price_spinbox.place(x=120, y=170, height=30)
price_spinbox.delete(0, "end")  # Set initial price to 0
price_spinbox.insert(0, "0")

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
add_button = tk.Button(form_frame, width=150, text="Add", image=add_btn_icon, compound=tk.LEFT, command=add_book,font=button_font, bg="#165d95", fg="white")

update_btn_icon = tk.PhotoImage(file="./assets/updateIcon.png")
update_button = tk.Button(form_frame, width=150, text="Update", image=update_btn_icon, compound=tk.LEFT, command=update_book, font=button_font, bg="#165d95", fg="white")

delete_btn_icon = tk.PhotoImage(file="./assets/deleteIcon.png")
delete_button = tk.Button(form_frame, width=150, text="Delete", image=delete_btn_icon, compound=tk.LEFT,command=delete_book, font=button_font, bg="#165d95",fg="white")

cancel_btn_icon = tk.PhotoImage(file="./assets/cancelIcon.png")
cancel_button = tk.Button(form_frame, width=150, text="Cancel", image=cancel_btn_icon, compound=tk.LEFT, command=cancel,font=button_font, bg="#165d95",fg="white")

add_button.place(x=180, y=245, height=40)
update_button.place(x=360, y=245, height=40)
delete_button.place(x=540, y=245, height=40)
cancel_button.place(x=720, y=245, height=40)

# Cover selection and display area
img_container = tk.Label(form_frame, relief="solid", borderwidth=2)
img_container.place(x=990, y=20, width=150, height=200)

# set default cover image
img = Image.open("./assets/byDefaultCover.jpg")
img = img.resize((150, 200), reducing_gap=Image.LANCZOS)
img = ImageTk.PhotoImage(img)
img_container.image = img
img_container['image'] = img

# select cover Image Button
choose_cover_btn_icon = tk.PhotoImage(file="./assets/browseIcon.png")
choose_cover_btn = tk.Button(form_frame, width=150, text="Choose Cover", image=choose_cover_btn_icon, compound=tk.LEFT, command=choose_cover, font=button_font, bg="#165d95", fg="white")
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
tk.Label(main_window, text="--- Available Book ---", font=section_font, bg="#165d95", fg="white").place(x=200, y=540)

# Third Frame (Table)
table_frame = tk.Frame(main_window)
table_frame.place(x=200, y=570, width=screen_width - 400, height=250)

# Create a Treeview widget to display the table
columns = ("Book ID", "Book Name", "Book Subject", "Author Name", "Publication", "Date of Publication", "Book Price", "Book Quantity", "Total Cost")
table = ttk.Treeview(table_frame, columns=columns, show="headings")

# Add headings to the table
for col in columns:
    table.heading(col, text=col)
    table.column(col, width=80)

# Add a vertical scrollbar
table_scrollbar = ttk.Scrollbar(table_frame, orient="vertical", command=table.yview)
table.configure(yscrollcommand=table_scrollbar.set)
table_scrollbar.pack(side="right", fill="y")

table.pack(fill="both", expand=True)

# Populate the table with random data
populate_table()

main_window.mainloop()
