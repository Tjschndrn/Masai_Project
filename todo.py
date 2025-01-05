import json
import os

# File to store tasks
TASK_FILE = "tasks.json"

# Load tasks from file
def load_tasks():
    if os.path.exists(TASK_FILE):
        with open(TASK_FILE, "r") as file:
            return json.load(file)
    return {"pending": [], "completed": []}

# Save tasks to file
def save_tasks(tasks):
    with open(TASK_FILE, "w") as file:
        json.dump(tasks, file, indent=4)

# Add a new task
def add_task(description, deadline):
    tasks = load_tasks()
    tasks["pending"].append({"description": description, "deadline": deadline})
    save_tasks(tasks)
    print("Task added successfully!")

# View tasks
def view_tasks():
    tasks = load_tasks()
    print("\nPending Tasks:")
    for idx, task in enumerate(tasks["pending"], 1):
        print(f"{idx}. {task['description']} (Deadline: {task['deadline']})")

    print("\nCompleted Tasks:")
    for idx, task in enumerate(tasks["completed"], 1):
        print(f"{idx}. {task['description']} (Deadline: {task['deadline']})")

# Mark task as completed
def complete_task(task_index):
    tasks = load_tasks()
    if 0 <= task_index < len(tasks["pending"]):
        completed_task = tasks["pending"].pop(task_index)
        tasks["completed"].append(completed_task)
        save_tasks(tasks)
        print("Task marked as completed!")
    else:
        print("Invalid task index.")

# Edit task
def edit_task(task_index, new_description, new_deadline):
    tasks = load_tasks()
    if 0 <= task_index < len(tasks["pending"]):
        tasks["pending"][task_index]["description"] = new_description
        tasks["pending"][task_index]["deadline"] = new_deadline
        save_tasks(tasks)
        print("Task edited successfully!")
    else:
        print("Invalid task index.")

# Delete task
def delete_task(task_index):
    tasks = load_tasks()
    if 0 <= task_index < len(tasks["pending"]):
        tasks["pending"].pop(task_index)
        save_tasks(tasks)
        print("Task deleted successfully!")
    else:
        print("Invalid task index.")

# Main menu
def main():
    while True:
        print("\nTo-Do List Menu")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Complete Task")
        print("4. Edit Task")
        print("5. Delete Task")
        print("6. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            description = input("Enter task description: ")
            deadline = input("Enter task deadline: ")
            add_task(description, deadline)
        elif choice == "2":
            view_tasks()
        elif choice == "3":
            view_tasks()
            task_index = int(input("Enter task index to mark as completed: ")) - 1
            complete_task(task_index)
        elif choice == "4":
            view_tasks()
            task_index = int(input("Enter task index to edit: ")) - 1
            new_description = input("Enter new task description: ")
            new_deadline = input("Enter new task deadline: ")
            edit_task(task_index, new_description, new_deadline)
        elif choice == "5":
            view_tasks()
            task_index = int(input("Enter task index to delete: ")) - 1
            delete_task(task_index)
        elif choice == "6":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()

