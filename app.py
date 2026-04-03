def main():
    tasks = []
    while True:
        print("\n--- TODO LIST ---")
        for i, task in enumerate(tasks, 1):
            print(f"{i}. {task}")
        print("\n1. Add Task\n2. Remove Task\n3. Exit")
        choice = input("Choose an option: ")
        if choice == '1':
            tasks.append(input("Enter the task: "))
        elif choice == '2':
            try:
                task_num = int(input("Enter number to remove: "))
                tasks.pop(task_num - 1)
            except (ValueError, IndexError):
                print("Invalid number!")
        elif choice == '3':
            break
if __name__ == "__main__":
    main()
