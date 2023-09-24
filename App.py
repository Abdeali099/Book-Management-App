import tkinter as tk
from tkinter import filedialog  # used for select cover image
from tkinter import ttk  # used for combo-box , Scrollbar
from PIL import Image, ImageTk  # used for set cover image
import random
import string

# Sample data store for books
books = []


def choose_cover():
    file_path = filedialog.askopenfilename(filetypes=[("Image files", "*.jpg *.jpeg *.png")])
    if file_path:
        # You can display the selected image on the button or elsewhere in your UI.
        print(f"Selected image: {file_path}")
        img_cover = Image.open(file_path)  # read the image file
        img_cover = img_cover.resize((150, 200), reducing_gap=Image.LANCZOS)  # new width & height
        img_cover = ImageTk.PhotoImage(img_cover)
        img_container.image = img_cover  # keep a reference! by attaching it to a widget attribute
        img_container['image'] = img_cover  # Show Image


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
    for _ in range(5):  # Add 50 random---fake data rows
        book_id = ''.join(random.choices(string.ascii_uppercase + string.digits, k=5))
        book_name = ''.join(random.choices(string.ascii_letters, k=10))
        book_subject = ''.join(random.choices(string.ascii_letters, k=8))
        author_name = ''.join(random.choices(string.ascii_letters, k=8))
        publication = ''.join(random.choices(string.ascii_letters, k=8))
        date_of_publication = f"{random.randint(2000, 2022)}-{random.randint(1, 12)}-{random.randint(1, 28)}"
        book_price = round(random.uniform(10, 50), 2)
        book_quantity = random.randint(1, 100)
        total_cost = round(book_price * book_quantity, 2)

        table.insert("", "end", values=(book_id, book_name, book_subject, author_name, publication,
                                        date_of_publication, book_price, book_quantity, total_cost))


def cancel():
    # Add code to clear the input fields.
    pass


# Function to calculate the total price
def calculate_total():
    # Add code to calculate the total price based on price and quantity.
    pass


# -------------------------- GUI Application -------------------------- #

# Create the main window
main_window = tk.Tk()
main_window.title("Book Management")

window_icon_image = tk.PhotoImage(
    file="C:/Users/abdea/Desktop/Study/Sem 7/Python/Labs/Lab-6/Book-Management-App/assets/BookStoreIcon.png")
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

# ---- First Frame  : Form ---- #

# Maintain Book section (Heading)
tk.Label(main_window, text="--- Maintain Book ---", font=section_font, bg="#165d95", fg="white").place(x=200, y=50)

# First Frame
form_frame = tk.Frame(main_window, width=screen_width - 400, height=300, bg="#60cb5f")
form_frame.place(x=200, y=80)

# Labels and Entry Widgets (Total : 6)
labels = ["Book ID", "Book Name", "Book Subject", "Author Name", "Publication", "Date of Publication"]

i = 0
j = 0

while i < len(labels):
    tk.Label(form_frame, text=labels[i], font=label_font, bg="#60cb5f", fg="black").place(x=20, y=j * 50 + 20)
    tk.Entry(form_frame, font=text_filed_font).place(x=180, y=j * 50 + 20, width=300, height=30)

    i += 1
    tk.Label(form_frame, text=labels[i], font=label_font, bg="#60cb5f", fg="black").place(x=500, y=j * 50 + 20)
    tk.Entry(form_frame, font=text_filed_font).place(x=660, y=j * 50 + 20, width=300, height=30)

    i += 1
    j += 1

# Price, Quantity, and Total (Total 3)
price_label = tk.Label(form_frame, text="Book Price", font=label_font, bg="#60cb5f", fg="black")
price_label.place(x=20, y=j * 50 + 20)
price_spinbox = tk.Spinbox(form_frame, from_=0, to=999999, width=8, command=calculate_total, font=text_filed_font)
price_spinbox.place(x=120, y=j * 50 + 20, height=30)

quantity_label = tk.Label(form_frame, text="Book Quantity", font=label_font, bg="#60cb5f", fg="black")
quantity_label.place(x=260, y=j * 50 + 20)
quantity_spinbox = tk.Spinbox(form_frame, from_=0, to=999, width=8, command=calculate_total, font=text_filed_font)
quantity_spinbox.place(x=390, y=j * 50 + 20, height=30)

total_label = tk.Label(form_frame, text="Total Cost", font=label_font, bg="#60cb5f", fg="black")
total_label.place(x=500, y=j * 50 + 20)
total_entry = tk.Entry(form_frame, state="readonly", font=text_filed_font)
total_entry.place(x=660, y=j * 50 + 20, width=300, height=30)

# Action Buttons (4 buttons)
add_button = tk.Button(form_frame, width=15, text="Add", command=add_book, font=button_font, bg="#165d95", fg="white")
update_button = tk.Button(form_frame, width=15, text="Update", command=update_book, font=button_font, bg="#165d95",
                          fg="white")
delete_button = tk.Button(form_frame, width=15, text="Delete", command=delete_book, font=button_font, bg="#165d95",
                          fg="white")
cancel_button = tk.Button(form_frame, width=15, text="Cancel", command=cancel, font=button_font, bg="#165d95",
                          fg="white")

add_button.place(x=180, y=(j + 2) * 45 + 20, height=30)
update_button.place(x=360, y=(j + 2) * 45 + 20, height=30)
delete_button.place(x=540, y=(j + 2) * 45 + 20, height=30)
cancel_button.place(x=720, y=(j + 2) * 45 + 20, height=30)

# Cover selection and display area
img_container = tk.Label(form_frame, relief="solid", borderwidth=2)
img_container.place(x=990, y=20, width=150, height=200)

# set default cover image
img = Image.open(
    "C:/Users/abdea/Desktop/Study/Sem 7/Python/Labs/Lab-6/Book-Management-App/assets/byDefaultCover.jpg")  # read the image file
img = img.resize((150, 200), reducing_gap=Image.LANCZOS)  # set width and height properly
img = ImageTk.PhotoImage(img)
img_container.image = img  # keep a reference! by attaching it to a widget attribute
img_container['image'] = img  # Show Image

# select cover Image Button
image_button = tk.Button(form_frame, width=15, text="Choose Cover", command=choose_cover, font=button_font,
                         bg="#165d95", fg="white")
image_button.place(x=980, y=250, height=30)

# ---- Second Frame  : Filter frame ---- #

# Filter Book (Heading)
tk.Label(main_window, text="--- Filter Book ---", font=section_font, bg="#165d95", fg="white").place(x=200, y=410)

# Second Frame (Search | Filter)
filter_frame = tk.Frame(main_window, width=screen_width - 825, height=70, bg="#60cb5f")
filter_frame.place(x=400, y=440)

# Dropdown for search criteria
search_criteria = tk.StringVar()
search_criteria.set("Id")  # Default search criteria
search_dropdown = ttk.Combobox(filter_frame, textvariable=search_criteria, state="readonly",
                               values=["Id", "Book Name", "Publication", "Book Subject"], font=label_font)
search_dropdown.place(x=20, y=20, width=150, height=30)

# Input field for search text
search_text = tk.Entry(filter_frame, font=text_filed_font)
search_text.place(x=185, y=20, width=300, height=30)

# Search Button
search_button = tk.Button(filter_frame, text="Search", command=search_books, font=button_font, bg="#165d95", fg="white")
search_button.place(x=500, y=20, width=250, height=30)

# ---- Third Frame  : Table frame ---- #

# Available Book (Heading)
tk.Label(main_window, text="--- Available Book ---", font=section_font, bg="#165d95", fg="white").place(x=200, y=540)

# Third Frame (Table)
table_frame = tk.Frame(main_window)
table_frame.place(x=200, y=570, width=screen_width - 400, height=250)

# Create a Treeview widget to display the table
columns = ("Book ID", "Book Name", "Book Subject", "Author Name", "Publication", "Date of Publication", "Book Price",
           "Book Quantity", "Total Cost")
table = ttk.Treeview(table_frame, columns=columns, show="headings")

# Add headings to the table
for col in columns:
    table.heading(col, text=col)
    table.column(col, width=80)  # Adjust column width as needed

# Add a vertical scrollbar
table_scrollbar = ttk.Scrollbar(table_frame, orient="vertical", command=table.yview)
table.configure(yscrollcommand=table_scrollbar.set)
table_scrollbar.pack(side="right", fill="y")

table.pack(fill="both", expand=True)

# Populate the table with random data
populate_table()

main_window.mainloop()
