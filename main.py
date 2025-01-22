from services.task_service import TaskService

def main():
    service = TaskService()

    while True:
        print("\nTask Manager")
        print("1. View tasks")
        print("2. Add task")
        print("3. Mark task as done")
        print("4. Exit")
        choice = input("Choose an option: ")

        if choice == "1":
            tasks = service.get_tasks()
            for task in tasks:
                status = "Done" if task['is_done'] else "Pending"
                print(f"[{status}] {task['id']}: {task['description']}")
        elif choice == "2":
            description = input("Enter task description: ")
            service.add_task(description)
        elif choice == "3":
            task_id = input("Enter task ID to mark as done: ")
            service.mark_task_done(task_id)
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid option. Try again.")

if __name__ == "__main__":
    main()
