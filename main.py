import tkinter as tk

class TaskApp:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title('Task Prioritization System')

        # Center the window on the screen
        self.window.geometry('300x500')  # Set the window width to 300 and height to 500
        self.window.update_idletasks()  # Update the window to get correct dimensions
        window_width = self.window.winfo_width()
        window_height = self.window.winfo_height()
        position_right = int(self.window.winfo_screenwidth()/2 - window_width/2)
        position_down = int(self.window.winfo_screenheight()/2 - window_height/2)
        self.window.geometry("+{}+{}".format(position_right, position_down))
        self.window.update_idletasks()  # Update the window to get correct dimensions

        self.header_label = tk.Label(self.window, text='Main Task', font=('Helvetica', 20, 'bold'))
        self.header_label.pack()

        self.main_task_frame = tk.Frame(self.window)
        self.main_task_frame.pack(fill='both', expand=True)

        self.current_task_label = tk.Label(self.main_task_frame, text='', font=('Helvetica', 20, 'bold'))
        self.current_task_label.pack(fill='x', pady=2, padx=10, anchor='n')

        self.spacer_label = tk.Label(self.window, text='', font=('Helvetica', 20, 'bold'))
        self.spacer_label.pack()

        self.tasks_frame = tk.Frame(self.window)
        self.tasks_frame.pack(fill='both', expand=True)

        self.task_entry = tk.Entry(self.window)
        self.task_entry.pack(side='bottom', fill='x', padx=10)
        self.task_entry.bind('<Return>', self.add_task)
        self.task_entry.focus_set()  # Automatically focus cursor onto the text box

    def create_task(self, label):
        def move_task_to_top(event=None):
            # Clear the current task label and update it with the clicked task's text
            self.current_task_label.config(text=label.cget("text"))
            # Remove the clicked task from the tasks_frame
            label.destroy()
        label.bind('<Button-1>', move_task_to_top)

    def add_task(self, event=None):
        """
        - Adds a new task to the task list.
        - Places the new task below the 'Main Task' and above other tasks.
        - Clears the task entry field after adding the task.
        """
        task_text = self.task_entry.get()
        if task_text.strip():
            label = tk.Label(self.tasks_frame, text=task_text, font=('Helvetica', 10, 'normal'), bg='white')
            # If there is no 'Main Task', just pack the new task normally
            label.pack(fill='x', pady=2, padx=10, anchor='n')
            self.create_task(label)
            self.task_entry.delete(0, tk.END)
    ...

    def run(self):
        self.window.mainloop()

if __name__ == "__main__":
    app = TaskApp()
    app.run()
