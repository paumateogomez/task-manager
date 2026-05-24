def show_menu():
    print("\n=== TASK MANAGER ===")
    print("1. View tasks")
    print("2. Add task")
    print("3. Complete task")
    print("4. Delete task")
    print("5. Exit")


def main():
    while True:
        show_menu()

        option = input("\nSelect an option: ")

        if option == "1":
            print("Viewing tasks...")

        elif option == "2":
            print("Adding task...")

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