from colorama import Fore
from tabulate import tabulate

import csv
from datetime import datetime

todo_list = {}

finished_tasks = []
not_finished_tasks = []

# Display tasks and their statuses
def view_tasks():
    print('Number of tasks: ' + str(len(todo_list)))
    print(Fore.GREEN + 'Number of finished tasks: ' + str(len(finished_tasks)))
    print(Fore.RED + 'Number of unfinished tasks: ' + str(len(not_finished_tasks)))
    print(Fore.RESET)
    print('** [TASKS] **')
    print(f'Unfinished tasks: {not_finished_tasks}')
    print(f'Finished tasks: {finished_tasks}')

    for n, i in enumerate(todo_list):
        if todo_list[i] == '[\u2713]':
            print(str(n + 1) + ') ' + todo_list[i] + ' ' + i)
        elif todo_list[i] == '[X]':
            print(str(n + 1) + ') ' + todo_list[i] + ' ' + i)
    print('\n')

    display()
    open_file()

# Open csv file and save tasks
def open_file():    
    with open('tasks.csv', 'a', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(["Task", "Status", "Date Created"])
        for task, status in todo_list.items():
            created_date = datetime.now().strftime("%Y-%m-%d")
            writer.writerow([task, status, created_date])


# Display tasks and status in a table
def display():
    tasks = []
    for task, status in todo_list.items():
        tasks.append([status, task])

    headers = ["Status", "Task"]

    print(tabulate(tasks, headers=headers, tablefmt="fancy_grid"))

# Check if task exist if not it adds it to the unfinished tasks
def new_task():
    print(Fore.BLUE + '** NEW TASK **')
    print(Fore.RESET)
    while True:
        while True:
            new_task_name = input('Add new task or back to menu(q): ')
            if new_task_name.lower() in todo_list:
                print('This name already in use!')
                pass
            elif new_task_name == 'q':
                return
            else:
                break

        todo_list[new_task_name.lower()] = '[X]'
        print('New task added to list!')
        not_finished_tasks.append(new_task_name.lower())

# Remove task from todo_list
def remove_task():
    print(Fore.RED + '** REMOVE TASK **')
    print(Fore.RESET)
    view_tasks()
    if len(todo_list) == 0:
        print('There is no task to remove')
        menu()
    while True:
        while True:
            remove_task_name = input('Which task would you like to remove? or back to menu(q): ')
            if remove_task_name == 'q':
                menu()
            elif remove_task_name in todo_list:
                del todo_list[remove_task_name]
                print('Task removed')
                try:
                    finished_tasks.remove(remove_task_name)
                except:
                    not_finished_tasks.remove(remove_task_name)
                break
            else:
                print("Can't find this task. Did you typed correctly?")
                pass


# Check if todo_list empty
def check_empty_tasks(todo_list):

    if len(todo_list) == 0:
        print('You have no task')
        return True
    return False

# Mark task as finished
def finished_task():
    print(Fore.GREEN + '** FINISHED TASK **')
    print(Fore.RESET)
    view_tasks()
    if check_empty_tasks(todo_list):
        return
    while True:
        while True:
            task_to_finish = input('Which task have you finished? or back to menu(q): ')
            if task_to_finish in todo_list:
                break
            elif task_to_finish == 'q':
                menu()
            else:
                print("Can't find it. Check correct task name")

        try:
            todo_list[task_to_finish] = '[\u2713]'
            not_finished_tasks.remove(task_to_finish)
            finished_tasks.append(task_to_finish)
            print('Task finished!')
        except:
            print('This task already finished!')

# Mark task as unfinished
def not_finished_task():
    print(Fore.YELLOW + '** UNFINISHED TASK **')
    print(Fore.RESET)
    view_tasks()
    if check_empty_tasks(todo_list):
        return
    while True:
        while True:
            task_to_unfinished = input('Which task have you not finished? or back to menu(q): ')
            if task_to_unfinished in todo_list:
                break
            elif task_to_unfinished == 'q':
                menu()
            else:
                print("Can't find task. Try again!")

        try:
            todo_list[task_to_unfinished] = '[X]'
            finished_tasks.remove(task_to_unfinished)
            not_finished_tasks.append(task_to_unfinished)
            print('Task uncompleted')
        except:
            print('You already uncompleted this task!')

# Display the menu and handle input
def menu():
    while True:
        view_tasks()
        print('\n', Fore.BLUE + '(1) Add Task\n', Fore.RED + '(2) Remove Task\n', Fore.GREEN + '(3) Finished Task\n', Fore.YELLOW + '(4) Un-finished Task\n', Fore.RESET + '(5) Exit\n')

        menu_choice = input('')
        if menu_choice == '1':
            new_task()
        elif menu_choice == '2':
            remove_task()
            return
        elif menu_choice == '3':
            finished_task()
        elif menu_choice == '4':
            not_finished_task()
        elif menu_choice == '5':
            exit()