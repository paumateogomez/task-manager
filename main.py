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
        print(f"{index}. {task}")


def add_task():
    task = input("\nEnter the new task: ")

    tasks.append(task)

    print("Task added successfully!")


def main():
    while True:
        show_menu()

        option = input("\nSelect an option: ")

        if option == "1":
            view_tasks()

        elif option == "2":
            add_task()

        elif option == "3":
            print("Completing task...")

        elif option == "4":
            print("Deleting task...")

        elif option == "5":
            print("Goodbye!")
            break

        else:
            print("Invalid option")


if __name__ == "__main__":
    main()