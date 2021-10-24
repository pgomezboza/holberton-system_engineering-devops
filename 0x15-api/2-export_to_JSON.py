#!/usr/bin/python3
"""
Extend your Python script to export data in the JSON format.
"""
import json
import requests
import sys

url = 'https://jsonplaceholder.typicode.com/users/{}/{}'
if __name__ == '__main__':
    _id = sys.argv[1]
    u = requests.get(url.format(_id, '')).json()
    todos = requests.get(url.format(_id, 'todos')).json()

    user = {_id: []}
    for t in todos:
        task = {'task': t.get('title'),
                'completed': t.get('completed'),
                'username': u.get('username')}
        user[_id].append(task)

    filename = '{}.json'.format(u['id'])
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(user, f)
