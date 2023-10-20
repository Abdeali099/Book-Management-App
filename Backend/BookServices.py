import tkinter as tk
from tkinter import END, filedialog
from tkinter import messagebox
from PIL import Image, ImageTk
from datetime import date, datetime

from Backend.Database import Database

# <----- Variables -------> #
form_input_book_data=[]
GUI = None
selected_tree_row_index = ""

# Global variables for images and its data
book_cover_path = DEFAULT_BOOK_COVER_PATH  = "./assets/byDefaultCover.jpg"
total_data_count = 0
book_cover_data_list = []

# objects 
database=None

class BookServices:
    
    def __init__(self) -> None:
        global database
        
        database=Database()
        
    @staticmethod
    def setGUIrefereces(gui_components):
        global GUI
        
        GUI = gui_components

    @staticmethod
    def fetch_all_data():
        return Database.fetch_all_data()
    
    @staticmethod
    def insert_data_in_table(table_data,fetched_data):
        
        global book_cover_data_list,total_data_count
        
        total_data_count=0
        
        # fetching previous store data and display it
        if len(fetched_data) != 0:
            
            for data in fetched_data:
                
                book_cover_data_list.append(data[-1])
                
                row_position = "even_row" if total_data_count%2==0 else "odd_row"
                
                table_data.insert('', 'end',tags=(row_position,),image=data[-1], values=data[:-1])
                
                total_data_count+=1
                

    @staticmethod
    def reset_table():
        # empty old data
        BookServices.empty_table()
        
        GUI['search_criteria'].set("Id")  # Default search criteria
        BookServices.insert_data_in_table(GUI['table_data'],Database.fetch_all_data())
        
                
    @staticmethod
    def add_book():
            
        global form_input_book_data,total_data_count
            
        """
        -> Add code to handle adding a book to the data store. \n
        -> Retrieve data from the input fields and append it to the 'books' list.
        """
        
        isInputValid = BookServices.get_input_data()
        
        if isInputValid : 
                    
            form_input_book_data.append(BookServices.convertToBinaryData(book_cover_path))
            
            isDataAdded=database.insert(form_input_book_data[1:])
            
            if isDataAdded :
                
                row_position = "even_row" if total_data_count%2==0 else "odd_row"
                total_data_count+=1
                
                # insert into table
                GUI['table_data'].insert('', 'end',tags=(row_position,), image=form_input_book_data[0],values=form_input_book_data[1:-1])

                BookServices.clear_input_fields()
                

    @staticmethod
    def update_book():
        
        global form_input_book_data,selected_tree_row_index
        
        if selected_tree_row_index == "" :
            messagebox.showerror('Error', 'Please select the data first.')
            return
                
        do_update=BookServices.get_confirmation("Are you sure to update the data?")
            
        if not do_update:
            return
                    
        isInputValid = BookServices.get_input_data(via="update")
        
        if isInputValid : 
                    
            form_input_book_data.append(BookServices.convertToBinaryData(book_cover_path))
            
            isDataUpdated=database.update(form_input_book_data[1:])
            
            if isDataUpdated :
                    
                # update tree
                GUI['table_data'].item(selected_tree_row_index, image=form_input_book_data[0],values=form_input_book_data[1:-1])
            
            
    @staticmethod
    def delete_book():
        
        global selected_tree_row_index
        
        if selected_tree_row_index == "" :
            messagebox.showerror('Error', 'Please select the data first.')
            return
                
        do_delete=BookServices.get_confirmation("Are you sure to delete the data?")
            
        if not do_delete:
            return
        
        isDataDeleted=database.delete(int( GUI['entry_book_id'].get()))
            
        if isDataDeleted :
                
            # delete from table
            GUI['table_data'].delete(selected_tree_row_index)
            
            BookServices.formate_row_color()

            BookServices.clear_input_fields()

    @staticmethod
    def formate_row_color():
        
        global total_data_count
        
        total_data_count = 0
        
        for record in GUI['table_data'].get_children():
            
            row_position = "even_row" if total_data_count%2==0 else "odd_row"
            
            GUI['table_data'].item(record, tags=(row_position,))
                
            total_data_count += 1
        
    @staticmethod
    def search_books():
        
        # get filed to be search 
        search_field = GUI['search_dropdown'].get().strip().lower().replace(" ", "_")
        print(search_field)
        
        # get search word
        search_keyword = GUI['search_text'].get()
        print(search_keyword)
        
        if search_keyword == '':
            messagebox.showerror('Error', 'Please enter what to be search.')
            return
        
        if search_field=="id" :
            try:
                search_keyword = int(search_keyword)
            except Exception as e :
                messagebox.showerror('Error', 'Please enter digits for Id.')
            
        print("search_filed : " , search_field , " keyword : ",search_keyword)
        
        searched_data = Database.query_book(search_field,search_keyword)
        
        if len(searched_data) == 0 :
            messagebox.showinfo("Information",'No data avialable.')
            return
                
        # empty old data
        BookServices.empty_table()

        BookServices.insert_data_in_table(GUI['table_data'],searched_data)
        
    @staticmethod
    def empty_table():
        for item in GUI['table_data'].get_children():
            GUI['table_data'].delete(item)

    @staticmethod
    def convertToBinaryData(file_path):
        
        """
        -> Convert binary format to images or files data
        Returns:
            _type_: Binary(BLOB)
        """
        
        with open(file_path, 'rb') as file:
            
            blobData = file.read()
        
        return blobData 


    @staticmethod
    def is_inputs_valid():
    
        global form_input_book_data
        
        try:
            
            try:
                form_input_book_data[1] = int(form_input_book_data[1])
            
            except ValueError as t:
                print("Id is not integer : ",t)
                messagebox.showerror('Error', 'Id must be a number')
                return False
            
            except Exception as e:
                print("Id is not proper : ",e)
                messagebox.showerror('Error', 'Please provide proper Id')
                return False
                
            
            if '' in form_input_book_data or None in form_input_book_data :
                messagebox.showerror('Error', 'Please provide all inputs properly')
                return False
            
            if float(form_input_book_data[9]) <= 0:
                messagebox.showerror('Error', "Total cost can't be Zero.")
                return False

        except Exception as e:
            print("Value Error", e)
            messagebox.showerror('Error', 'Please provide proper inputs')
            return False

        return True
    
    
    @staticmethod
    def get_input_data(via="add"):
        
        global form_input_book_data

        try:
                    
            # Retrieve data from the input fields
            book_id = GUI['entry_book_id'].get()
            book_name = GUI['entry_book_name'].get()
            book_subject = GUI['entry_book_subject'].get()
            author_name = GUI['entry_author_name'].get()
            publication = GUI['entry_publication'].get()

            date_of_publication = GUI['date_entry'].get_date()
            date_of_publication = date_of_publication.strftime("%d/%m/%Y")

            book_price = GUI['price_spinbox'].get()
            book_quantity = GUI['quantity_spinbox'].get()
            total_cost = GUI['total_entry'].get()
            
            if via == "update" and book_cover_path == DEFAULT_BOOK_COVER_PATH :
                
                user_selected_cover = GUI['table_data'].item(selected_tree_row_index)['image'][0]
                    
            else:
    
                img_choosen = Image.open(book_cover_path)
                img_choosen = img_choosen.resize((150,200), reducing_gap=Image.LANCZOS)
                user_selected_cover = ImageTk.PhotoImage(img_choosen)
                    
            form_input_book_data = [user_selected_cover,book_id, book_name, book_subject, author_name, publication, date_of_publication, book_price, book_quantity, total_cost]

            return BookServices.is_inputs_valid()
        
        except Exception as e :
            messagebox.showerror('Error', 'Provide proper values!')
            print("Error in getting book data : ",e)
            

    @staticmethod
    def set_book_cover(img_container,default=False,object=None):
    
        """
        -> Set book cover image to label. \n
        -> If default is False user have to choose path.
        """
        
        global book_cover_path
        
        if not object : 
            
            if not default : 
                book_cover_path = filedialog.askopenfilename(filetypes=[("Image files", "*.jpg *.jpeg *.png")])
                
                if not book_cover_path :
                    return

            else:
                book_cover_path=DEFAULT_BOOK_COVER_PATH
                
            img_cover = Image.open(book_cover_path)
            img_cover = img_cover.resize((150, 200), reducing_gap=Image.LANCZOS)
            img_cover = ImageTk.PhotoImage(img_cover)
            img_container.image = img_cover
            img_container['image'] = img_cover
            
        else :
            img_container.image = object
            img_container['image'] = object
            

    @staticmethod
    def get_confirmation(msg="Are you sure, you want to proceed??"):
        
        """
        -> Custom message Confirmation window. \n
        -> Return 'True' if yes clicked , other wise 'False'
        """
        
        result = messagebox.askyesno("Confirmation", msg)
        return result
        

    @staticmethod
    def clear_input_fields(confirmation=False):
        
        global selected_tree_row_index
            
        """
        -> This function clear the input fields and set initial value of some entries. \n
        -> Use also as "Cancel".
        """
        
        if confirmation :
            do_clear=BookServices.get_confirmation("Are you sure to clear fields?")
            
            if not do_clear:
                return
        
        GUI['entry_book_id'].config(state="normal",cursor="xterm")
        GUI['entry_book_id'].delete(0, tk.END)
        GUI['entry_book_name'].delete(0, tk.END)
        GUI['entry_book_subject'].delete(0, tk.END)
        GUI['entry_author_name'].delete(0, tk.END)
        GUI['entry_publication'].delete(0, tk.END)
        
        GUI['date_entry'].set_date(date.today())
        
        GUI['price_spinbox'].delete(0,tk.END)  
        GUI['price_spinbox'].insert(0, "0.00")
        
        GUI['quantity_spinbox'].delete(0, tk.END)  
        GUI['quantity_spinbox'].insert(0, "0")
        
        GUI['total_entry'].config(state="normal")  
        GUI['total_entry'].delete(0, tk.END)  
        GUI['total_entry'].insert(0, "0.00")
        GUI['total_entry'].config(state="readonly") 
        
        #table related
        selected_tree_row_index=""
        
        selected_item = GUI['table_data'].selection()
        
        if selected_item:
                GUI['table_data'].selection_remove(selected_item)
    
        BookServices.set_book_cover(GUI['img_container'],default=True)
        
    @staticmethod
    def select_row_of_table(event):
        
        global selected_tree_row_index

        try:

            selected_tree_row_index = GUI['table_data'].selection()[0]

            selected_item = GUI['table_data'].item(selected_tree_row_index)['values']
            row_img = GUI['table_data'].item(selected_tree_row_index)['image']

            GUI['entry_book_id'].delete(0, END)
            GUI['entry_book_id'].insert(0, selected_item[0])
            GUI['entry_book_id'].config(state="readonly",cursor="X_cursor")  
            
            GUI['entry_book_name'].delete(0, END)
            GUI['entry_book_name'].insert(0,selected_item[1])

            GUI['entry_book_subject'].delete(0, END)
            GUI['entry_book_subject'].insert(0, selected_item[2])

            GUI['entry_author_name'].delete(0, END)
            GUI['entry_author_name'].insert(0,selected_item[3])

            GUI['entry_publication'].delete(0, END)
            GUI['entry_publication'].insert(0,selected_item[4])

            GUI['date_entry'].set_date(datetime.strptime(selected_item[5], '%d/%m/%Y').date())

            GUI['price_spinbox'].delete(0, END)
            GUI['price_spinbox'].insert(0,selected_item[6])

            GUI['quantity_spinbox'].delete(0, END)
            GUI['quantity_spinbox'].insert(0,selected_item[7])

            GUI['total_entry'].config(state="normal")
            GUI['total_entry'].delete(0, END)
            GUI['total_entry'].insert(0,selected_item[8])
            GUI['total_entry'].config(state="readonly")  
                        
            BookServices.set_book_cover(GUI['img_container'],object=row_img[0])
            
            return

        except Exception as e:
            print("Error in selection row  : ", e)
