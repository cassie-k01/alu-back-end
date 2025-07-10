
#!/usr/bin/python3
"""
Script to retrieve TODO list progress for a given employee from a REST API.
Usage: python 0-gather_data_from_an_API.py <employee_id>
Outputs the employee’s name, task completion stats, and titles of completed tasks.
"""
import requests
import sys
if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python api/your_script.py <employee_id>")
        sys.exit(1)  
    if not sys.argv[1].isdigit():
        print("Error: Employee ID must be a number.")
        sys.exit(1) 
    emp_id = int(sys.argv[1])
    base_url = "https://jsonplaceholder.typicode.com"
    user_response = requests.get(f"{base_url}/users/{emp_id}")
    todos_response = requests.get(f"{base_url}/todos?userId={emp_id}")
    employee_name = user_response.json().get("name")
    todos = todos_response.json()
    total_tasks = len(todos)
    done_tasks = [task for task in todos if task.get("completed")]
    print(f"Employee {employee_name} is done with tasks({len(done_tasks)}/{total_tasks}):")
    print("Completed tasks:")
    for task in done_tasks:
        print(f"\t {task.get('title')}")