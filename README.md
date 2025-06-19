# Task Tracker CLI

Task Tracker CLI is a simple command-line application for managing your tasks. It allows you to add, update, delete, and list tasks with statuses such as "todo", "in-progress", and "done". Additional features include setting task priorities, due dates, and notes, as well as sorting and clearing tasks. Tasks are stored in a JSON file named `tasks.json` in the current directory. This is a solution for the [Task Tracker](https://github.com/techgirldiaries/task-tracker-cli) challenge from [Roadmap.sh](https://roadmap.sh/projects/task-tracker).

## How to Use

If you wish to clone the repository, run:

```bash
git clone https://github.com/techgirldiaries/task-tracker-cli.git
cd task-tracker-cli
```

Alternatively, you can save the code directly to a file named `task-cli.py`.

1. **Save the code** to a file named `task-cli.py`.

2. **For Unix-like systems (Linux, macOS)**:
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

3. **For Windows**:
   - Run the script using Python:

     ```bash
     python task-cli.py [command] [arguments]
     ```

   - Or, if `.py` files are associated with Python:

     ```bash
     task-cli.py [command] [arguments]
     ```

## Available Commands

- **Add a new task** (with optional priority, due date, and notes):

  ```bash
  python task-cli.py add "Buy groceries" high 2025-06-30 "Get milk and eggs"
  ```

- **Update a task** (update description, priority, due date, or notes):

  ```bash
  python task-cli.py update 1 "Buy groceries and cook dinner" medium 2025-07-01 "Include dessert"
  ```

- **Delete a task**:

  ```bash
  python task-cli.py delete 1
  ```

- **Clear all tasks** (requires confirmation):

  ```bash
  python task-cli.py clear
  ```

- **Mark a task as in progress or done**:

  ```bash
  python task-cli.py mark-in-progress 1
  python task-cli.py mark-done 1
  ```

- **List all tasks** (optionally filtered by status and sorted by priority or due date):

  ```bash
  python task-cli.py list
  python task-cli.py list todo priority
  python task-cli.py list in-progress due-date
  python task-cli.py list done
  ```

- **Show help**:

  ```bash
  python task-cli.py help
  ```

## Features

- **File Storage**: Uses a JSON file (`tasks.json`) to store tasks.
- **Task Management**:
  - Add new tasks with descriptions, priority (low, medium, high), due date (YYYY-MM-DD), and notes.
  - Update task descriptions, priority, due date, or notes.
  - Delete individual tasks.
  - Clear all tasks with user confirmation.
  - Mark tasks as "todo", "in-progress", or "done".
- **Task Listing**:
  - List all tasks with full details.
  - Filter tasks by status ("todo", "in-progress", "done").
  - Sort tasks by priority or due date.
- **Task Properties**:
  - Unique ID.
  - Description.
  - Status ("todo", "in-progress", "done").
  - Priority ("low", "medium", "high").
  - Due date (optional, in YYYY-MM-DD format).
  - Notes (optional).
  - Creation timestamp.
  - Last update timestamp.
- **Error Handling**:
  - Invalid commands.
  - Missing or invalid arguments (e.g., task ID, status, priority, due date).
  - Invalid date formats.
  - File operation errors.

## Implementation Notes

- Uses Python's built-in `json` and `datetime` modules for file operations and date handling.
- No external dependencies required.
- Simple command-line interface with positional arguments.
- Comprehensive error handling for commands, arguments, and file operations.
- Maintains all required and extended task properties.
- Automatically creates the `tasks.json` file if it doesn't exist.
