#!/usr/bin/python3
"""
This script retrieves and displays information about a given employee's TODO list progress using a REST API.
"""

import requests
import sys


def get_employee_todo_progress(employee_id):
    """
    Returns a progress report for a given employee's TODO list.

    :param employee_id: The ID of the employee
    :type employee_id: int
    """
    # Fetch employee data
    employee_response = requests.get(f"https://jsonplaceholder.typicode.com/users/{employee_id}")
    employee_data = employee_response.json()
    employee_name = employee_data['name']

    # Fetch employee's todo list
    todo_response = requests.get(f"https://jsonplaceholder.typicode.com/users/{employee_id}/todos")
    todo_data = todo_response.json()

    # Calculate completed and total number of tasks
    completed_tasks = [task for task in todo_data if task.get('completed')]
    num_completed_tasks = len(completed_tasks)
    num_total_tasks = len(todo_data)

    # Print progress report
    print(f"Employee {employee_name} is done with tasks({num_completed_tasks}/{num_total_tasks}):")
    for task in completed_tasks:
        print(f"\t{task.get('title')}")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 todo_progress.py <employee_id>")
        sys.exit(1)

    employee_id = int(sys.argv[1])
    get_employee_todo_progress(employee_id)
