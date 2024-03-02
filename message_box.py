import tkinter as tk
from tkinter import ttk
from tkinter import messagebox as m_box 

win= tk.Tk()
# label frame
label_frame = ttk.LabelFrame(win, text = 'Contact Detail')
label_frame.grid(row = 0 , column = 0 , padx = 40, pady = 10 )

# labels
name_label = ttk.Label(label_frame,text= 'Enter you Name :'  , font= ('Helvetica',15))
age_label = ttk.Label (label_frame,text= 'Enter your Age ',font= ('Helvetica',15))

#entry box variables
name_var = tk.StringVar()
age_var = tk.StringVar()

# entry box 
name_entry = tk.Entry(label_frame,width= 35,textvariable= name_var)
age_entry = tk.Entry(label_frame,width=35,textvariable= age_var)
name_entry.focus()

#grid
name_label.grid(row = 0 , column=0,padx= 5 ,pady=5,sticky= tk.W)
age_label.grid(row = 0 , column=1,padx= 5 ,pady=5,sticky= tk.W)
name_entry.grid(row = 1 , column=0,padx= 5 ,pady=5,sticky= tk.W)
age_entry.grid(row = 1 , column=1  ,padx= 5 ,pady=5,sticky= tk.W)
# name_label.grid(row = 0 , column=0,padx= 5 ,pady=5,sticky= tk.W)

def submit():
    # m_box.showinfo("title",'content of this message box!!')
    name = name_var.get()
    age = age_var.get()
    if name == '' or age == '':
        m_box.showerror('Error','Please fill both name and age ')

    else:
        try :
            age = int(age)
        except ValueError:
            m_box.showerror('ERROR',"Only digit are allow in age ")  # first argument is title and second argument is message 
        else :
            if age<18 :
                m_box.showwarning('"Warning', ' Your age not 18 , visit this context on your risk ')
            print(f'{name} is{age}')



submit_btn = ttk.Button(win,text = 'Submit',command= submit )
submit_btn.grid(row= 1,columnspan=2,padx = 40 )


win.mainloop()