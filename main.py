from datetime import datetime
import sys

def main():
    # Initialize task list
    tasks = []
    days_of_the_week = {
        "1": "Monday",
        "2": "Tuesday",
        "3": "Wednesday",
        "4": "Thursday",
        "5": "Friday",
        "6": "Saturday",
        "7": "Sunday"
    }
    
    # Automatically display tasks at start
    print_current_tasks(tasks, days_of_the_week)
    
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
            add_task(tasks, days_of_the_week)
        elif action == 2:
            complete_task(tasks, days_of_the_week)
        elif action == 3:
            remove_task(tasks)
        elif action == 4:
            print_current_tasks(tasks, days_of_the_week)
        elif action == 5:
            print_completed_tasks(tasks, days_of_the_week)
        elif action == 6:
            sys.exit()

# Option functions
# 1. Add task
def add_task(tasks, days_of_the_week):
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
        task_day_number = input("Weekday: ")

        if task_day_number in days_of_the_week:
            task_day = days_of_the_week[task_day_number]
            break
        else:
            print("\nINVALID WEEKDAY NUMBER. PLEASE ENTER A NUMBER BETWEEN 1 AND 7.\n")
            continue

    # Sort tasks based on weekday
    # Generate number of chosen weekday

    
    # Add to tasks
    tasks.append({"name": task_name, "weekday": task_day, "completed": False})


# 2. Complete task
def complete_task(tasks, days_of_the_week):
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
def print_current_tasks(tasks, days_of_the_week):
    current_tasks = [task for task in tasks if not task["completed"]]

    if not current_tasks:
        print("NO CURRENT TASKS TO DISPLAY")
        return
    
    # Iterate through tasks and check if completed flag is False
    k = 0
    for task in tasks:
        if not task["completed"]:
            k += 1
            print(
                    "TASK #" + str(k) + "\n",
                    task["name"] + "\n",
                    task["weekday"] + "\n",
                    "--------------------------------",
                    sep=""
                )


# 5. View completed tasks
def print_completed_tasks(tasks, days_of_the_week):
    completed_tasks = [task for task in tasks if task["completed"]]

    if not completed_tasks:
        print("NO COMPLETED TASKS TO DISPLAY")
        return

    # Iterate through completed tasks and print them
    k = 0
    for task in completed_tasks:
        k += 1
        print(
                "COMPLETED TASK #" + str(k) + "\n",
                task["name"] + "\n",
                task["weekday"] + "\n",
                task["completed_at"] + "\n",
                "--------------------------------",
                sep=""
            )

main()

# FEATURES TO ADD
    # Sort task list by weekday
    # Add substeps
    # Suggestions from AI?
        # Create a task class?
