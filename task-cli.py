import sys
import json
import os
from datetime import datetime

TASKS_FILE = "tasks.json"

def load_tasks():
    if not os.path.exists(TASKS_FILE):
        return []
    with open(TASKS_FILE, 'r') as f:
        try:
            return json.load(f)
        except json.JSONDecodeError:
            return []

def save_tasks(tasks):
    with open(TASKS_FILE, 'w') as f:
        json.dump(tasks, f, indent=2)

def add_task(description):
    tasks = load_tasks()
    new_id = max([task['id'] for task in tasks], default=0) + 1
    now = datetime.now().isoformat()
    new_task = {
        'id': new_id,
        'description': description,
        'status': 'todo',
        'createdAt': now,
        'updatedAt': now
    }
    tasks.append(new_task)
    save_tasks(tasks)
    print(f"Task added successfully (ID: {new_id})")

def update_task(task_id, new_description):
    tasks = load_tasks()
    for task in tasks:
        if task['id'] == task_id:
            task['description'] = new_description
            task['updatedAt'] = datetime.now().isoformat()
            save_tasks(tasks)
            print(f"Task {task_id} updated successfully")
            return
    print(f"Task {task_id} not found")

def delete_task(task_id):
    tasks = load_tasks()
    for i, task in enumerate(tasks):
        if task['id'] == task_id:
            del tasks[i]
            save_tasks(tasks)
            print(f"Task {task_id} deleted successfully")
            return
    print(f"Task {task_id} not found")

def mark_task(task_id, status):
    valid_statuses = ['todo', 'in-progress', 'done']
    if status not in valid_statuses:
        print(f"Invalid status. Must be one of: {', '.join(valid_statuses)}")
        return
    
    tasks = load_tasks()
    for task in tasks:
        if task['id'] == task_id:
            task['status'] = status
            task['updatedAt'] = datetime.now().isoformat()
            save_tasks(tasks)
            print(f"Task {task_id} marked as {status}")
            return
    print(f"Task {task_id} not found")

def list_tasks(status_filter=None):
    tasks = load_tasks()
    
    if status_filter:
        valid_statuses = ['todo', 'in-progress', 'done']
        if status_filter not in valid_statuses:
            print(f"Invalid status filter. Must be one of: {', '.join(valid_statuses)}")
            return
        
        filtered_tasks = [task for task in tasks if task['status'] == status_filter]
        if not filtered_tasks:
            print(f"No tasks with status '{status_filter}'")
            return
        tasks = filtered_tasks
    
    if not tasks:
        print("No tasks found")
        return
    
    print("\nTask List:")
    for task in tasks:
        print(f"ID: {task['id']}")
        print(f"Description: {task['description']}")
        print(f"Status: {task['status']}")
        print(f"Created: {task['createdAt']}")
        print(f"Updated: {task['updatedAt']}")
        print("-" * 30)

def print_usage():
    print("""Usage:
    task-cli add "Task description"          - Add a new task
    task-cli update <id> "New description"   - Update a task
    task-cli delete <id>                     - Delete a task
    task-cli mark-in-progress <id>           - Mark task as in-progress
    task-cli mark-done <id>                  - Mark task as done
    task-cli list                           - List all tasks
    task-cli list todo                      - List todo tasks
    task-cli list in-progress               - List in-progress tasks
    task-cli list done                      - List done tasks
    """)

def main():
    if len(sys.argv) < 2:
        print_usage()
        return
    
    command = sys.argv[1].lower()
    
    try:
        if command == "add":
            if len(sys.argv) < 3:
                print("Error: Missing task description")
                return
            description = sys.argv[2]
            add_task(description)
        
        elif command == "update":
            if len(sys.argv) < 4:
                print("Error: Missing task ID or new description")
                return
            task_id = int(sys.argv[2])
            new_description = sys.argv[3]
            update_task(task_id, new_description)
        
        elif command == "delete":
            if len(sys.argv) < 3:
                print("Error: Missing task ID")
                return
            task_id = int(sys.argv[2])
            delete_task(task_id)
        
        elif command == "mark-in-progress":
            if len(sys.argv) < 3:
                print("Error: Missing task ID")
                return
            task_id = int(sys.argv[2])
            mark_task(task_id, 'in-progress')
        
        elif command == "mark-done":
            if len(sys.argv) < 3:
                print("Error: Missing task ID")
                return
            task_id = int(sys.argv[2])
            mark_task(task_id, 'done')
        
        elif command == "list":
            if len(sys.argv) > 2:
                status_filter = sys.argv[2].lower()
                list_tasks(status_filter)
            else:
                list_tasks()
        
        else:
            print(f"Unknown command: {command}")
            print_usage()
    
    except ValueError:
        print("Error: Task ID must be a number")
    except Exception as e:
        print(f"An error occurred: {str(e)}")

if __name__ == "__main__":
    main()