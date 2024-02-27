
import tkinter as tk 
from tkinter import ttk 

win = tk.Tk()
win.title("Loop")

lables = ['what is your name','what is you age ','what is your gender :','Country:',"State:",'City:']  # cearte a list of labels



for i in range(len(lables)): # create a labels 
    cur_lablel = 'lable' +str(i)
    cur_lable = ttk.Label(win,text= lables[i])
    cur_lable.grid(row= i , column=0 , sticky=tk.W , padx = 2 ,pady = 2  )


# name_entry = ttk.Entry(win,width=16 )
# name_entry.grid(row =0,column= 1  )
# create a dictionary to store a variabel 
user_info = {
    'name':tk.StringVar()
,    'age' :tk.StringVar()   
, 'gender': tk.StringVar() , 
'country' : tk.StringVar(),
'state' : tk.StringVar(),
'city'  : tk.StringVar()
}
# Enter box  
counter = 0 
for i in user_info:
    cur_entrybox = 'entry' +i
    cur_entrybox = ttk.Entry(win,width = 16 , textvariable= user_info[i] )
    cur_entrybox.grid(row = counter ,column= 1 , padx = 2  , pady = 2)
    counter += 1

def submit():
    print(user_info['name'].get())
    print(user_info['age'].get())
    print(user_info['gender'].get())
    print(user_info['country'].get())
    print(user_info['state'].get())
    print(user_info['city'].get())
   
submit_btn = ttk.Button(win,text = 'Submit',command= submit)  # create a button 
submit_btn.grid(row= 6 , columnspan = 2 ) 

win.mainloop()