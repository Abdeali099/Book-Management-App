# backend/database.py

import sqlite3
import io

import tkinter as tk
# import sqlite3
import re
# import io
from tkinter import filedialog
from tkinter import messagebox
from tkinter import ttk
from tkcalendar import DateEntry
from PIL import Image, ImageTk
from datetime import date

class Database:
    # Queries
    fetch_all_data_query = "SELECT * FROM books;"
    insert_query = "INSERT INTO books VALUES (?,?,?,?,?,?,?,?,?,?);"
    # update_query = "UPDATE routers SET hostname=? , brand=? , ram=? , flash=? WHERE id = ?;"
    # delete_query = "DELETE FROM routers WHERE id = ?;"
    # search_query = "SELECT * FROM routers WHERE hostname LIKE ? ;"
    
    # class objects
    cursor=None
    connection = None

    # run only for once
    def __init__(self):
        
        Database.connection = sqlite3.connect("./Backend/Books.db")
        Database.cursor = Database.connection.cursor()
        Database.cursor.execute(
            """
            CREATE TABLE IF NOT EXISTS 
            books (id INTEGER PRIMARY KEY, 
                     subject TEXT, 
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

    # @classmethod
    @staticmethod
    # Populate data at window loading / Opening
    def fetch_all_data():
    
        book_data_for_table=[]
        
        initial_data = Database.cursor.execute(Database.fetch_all_data_query)
        books_data = initial_data.fetchall()
        
        
        if len(books_data) != 0:
            
            for data in books_data:
                                
                cover_blob = data[-1]
                data=list(data)
                data[-1] = Database.convert_blob_to_image(cover_blob)            
                book_data_for_table.append(data)

        
        return book_data_for_table
            
                
    def insert(self, valid_input_data):
        
        try:
            # save to database
            Database.cursor.execute(Database.insert_query, valid_input_data)
            Database.connection.commit()
        
        except Exception as e:
            print('Error in saving data : ', e)
            messagebox.showerror('Error', 'Error in saving data into database,try again...')
            return False
        
        return True

    @staticmethod
    def convert_blob_to_image(blob_data):
                
        try:
            # Assuming the blob_data is in bytes format
            image_stream = io.BytesIO(blob_data)
            img = Image.open(image_stream)
            img = img.resize((80, 80), Image.LANCZOS)  # Adjust size as needed
            img = ImageTk.PhotoImage(img)
            return img
        
        except Exception as e:
            print(f"Error converting BLOB to image: {e}")
            return None

    def search_by_hostname(self, search_hostname):
         pass # Your existing search_by_hostname method

    def search_by_query(self, search_query):
         pass # Your existing search_by_query method

"""
class Database:
    
    # Queries
    fetch_all_data_query = "SELECT * FROM books;"
    insert_query = "INSERT INTO books VALUES (?,?,?,?,?,?,?,?,?,?);"
    # update_query = "UPDATE routers SET hostname=? , brand=? , ram=? , flash=? WHERE id = ?;"
    # delete_query = "DELETE FROM routers WHERE id = ?;"
    # search_query = "SELECT * FROM routers WHERE hostname LIKE ? ;"
    
    # class objects
    cursor=None
    connection = None

    # run only for once
    def __init__(self, database_name):
        
        self.database_name = database_name
        Database.connection = sqlite3.connect(database_name)
        Database.cursor = Database.connection.cursor()
        Database.cursor.execute(
            CREATE TABLE IF NOT EXISTS 
            books (id INTEGER PRIMARY KEY, 
                     subject TEXT, 
                     book_name TEXT, 
                     author_name TEXT, 
                     publication TEXT,
                     pub_date TEXT,
                     price REAL,
                     quantity INTEGER,
                     cost REAL,
                     cover BLOB)

        Database.connection.commit()

    # Populate data at window loading / Opening
    def fetch_all_data(self):
        
        global book_cover_data_list
        
        initial_data = self.cursor.execute(Database.fetch_all_data_query)
        books_data = initial_data.fetchall()

        if len(books_data) != 0:
            
            for data in books_data:
                
                cover_blob = data[-1]
                img = self.convert_blob_to_image(cover_blob)
                book_cover_data_list.append(img)

                # Insert the data along with the image
                table_data.insert('', 'end', image=img, values=data[:-1])
                

    # ---- CRUD Operation Methods (Database)  ---- #

    # 1 : Insert Data
    def insert(self, valid_input_data):
                
        try:
            # save to database
            Database.cursor.execute(Database.insert_query, valid_input_data)
            Database.connection.commit()
            
            
        except Exception as e:
            print('Error in saving data : ', e)
            messagebox.showerror('Error', 'Error in saving data,try again...')
            return False
            
        return True

    # 2 : Update Data
    def update(self, valid_input_data):
        pass
        # try:
        #     # update to database
        #     update_values = valid_input_data[1::]
        #     update_values.append(valid_input_data[0])

        #     self.cursor.execute(Database.update_query, update_values)
        #     Database.connection.commit()

        #     # update tree
        #     router_tree_view.item(selected_tree_row_index, values=valid_input_data)

        # except Exception as e:
        #     print('Error in updating data : ', e)
        #     messagebox.showerror('Error', 'Error in updating data,try again...')

    # 3 : Delete Data
    def delete(self, delete_id):
        
        pass

        # try:
        #     # delete from database
        #     self.cursor.execute(Database.delete_query, [delete_id])
        #     Database.connection.commit()

        #     # delete temporary
        #     router_tree_view.delete(selected_tree_row_index)

        # except Exception as e:
        #     print('Error in deleting data : ', e)
        #     messagebox.showerror('Error', 'Error in deleting data,try again...')

    def convert_blob_to_image(self, blob_data):
                
        try:
            # Assuming the blob_data is in bytes format
            image_stream = io.BytesIO(blob_data)
            img = Image.open(image_stream)
            img = img.resize((80, 80), Image.LANCZOS)  # Adjust size as needed
            img = ImageTk.PhotoImage(img)
            return img
        
        except Exception as e:
            print(f"Error converting BLOB to image: {e}")
            return None
        
    # 4 : search hostname
    def search_by_hostname(self, search_hostname):
        pass
        
        # initial_data = self.cursor.execute(Database.hostname_search_query, ('%' + search_hostname + '%',))
        # routers_data = initial_data.fetchall()

        # if len(routers_data) != 0:
        #     for data in routers_data:
        #         router_tree_view.insert('', 'end', values=data)

    def search_by_query(self, search_query):
        pass
    
        # initial_data = self.cursor.execute(search_query)
        # routers_data = initial_data.fetchall()

        # if len(routers_data) != 0:
        #     for data in routers_data:
        #         router_tree_view.insert('', 'end', values=data)
"""