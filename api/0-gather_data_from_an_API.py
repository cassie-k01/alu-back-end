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
        print("Error: Employee ID must be an integer")
        sys.exit(1)

    # API endpoints
    todos_url = "https://jsonplaceholder.typicode.com/todos"
    users_url = "https://jsonplaceholder.typicode.com/users"

    # Fetch data
    users_response = requests.get(users_url)
    todos_response = requests.get(todos_url)

    if users_response.status_code != 200 or todos_response.status_code != 200:
        print("Error: Could not retrieve data from API")
        sys.exit(1)

    users = users_response.json()
    todos = todos_response.json()

    # Find employee name
    employee_name = next(
        (user.get("name") for user in users if user.get("id") == employee_id),
        "Unknown"
    )

    # Filter tasks by employee
    employee_tasks = [task for task in todos if task.get("userId") == employee_id]
    done_tasks = [task.get("title") for task in employee_tasks if task.get("completed")]

    # Print results
    print(f"Employee {employee_name} is done with tasks({len(done_tasks)}/{len(employee_tasks)}):")
    for title in done_tasks:
        print(f"\t {title}")
