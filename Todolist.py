import json

# Initialize an empty to-do list
tasks = []

def save_tasks():
    with open('tasks.json', 'w') as file:
        json.dump(tasks, file)

def load_tasks():
    try:
        with open('tasks.json', 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return []

def list_tasks():
    if not tasks:
        print("No tasks to display.")
    else:
        for i, task in enumerate(tasks, start=1):
            print(f"{i}. Title: {task['title']}")
            print(f"   Description: {task['description']}")
            print(f"   Due Date: {task['due_date']}")
            print(f"   Status: {'Completed' if task['completed'] else 'Pending'}")
            print()

def create_task():
    title = input("Enter task title: ")
    description = input("Enter task description: ")
    due_date = input("Enter due date: ")

    new_task = {
        "title": title,
        "description": description,
        "due_date": due_date,
        "completed": False
    }

    tasks.append(new_task)
    save_tasks()
    print("Task created successfully!")

def delete_task():
    list_tasks()
    try:
        task_num = int(input("Enter the task number to delete: "))
        if 1 <= task_num <= len(tasks):
            del tasks[task_num - 1]
            save_tasks()
            print("Task deleted successfully!")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Invalid input. Please enter a number.")

if __name__ == "__main__":
    tasks = load_tasks()
    while True:
        print("\nTo-Do List Application")
        print("1. List Tasks")
        print("2. Create Task")
        print("3. Delete Task")
        print("4. Quit")
        choice = input("Enter your choice: ")

        if choice == '1':
            list_tasks()
        elif choice == '2':
            create_task()
        elif choice == '3':
            delete_task()
        elif choice == '4':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")
