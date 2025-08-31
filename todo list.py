import tkinter as tk
from tkinter import messagebox

def add_task():
    task=task_entry.get()
    if task !="":
        task_listbox.insert(tk.END,task)
        task_entry.delete(0,tk.END)
    else:
        messagebox.showwarning("warning","please enter the task first")

def delete_task():
    try:
        select_task = task_listbox.curselection()[0]        
        task_listbox.delete(select_task)
    except:
        messagebox.showwarning("warning","please select the task first")    

def clear_task():
    task_listbox.delete(0,tk.END)

root = tk.Tk()
root.title("To-do list")
root.geometry("500x500")
root.config(bg="lightyellow") 

task_entry=tk.Entry(root,width=50,font=("Times new roman",15))
task_entry.pack(pady=15)

add_button = tk.Button(root,text="add task",width=16,command=add_task)
add_button.pack(pady=6)

delete_button = tk.Button(root,text="delete task",width=16,command=delete_task)
delete_button.pack(pady=6)

clear_button = tk.Button(root,text="clear task",width=16,command=clear_task)
clear_button.pack(pady=6)

task_listbox=tk.Listbox(root,width=50,height=15,selectmode=tk.SINGLE,font=("Times new roman",15))
task_listbox.pack(pady=15)

root.mainloop()


