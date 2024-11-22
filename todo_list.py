from tkinter import *
from tkinter import ttk
import tkinter.font
import json
from ttkthemes import ThemedTk

def add_task():
    task = task_var.get()
    if task:
        task_panel.insert("",tkinter.END,values=(task,))
        task_var.set("")

def delete_task():
    item = task_panel.selection()
    if item:
        task_panel.delete(item)

def save_task():
    tasks = []
    for child in task_panel.get_children():
        task = task_panel.item(child)["values"][0]
        tasks.append(task)
    with open("tasks.json","w") as f:
        json.dump(tasks,f)

def retrieve_tasks():
    try:
        with open("tasks.json","r") as f:
            tasks = json.load(f)
        for task in tasks:
            task_panel.insert("",tkinter.END,values=(task,))
    except:
        pass
    
if __name__ == "__main__":
    window = ThemedTk()
    window.title("Todo List")
    icon_image = PhotoImage(file="icon.png")
    window.iconphoto(False,icon_image)
    window_frame = ttk.Frame(window,padding="20 20 20 20")
    task_var = StringVar()
    task_entry = ttk.Entry(window_frame,textvariable=task_var,font=("",15),width=30)
    task_entry.grid(row=0,column=0,padx=(0,10),pady=(0,20))
    add_task_button = ttk.Button(window_frame,text="Add Task",width=8,command=add_task)
    add_task_button.grid(row=0,column=1,pady=(0,20))
    task_panel = ttk.Treeview(window_frame,columns=("Task",),show="headings",height=20)
    task_panel.heading("Task",text="Tasks")
    task_panel.grid(row=1,column=0,columnspan=2,sticky="nesw")
    task_panel_scrollbar = ttk.Scrollbar(window_frame,orient=tkinter.VERTICAL,command=task_panel.yview)
    task_panel_scrollbar.grid(row=1,column=2,sticky="ns")
    task_panel.configure(yscrollcommand=task_panel_scrollbar.set)
    retrieve_tasks()
    delete_task_button = ttk.Button(window_frame,text="Delete Task",command=delete_task)
    delete_task_button.grid(row=2,column=0,sticky="ew",padx=(0,10),pady=(10,0))
    save_task_button = ttk.Button(window_frame,text="Save Tasks",command=save_task)
    save_task_button.grid(row=2,column=1,pady=(10,0))
    window_frame.pack()
    style = ttk.Style()
    style.theme_use("radiance")
    style.configure("TFrame",background=window.cget("bg"))
    window.mainloop()
