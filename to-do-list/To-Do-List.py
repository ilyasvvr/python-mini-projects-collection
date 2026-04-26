# Simple To-Do List Application
# Author: ilyasvvr
# Language: Python

print("Welcome to To-Do List")

todo_list = []

while True:
    print("\nChoose an operation:")
    print("1. Add new task")
    print("2. Edit task")
    print("3. Remove task")
    print("4. Show tasks")
    print("5. Quit")

    try:
        operation = int(input("Enter number: "))
    except ValueError:
        print("Please enter a number.")
        continue

    # Add new task
    if operation == 1:
        task = input("Enter task name: ")
        todo_list.append(task)
        print("Task added successfully.")

    # Edit task
    elif operation == 2:
        if not todo_list:
            print("No tasks to edit.")
            continue

        for i, task in enumerate(todo_list):
            print(f"{i}: {task}")

        index = int(input("Enter task number to edit: "))

        if 0 <= index < len(todo_list):
            new_task = input("Enter new task name: ")
            todo_list[index] = new_task
            print("Task updated successfully.")
        else:
            print("Invalid task number.")

    # Remove task
    elif operation == 3:
        if not todo_list:
            print("No tasks to remove.")
            continue

        for i, task in enumerate(todo_list):
            print(f"{i}: {task}")

        index = int(input("Enter task number to remove: "))

        if 0 <= index < len(todo_list):
            removed = todo_list.pop(index)
            print(f"Task removed: {removed}")
        else:
            print("Invalid task number.")

    # Show tasks
    elif operation == 4:
        if not todo_list:
            print("Your to-do list is empty.")
        else:
            print("\nYour tasks:")
            for i, task in enumerate(todo_list):
                print(f"{i}: {task}")

    # Quit program
    elif operation == 5:
        print("Good bye!")
        break

    else:
        print("Invalid choice. Try again.")

