#!/usr/bin/python3
"""script that fetches data from api and exlort in json file"""
import csv
import json
import requests
import sys

if __name__ == "__main__":
    user_url = 'https://jsonplaceholder.typicode.com/users/'
    user_info = requests.get(user_url)
    user_json = user_info.json()
    dictionary = {}

    for user in user_json:
        id = user['id']
        user_url = 'https://jsonplaceholder.typicode.com/users/{}'.format(id)
        todo = 'https://jsonplaceholder.typicode.com/todos?userId={}'.format(
            id)
        todo = requests.get(todo)
        todo_json = todo.json()
        user_info = requests.get(user_url)
        user_json = user_info.json()
        username = user_json.get('username')
        filename = 'todo_all_employees.json'
        json_list = []
        for task in todo_json:
            status = task['completed']
            title = task["title"]
            json_list.append({
                "username": "{}".format(username),
                "task": "{}".format(task['title']),
                "completed": "{}".format(task['completed'])})
            dictionary[str(id)] = json_list

            with open(filename, 'w') as jsonfile:
                json.dump(dictionary, jsonfile)
