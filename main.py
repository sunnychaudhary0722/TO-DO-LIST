import tkinter as tk
from tkinter import ttk, messagebox
from datetime import datetime

def add_task():
    task_string = task_field.get()
    if len(task_string) == 0:
        messagebox.showinfo('Error', 'Field is Empty.')
    else:
        task_with_timestamp = f"{task_string} - {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}"
        tasks.append(task_with_timestamp)
        save_tasks_to_file()
        list_update()
        task_field.delete(0, 'end')

def list_update():
    clear_list()
    for task in tasks:
        task_listbox.insert('end', task)

def delete_task():
    try:
        the_value = task_listbox.get(task_listbox.curselection())
        if the_value in tasks:
            tasks.remove(the_value)
            save_tasks_to_file()
            list_update()
    except:
        messagebox.showinfo('Error', 'No Task Selected. Cannot Delete.')

def delete_all_tasks():
    message_box = messagebox.askyesno('Delete All', 'Are you sure?')
    if message_box == True:
        while(len(tasks) != 0):
            tasks.pop()
        save_tasks_to_file()
        list_update()

def clear_list():
    task_listbox.delete(0, 'end')

def close():
    save_tasks_to_file()
    print("Tasks saved to file.")
    print(tasks)
    guiWindow.destroy()

def save_tasks_to_file():
    try:
        with open("tasks.txt", "w") as file:
            for task in tasks:
                file.write(task + "\n")
        print("Tasks saved to file.")
    except Exception as e:
        print("Error saving tasks to file:", e)

def load_tasks_from_file():
    try:
        with open("tasks.txt", "r") as file:
            for line in file:
                tasks.append(line.strip())
    except FileNotFoundError:
        print("No previous tasks found.")
    except Exception as e:
        print("Error loading tasks from file:", e)

if __name__ == "__main__":
    guiWindow = tk.Tk()
    guiWindow.title("To-Do List Manager")
    guiWindow.geometry("400x300")

    tasks = []

    load_tasks_from_file()

    header_frame = tk.Frame(guiWindow)
    functions_frame = tk.Frame(guiWindow)
    listbox_frame = tk.Frame(guiWindow)

    header_frame.pack(fill="both")
    functions_frame.pack(side="left", expand=True, fill="both")
    listbox_frame.pack(side="right", expand=True, fill="both")

    header_label = ttk.Label(header_frame, text="To-Do List", font=("Arial", 24))
    header_label.pack(pady=10)

    task_label = ttk.Label(functions_frame, text="Enter the Task:")
    task_label.grid(row=0, column=0, padx=10, pady=5)

    task_field = ttk.Entry(functions_frame, font=("Arial", 12))
    task_field.grid(row=0, column=1, padx=10, pady=5)

    add_button = ttk.Button(functions_frame, text="Add Task", command=add_task)
    add_button.grid(row=1, column=0, columnspan=2, padx=10, pady=5, sticky="ew")

    del_button = ttk.Button(functions_frame, text="Delete Task", command=delete_task)
    del_button.grid(row=2, column=0, columnspan=2, padx=10, pady=5, sticky="ew")

    del_all_button = ttk.Button(functions_frame, text="Delete All Tasks", command=delete_all_tasks)
    del_all_button.grid(row=3, column=0, columnspan=2, padx=10, pady=5, sticky="ew")

    exit_button = ttk.Button(functions_frame, text="Exit", command=close)
    exit_button.grid(row=4, column=0, columnspan=2, padx=10, pady=5, sticky="ew")

    task_listbox = tk.Listbox(listbox_frame)
    task_listbox.pack(fill="both", expand=True, padx=10, pady=10)

    list_update()

    guiWindow.mainloop()

