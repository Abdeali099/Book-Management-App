from tkinter import ttk
import tkinter as tk
from PIL import Image,ImageTk

# Creating tkinter my_w
my_w = tk.Tk()
my_w.geometry("380x380") 
my_w.title("www.plus2net.co/m") 
 
# Using treeview widget style 
style = ttk.Style()
style.configure('Treeview', rowheight=100)  # increase height 

trv = ttk.Treeview(my_w, selectmode ='browse',height=3)  
trv.grid(row=1,column=1,rowspan=5,padx=30,pady=20)

# number of columns
trv["columns"] = ("1")
# Defining heading
trv['show'] = 'tree headings'
#trv['show'] = 'tree'

trv.heading("#0", text ="#") # Text of the column 
trv.column("#0", width = 150, anchor ='center') # Width of column
# Headings  
# respective columns
trv.heading("1", text ="Name")
trv.column("1", width = 130, anchor ='center')

    
img_path = "./assets/byDefaultCover.jpg"
img = Image.open(img_path)
img = img.resize((50, 50), reducing_gap=Image.LANCZOS)  # Adjust the size as needed
img1 = ImageTk.PhotoImage(img)
    
# img1 = ImageTk.PhotoImage(Image.open("./assets/byDefaultCover.jpg"))
img2 = ImageTk.PhotoImage(Image.open("./assets/addIcon.png"))
img3 = ImageTk.PhotoImage(Image.open("./assets/byDefaultCover.jpg"))

trv.insert("",'end',iid='1',open=True,text='100',image=img1,values=('na-Alex'))
trv.insert("",'end',iid=2,open=True,text='200',image=img2,values=('n1-Alex'))
trv.insert("",'end',iid='3',open=True,text='300',image=img3,values =('Child-Alex'))

my_w.mainloop()