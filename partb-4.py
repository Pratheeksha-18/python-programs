import tkinter as tk
def button_click(number):
    current=entry.get()
    entry.delete(0,tk.END)
    entry.insert(0,current+str(number))
def button_clear():
    entry.delete(0,tk.END)
def button_equal():
    try:
        result=eval(entry.get())
        entry.delete(0,tk.END)
        entry.insert(0,str(result))
    except Exception as e:
        entry.delete(0,tk.END)
        entry.insert(0, "Error")
def button_exit():
    root.destroy()
root=tk.Tk()
root.title("Simple Calculator")
entry=tk.Entry(root,width=35,borderwidth=5)
entry.grid(row=0,column=0,columnspan=4,padx=10,pady=10)
buttons=[
    ('7',1,0),('8',1,1),('9',1,2),
    ('4',2,0),('5',2,1),('6',2,2),
    ('1',3,0),('2',3,1),('3',3,2),
    ('0',4,0),('.',4,1),
    ('+',1,3),('-',2,3),
    ('*',3,3),('/',4,3),
    ('=',4,2),('c',0,3),
    ('Exit',5,0)
    ]
for text,row,col in buttons:
    if text=='=':
        action=button_equal
    elif text=='c':
        action=button_clear
    elif text=='Exit':
        action=button_exit
    else:
        action=lambda x=text:button_click(x)
    tk.Button(root,text=text,padx=20,pady=20,command=action).grid(row=row,column=col)
root.mainloop()    
