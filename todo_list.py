from tkinter import *

def add_task():
    task = task_entry.get()
    if task != "":
        task_listbox.insert(END, task)
        task_entry.delete(0, END)

def delete_task():
    selected = task_listbox.curselection()
    if selected:
        task_listbox.delete(selected)

def clear_tasks():
    task_listbox.delete(0, END)

root = Tk()
root.title("To-Do List")
root.geometry("400x400")

task_entry = Entry(root, width=30)
task_entry.pack(pady=10)

add_button = Button(root, text="Add Task", command=add_task)
add_button.pack()

task_listbox = Listbox(root, width=40, height=10)
task_listbox.pack(pady=10)

delete_button = Button(root, text="Delete Task", command=delete_task)
delete_button.pack(pady=5)

clear_button = Button(root, text="Clear All", command=clear_tasks)
clear_button.pack(pady=5)

root.mainloop()