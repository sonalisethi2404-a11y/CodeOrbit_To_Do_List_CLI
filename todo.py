
# To-Do List CLI Application

# List to store tasks
tasks = []

# Function to load previously saved tasks
def load_tasks():
    try:
        with open("tasks.txt", "r") as file:
            for line in file:
                task = line.strip()
                if task:
                    tasks.append(task)

    except FileNotFoundError:
        print("No previous task file found. Starting fresh!")

# Function to save tasks permanently
def save_tasks():
    with open("tasks.txt", "w") as file:
        for task in tasks:
            file.write(task + "\n")

# Function to add a task
def add_task():
    task = input("Enter your task: ").strip()

    if task:
        tasks.append(task)
        save_tasks()
        print("Task added successfully!")
    else:
        print("Task cannot be empty!")

# Function to view all tasks
def view_tasks():
    if not tasks:
        print("\nYour to-do list is empty!")
    else:
        print("\n===== YOUR TASKS =====")

        for index, task in enumerate(tasks, start=1):
            print(f"{index}. {task}")

# Function to remove a task
def remove_task():
    view_tasks()

    if not tasks:
        return

    try:
        task_number = int(input("Enter task number to remove: "))

        if 1 <= task_number <= len(tasks):
            removed_task = tasks.pop(task_number - 1)
            save_tasks()
            print(f"Task '{removed_task}' removed successfully!")
        else:
            print("Invalid task number!")

    except ValueError:
        print("Please enter a valid number!")

# Main function
def main():

    # Load saved tasks when program starts
    load_tasks()

    while True:
        print("\n===== TO-DO LIST APP =====")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Remove Task")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_task()

        elif choice == "2":
            view_tasks()

        elif choice == "3":
            remove_task()

        elif choice == "4":
            print("Thank you for using To-Do List App!")
            break

        else:
            print("Invalid choice! Please try again.")

# Program execution starts here
if __name__ == "__main__":
    main()