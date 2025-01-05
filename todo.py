import os

# File to store tasks
TASK_FILE = "tasks.txt"


# Load tasks from the file
def load_tasks():
    tasks = []
    if os.path.exists(TASK_FILE):
        with open(TASK_FILE, "r") as file:
            for line in file:
                task_data = line.strip().split(",")
                tasks.append({
                    "id": int(task_data[0]),
                    "description": task_data[1],
                    "deadline": task_data[2],
                    "status": task_data[3]
                })
    return tasks


# Save tasks to the file
def save_tasks(tasks):
    with open(TASK_FILE, "w") as file:
        for task in tasks:
            file.write(f"{task['id']},{task['description']},{task['deadline']},{task['status']}\n")


# Add a new task
def add_task(description, deadline):
    tasks = load_tasks()
    task_id = tasks[-1]["id"] + 1 if tasks else 1
    tasks.append({
        "id": task_id,
        "description": description,
        "deadline": deadline,
        "status": "Pending"
    })
    save_tasks(tasks)
    print("Task added successfully!")


# View all tasks
def view_tasks():
    tasks = load_tasks()
    if not tasks:
        print("No tasks available.")
        return

    print("\nTasks:")
    for task in tasks:
        print(f"{task['id']}. {task['description']} (Deadline: {task['deadline']}) - {task['status']}")


# Mark a task as completed
def mark_task_completed(task_id):
    tasks = load_tasks()
    for task in tasks:
        if task["id"] == task_id:
            task["status"] = "Completed"
            save_tasks(tasks)
            print("Task marked as completed!")
            return
    print("Task ID not found.")


# Edit a task
def edit_task(task_id, new_description, new_deadline):
    tasks = load_tasks()
    for task in tasks:
        if task["id"] == task_id:
            task["description"] = new_description
            task["deadline"] = new_deadline
            save_tasks(tasks)
            print("Task edited successfully!")
            return
    print("Task ID not found.")


# Delete a task
def delete_task(task_id):
    tasks = load_tasks()
    tasks = [task for task in tasks if task["id"] != task_id]
    save_tasks(tasks)
    print("Task deleted successfully!")


# Main menu
def main():
    while True:
        print("\nTo-Do List Menu")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Mark Task as Completed")
        print("4. Edit Task")
        print("5. Delete Task")
        print("6. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            description = input("Enter task description: ")
            deadline = input("Enter task deadline (YYYY-MM-DD): ")
            add_task(description, deadline)
        elif choice == "2":
            view_tasks()
        elif choice == "3":
            view_tasks()
            task_id = int(input("Enter task ID to mark as completed: "))
            mark_task_completed(task_id)
        elif choice == "4":
            view_tasks()
            task_id = int(input("Enter task ID to edit: "))
            new_description = input("Enter new task description: ")
            new_deadline = input("Enter new task deadline (YYYY-MM-DD): ")
            edit_task(task_id, new_description, new_deadline)
        elif choice == "5":
            view_tasks()
            task_id = int(input("Enter task ID to delete: "))
            delete_task(task_id)
        elif choice == "6":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()

