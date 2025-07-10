#!/usr/bin/python3
"""
Module: 0-gather_data_from_an_API

This script retrieves TODO list progress for a specific employee
from the JSONPlaceholder API.

It displays the employee's name, number of completed tasks,
total tasks, and the titles of completed tasks.

Usage:
    python3 0-gather_data_from_an_API.py <employee_id>

Dependencies:
    - requests
    - sys
"""

import requests
import sys

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 0-gather_data_from_an_API.py <employee_id>")
        sys.exit(1)

    try:
        employee_id = int(sys.argv[1])
    except ValueError:
        print("Error: Employee ID must be an integer.")
        sys.exit(1)

    users_url = "https://jsonplaceholder.typicode.com/users"
    todos_url = "https://jsonplaceholder.typicode.com/todos"

    user_response = requests.get(users_url)
    todo_response = requests.get(todos_url)

    if user_response.status_code != 200 or todo_response.status_code != 200:
        print("Error: Failed to fetch data from API.")
        sys.exit(1)

    users = user_response.json()
    todos = todo_response.json()

    employee_name = next(
        (user.get("name") for user in users if user.get("id") == employee_id),
        None
    )

    if not employee_name:
        print("Error: Employee not found.")
        sys.exit(1)

    employee_tasks = [task for task in todos if task.get("userId") == employee_id]
    completed_tasks = [task.get("title") for task in employee_tasks if task.get("completed")]

    print(f"Employee {employee_name} is done with tasks({len(completed_tasks)}/{len(employee_tasks)}):")
    for title in completed_tasks:
        print(f"\t {title}")