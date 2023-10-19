"""
This a main file to run project.
"""

from os import getcwd
import sys
sys.path.append(getcwd())

from Frontend.BookManagmentGUI import BookManagmentGUI

if __name__ == "__main__":
    
    gui = BookManagmentGUI()
    gui.mainloop()
