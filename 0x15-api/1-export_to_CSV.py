#!/usr/bin/python3
"""script that fetches data from api"""
import csv
import requests
import sys

if __name__ == "__main__":
    id = sys.argv[1]
    user_url = 'https://jsonplaceholder.typicode.com/users/{}'.format(id)
    todo_url = user_url + '/todos'

    todo = requests.get(todo_url)
    todo_json = todo.json()
    user_info = requests.get(user_url)
    user_json = user_info.json()

    username = user_json.get('name')
    filename = "{}.csv".format(id)
    with open(filename, 'w', newline='') as csvfile:
        for task in todo_json:
            status = task['completed']
            title = task["title"]
            csvfile.write(
                '"{}","{}","{}","{}"\n'.format(
                    id, username, status, title))
