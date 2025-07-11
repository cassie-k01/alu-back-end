#!/usr/bin/python3
"""Fetches a user's todo list from an API and exports it to a JSON file."""

import json
import requests
import sys


def main():
    """Main function"""
    # Validate user input
    if len(sys.argv) != 2:
        print("Usage: python3 1-export_to_JSON.py <user_id>")
        sys.exit(1)

    try:
        user_id = int(sys.argv[1])
    except ValueError:
        print("User ID must be an integer.")
        sys.exit(1)

    # Define endpoints
    todo_url = "https://jsonplaceholder.typicode.com/todos"
    user_url = f"https://jsonplaceholder.typicode.com/users/{user_id}"

    try:
        todos = requests.get(todo_url).json()
        user_info = requests.get(user_url).json()
    except requests.exceptions.RequestException as e:
        print(f"Failed to fetch data: {e}")
        sys.exit(1)

    # Extract username
    user_name = user_info.get("username", "Unknown")

    # Filter tasks for the user
    tasks = [
        {
            "task": todo.get("title"),
            "completed": todo.get("completed"),
            "username": user_name,
        }
        for todo in todos if todo.get("userId") == user_id
    ]

    output = {str(user_id): tasks}

    # Export to JSON file
    file_name = f"{user_id}.json"
    try:
        with open(file_name, "w") as file:
            json.dump(output, file)
        print(f"Exported {len(tasks)} tasks for user '{user_name}' to {file_name}")
    except IOError as e:
        print(f"File write error: {e}")

if __name__ == "__main__":
    main()
