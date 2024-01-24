import tkinter as tk

class TaskApp:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title('Task Prioritization System')

        # Center the window on the screen
        window_width = self.window.winfo_reqwidth()
        window_height = self.window.winfo_reqheight()
        position_right = int(self.window.winfo_screenwidth()/2 - window_width/2)
        position_down = int(self.window.winfo_screenheight()/2 - window_height/2)
        self.window.geometry("+{}+{}".format(position_right, position_down))

        self.header_label = tk.Label(self.window, text='Main Task', font=('Helvetica', 20, 'bold'))
        self.header_label.pack()

        self.tasks_frame = tk.Frame(self.window)
        self.tasks_frame.pack(fill='both', expand=True)

        self.task_entry = tk.Entry(self.window)
        self.task_entry.pack(side='bottom', fill='x', padx=10)
        self.task_entry.bind('<Return>', self.add_task)
        self.task_entry.focus_set()  # Automatically focus cursor onto the text box

    def create_task(self, label):
        def move_task_to_top(event=None):
            # Move the label to the top of the tasks_frame
            label.lift()
            # Reorder all tasks to maintain the current order except for the one clicked
            label.pack_forget()
            label.pack(fill='x', pady=2, padx=10, anchor='n')
            label.config(font=('Helvetica', 10, 'bold'))
            # Move the clicked task to the top of the list
            self.tasks_frame.pack_propagate(False)  # Prevent the frame from resizing
            for task in self.tasks_frame.winfo_children():
                if task != label:
                    task.pack_forget()
            for task in self.tasks_frame.winfo_children():
                if task != label:
                    task.pack(fill='x', pady=2, padx=10, anchor='n')
                    task.config(font=('Helvetica', 10, 'normal'))
        label.bind('<Button-1>', move_task_to_top)
        move_task_to_top()

    def add_task(self, event=None):
        task_text = self.task_entry.get()
        if task_text.strip():
            label = tk.Label(self.tasks_frame, text=task_text, font=('Helvetica', 10, 'normal'), bg='white')
            label.pack(fill='x', pady=2, padx=10, anchor='n')
            self.create_task(label)
            self.task_entry.delete(0, tk.END)

    def run(self):
        self.window.mainloop()

if __name__ == "__main__":
    app = TaskApp()
    app.run()
