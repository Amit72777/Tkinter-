import tkinter as tk
from tkinter import ttk 

win = tk.Tk()
win.title("Member Turtorial")

def func():
    print("fun called")

#Menu 
menubar = tk.Menu(win)



def edit():
    pass 
main_menu  = tk.Menu(win)
file_menu = tk.Menu(main_menu,tearoff= 0 )
file_menu.add_command( label= 'New file', command= func)
file_menu.add_command( label= 'New Window', command= func)
file_menu.add_command( label= 'Save file ', command= func)
file_menu.add_command( label= 'Save as  file', command= func)

edit_menu = tk.Menu(win,tearoff= 0 )
edit_menu.add_command(label = "Copy",command=edit)
edit_menu.add_command(label = "Paste ",command=edit)
edit_menu.add_separator()
edit_menu.add_command(label = "Undo",command=edit)
edit_menu.add_command(label = "Redo ",command=edit)



main_menu.add_cascade(label = 'File',menu = file_menu)
main_menu.add_cascade(label = 'Edit', menu= edit_menu)

win.config(menu = main_menu )

win.mainloop()