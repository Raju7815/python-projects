import tkinter as tk
from tkinter import messagebox
import json
import os

# Defining the file where tasks will be saved
TASKS_FILE = 'tasks.json'

# Loading tasks from file
def load_tasks():
    if os.path.exists(TASKS_FILE):
        with open(TASKS_FILE, 'r') as file:
            return json.load(file)
    return []

# Saves tasks to file
def save_tasks(tasks):
    with open(TASKS_FILE, 'w') as file:
        json.dump(tasks, file, indent=4)

# Adds a new task
def add_task():
    description = entry_task.get()
    if description:
        tasks.append({'description': description, 'completed': False})
        save_tasks(tasks)
        update_task_list()
        entry_task.delete(0, tk.END)
    else:
        messagebox.showwarning("Warning", "Task description cannot be empty.")

# Completes a task
def complete_task(index):
    if 0 <= index < len(tasks):
        tasks[index]['completed'] = True
        save_tasks(tasks)
        update_task_list()
    else:
        messagebox.showwarning("Warning", "Invalid task number.")

# Updates the task list in the GUI
def update_task_list():
    listbox_tasks.delete(0, tk.END)
    for i, task in enumerate(tasks):
        status = '✓' if task['completed'] else '✗'
        listbox_tasks.insert(tk.END, f"{i + 1}. {task['description']} [{status}]")

# Marks the selected task as completed
def mark_task_completed():
    try:
        index = listbox_tasks.curselection()[0]
        complete_task(index)
    except IndexError:
        messagebox.showwarning("Warning", "No task selected.")

# Set up the GUI
root = tk.Tk()
root.title("To-Do List")

# Entry for new tasks
entry_task = tk.Entry(root, width=40)
entry_task.pack(pady=10)

# Button to add new tasks
button_add_task = tk.Button(root, text="Add Task", command=add_task)
button_add_task.pack(pady=5)

# Listbox to display tasks
listbox_tasks = tk.Listbox(root, width=50, height=15)
listbox_tasks.pack(pady=10)

# Button to mark task as completed
button_complete_task = tk.Button(root, text="Complete Task", command=mark_task_completed)
button_complete_task.pack(pady=5)

# Initialize tasks and update the GUI
tasks = load_tasks()
update_task_list()

root.mainloop()