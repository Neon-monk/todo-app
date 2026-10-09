# Stored tasks
current_tasks = [{}]

def user_action(choice):
    choice = int(choice)

# Automatically display tasks at start
print(current_tasks)

# Prompt user for next action
print(
        "1. Add task",
        "2. Complete task",
        "3. Remove task",
        "4. View current tasks",
        "5. View completed tasks",
        "6. Exit\n",
        sep="\n"
    )
action = input("What would you like to do?  Enter a number: ")


# Options
# 1. Add task
def add_task():
    # Prompt user for task
        # Add to tasks

# 2. Complete task
def complete_task():
    # Iterate through tasks
        # Check if completed flag is False and set to True

# 3. Remove task
def remove_task():
    # Prompt for task
    # Iterate through tasks
        # Remove from tasks

# 4. View current tasks
def print_current_tasks():
    current_tasks = [{}]
    # Iterate through tasks
        # Check if completed flag is False
            # Add to current_tasks
    
    print(current_tasks)

# 5. View completed tasks
def print_completed_tasks():
    completed_tasks = [{}]
    # Iterate through tasks
        # Check if completed flag is True
            # Add to completed_tasks

    print(completed_tasks)

# 6. Exit


# FEATURES TO ADD
    # Assign tasks to weekday
