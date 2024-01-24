#!/bin/bash

echo "tkinter" > requirements.txt

cat <<EOT > main.py
import tkinter as tk

def create_task(label):
    def move_task_to_top(event):
        tasks_frame.lift(label)
        label.config(font=('Helvetica', 10, 'bold'))
        for task in tasks_frame.winfo_children():
            if task != label:
                task.config(font=('Helvetica', 10, 'normal'))
    label.bind('<Button-1>', move_task_to_top)

def add_task():
    task_text = task_entry.get()
    if task_text.strip():
        label = tk.Label(tasks_frame, text=task_text, font=('Helvetica', 10, 'normal'), bg='white')
        label.pack(fill='x', pady=2, padx=10, anchor='n')
        create_task(label)
        task_entry.delete(0, tk.END)

window = tk.Tk()
window.title('Task Prioritization System')

header_label = tk.Label(window, text='Main Task', font=('Helvetica', 20, 'bold'))
header_label.pack()

tasks_frame = tk.Frame(window)
tasks_frame.pack(fill='both', expand=True)

task_entry = tk.Entry(window)
task_entry.pack(side='bottom', fill='x', padx=10)

task_button = tk.Button(window, text='Submit', command=add_task)
task_button.pack(side='bottom')

window.mainloop()
EOT
