def print_todo_list(todo_list):
    # Display the current to-do list with task numbers, completion status, and descriptions
    print("\nTo-Do List:\n")
    for i, task in enumerate(todo_list, start=1):
        status = "[x]" if task["completed"] else "[ ]"
        print(f"{i}. {status} {task['description']}")
    print("\n")

def mark_task_completed(todo_list, task_number):
    # Mark a task as completed based on the task number provided by the user
    if 1 <= task_number <= len(todo_list):
        todo_list[task_number - 1]["completed"] = True
        print("Task marked as completed!\n")
    else:
        print("Invalid task number. Please try again.\n")

def add_task(todo_list, description):
    # Add a new task to the to-do list
    todo_list.append({"description": description, "completed": False})
    print("Task added to the to-do list!\n")

def main():
    # Initialize an empty to-do list
    todo_list = []

    while True:
        # Display the current to-do list and menu options
        print_todo_list(todo_list)
        print("Menu:")
        print("1. Mark task as completed")
        print("2. Add a new task")
        print("3. Quit")

        # Get the user's choice
        choice = input("Enter your choice (1/2/3): ")

        if choice == "1":
            # If the user chooses to mark a task as completed, get the task number and mark it
            task_number = int(input("Enter the task number to mark as completed: "))
            mark_task_completed(todo_list, task_number)
        elif choice == "2":
            # If the user chooses to add a new task, get the task description and add it
            new_task = input("Enter the description of the new task: ")
            add_task(todo_list, new_task)
        elif choice == "3":
            # If the user chooses to quit, exit the loop and end the program
            print("Goodbye!")
            break
        else:
            # If the user enters an invalid choice, prompt them to try again
            print("Invalid choice. Please enter 1, 2, or 3.\n")

if __name__ == "__main__":
    # Call the main function when the script is run
    main()
