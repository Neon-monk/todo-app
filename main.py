from datetime import datetime
import sys

from matplotlib.dates import WEEKDAYS

def main():
    # Initialize task list
    tasks = []
    WEEKDAYS = {
                "1": "Monday",
                "2": "Tuesday",
                "3": "Wednesday",
                "4": "Thursday",
                "5": "Friday",
                "6": "Saturday",
                "7": "Sunday",
    }
    WEEKDAY_ORDER = {day: int(number) for number, day in WEEKDAYS.items()}
    
    # Automatically display tasks at start
    print_current_tasks(tasks, WEEKDAYS)
    
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
            add_task(tasks, WEEKDAYS)
        elif action == 2:
            complete_task(tasks, WEEKDAYS)
        elif action == 3:
            remove_task(tasks)
        elif action == 4:
            print_current_tasks(tasks, WEEKDAY_ORDER)
        elif action == 5:
            print_completed_tasks(tasks, WEEKDAY_ORDER)
        elif action == 6:
            sys.exit()

# Option functions
# 1. Add task
def add_task(tasks, WEEKDAYS):
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

    # Prompt user for weekday number and check if valid
    while True:
        task_day = WEEKDAYS.get(input("Weekday: ").strip())
        if task_day is not None:
            break
        print("\nINVALID WEEKDAY NUMBER. PLEASE ENTER A NUMBER BETWEEN 1 AND 7.\n")

    # Add to tasks
    tasks.append({"name": task_name, "weekday": task_day, "completed": False})


# 2. Complete task
def complete_task(tasks, WEEKDAYS):
    task_name = input("Name of task: ").capitalize()

    # Iterate through tasks and check for correct task name
    for task in tasks:
        if task["name"] == task_name:
            if task["completed"]:
                print("\nTHAT TASK WAS ALREADY COMPLETED ON " + task["completed_at"])
                break
            else:
                task["completed"] = True
                task["completed_at"] = datetime.now().strftime("%-m/%-d/%y - %-I:%M")
                break


# 3. Remove task
def remove_task(tasks):
    task_name = input("Name of task: ").capitalize()
    
    # Iterate through tasks and check for correct task name
    for task in tasks:
        if task["name"] == task_name:
            tasks.remove(task)
            break

    print("\nTHAT TASK DOES NOT EXIST")


# 4. View current tasks
def print_current_tasks(tasks, WEEKDAY_ORDER):
    sorted_current_tasks = sorted(
            (task for task in tasks if not task["completed"]),
            key=lambda task: WEEKDAY_ORDER[task["weekday"]],
    )

    if not sorted_current_tasks:
        print("NO CURRENT TASKS TO DISPLAY")
        return
    
    # Print sorted current tasks
    k = 0
    for i in sorted_current_tasks:
        k += 1
        print(
            "TASK #" + str(k) + "\n",
            i["name"] + "\n",
            i["weekday"] + "\n",
            "--------------------------------",
            sep=""
        )


# 5. View completed tasks
def print_completed_tasks(tasks, WEEKDAY_ORDER):
    sorted_completed_tasks = sorted(
            (task for task in tasks if task["completed"]),
            key=lambda task: WEEKDAY_ORDER[task["weekday"]],
    )
    
    if not sorted_completed_tasks:
        print("NO COMPLETED TASKS TO DISPLAY")
        return
    
    # Print sorted completed tasks
    k = 0
    for i in sorted_completed_tasks:
        k += 1
        print(
            "TASK #" + str(k) + "\n",
            i["name"] + "\n",
            i["weekday"] + "\n",
            "--------------------------------",
            sep=""
        )

main()

# FEATURES TO ADD
    # Add substeps
    # Suggestions from AI?
        # Create a task class?
