from colorama import Fore
from datetime import date

todo_list = {}

finished_tasks = []
not_finished_tasks = []

no_tasks = False

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

def new_task():
    print('** NEW TASK **')
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

def remove_task():
    print('** REMOVE TASK **')
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

def finished_task():
    print('** FINISHED TASK **')
    view_tasks()
    while True:
        while True:
            if len(todo_list) == 0:
                print('You have no task')
                no_tasks = True
                break
            else:
                no_tasks = False

            task_to_finish = input('Which task have you finished? or back to menu(q): ')

            if task_to_finish in todo_list:
                break
            elif task_to_finish == 'q':
                menu()
            else:
                print("Can't find it. Check correct task name")
                pass

        if no_tasks == False:
            try:
                todo_list[task_to_finish] = '[\u2713]'
                not_finished_tasks.remove(task_to_finish)
                finished_tasks.append(task_to_finish)
                print('Task finished!')
            except:
                print('This task already finished!')
        else:
            pass

def not_finished_task():
    print('** UNFINISHED TASK **')
    view_tasks()
    while True:
        while True:
            if len(todo_list) == 0:
                print('You have no task')
                no_task = True
                break
            else:
                no_task = False

            task_to_unfinished = input('Which task have you not finished? or back to menu(q): ')

            if task_to_unfinished in todo_list:
                break
            elif task_to_unfinished == 'q':
                menu()
            else:
                print("Can't find task. Try again!")
                pass

        if no_task == False:
            try:
                todo_list[task_to_unfinished] = '[X]'
                finished_tasks.remove(task_to_unfinished)
                not_finished_tasks.append(task_to_unfinished)
                print('Task uncompleted')
            except:
                print('You already uncompleted this task!')
        else:
            pass

def menu():
    view_tasks()
    print('''
        (1) Add Task
        (2) Remove Task
        (3) Finished Task
        (4) Un-finished Task
        (5) Exit
        ''')

    menu_choice = input('')
    if menu_choice == '1':
        new_task()
    elif menu_choice == '2':
        remove_task()
    elif menu_choice == '3':
        finished_task()
    elif menu_choice == '4':
        not_finished_task()
    elif menu_choice == '5':
        exit()

    while True:
        menu()


menu()