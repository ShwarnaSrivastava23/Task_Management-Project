import tkinter as tk
import random
from os import remove
from tkinter import messagebox as msg
#my_w = tk.Tk()

root = tk.Tk()
root.configure(bg="white")
root.title("My Super To Do List")

root.minsize(400,400)
root.maxsize(400,400)

#Create and empty list
tasks = []
"for testing purpose of default list"
tasks = ["Call mom", "Eat healthy food", "Time management"]

def update_listbox():
    clear_listbox()
    for task in tasks:
        lb_tasks.insert("end", task)

def clear_listbox():
    lb_tasks.delete(0, "end")

def add_task():
    task = txt_input.get()
    if task !="":
        tasks.append(task)
        update_listbox()
    else:
        lbl_display["text"] = "Please enter a task"
    txt_input.delete(0,"end")


def del_all():
    confirmed = msg.askyesno("Please confirm", "Do you really want to delete all tasks")
    if confirmed == True:
        global tasks
        tasks = []
        #Update the list box
        update_listbox()


def del_one():
    task= lb_tasks.get("active")                                           #Get the text of the currently selected item
    if task in tasks:
        tasks.remove(task)                                                  #Confirm it is in the list
    update_listbox()

def sort_asc():
    tasks.sort()
    update_listbox()

def sort_desc():
    tasks.sort()                                                            #Sort the list
    tasks.reverse()
    update_listbox()

def choose_random():
    task = random.choice(tasks)
    lbl_display["text"]=task

def number_of_tasks():
    number_of_tasks = len(tasks)
    lbl_display["text"]=tasks
    msg = "Number of tasks: %s" %number_of_tasks
    lbl_display["text"]=msg


lbl_title = tk.Label(root, text="To-Do-List", bg="white")
lbl_title.grid(row=0,column=0)

lbl_display = tk.Label(root, text="", bg="white")
lbl_display.grid(row=0,column=1)

txt_input = tk.Entry(root, width=15)
txt_input.grid(row=1,column=1)


btn_add_task = tk.Button(root, text="Add task", fg="green", bg="white", command = add_task)
btn_add_task.grid(row=1,column=0)

btn_del_all = tk.Button(root, text="Delete All", fg="green", bg="white", command = del_all)
btn_del_all.grid(row=2,column=0)

btn_del_one = tk.Button(root, text="Delete one", fg="green", bg="white", command = del_one)
btn_del_one.grid(row=3,column=0)

btn_sort_asc = tk.Button(root, text="Sort(ASC)", fg="green", bg="white", command = sort_asc )
btn_sort_asc.grid(row=4,column=0)

btn_sort_desc = tk.Button(root, text="Sort(DESC)", fg="green", bg="white", command = sort_desc)
btn_sort_desc.grid(row=5,column=0)

btn_choose_random = tk.Button(root, text="Choose Random", fg="green", bg="white", command= choose_random)
btn_choose_random.grid(row=6,column=0)

btn_number_of_tasks = tk.Button(root, text="Number of tasks", fg="green", bg="white", command = number_of_tasks)
btn_number_of_tasks.grid(row=7,column=0)

btn_exit = tk.Button(root, text="", fg="green", bg="white", command = exit )
btn_exit.grid(row=8,column=0)

lb_tasks = tk.Listbox(root)
lb_tasks.grid(row=2,column=1,rowspan=7)
root.mainloop()


