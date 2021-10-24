#!/usr/bin/python3
"""
Extend your Python script to export data in the CSV format.
"""
import csv
import requests
import sys

url = 'https://jsonplaceholder.typicode.com/users/{}/{}'
if __name__ == '__main__':
    _id = sys.argv[1]
    u = requests.get(url.format(_id, '')).json()
    todos = requests.get(url.format(_id, 'todos')).json()

    username = u.get('username')
    data = []
    for task in todos:
        data.append([_id, username, task.get('completed'), task.get('title')])

    filename = '{}.csv'.format(_id)
    with open(filename, 'w', encoding='utf-8') as f:
        writer = csv.writer(f, quoting=csv.QUOTE_ALL)
        writer.writerows(data)
