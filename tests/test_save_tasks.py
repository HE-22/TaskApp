# FILEPATH: /Users/hassen/LocalDev/PYTHON_PROJECTS/Todo++/tests/test_task_app.py

import pytest
import json
from main import TaskApp
from unittest.mock import mock_open, patch

@pytest.fixture
def app():
    return TaskApp()

def test_save_tasks(app):
    # Mock data to be saved
    mock_data = {'tasks': ['task1', 'task2'], 'current_task': 'task1', 'completed_tasks': []}
    app.current_task_label.config(text='task1')
    for task in mock_data['tasks']:
        app.add_task(task)

    # Use mock_open to simulate file opening and writing
    m = mock_open()
    with patch('builtins.open', m, create=True):
        with patch('json.dump') as mock_json_dump:
            app.save_tasks()
            # Check if the file is opened in write mode
            m.assert_called_once_with('todo.json', 'w')
            # Check if the data is dumped correctly
            mock_json_dump.assert_called_once_with(mock_data, m())