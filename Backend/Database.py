from tkinter import messagebox
from PIL import Image, ImageTk
import sqlite3
import io

class Database:
    
    # Queries
    fetch_all_data_query = "SELECT * FROM books;"
    insert_query = "INSERT INTO books VALUES (?,?,?,?,?,?,?,?,?,?);"
    update_query = "UPDATE books SET book_subject=? , book_name=? , author_name=? , publication=?, pub_date=? , price=? , quantity=? , cost=? ,cover =? WHERE id = ?;"
    delete_query = "DELETE FROM books WHERE id = ?;"
    search_query = "SELECT * FROM books WHERE {field} LIKE ? ;"
    
    # class objects
    cursor=None
    connection = None

    def __init__(self):
        
        Database.connection = sqlite3.connect("./Backend/Books.db")
        Database.cursor = Database.connection.cursor()
        Database.cursor.execute(
            """
            CREATE TABLE IF NOT EXISTS 
            books (id INTEGER PRIMARY KEY, 
                     book_subject TEXT, 
                     book_name TEXT, 
                     author_name TEXT, 
                     publication TEXT,
                     pub_date TEXT,
                     price REAL,
                     quantity INTEGER,
                     cost REAL,
                     cover BLOB)
            """)

        Database.connection.commit()

    @staticmethod
    def fetch_all_data():
        
        """
        -> Fetch all data stored in database
        Returns:
            _type_: list
        """
    
        book_data_for_table=[]
        
        try:
        
            initial_data = Database.cursor.execute(Database.fetch_all_data_query)
            books_data = initial_data.fetchall()
            
            if len(books_data) != 0:
                
                for data in books_data:
                                    
                    cover_blob = data[-1]
                    data=list(data)
                    data[-1] = Database.convert_blob_to_image(cover_blob)            
                    book_data_for_table.append(data)

        except Exception as e:
            print('Error in fetching data : ', e)
            messagebox.showerror('Error', 'Error in fetching data from database,try again...')

        return book_data_for_table
                
    def insert(self, valid_input_data):
        
        """
        -> Insert one book data into database.
        Returns:
            _type_: boolean
        """
        
        try:
            Database.cursor.execute(Database.insert_query, valid_input_data)
            Database.connection.commit()
            
        except sqlite3.IntegrityError as e:
            print('Error in saving data - Unique constraint violation:', e)
            messagebox.showerror('Error', 'Error: Duplicate entry, try again...')
            return False
                
        except Exception as e:
            print('Error in saving data : ', e)
            messagebox.showerror('Error', 'Error in saving data into database,try again...')
            return False
        
        return True
    
    def update(self, valid_input_data):
        
        """
        -> Update one book data into database.
        Returns:
            _type_: boolean
        """

        try:
            # update to database
            update_values = valid_input_data[1::]
            update_values.append(valid_input_data[0])

            Database.cursor.execute(Database.update_query, update_values)
            Database.connection.commit()

        
        except Exception as e:
            print('Error in updating data : ', e)
            messagebox.showerror('Error', 'Error in updating data,try again...')
            return False
        
        return True

    
    def delete(self, delete_id):
        
        """
        -> Delete one book data from database.
        Returns:
            _type_: boolean
        """
    
        try:
            Database.cursor.execute(Database.delete_query, [delete_id])
            Database.connection.commit()
            
        except Exception as e:
            print('Error in deleting data : ', e)
            messagebox.showerror('Error', 'Error in deleting data,try again...')
            return False

        return True

    @staticmethod
    def query_book(field,keyword):
             
        """
        -> Fetching require data with field and kewyword.
        Returns:
            _type_: list
        """

        book_data_for_table=[]
        
        try:
        
            search_query=Database.search_query.format(field=field)
            
            initial_data = Database.cursor.execute(search_query,[keyword])
            books_data = initial_data.fetchall()
                    
            if len(books_data) != 0:
                
                for data in books_data:
                                    
                    cover_blob = data[-1]
                    data=list(data)
                    data[-1] = Database.convert_blob_to_image(cover_blob)            
                    book_data_for_table.append(data)

        except Exception as e:
            print('Error in searching data : ', e)
            messagebox.showerror('Error', 'Error in seraching data from database,try again...')

        return book_data_for_table

    @staticmethod
    def convert_blob_to_image(blob_data):
        
        """
        -> Convert store blob image to PIL image to show in form and store into table.
        Returns:
            _type_: PIL Image (object)
        """
                
        try:
            image_stream = io.BytesIO(blob_data)
            img = Image.open(image_stream)
            img = img.resize((150,200), Image.LANCZOS)  # Adjust size as needed
            img = ImageTk.PhotoImage(img)
            return img
        
        except Exception as e:
            print(f"Error converting BLOB to image: {e}")
            messagebox.showerror('Error', 'Error in fetching images from database,try again..')
            return None

            