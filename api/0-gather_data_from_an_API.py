#!/usr/bin/python3
"""Script to get todos for a user from API"""

import requests
import sys


def main():
    """Main function to retrieve user task data"""
    if len(sys.argv) < 2:
        print("Usage: python3 1-export_to_CSV.py <user_id>")
        sys.exit(1)

    user_id = int(sys.argv[1])
    todo_url = "https://jsonplaceholder.typicode.com/todos"
    user_url = f"https://jsonplaceholder.typicode.com/users/{user_id}"

    try:
        todos = requests.get(todo_url).json()
        user_info = requests.get(user_url).json()
    except requests.exceptions.RequestException as e:
        print(f"Error fetching data: {e}")
        sys.exit(1)

    employee_name = user_info.get("name")
    completed_tasks = [todo["title"] for todo in todos
                       if todo["userId"] == user_id and todo["completed"]]
    total_tasks = len([todo for todo in todos if todo["userId"] == user_id])

    print(f"Employee Name: {employee_name}")
    print(f"To Do Count: {len(completed_tasks)}/{total_tasks}")

    for i, task in enumerate(completed_tasks, 1):
        print(f"Task {i}: {task}")

if __name__ == '__main__':
    main()
