import threading
import tkinter as tk
import json
import pygame

from config import COMPLETE_TASK_SFX_PATH

class TaskApp:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title('')

        # Center the window on the screen
        window_width = 350
        window_height = 500
        screen_width = self.window.winfo_screenwidth()
        screen_height = self.window.winfo_screenheight()
        position_right = int(screen_width / 2 - window_width / 2)
        position_down = int(screen_height / 2 - window_height / 2)
        self.window.geometry(f'{window_width}x{window_height}+{position_right}+{position_down}')

        self.main_task_frame = tk.Frame(self.window)
        self.main_task_frame.pack(fill='both', expand=True)

        self.current_task_label = tk.Label(self.main_task_frame, text='', font=('San Francisco', 20, 'bold'), wraplength=window_width)
        self.current_task_label.pack(fill='x', pady=2, padx=10, anchor='n')

        self.spacer_label = tk.Label(self.window, text='', font=('San Francisco', 20, 'bold'))
        self.spacer_label.pack()

        self.tasks_frame = tk.Frame(self.window)
        self.tasks_frame.pack(fill='both', expand=True)

        # Task entry box with rounded edges
        self.task_entry = tk.Entry(self.window, font=('San Francisco', 15), bd=1, relief='solid', highlightthickness=2, highlightbackground="grey", highlightcolor="grey")
        self.task_entry.pack(side='bottom', fill='x', padx=10, pady=10)
        self.task_entry.bind('<Return>', self.add_task)
        self.task_entry.focus_set()
        # Apply rounded edges style to the task entry box
        self.task_entry.configure(highlightthickness=1, highlightbackground="#D3D3D3", highlightcolor="#D3D3D3", relief='solid')

        self.load_tasks()

        # Bind Command + R to refresh the UI
        self.window.bind('<Command-r>', self.refresh_ui)
        # Bind Command + D to complete the current task
        self.window.bind('<Command-d>', self.complete_task)
        # Bind Command + minus to clear all tasks
        self.window.bind('<Command-minus>', self.clear_all_tasks)

    def create_task(self, label):
        def swap_task_with_main(event=None):
            # Swap the clicked task with the current main task
            current_task = self.current_task_label.cget("text")
            clicked_task = label.cget("text")
            if current_task:
                label.config(text=current_task)
            else:
                label.destroy()
            self.current_task_label.config(text=clicked_task)
            self.save_tasks()
        label.bind('<Button-1>', swap_task_with_main)

    def complete_task(self, event=None):
        """Move the current main task to the completed tasks list."""
        current_task = self.current_task_label.cget("text").strip()  # Ensure no whitespace
        if current_task:  # Check if there is a current task
            self.completed_tasks.append(current_task)  # Add it to the completed tasks list
            self.current_task_label.config(text='')  # Clear the current task label
            self.save_tasks()  # Save the updated tasks
            self.play_completion_sound()  # Play the task completion sound

    def clear_all_tasks(self, event=None):
        """Clear all tasks without saving them to the completed tasks list."""
        self.current_task_label.config(text='')  # Clear the current task label
        for widget in self.tasks_frame.winfo_children():
            widget.destroy()  # Destroy each task widget
        self.save_tasks()  # Save the updated tasks

    def play_completion_sound(self):
        """Play the task completion sound using pygame to avoid blocking."""
        try:
            pygame.mixer.init()
            pygame.mixer.music.load(COMPLETE_TASK_SFX_PATH)
            pygame.mixer.music.play()
        except Exception as e:
            print(f"Error playing sound: {e}")

    def load_tasks(self):
        """Load tasks from a JSON file."""
        try:
            with open('data/todo.json', 'r') as file:
                data = json.load(file)
                # Check if data is a dictionary with expected keys
                if isinstance(data, dict) and 'tasks' in data and 'current_task' in data:
                    tasks = data['tasks']
                    current_task = data['current_task']
                    # Load completed tasks if they exist in the file
                    self.completed_tasks = data.get('completed_tasks', [])
                else:
                    # If data is not in the expected format, treat it as a list of tasks
                    tasks = data
                    current_task = ""
                    self.completed_tasks = []
                
                # Clear the tasks_frame before loading new tasks
                for widget in self.tasks_frame.winfo_children():
                    widget.destroy()
                
                # Add tasks from the loaded data
                for task_text in tasks:
                    self.add_task_from_load(task_text)
                
                # Update the current task label
                if current_task:
                    self.current_task_label.config(text=current_task)
        except FileNotFoundError:
            pass  # No tasks to load

    def save_tasks(self):
        """Save tasks to a JSON file."""
        tasks = [label.cget("text") for label in self.tasks_frame.winfo_children()]
        current_task = self.current_task_label.cget("text")
        
        with open('data/todo.json', 'w') as file:
            json.dump({
                'tasks': tasks,
                'current_task': current_task,
                'completed_tasks': self.completed_tasks  # Save the completed tasks list
            }, file)

    def add_task_from_load(self, task_text):
        """Add a task from the loaded data without saving."""
        label = tk.Label(self.tasks_frame, text=task_text, font=('San Francisco', 15, 'normal'), bg='#585454', fg='white')
        label.pack(fill='x', pady=2, padx=10, anchor='n')
        self.create_task(label)

    def add_task(self, event=None):
        """
        - Adds a new task to the task list.
        - Places the new task below the 'Main Task' and above other tasks.
        - Clears the task entry field after adding the task.
        """
        task_text = self.task_entry.get()
        if task_text.strip():
            label = tk.Label(self.tasks_frame, text=task_text, font=('San Francisco', 15, 'normal'), bg='white', fg='black')
            # If there is no 'Main Task', just pack the new task normally
            label.pack(fill='x', pady=2, padx=10, anchor='n')
            self.create_task(label)
            self.task_entry.delete(0, tk.END)
            self.save_tasks()

    def refresh_ui(self, event=None):
        """
        - Clears the current tasks displayed in the UI.
        - Reloads tasks from the todo.json file.
        - Redraws the UI with the updated tasks.
        """
        # Clear the current tasks displayed in the tasks_frame
        for widget in self.tasks_frame.winfo_children():
            widget.destroy()
        
        # Reload the tasks from the todo.json file
        self.load_tasks()

    def run(self):
        self.window.mainloop()

if __name__ == "__main__":
    app = TaskApp()
    app.run()
