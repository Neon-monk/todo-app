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
    print_current_tasks(tasks, WEEKDAY_ORDER)
    
    while True:
        # Prompt user for next action
        print(
            "\n1. Add task",
            "2. Add subtask",
            "3. Complete task",
            "4. Remove task",
            "5. View current tasks",
            "6. View completed tasks",
            "7. Exit\n",
            sep="\n"
        )

        # Prompt again until user enters an action from 1 to 7
        while True:
            choice = input("What would you like to do?  Enter a number: ").strip()
            if choice in {"1", "2", "3", "4", "5", "6", "7"}:
                action = int(choice)
                break
            print("\nINVALID CHOICE. PLEASE ENTER A NUMBER BETWEEN 1 AND 7.\n")

        print()

        if action == 1:
            add_task(tasks, WEEKDAYS)
        elif action == 2:
            add_subtask(tasks)
        elif action == 3:
            complete_task(tasks, WEEKDAYS)
        elif action == 4:
            remove_task(tasks)
        elif action == 5:
            print_current_tasks(tasks, WEEKDAY_ORDER)
        elif action == 6:
            print_completed_tasks(tasks, WEEKDAY_ORDER)
        elif action == 7:
            sys.exit()

# Option functions
# 1. Add task
def add_task(tasks, WEEKDAYS):
    task_name = input("Name of task: ").strip().capitalize()

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

# 2. Add subtask
def add_subtask(tasks):
    while True:
        task_name = input("Name of task: ").strip().capitalize()
        task = next((task for task in tasks if task["name"] == task_name), None)

        if task is not None:
            break

        print("\nTHAT TASK DOES NOT EXIST\n")

    subtasks = task.setdefault("subtask", [])

    while True:
        subtask_name = input("Name of subtask: ").strip().capitalize()

        if subtask_name not in subtasks:
            subtasks.append(subtask_name)
            return

        print("\nTHAT SUBTASK ALREADY EXISTS\n")

# 3. Complete task
def complete_task(tasks, WEEKDAYS):
    task_name = input("Name of task: ").strip().capitalize()

    for task in tasks:
        if task["name"] == task_name:
            if task["completed"]:
                print(f"\nTHAT TASK WAS ALREADY COMPLETED ON {task.get('completed_at', 'unknown')}")
                return

            task["completed"] = True
            task["completed_at"] = datetime.now().strftime("%m/%d/%y - %I:%M %p")
            print(f"\n{task_name} marked as complete")
            return

    print("\nTHAT TASK DOES NOT EXIST")


# 4. Remove task
def remove_task(tasks):
    task_name = input("Name of task: ").strip().capitalize()
    
    # Iterate through tasks and check for correct task name
    for task in tasks:
        if task["name"] == task_name:
            tasks.remove(task)
            print(f"\n{task_name} removed")
            return

    print("\nTHAT TASK DOES NOT EXIST")


# 5. View current tasks
def print_current_tasks(tasks, WEEKDAY_ORDER):
    sorted_current_tasks = sorted(
        (task for task in tasks if not task["completed"]),
        key=lambda task: WEEKDAY_ORDER[task["weekday"]],
    )

    if not sorted_current_tasks:
        print("NO CURRENT TASKS TO DISPLAY")
        return
    
    # Print sorted current tasks
    current_weekday = None
    for task in sorted_current_tasks:
        if task["weekday"] != current_weekday:
            if current_weekday is not None:
                print("--------------------------------")

            current_weekday = task["weekday"]
            print(current_weekday)

        print(f"• {task['name']}")

        for subtask in task.get("subtask", []):
            print(f"  • {subtask}")

    print("--------------------------------")


# 6. View completed tasks
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
    # Suggestions from AI?
        # Create a task class?
