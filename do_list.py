tasks = []
while True:
    print("\n1. Add Task")
    print("2. view Tasks")
    print("3. Exit")
    
    choice = input("Choose an option: ")
    if choice == "1":
        task = input("Enter a task: ")
        tasks.append(task)
        print("Task added.")
    elif choice == "2":
        print("\nYour Tasks:")
        for i, task in enumerate(tasks, 1):
            print(f"{1}. {task}")
    elif choice == "3":
        print("Goodbye!")
        break
        