import sys

def main():
    # Initialize task list
    tasks = []
    
    # Automatically display tasks at start
    print_current_tasks(tasks)
    
    while True:
        # Prompt user for next action
        print(
                "\n1. Add task",
                "2. Complete task",
                "3. Remove task",
                "4. View current tasks",
                "5. View completed tasks",
                "6. Exit\n",
                sep="\n"
            )

        # Prompt user for next action and convert choice to integer
        action = int(input("What would you like to do?  Enter a number: "))
        print()

        if action == 1:
            add_task(tasks)
        elif action == 2:
            complete_task(tasks)
        elif action == 3:
            remove_task(tasks)
        elif action == 4:
            print_current_tasks(tasks)
        elif action == 5:
            print_completed_tasks(tasks)
        elif action == 6:
            sys.exit()

# Option functions
# 1. Add task
def add_task(tasks):
    # Prompt user for task
    task_name = input("Name of task: ")
    
    # Add to tasks
    tasks.append({"name": task_name, "completed": False})


# 2. Complete task
def complete_task(tasks):
    # Prompt for task
    task_name = input("Name of task: ")

    # Iterate through tasks and check for correct task name
    for i in tasks:
        if i["name"] == task_name:
            i["completed"] = True
            break

# 3. Remove task
def remove_task(tasks):
    # Prompt for task
    task_name = input("Name of task: ")
    
    # Iterate through tasks and check for correct task name
    for i in tasks:
        if i["name"] == task_name:
            tasks.remove(i)
            break

# 4. View current tasks
def print_current_tasks(tasks):
    current_tasks = []
    # Iterate through tasks and check if completed flag is False
    for i in tasks:
        if not i["completed"]:
            current_tasks.append(i)

    if not current_tasks:
            print("No current tasks to display")
    else:
        print(current_tasks)

# 5. View completed tasks
def print_completed_tasks(tasks):
    completed_tasks = []
    # Iterate through tasks and check if completed flag is True
    for i in tasks:
        if i["completed"]:
            completed_tasks.append(i)

    if not completed_tasks:
            print("No completed tasks to display")
    else:
        print(completed_tasks)

main()

# FEATURES TO ADD
    # Assign tasks to weekday
