import tkinter as tk
import json
from tkinter import messagebox
from add_task import add, view, task_done

try:
    file=open("tasks.json", "r")
    tasks=json.load(file)
    file.close()
except FileNotFoundError:
    tasks=[]


root=tk.Tk()
root.title("To Do List")
root.geometry("400x400")

imptask= tk.Label(root, text="Important Tasks", font="Arial 15 bold")
imptask.pack(pady=10)


for impotask in tasks:
    done=tk.BooleanVar(value=False if "completed" not in impotask else impotask["completed"])
    if impotask["priority"]=="Important":
        all_tasks=tk.Checkbutton(root, 
                                 text=impotask["task"], 
                                 variable=done,
                                 font="Arial 15", 
                                 anchor="w", 
                                 width=50)
        all_tasks.pack(padx=20, pady=10)
        all_tasks.bind(
            "<Button-3>",
            lambda event: right_click(root, event)
            )


def right_click(root, event):
    menu = tk.Menu(root, tearoff=0)
    menu.add_command(label="Delete", command=lambda: print("Delete clicked"))
    menu.add_command(label="Edit", command=lambda: print("Edit clicked"))
    menu.add_command(label="Mark as Done", command=lambda: [done.set(True), task_done(event)])
    menu.post(event.x_root, event.y_root) 


button=tk.Button(root, text="Add Tasks", command=add)
button.pack(pady=20)

button2=tk.Button(root, text="View All", command=view)
button2.pack(pady=10)

def on_closing():
    if messagebox.askyesno("Quit", "Are you sure you want to quit?"):
        root.destroy()


root.protocol("WM_DELETE_WINDOW", on_closing)
root.mainloop()
