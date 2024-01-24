import sys
import json

from main import TaskApp

def quickadd(task_text):
    """
    - Adds a new task to the task list in the data/todo.json file.
    - Loads existing tasks, appends the new task, and saves back to the file.
    """
    try:
        with open('data/todo.json', 'r') as file:
            data = json.load(file)
    except FileNotFoundError:
        data = {'tasks': [], 'current_task': '', 'completed_tasks': []}

    # Append the new task to the tasks list
    data['tasks'].append(task_text)

    # Save the updated tasks back to the data/todo.json file
    with open('data/todo.json', 'w') as file:
        json.dump(data, file)

if __name__ == "__main__":
    # Check if there is a command line argument for the task
    if len(sys.argv) > 1:
        # Add each task provided as a command line argument
        for task in sys.argv[1:]:
            quickadd(task)
    else:
        # If no command line arguments, start the GUI app
        app = TaskApp()
        app.run()