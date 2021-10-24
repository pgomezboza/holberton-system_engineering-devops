#!/usr/bin/python3
"""
Script that, using this REST API, for a given employee ID,
returns information about his/her TODO list progress.
"""

import requests
import sys

url = 'https://jsonplaceholder.typicode.com/users/{}/{}'
if __name__ == '__main__':
    _id = sys.argv[1]
    user = requests.get(url.format(_id, '')).json()
    todos = requests.get(url.format(_id, 'todos')).json()

    name = user.get('name')
    tasks_completed = list(filter(lambda task: task.get('completed'), todos))
    print('Employee {} is done with tasks({}/{}):'
          .format(name, len(tasks_completed), len(todos)))
    for task in tasks_completed:
        print('\t {}'.format(task.get('title')))
