import tkinter as tk

tasks = []


def add_task():
    task = entry_task.get()
    if task:
        tasks.append(task)
        update_listbox()


def remove_task():
    selected_task = listbox_tasks.curselection()
    if selected_task:
        index = selected_task[0]
        tasks.pop(index)
        update_listbox()


def update_listbox():
    listbox_tasks.delete(0, tk.END)
    for task in tasks:
        listbox_tasks.insert(tk.END, task)


root = tk.Tk()

root.title("Задачи 2.0")

# Create input entry and buttons
entry_task = tk.Entry(root, bg='midnightblue', width=99)
entry_task.pack()

button_add = tk.Button(root, text="Добавить задачу", bg='white', fg='green', command=add_task)
button_add.pack()

button_remove = tk.Button(root, text="Удалить задачу", bg='white', fg='red', command=remove_task)
button_remove.pack()

listbox_tasks = tk.Listbox(root, background='dimgrey', height=50, width=100)
listbox_tasks.pack()

root.mainloop()

