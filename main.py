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
    task_name = input("Name of task: ").capitalize()
    print(
            "\n1. Monday",
            "2. Tuesday",
            "3. Wednesday",
            "4. Thursday",
            "5. Friday",
            "6. Saturday",
            "7. Sunday\n",
            sep="\n"
        )

    # ***** BETTER WAY TO BREAK OUT OF THE LOOP? *****
    while True:
        task_day_number = input("Weekday: ").capitalize()

        if task_day_number == "1":
            task_day = "Monday"
            break
        elif task_day_number == "2":
            task_day = "Tuesday"
            break
        elif task_day_number == "3":
            task_day = "Wednesday"
            break
        elif task_day_number == "4":
            task_day = "Thursday"
            break
        elif task_day_number == "5":
            task_day = "Friday"
            break
        elif task_day_number == "6":
            task_day = "Saturday"
            break
        elif task_day_number == "7":
            task_day = "Sunday"
            break
        else:
            print("\nInvalid weekday number. Please enter a number between 1 and 7.\n")
            continue

    # Add to tasks
    tasks.append({"name": task_name, "weekday": task_day, "completed": False})


# 2. Complete task
def complete_task(tasks):
    # Prompt for task
    task_name = input("Name of task: ").capitalize()

    # Iterate through tasks and check for correct task name
    for i in tasks:
        if i["name"] == task_name:
            i["completed"] = True
            break


# 3. Remove task
def remove_task(tasks):
    # Prompt for task
    task_name = input("Name of task: ").capitalize()
    
    # Iterate through tasks and check for correct task name
    for i in tasks:
        if i["name"] == task_name:
            tasks.remove(i)
            break


# 4. View current tasks
def print_current_tasks(tasks):
    if not tasks:
        print("No current tasks to display")
    else:
        # Iterate through tasks and check if completed flag is False
        k = 0
        for i in tasks:
            if not i["completed"]:
                k += 1
                print(
                        "TASK #" + str(k) + "\n",
                        i["name"] + "\n",
                        i["weekday"] + "\n",
                        "--------------------------------",
                        sep=""
                    )


# 5. View completed tasks
def print_completed_tasks(tasks):
    if not tasks:
            print("No completed tasks to display")
    else:
        # Iterate through tasks and check if completed flag is False
        k = 0
        for i in tasks:
            if i["completed"]:
                k += 1
                print(
                        "COMPLETED TASK #" + str(k) + "\n",
                        i["name"] + "\n",
                        i["weekday"] + "\n",
                        "--------------------------------",
                        sep=""
                    )

main()

# FEATURES TO ADD
    # Add time to completed tasks
    # Make the lists print neater
        # Sort by weekday
    # Return message if a task is already completed or not (eg. the user is trying to complete a completed task)
    # Add substeps
    # Suggestions from AI?
        # Create a task class?
