#!/usr/bin/python3
"""gets employees data from api using requests"""

import requests
import sys

if __name__ == '__main__':
    id = sys.argv[1]
    todo_url = 'https://jsonplaceholder.typicode.com/todos?userId={}'.format(
        id)
    user_url = 'https://jsonplaceholder.typicode.com/users/{}'.format(id)

    todo = requests.get(todo_url)
    todo_json = todo.json()
    user_info = requests.get(user_url)
    user_json = user_info.json()

    completed_tasks = [task for task in todo_json if task['completed']]
    complete = len(completed_tasks)
    total_tasks = len(todo_json)
    username = user_json.get('username')

    print(
        f"Employee {username} is done with tasks({complete}/{total_tasks}):")
    for task in completed_tasks:
        print(f"\t {task['title']}")
