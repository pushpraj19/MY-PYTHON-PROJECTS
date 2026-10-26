import tkinter as tk
import json
import datetime






def add():
    window=tk.Tk()
    window.title("Add Task")
    window.geometry("250x320")
    window.resizable(False,False)


    title_label = tk.Label(window, text="Title:", font=("Arial", 18))
    title_label.pack()
    title_entry = tk.Entry(window, width=30)
    title_entry.pack()

    task_label = tk.Label(window, text="Task:", font=("Arial", 18))
    task_label.pack()
    task_entry = tk.Entry(window, width=30)
    task_entry.pack()

    date_label = tk.Label(window, text="Date: Days", font=("Arial", 14))
    date_label.pack()

    date_entry = tk.Entry(window, width=30)
    date_entry.pack()

    choice=tk.StringVar(window)
    choice.set("Select the priority")
    priority=tk.OptionMenu(window, 
                          choice,
                          "Important",
                           "Normal"
                           )
    priority.config(width=20)
    priority.pack(pady=20)
    
    task_update=tk.Label(window, text="", fg="green")
    

    add_button = tk.Button(window, text="Add Task", command=lambda: add_task(task_update, title_entry.get(), task_entry.get(), date_entry.get(), choice.get()))
    
    add_button.pack(padx=20, pady=20)
    task_update.pack()

    



def add_task(task_update, title, task, date, choice):
    try:
        file=open("tasks.json", "r")
        tasks=json.load(file)
        file.close()
    except FileNotFoundError:
        tasks=[]

    today = datetime.date.today().strftime("%Y-%m-%d")
    
    try:
        title=title.strip()
        task=task.strip()
        priority=choice
        final_date=(datetime.date.today() + datetime.timedelta(days=int(date))).strftime("%Y-%m-%d")


        if title  not in [task["title"] for task in tasks] and task not in [task["task"] for task in tasks]:
            todo = {
                    "id": len(tasks) + 1,
                    "title": title,
                    "task": task, 
                    "priority": priority,      
                    "date":today,
                    "Final Date":final_date,
                    "completed":False
                }
            tasks.append(todo)
            with open("tasks.json", "w") as file:
                json.dump(tasks, file, indent=4)

            task_update.config(text="Task added successfully", fg="green")
        
        else:
            task_update.config(text="Task already exists", fg="red")

    except:
        task_update.config(text="Please fill all the fields", fg="red")


def view():
    view_window=tk.Tk()
    view_window.title("View All Tasks")
    view_window.geometry("400x400")
    view_window.resizable(False,False)

    try:
        file=open("tasks.json", "r")
        tasks=json.load(file)
        file.close()
    except:
        tasks=[]
        
    
    for task in tasks:
        done=tk.BooleanVar(value=False if "completed" not in task else task["completed"])
        if task["task"]:
            all_tasks=tk.Checkbutton(view_window, 
                                    text=task["task"], 
                                    variable=done,
                                    font="Arial 15", 
                                    anchor="w", 
                                    width=50)
            all_tasks.pack(padx=20, pady=10)
            all_tasks.bind(
                "<Button-3>",
                lambda event: right_click(view_window, event)
                )


def right_click(view_window, event):
    menu = tk.Menu(view_window, tearoff=0)
    menu.add_command(label="Delete", command=lambda: print("Delete clicked"))
    menu.add_command(label="Edit", command=lambda: print("Edit clicked"))
    menu.post(event.x_root, event.y_root) 

def task_done(event):
    try:
        file=open("tasks.json", "r")
        tasks=json.load(file)
        file.close()
    except FileNotFoundError:
        tasks=[]

    for task in tasks:
        if task["task"] == event.widget.cget("text"):
            task["completed"] = True
            break

    with open("tasks.json", "w") as file:
        json.dump(tasks, file, indent=4)