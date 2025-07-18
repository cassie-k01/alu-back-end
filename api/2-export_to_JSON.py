#!/usr/bin/python3
"""Fetches a user's todo list from an API and exports it to a JSON file."""

import json
import requests
import sys


def main():
    """main function"""
    user_id = int(sys.argv[1])
    todo_url = 'https://jsonplaceholder.typicode.com/todos'
    user_url = 'https://jsonplaceholder.typicode.com/users/{}'.format(user_id)

    response = requests.get(todo_url)
    user_name = requests.get(user_url).json().get('username')
    user_data = []
    output = {user_id: user_data}

    for todo in response.json():
        if todo.get('userId') == user_id:
            user_data.append(
                {
                    "task": todo.get('title'),
                    "completed": todo.get('completed'),
                    "username": user_name,
                })
    print(output)
    file_name = "{}.json".format(user_id)
    with open(file_name, 'w') as file:
        json.dump(output, file)


if __name__ == '__main__':
    main()
