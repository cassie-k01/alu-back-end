#!/usr/bin/python3
"""
Script to retrieve TODO list progress for a given employee from a REST API.
Usage: python 0-gather_data_from_an_API.py <employee_id>
Outputs the employee’s name, task completion stats, and titles of completed tasks.
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

    # API URLs
    user_url = f"https://jsonplaceholder.typicode.com/users/{employee_id}"
    todos_url = f"https://jsonplaceholder.typicode.com/todos?userId={employee_id}"

    # Request employee data
    user_response = requests.get(user_url)
    if user_response.status_code != 200:
        print("Error: Employee not found.")
        sys.exit(1)

    employee_name = user_response.json().get("name", "Unknown").strip()

    # Request tasks
    todos_response = requests.get(todos_url)
    todos = todos_response.json()

    # Process tasks
    done_tasks = [task for task in todos if task.get("completed")]
    total_tasks = len(todos)

    # Output result
    print(f"Employee {employee_name} is done with tasks({len(done_tasks)}/{total_tasks}):")
    for task in done_tasks:
        print(f"\t {task.get('title')}")
