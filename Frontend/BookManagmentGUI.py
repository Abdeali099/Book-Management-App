import tkinter as tk
import re
from tkinter import filedialog
from tkinter import messagebox
from tkinter import ttk
from tkcalendar import DateEntry
from PIL import Image, ImageTk
from datetime import date
from Backend.BookServices import BookServices


# <----- Variables -------> #

# Sample data store for books
form_input_book_data= []
stored_books_data_list = []

# pattern for totalcost
pattern_real_number = re.compile(r"^\d+(\.\d+)?$")
pattern_natural_number = re.compile(r"^\d?$")

# Global variables for images and its data
extra_gloabl_data_list = []
icons_list = []
book_cover_data_list = []
default_book_cover = None
user_selected_cover = None


class BookManagmentGUI(tk.Tk):
    
    def __init__(self) -> None:
        
        global book_cover_data_list,icons_list
        
        super().__init__()
        
        # BookService object
        bookservice=BookServices()
        
        # configuration for main window
        self.title("Book Management")

        style = ttk.Style(self)
        style.theme_use('clam')  

        window_icon_image = tk.PhotoImage(file="./assets/BookStoreIcon.png")
        icons_list.append(window_icon_image)
        self.iconphoto(False, window_icon_image)

        # Configure the main window size and position
        screen_width = self.winfo_screenwidth()
        self.state('zoomed')
        self['background'] = '#165d95'

        # Different types of font for different element
        title_font = ("Arial", 24, "bold")
        section_font = ("Fira Code", 12, "bold")
        table_heading_font = ("Fira Code", 10, "bold")
        label_font = ("Arial", 12, "bold")
        button_font = ("Arial", 12, "bold")
        text_filed_font = ("Fira Code", 12, "normal")

        #  Title : Admin Panel
        admin_label = tk.Label(self, text="Admin Panel", font=title_font, bg="#165d95", fg="white")
        admin_label.place(x=screen_width / 2 - 100, y=20)

        # ---- 1) First Frame  : Form ---- #

        # Maintain Book section (Heading)
        tk.Label(self, text="--- Maintain Book ---", font=section_font, bg="#165d95", fg="white").place(x=200, y=50)

        # First Frame
        form_frame = tk.Frame(self, width=screen_width - 400, height=300, bg="#60cb5f")
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
        price_spinbox = tk.Spinbox(form_frame, from_=0, to=999999, width=8,font=text_filed_font)
        price_spinbox.place(x=120, y=170, height=30)
        price_spinbox.delete(0, "end")  # Set initial price to 0
        price_spinbox.insert(0, "0.00")

        quantity_label = tk.Label(form_frame, text="Book Quantity", font=label_font, bg="#60cb5f", fg="black")
        quantity_label.place(x=260, y=170)
        quantity_spinbox = tk.Spinbox(form_frame, from_=0, to=999, width=8, font=text_filed_font)
        quantity_spinbox.place(x=390, y=170, height=30)
        quantity_spinbox.delete(0, "end")  # Set initial quantity to 0
        quantity_spinbox.insert(0, "0")
        
        total_label = tk.Label(form_frame, text="Total Cost", font=label_font, bg="#60cb5f", fg="black")
        total_label.place(x=500, y=170)
        total_entry = tk.Entry(form_frame, font=text_filed_font)
        total_entry.insert(0, "0.00")
        total_entry.config(state="readonly")  # Disable editing
        total_entry.place(x=660, y=170, width=300, height=30)

        price_spinbox.config(command=lambda : BookManagmentGUI.calculate_total(price_spinbox,quantity_spinbox,total_entry))
        price_spinbox.bind("<KeyRelease>", lambda event: BookManagmentGUI.calculate_total(price_spinbox,quantity_spinbox,total_entry))
        
        quantity_spinbox.config(command=lambda : BookManagmentGUI.calculate_total(price_spinbox,quantity_spinbox,total_entry))
        quantity_spinbox.bind("<KeyRelease>", lambda event: BookManagmentGUI.calculate_total(price_spinbox,quantity_spinbox,total_entry))
        
        # Action Buttons (4 buttons)

        add_btn_icon = tk.PhotoImage(file="./assets/addIcon.png")
        icons_list.append(add_btn_icon)
        add_button = tk.Button(form_frame, width=150, cursor="hand2",text="Add", image=add_btn_icon, compound=tk.LEFT, command=BookServices.add_book,font=button_font, bg="#165d95", fg="white")

        update_btn_icon = tk.PhotoImage(file="./assets/updateIcon.png")
        icons_list.append(update_btn_icon)
        update_button = tk.Button(form_frame, width=150, cursor="hand2",text="Update", image=update_btn_icon, compound=tk.LEFT, command=BookServices.update_book, font=button_font, bg="#165d95", fg="white")

        delete_btn_icon = tk.PhotoImage(file="./assets/deleteIcon.png")
        icons_list.append(delete_btn_icon)
        delete_button = tk.Button(form_frame, width=150,cursor="hand2", text="Delete", image=delete_btn_icon, compound=tk.LEFT,command=BookServices.delete_book, font=button_font, bg="#165d95",fg="white")

        cancel_btn_icon = tk.PhotoImage(file="./assets/cancelIcon.png")
        icons_list.append(cancel_btn_icon)
        cancel_button = tk.Button(form_frame, width=150,cursor="hand2", text="Cancel", image=cancel_btn_icon, compound=tk.LEFT, command=lambda : BookServices.clear_input_fields(confirmation=True),font=button_font, bg="#165d95",fg="white")

        add_button.place(x=180, y=245, height=40)
        update_button.place(x=360, y=245, height=40)
        delete_button.place(x=540, y=245, height=40)
        cancel_button.place(x=720, y=245, height=40)

        # Cover selection and display area
        img_container = tk.Label(form_frame, relief="solid", borderwidth=2)
        img_container.place(x=990, y=20, width=150, height=200)

        # set default cover image
        BookServices.set_book_cover(img_container,default=True)

        # select cover Image Button
        choose_cover_btn_icon = tk.PhotoImage(file="./assets/browseIcon.png")
        icons_list.append(choose_cover_btn_icon)
        choose_cover_btn = tk.Button(form_frame, width=150,cursor="hand2", text="Choose Cover", image=choose_cover_btn_icon, compound=tk.LEFT, command=lambda : BookServices.set_book_cover(img_container), font=button_font, bg="#165d95", fg="white")
        choose_cover_btn.place(x=980, y=250, height=35)

        # ---- 2) Second Frame  : Filter frame ---- #

        # Filter Book (Heading)
        tk.Label(self, text="--- Filter Book ---", font=section_font, bg="#165d95", fg="white").place(x=400, y=410)

        # Second Frame (Search | Filter)
        filter_frame = tk.Frame(self, width=screen_width - 825, height=70, bg="#60cb5f")
        filter_frame.place(x=400, y=440)

        # Dropdown for search criteria
        search_criteria = tk.StringVar()
        extra_gloabl_data_list.append(search_criteria)
        search_criteria.set("Id")  # Default search criteria
        search_dropdown = ttk.Combobox(filter_frame, cursor="hand2",textvariable=search_criteria, state="readonly", values=["Id", "Book Name", "Publication", "Book Subject"], font=label_font)
        search_dropdown.place(x=20, y=20, width=150, height=30)

        # Input field for search text
        search_text = tk.Entry(filter_frame, font=text_filed_font)
        search_text.place(x=185, y=20, width=300, height=30)

        # Search Button
        search_btn_icon = tk.PhotoImage(file="./assets/searchIcon.png")
        icons_list.append(search_btn_icon)
        search_button = tk.Button(filter_frame,cursor="hand2", text="Search", image=search_btn_icon,compound=tk.LEFT, command=BookServices.search_books, font=button_font, bg="#165d95", fg="white")
        search_button.place(x=500, y=20, width=250, height=30)

        # ---- Third Frame  : Table frame ---- #

        # Available Book (Heading)
        tk.Label(self, text="--- Available Book ---", font=section_font, bg="#165d95", fg="white").place(x=50, y=540)

        # Third Frame (Table)
        table_frame = tk.Frame(self)
        table_frame.place(x=50, y=570, width=screen_width - 100, height=250)
        
        #  Create a Treeview widget to display the table
        table_data = ttk.Treeview(table_frame, selectmode ='browse',height=3)  

        # Defining of columns
        columns =  ("Book ID", "Book Name", "Book Subject", "Author Name", "Publication", "Publication Date", "Book Price", "Book Quantity", "Total Cost")
        table_data["columns"] = columns

        # Defining heading
        # table_data['show'] = 'tree headings' # if do not want to show images in table (If do this set resize to (80,80) insted of (150,200) when set to table)
        table_data['show'] = 'headings' # if do not want to show images in table (If do this set resize to (150,200) insted of (80,80) when set to table)

        #  style for table 
        style.configure('Treeview.Heading',cursor="hand2", background="#165d95",font=table_heading_font,foreground="white")
        style.configure('Treeview',font=text_filed_font,rowheight=50,cursor="hand2")
        table_data.bind('<<TreeviewSelect>>', BookServices.select_row_of_table)
        table_data.bind("<Enter>", BookManagmentGUI.on_table_enter)
        table_data.bind("<Leave>", BookManagmentGUI.on_table_leave)
        table_data.tag_configure("even_row", background="#f7ebd5")  # or any other light color
        table_data.tag_configure("odd_row", background="#a6cee1")  # or any other dark color

        # initilaizing heading-column
        table_data.heading("#0", text ="Book Cover") # Text of the column 
        table_data.column("#0", width = 80, anchor ='center') # Width of column

        for col in columns:
            table_data.heading(col, text=col)
            table_data.column(col, width=120,anchor=tk.CENTER)
            
        # Add a vertical scrollbar
        table_scrollbar = ttk.Scrollbar(table_frame, orient="vertical", command=table_data.yview)
        table_data.configure(yscrollcommand=table_scrollbar.set)
        table_scrollbar.pack(side="right", fill="y")

        table_data.pack(fill="both", expand=True)
        
        fetched_data=BookServices.fetch_all_data()
        total_data_count = 0
                
        # fetching previous store data and display it
        if len(fetched_data) != 0:
            
            for data in fetched_data:
                
                book_cover_data_list.append(data[-1])
                
                row_position = "even_row" if total_data_count%2==0 else "odd_row"
                
                table_data.insert('', 'end',tags=(row_position,),image=data[-1], values=data[:-1])
                
                total_data_count+=1
                
        # passing gui component refrence to service 
        
        selected_variables = ["entry_book_id","entry_book_name","entry_book_subject","entry_author_name","entry_publication","date_entry","price_spinbox","quantity_spinbox","total_entry","img_container","table_data"]

        gui_component = {key: value for key, value in locals().items() if key in selected_variables}

        BookServices.setGUIrefereces(gui_component,total_data_count)

    @staticmethod
    def calculate_total(price_spinbox,quantity_spinbox,total_entry):
    
        """
        -> This function calls whenever price or quantity changes and calcluate total and set it.
        """
        
        try:
            # Get the values from the price and quantity spinboxes
                
            price = float(price_spinbox.get())
            quantity = int(quantity_spinbox.get())

            # Calculate the total cost
            total_cost = round(price * quantity, 2)

            # Update the total cost entry field
            total_entry.config(state="normal")  # Enable editing
            total_entry.delete(0, "end")  # Clear previous value
            total_entry.insert(0, str(total_cost))  # Insert the new total cost
            total_entry.config(state="readonly")  # Disable editing
                
        except Exception as e :
            messagebox.showerror('Error', 'Provide proper value of price or quantity')
            print("Error in reading price | quantity : ",e)


    @staticmethod
    def on_table_enter(event):
        table_data = event.widget
        table_data["cursor"] = "hand2"

    @staticmethod
    def on_table_leave(event):
        table_data = event.widget
        table_data["cursor"] = ""