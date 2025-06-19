# Task Tracker CLI

Task Tracker CLI is a simple command-line tool for managing your tasks. It allows you to add, update, delete and list tasks with statuses such as "todo", "in-progress" and "done". Tasks are stored in a JSON file named `tasks.json` in the current directory.

## How to Use

1. Save the code to a file named `task-cli.py`.

2. **For Windows:**
   - Run the script using Python:

     ```bash
     python task-cli [command] [arguments]
     ```

   - Or, if `.py` files are associated with Python:

     ```bash
     task-cli.py [command] [arguments]
     ```

3. **For Unix-like systems (Linux, macOS):**
   - Make the script executable:

     ```bash
     chmod +x task-cli.py
     ```

   - Run the script directly:

     ```bash
     ./task-cli.py [command] [arguments]
     ```

   - Or run it with Python:

     ```bash
     python task-cli.py [command] [arguments]
     ```

## Available Commands

- **Add a new task**:

  ```bash
  python task-cli.py add "Buy groceries"
  ```

- **Update a task**:

  ```bash
  python task-cli.py update 1 "Buy groceries and cook dinner"
  ```

- **Delete a task**:

  ```bash
  python task-cli.py delete 1
  ```

- **Mark a task as in progress or done**:

  ```bash
  python task-cli.py mark-in-progress 1
  python task-cli.py mark-done 1
  ```

- **List all tasks**:

  ```bash
  python task-cli.py list
  ```

- **List tasks by status**:

  ```bash
  python task-cli.py list todo
  python task-cli.py list in-progress
  python task-cli.py list done
  ```

## Features

- **File Storage**: Uses a JSON file (`tasks.json`) to store tasks.
- **Task Management**:
  - Add new tasks with descriptions.
  - Update task descriptions.
  - Delete tasks.
  - Mark tasks as "todo", "in-progress", or "done".
- **Task Listing**:
  - List all tasks.
  - Filter tasks by status ("todo", "in-progress", "done").
- **Task Properties**:
  - Unique ID
  - Description
  - Status
  - Creation timestamp
  - Last update timestamp
- **Error Handling**:
  - Invalid commands
  - Missing arguments
  - Invalid task IDs
  - File operations

## Implementation Notes

- Uses Python's built-in `json` module for file operations.
- No external dependencies required.
- Simple command-line interface with positional arguments.
- Comprehensive error handling.
- Automatically creates the `tasks.json` file if it doesn't exist.
