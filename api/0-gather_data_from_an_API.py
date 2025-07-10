#!/usr/bin/python3
import requests
import sys
if __name__ == "__main__":

    # Check if the user gave us an employee ID when starting the script
    if len(sys.argv) < 2:
        print("Usage: python api/your_script.py <employee_id>")  # Help message for the user
        sys.exit(1)  # Stop the script because we can't continue without an ID

    # Check if the given employee ID is actually a number
    if not sys.argv[1].isdigit():
        print("Error: Employee ID must be a number.")  # Tell the user they made a mistake
        sys.exit(1)  # Stop the script again

    # Turn the employee ID into a real number (it started as text)
    emp_id = int(sys.argv[1])

    # This is the website where we're getting employee and task data from
    base_url = "https://jsonplaceholder.typicode.com"

    # Ask the website for information about the employee
    user_response = requests.get(f"{base_url}/users/{emp_id}")

    # Ask the website for that employee's tasks (to-do list)
    todos_response = requests.get(f"{base_url}/todos?userId={emp_id}")

    # Grab the employee's name from the info we got back
    employee_name = user_response.json().get("name")

    # Turn the list of tasks we got into a format Python can easily work with
    todos = todos_response.json()

    # Count how many total tasks there are for this employee
    total_tasks = len(todos)

    # Make a list of only the tasks that are marked as "completed"
    done_tasks = [task for task in todos if task.get("completed")]

    # Print out how many tasks the employee has finished
    print(f"Employee {employee_name} is done with tasks({len(done_tasks)}/{total_tasks}):")

    # Go through each completed task and print its title
    for task in done_tasks:
        print(f"\t {task.get('title')}")