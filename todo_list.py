tasks = []

while True:
    print("\n1. Add Task")
    print("2. View Tasks")
    print("3. Delete Task")
    print("4. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        task = input("Enter task: ")
        tasks.append(task)
        print("Task added.")

    elif choice == "2":
        if not tasks:
            print("No tasks.")
        else:
            for i, task in enumerate(tasks, 1):
                print(f"{i}. {task}")

    elif choice == "3":
        number = int(input("Enter task number: "))
        if 1 <= number <= len(tasks):
            tasks.pop(number - 1)
            print("Task deleted.")
        else:
            print("Invalid task number.")

    elif choice == "4":
        print("Goodbye!")
        break

    else:
        print("Invalid choice.")

OUTPUT:
1. Add Task
2. View Tasks
3. Delete Task
4. Exit
Enter choice: 1
Enter task: Complete Python assignment
Task added.

1. Add Task
2. View Tasks
3. Delete Task
4. Exit
Enter choice: 1
Enter task: Read a Python book
Task added.

1. Add Task
2. View Tasks
3. Delete Task
4. Exit
Enter choice: 2
1. Complete Python assignment
2. Read a Python book

1. Add Task
2. View Tasks
3. Delete Task
4. Exit
Enter choice: 3
Enter task number: 1
Task deleted.

1. Add Task
2. View Tasks
3. Delete Task
4. Exit
Enter choice: 2
1. Read a Python book

1. Add Task
2. View Tasks
3. Delete Task
4. Exit
Enter choice: 4
Goodbye!
