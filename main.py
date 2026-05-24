tasks = []


def show_menu():
    print("\n=== TASK MANAGER ===")
    print("1. View tasks")
    print("2. Add task")
    print("3. Complete task")
    print("4. Delete task")
    print("5. Exit")


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

    tasks.append({"title": task, "completed": False  })

    print("Task added successfully!")

def complete_task():

    view_tasks()

    if not tasks:
        return

    try:
        task_number = int(input("\nTask number to complete: "))

        tasks[task_number - 1]["completed"] = True

        print("Task completed successfully!")

    except:
        print("Invalid task number.")
        

def delete_task():

    view_tasks()

    if not tasks:
        return

    try:
        task_number = int(input("\nTask number to delete: "))

        deleted_task = tasks.pop(task_number - 1)

        print(f"Task '{deleted_task['title']}' deleted successfully!")

    except:
        print("Invalid task number.")

def main():
    while True:
        show_menu()

        option = input("\nSelect an option: ")

        if option == "1":
            view_tasks()

        elif option == "2":
            add_task()

        elif option == "3":
            complete_task()

        elif option == "4":
            delete_task()

        elif option == "5":
            print("Goodbye!")
            break

        else:
            print("Invalid option")


if __name__ == "__main__":
    main()