import tkinter as tk
from tkinter import messagebox
def calculate_compound_interest():
    try:
        principal=float(principal_entry.get())
        rate=float(rate_entry.get())
        years=int(years_entry.get())
        compound_interest=principal*(1+rate/100)**years-principal
        result_entry.config(state="normal")
        result_entry.delete(0,tk.END)
        result_entry.insert(0,f"{compound_interest:.2f}")
        result_entry.config(state="readonly")
    except ValueError:
        messagebox.showerror("Error","please enter valid numbers")
def clear_entries():
    principal_entry.delete(0,tk.END)
    rate_entry.delete(0,tk.END)
    years_entry.delete(0,tk.END)    
    result_entry.config(state="normal")
    result_entry.delete(0,tk.END)
    result_entry.config(state="readonly")
root=tk.Tk()
root.title("Compound Interest Calculator")
principal_label=tk.Label(root,text="Principal Amount:")
principal_label.grid(row=0,column=0,padx=5,pady=5)
principal_entry=tk.Entry(root)
principal_entry.grid(row=0,column=1,padx=5,pady=5)
rate_label=tk.Label(root,text="Rate of Interest(%):")
rate_label.grid(row=1,column=0,padx=5,pady=5)
rate_entry=tk.Entry(root)
rate_entry.grid(row=1,column=1,padx=5,pady=5)
years_label=tk.Label(root,text="Number of years:")
years_label.grid(row=2,column=0,padx=5,pady=5)
years_entry=tk.Entry(root)
years_entry.grid(row=2,column=1,padx=5,pady=5)
result_label=tk.Label(root,text="Compound Interest:")
result_label.grid(row=3,column=0,padx=5,pady=5)
result_entry=tk.Entry(root)
result_entry.grid(row=3,column=1,padx=5,pady=5)
calculate_button=tk.Button(root,text="Submit",command=calculate_compound_interest)
calculate_button.grid(row=4,column=0,columnspan=2,padx=5,pady=5)
clear_button=tk.Button(root,text="clear",command=clear_entries)
clear_button.grid(row=5,column=0,columnspan=2,padx=5,pady=5)
root.mainloop()





    
