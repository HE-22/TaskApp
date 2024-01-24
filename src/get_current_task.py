import json

def get_current_task(json_file_path):
    """
    Return the value of the current task from the specified todo.json file.

    Args:
    - json_file_path: The file path to the todo.json file.

    Returns:
    - The current task as a string, or an empty string if not found or on error.
    """
    try:
        with open(json_file_path, 'r') as file:
            data = json.load(file)
            return data.get('current_task', '')  # Return the current task if it exists, otherwise return an empty string
    except FileNotFoundError:
        print("The todo.json file was not found.")
        return ''
    except json.decoder.JSONDecodeError:
        print("Error decoding JSON from the todo.json file.")
        return ''

# Example usage:
if __name__ == "__main__":
    current_task = get_current_task('/Users/hassen/LocalDev/PYTHON_PROJECTS/Todo++/data/todo.json')
    print(current_task)