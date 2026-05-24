from src.task_service import (
    load_tasks,
    view_tasks,
    add_task,
    complete_task,
    delete_task
)


def show_menu():
    print("\n=== TASK MANAGER ===")
    print("1. View tasks")
    print("2. Add task")
    print("3. Complete task")
    print("4. Delete task")
    print("5. Exit")


def main():
    load_tasks()

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