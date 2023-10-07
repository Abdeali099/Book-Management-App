import tkinter  as tk 
from tkinter import ttk
from tkcalendar import DateEntry
my_w = tk.Tk()
my_w.geometry("380x200")  
sel=tk.StringVar() # declaring string variable 
style = ttk.Style(my_w)
style.theme_use('clam') #Theme to be changed # alt , classic, clam

style.configure('my.DateEntry',
                fieldbackground='white',
                background='dark green',
                foreground='dark blue',
                arrowcolor='black',
				)

cal=DateEntry(my_w,style='my.DateEntry',selectmode='day',textvariable=sel,date_pattern="dd/mm/yyyy")
cal.grid(row=1,column=1,padx=20)

my_w.mainloop()