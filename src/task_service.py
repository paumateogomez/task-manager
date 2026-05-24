import json

tasks = []


def load_tasks():
    global tasks

    try:
        with open("data/tasks.json", "r") as file:
            tasks = json.load(file)
    except:
        tasks = []


def save_tasks():
    with open("data/tasks.json", "w") as file:
        json.dump(tasks, file, indent=4)


def view_tasks():
    if not tasks:
        print("\nNo tasks available.")
        return

    print("\nTasks:")

    for index, task in enumerate(tasks, start=1):
        status = "[X]" if task["completed"] else "[ ]"
        print(f"{index}. {status} {task['title']}")


def add_task():
    task = input("\nEnter the new task: ")

    tasks.append({
        "title": task,
        "completed": False
    })

    save_tasks()
    print("Task added successfully!")


def complete_task():
    view_tasks()

    if not tasks:
        return

    try:
        task_number = int(input("\nTask number to complete: "))
        if task_number < 1 or task_number > len(tasks):
            print("Invalid task number.")
    return
        tasks[task_number - 1]["completed"] = True
        save_tasks()
        print("Task completed successfully!")

    except:
        print("Invalid task number.")


def delete_task():
    view_tasks()

    if not tasks:
        return

    try:
        task_number = int(input("\nTask number to delete: "))
        if task_number < 1 or task_number > len(tasks):
            print("Invalid task number.")
            return
        deleted_task = tasks.pop(task_number - 1)
        save_tasks()
        print(f"Task '{deleted_task['title']}' deleted successfully!")

    except:
        print("Invalid task number.")