# todo.py - A simple to-do list program

class ToDoList:
    def __init__(self):
        self.tasks = []
    
    def add_task(self, task):
        self.tasks.append({"task": task, "completed": False})
        print(f"Added task: '{task}'")

    def complete_task(self, task_number):
        if 0 <= task_number < len(self.tasks):
            self.tasks[task_number]["completed"] = True
            print(f"Task '{self.tasks[task_number]['task']}' marked as complete.")
        else:
            print("Invalid task number.")

    def delete_task(self, task_number):
        if 0 <= task_number < len(self.tasks):
            removed_task = self.tasks.pop(task_number)
            print(f"Task '{removed_task['task']}' has been deleted.")
        else:
            print("Invalid task number.")

    def show_tasks(self):
        if not self.tasks:
            print("No tasks in your to-do list.")
        else:
            for i, task in enumerate(self.tasks):
                status = "Done" if task["completed"] else "Pending"
                print(f"{i + 1}. {task['task']} [{status}]")

def main():
    todo_list = ToDoList()
    
    while True:
        print("\n1. Add Task\n2. Show Tasks\n3. Mark Task as Complete\n4. Delete Task\n5. Exit")
        choice = input("Choose an option: ")

        if choice == '1':
            task = input("Enter the task: ")
            todo_list.add_task(task)
        elif choice == '2':
            todo_list.show_tasks()
        elif choice == '3':
            todo_list.show_tasks()
            task_num = int(input("Enter the task number to mark as complete: ")) - 1
            todo_list.complete_task(task_num)
        elif choice == '4':
            todo_list.show_tasks()
            task_num = int(input("Enter the task number to delete: ")) - 1
            todo_list.delete_task(task_num)
        elif choice == '5':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
a
