import tkinter as tk
from tkinter import filedialog
from tkinter import ttk
import random
import string

# Sample data store for books
books = []


def choose_image():
    file_path = filedialog.askopenfilename(filetypes=[("Image files", "*.jpg *.jpeg *.png")])
    if file_path:
        # You can display the selected image on the button or elsewhere in your UI.
        print(f"Selected image: {file_path}")


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
    for _ in range(50):  # Add 50 random/fake data rows
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


# Create the main window
main_window = tk.Tk()
main_window.title("Book Management")

# Configure the main window size and position
screen_width = main_window.winfo_screenwidth()
screen_height = main_window.winfo_screenheight()
main_window.geometry(f'{screen_width}x{screen_height}')

tk.Label(main_window, text="Admin Panel").place(x=screen_width / 2 - 50, y=20)

tk.Label(main_window, text="-- Maintain Book --").place(x=200, y=50)

# First Frame (Add/Update/Delete)
form_frame = tk.Frame(main_window, relief="solid", borderwidth=2, width=screen_width - 400, height=350)
form_frame.place(x=200, y=80)

# Labels and Entry Widgets
labels = ["Book ID", "Book Name", "Book Subject", "Author Name", "Publication", "Date of Publication"]

i = 0
j = 0

while i < len(labels):
    tk.Label(form_frame, text=labels[i]).place(x=20, y=j * 50 + 20)
    tk.Entry(form_frame).place(x=180, y=j * 50 + 20, width=200, height=30)

    i += 1
    tk.Label(form_frame, text=labels[i]).place(x=400, y=j * 50 + 20)
    tk.Entry(form_frame).place(x=560, y=j * 50 + 20, width=200, height=30)

    i += 1
    j += 1

# Price, Quantity, and Total
price_label = tk.Label(form_frame, text="Book Price")
price_label.place(x=20, y=j * 50 + 20)
price_spinbox = tk.Spinbox(form_frame, from_=0, to=999999, width=10, command=calculate_total)
price_spinbox.place(x=120, y=j * 50 + 20, height=20)

quantity_label = tk.Label(form_frame, text="Book Quantity")
quantity_label.place(x=200, y=j * 50 + 20)
quantity_spinbox = tk.Spinbox(form_frame, from_=0, to=999, width=10, command=calculate_total)
quantity_spinbox.place(x=300, y=j * 50 + 20, height=20)

total_label = tk.Label(form_frame, text="Total Cost")
total_label.place(x=400, y=j * 50 + 20)
total_entry = tk.Entry(form_frame, state="readonly")
total_entry.place(x=560, y=j * 50 + 20, width=200, height=30)

# Action Buttons
add_button = tk.Button(form_frame, width=20, text="Add", command=add_book)
update_button = tk.Button(form_frame, width=20, text="Update", command=update_book)
delete_button = tk.Button(form_frame, width=20, text="Delete", command=delete_book)
cancel_button = tk.Button(form_frame, width=20, text="Cancel", command=cancel)

add_button.place(x=50, y=(j + 2) * 45 + 20, height=30)
update_button.place(x=230, y=(j + 2) * 45 + 20, height=30)
delete_button.place(x=410, y=(j + 2) * 45 + 20, height=30)
cancel_button.place(x=590, y=(j + 2) * 45 + 20, height=30)

# Image Frame
img_choose_frame = tk.Frame(form_frame, relief="solid", borderwidth=2, width=350, height=300)
img_choose_frame.place(x=800, y=20)
# Image Button
image_button = tk.Button(img_choose_frame, width=20, text="Choose Image", command=choose_image)
image_button.place(x=100, y=250, height=30)

tk.Label(main_window, text="-- Filter Book --").place(x=200, y=460)

# Second Frame (Search)
filter_frame = tk.Frame(main_window, relief="solid", borderwidth=2, width=screen_width - 800, height=70)
filter_frame.place(x=400, y=490)

# Dropdown for search criteria
search_criteria = tk.StringVar()
search_criteria.set("Id")  # Default search criteria
search_dropdown = ttk.Combobox(filter_frame, textvariable=search_criteria,
                               values=["Id", "Book Name", "Publication", "Book Subject"])
search_dropdown.place(x=20, y=20, width=150, height=30)

# Input field for search text
search_text = tk.Entry(filter_frame)
search_text.place(x=200, y=20, width=250, height=30)

# Search Button
search_button = tk.Button(filter_frame, text="Search", command=search_books)
search_button.place(x=500, y=20, width=250, height=30)

tk.Label(main_window, text="-- Available Book --").place(x=200, y=590)

# Third Frame (Table)
table_frame = tk.Frame(main_window)
table_frame.place(x=200, y=620, width=screen_width - 400, height=200)

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
