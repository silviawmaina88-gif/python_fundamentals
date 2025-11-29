tasks = [] # stores all the tasks
completed_tasks = [] # stores all the task marked completed

def addTask():
    try:
        new_task = input('Enter a new task: ').lower().strip()
        if new_task in tasks:
            print(f"({new_task}) already in the tasks")
        tasks.append(new_task)
        print('Task added successfully in list')
    except ValueError:
        print('Something went wrong while adding task')
    
def removeTask():
    try:
        task_to_remove = input('Enter task to remove: ')
        if task_to_remove not in tasks:
            print(f"{task_to_remove} not found!!")
        index = tasks.index(task_to_remove)
        tasks.pop(index)
        print(f"{task_to_remove} has been removed successfully")
    except ValueError:
        print('Something went wrong while removing task')

def markAsCompleted():
    try:
        task = input('Enter a task to mark as completed: ')
        if task in tasks:
            completed_tasks.append(task)
        print(f"{task} completed successfully")
    except ValueError:
        print('Something went wrong')

def displayTasks():
    if tasks:
        print(tasks)

while True:
    print('Welcome to TODO LIST application')
    print('\n1. Add Task')
    print('\n2. Remove Task')
    print('\n3. Mark Task as Completed')
    print('\n4. Display All Tasks')
    print('\n5. Exit Application')

    option = input('Choose your option above: ')
    if option == '1':
        addTask()
    elif option == '2':
        removeTask()
    elif option == '3':
        markAsCompleted()
    elif option == '4':
        displayTasks()
    elif option == '5':
       break
    else:
        print('Invalid option')