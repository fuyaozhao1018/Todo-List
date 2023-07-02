from tkinter import *  
from tkinter import messagebox

def add_task():
    task = entry.get()
    if task:
        listbox.insert(END, task)
        entry.delete(0, END)
    else:
        messagebox.showwarning("Warning", "Please enter a task.")

def delete_task():
    try:
        index = listbox.curselection()
        listbox.delete(index)
    except:
        messagebox.showwarning("Warning", "Please select a task.")

def clear_tasks():
    listbox.delete(0, END)

def main():
    global entry, listbox
    line = 0
    root = Tk()
    root.title("ToDo List")

    label = Label(root, text="Enter Task ^_^", font=("Arial", 12))
    label.pack(pady=10)

    # Create and pack the task entry widget
    entry = Entry(root, font=("Arial", 14))
    entry.pack(pady=10)

    # Create and pack the task listbox widget
    listbox = Listbox(root, selectmode=SINGLE,  font=("Arial", 12), width=50)
    listbox.pack(pady=10)

    # Create and pack the buttons
    button_frame = Frame(root)
    button_frame.pack(pady=10)

  
    add_button = Button( button_frame, activebackground='yellow', text="Add Task", font=("Arial", 12), command=add_task)
    add_button.grid(row=0, column=0, padx=5)

    delete_button = Button(button_frame,activebackground='yellow', text="Delete Task", font=("Arial", 12), command=delete_task)
    delete_button.grid(row=0, column=1, padx=5)

    clear_button = Button(button_frame, activebackground='yellow', text="Clear All", font=("Arial", 12), command=clear_tasks)
    clear_button.grid(row=0, column=2, padx=5)


    root.mainloop()

if __name__ == "__main__":
    main()
