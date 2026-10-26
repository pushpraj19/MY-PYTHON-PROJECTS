import tkinter as tk

root = tk.Tk()
root.title("Simple Calculator")
root.geometry("300x400")
root.resizable(False, False)


button_frame = tk.Frame(root)
button_frame.pack(side="bottom", padx=10, pady=10)



lable= tk.Label(root, text="", anchor="e", font=("Arial", 24), bg="white", fg="black")
lable.pack(fill="both", padx=10, pady=20)


def calculate():
    result=(lable.cget("text"))
    try:
        result = eval(result)
    except:
        result = "Error"

    lable.config(text=str(result))

def special(symbol):
    data=lable.cget("text")




but1= tk.Button(button_frame, text="7", width=5, height=2, command=lambda: lable.config(text=lable.cget("text") + "7"))
but1.grid(row=0, column=0, padx=5, pady=5)
but2= tk.Button(button_frame, text="8", width=5, height=2, command=lambda: lable.config(text=lable.cget("text") + "8"))
but2.grid(row=0, column=1, padx=5, pady=5)
but3= tk.Button(button_frame, text="9", width=5, height=2, command=lambda: lable.config(text=lable.cget("text") + "9"))
but3.grid(row=0, column=2, padx=5, pady=5)
but4= tk.Button(button_frame, text="/", width=5, height=2, command=lambda: lable.config(text=lable.cget("text") + "/"))
but4.grid(row=0, column=3, padx=5, pady=5)
but5= tk.Button(button_frame, text="4", width=5, height=2, command=lambda: lable.config(text=lable.cget("text") + "4"))
but5.grid(row=1, column=0, padx=5, pady=5)
but6= tk.Button(button_frame, text="5", width=5, height=2, command=lambda: lable.config(text=lable.cget("text") + "5"))
but6.grid(row=1, column=1, padx=5, pady=5)
but7= tk.Button(button_frame, text="6", width=5, height=2, command=lambda: lable.config(text=lable.cget("text") + "6"))
but7.grid(row=1, column=2, padx=5, pady=5)
but8= tk.Button(button_frame, text="*", width=5, height=2, command=lambda: lable.config(text=lable.cget("text") + "*"))
but8.grid(row=1, column=3, padx=5, pady=5)
but9= tk.Button(button_frame, text="1", width=5, height=2, command=lambda: lable.config(text=lable.cget("text") + "1"))
but9.grid(row=2, column=0, padx=5, pady=5)
but10= tk.Button(button_frame, text="2", width=5, height=2, command=lambda: lable.config(text=lable.cget("text") + "2"))
but10.grid(row=2, column=1, padx=5, pady=5 )
but11= tk.Button(button_frame, text="3", width=5, height=2, command=lambda: lable.config(text=lable.cget("text") + "3"))
but11.grid(row=2, column=2, padx=5, pady=5)
but12= tk.Button(button_frame, text="-", width=5, height=2, command=lambda: lable.config(text=lable.cget("text") + "-"))
but12.grid(row=2, column=3, padx=5, pady=5)
but13= tk.Button(button_frame, text=".", width=5, height=2, command=lambda: lable.config(text=lable.cget("text") + "."))
but13.grid(row=3, column=0, padx=5, pady=5)
but14= tk.Button(button_frame, text="0", width=5, height=2, command=lambda: lable.config(text=lable.cget("text") + "0"))
but14.grid(row=3, column=1, padx=5, pady=5)
but15= tk.Button(button_frame, text="+", width=5, height=2, command=lambda: lable.config(text=lable.cget("text") + "+"))
but15.grid(row=3, column=2, padx=5, pady=5)
but16= tk.Button(button_frame, text="=", width=5, height=2, command=calculate)
but16.grid(row=3, column=3, padx=5, pady=5)
but17= tk.Button(button_frame, text="C", width=5, height=2, command=lambda: lable.config(text=""))
but17.grid(row=1, column=5, padx=5, pady=5)
but18= tk.Button(button_frame, text="Del", width=5, height=2, command=lambda: lable.config(text=lable.cget("text")[:-1]))
but18.grid(row=0, column=5, padx=5, pady=5)
but19= tk.Button(button_frame, text="^2", width=5, height=2, command=lambda: lable.config(text=lable.cget("text") + "**"))
but19.grid(row=2, column=5, padx=5, pady=5)


root.mainloop()

