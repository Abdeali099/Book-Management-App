import tkinter as tk
from tkinter import filedialog
from tkinter import ttk

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


# Function to populate the table with book data
def populate_table():
    # Add code to populate the table with data from the 'books' list.
    pass


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

# Center the main window
window_width = 1200
window_height = 700
screen_width = main_window.winfo_screenwidth()
screen_height = main_window.winfo_screenheight()
x_coordinate = (screen_width / 2) - (window_width / 2)
y_coordinate = (screen_height / 2) - (window_height / 2)
main_window.geometry(f'{window_width}x{window_height}+{int(x_coordinate)}+{int(y_coordinate)}')

# First Frame (Add/Update/Delete)
form_frame = tk.Frame(main_window, relief="solid", borderwidth=2)
form_frame.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")

# Labels and Entry Widgets
labels = ["Book ID", "Book Name", "Book Subject", "Author Name", "Publication", "Date of Publication"]

i = 0
j = 0

while i < len(labels):
    tk.Label(form_frame, text=labels[i]).grid(row=j, column=0, padx=5, pady=5, sticky="e")
    tk.Entry(form_frame).grid(row=j, column=1, padx=5, pady=5, sticky="w")

    i += 1
    tk.Label(form_frame, text=labels[i]).grid(row=j, column=1, padx=5, pady=5, sticky="e")
    tk.Entry(form_frame).grid(row=j, column=2, padx=5, pady=5, sticky="w")

    i += 1
    j += 1

# Price, Quantity, and Total
price_label = tk.Label(form_frame, text="Book Price")
price_label.grid(row=len(labels), column=0, padx=5, pady=5, sticky="e")
price_spinbox = tk.Spinbox(form_frame, from_=0, to=999999, width=10, command=calculate_total)
price_spinbox.grid(row=len(labels), column=1, padx=5, pady=5, sticky="w")

quantity_label = tk.Label(form_frame, text="Book Quantity")
quantity_label.grid(row=len(labels) + 1, column=0, padx=5, pady=5, sticky="e")
quantity_spinbox = tk.Spinbox(form_frame, from_=0, to=999, width=10, command=calculate_total)
quantity_spinbox.grid(row=len(labels) + 1, column=1, padx=5, pady=5, sticky="w")

total_label = tk.Label(form_frame, text="Total Cost")
total_label.grid(row=len(labels) + 2, column=0, padx=5, pady=5, sticky="e")
total_entry = tk.Entry(form_frame, state="readonly")
total_entry.grid(row=len(labels) + 2, column=1, padx=5, pady=5, sticky="w")

# Image Button
image_button = tk.Button(form_frame, text="Choose Image", command=choose_image)
image_button.grid(row=0, column=2, padx=5, pady=5, rowspan=len(labels) + 3)

# Action Buttons
add_button = tk.Button(form_frame, text="Add", command=add_book)
update_button = tk.Button(form_frame, text="Update", command=update_book)
delete_button = tk.Button(form_frame, text="Delete", command=delete_book)
cancel_button = tk.Button(form_frame, text="Cancel", command=cancel)

add_button.grid(row=len(labels) + 3, column=0, padx=5, pady=10)
update_button.grid(row=len(labels) + 3, column=1, padx=5, pady=10)
delete_button.grid(row=len(labels) + 3, column=2, padx=5, pady=10)
cancel_button.grid(row=len(labels) + 3, column=3, padx=5, pady=10)

# Second Frame (Search)
frame2 = tk.Frame(main_window)
frame2.grid(row=0, column=1, padx=10, pady=10, sticky="nsew")

# Dropdown for search criteria
search_criteria = tk.StringVar()
search_criteria.set("Id")  # Default search criteria
search_dropdown = ttk.Combobox(frame2, textvariable=search_criteria,
                               values=["Id", "Book Name", "Publication", "Book Subject"])
search_dropdown.grid(row=0, column=0, padx=5, pady=5, sticky="e")

# Input field for search text
search_text = tk.Entry(frame2)
search_text.grid(row=0, column=1, padx=5, pady=5, sticky="w")

# Search Button
search_button = tk.Button(frame2, text="Search", command=search_books)
search_button.grid(row=0, column=2, padx=5, pady=5)

# Third Frame (Table)
frame3 = tk.Frame(main_window)
frame3.grid(row=1, column=0, columnspan=2, padx=10, pady=10, sticky="nsew")

# Create a Treeview widget to display the table
columns = ("Book ID", "Book Name", "Book Subject", "Author Name", "Publication", "Date of Publication", "Book Price",
           "Book Quantity", "Total Cost")
table = ttk.Treeview(frame3, columns=columns, show="headings")

# Add headings to the table
for col in columns:
    table.heading(col, text=col)
    table.column(col, width=120)

table.grid(row=0, column=0, padx=5, pady=5, sticky="nsew")

# Populate the table with book data
populate_table()

# Configure grid column and row weights for resizing
main_window.grid_rowconfigure(1, weight=1)
main_window.grid_columnconfigure(0, weight=1)
form_frame.grid_rowconfigure(len(labels) + 4, weight=1)
form_frame.grid_columnconfigure(1, weight=1)
frame2.grid_rowconfigure(0, weight=1)
frame2.grid_columnconfigure(1, weight=1)
frame3.grid_rowconfigure(0, weight=1)
frame3.grid_columnconfigure(0, weight=1)

main_window.mainloop()
