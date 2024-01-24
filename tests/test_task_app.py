import pytest
import json
from src.main import TaskApp
from unittest.mock import mock_open, patch

@pytest.fixture
def app():
    return TaskApp()

def test_load_tasks_with_valid_data(app):
    # Mock data to be loaded
    mock_data = {'tasks': ['task1', 'task2'], 'current_task': 'task1'}
    # Use mock_open to simulate file opening and reading
    with patch('builtins.open', mock_open(read_data=json.dumps(mock_data))):
        with patch('json.load', return_value=mock_data):
            app.load_tasks()
            # Check if the current task label is set correctly
            assert app.current_task_label.cget("text") == 'task1'
            # Check if the tasks are loaded correctly
            assert len(app.tasks_frame.winfo_children()) == len(mock_data['tasks'])

# def test_load_tasks_with_no_file(app):
#     with patch('builtins.open', side_effect=FileNotFoundError):
#         app.load_tasks()
#         # Check if the current task label is empty
#         assert app.current_task_label.cget("text") == ''
#         # Check if no tasks are loaded
#         assert len(app.tasks_frame.winfo_children()) == 0