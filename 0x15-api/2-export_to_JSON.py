#!/usr/bin/python3
"""script that fetches data from api and exlort in json file"""
import csv
import json
import requests
import sys

if __name__ == "__main__":
    id = sys.argv[1]
    todo_url = 'https://jsonplaceholder.typicode.com/todos?userId={}'.format(
        id)
    user_url = 'https://jsonplaceholder.typicode.com/users/{}'.format(id)

    todo = requests.get(todo_url)
    todo_json = todo.json()
    user_info = requests.get(user_url)
    user_json = user_info.json()

    username = user_json.get('name')
    filename = '{}.json'.format(id)
    json_list = []
    for task in todo_json:
        status = task['completed']
        title = task["title"]
        json_list.append({
            "task": "{}".format(task['title']),
            "completed": "{}".format(task['completed']),
            "username": "{}".format(username)})
        with open(filename, 'w') as jsonfile:
            json.dump({id: json_list}, jsonfile)
