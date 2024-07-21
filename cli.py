#from functions import get_todos, write_todos, todos_print
import functions
import time

now = time.strftime("%H:%M:%S %d-%m-%Y")

print("The current time is:" + now)

while True:
    user_action = input('Type "add", "show", "edit", "complete" or "exit"')
    user_action = user_action.strip().lower()

 #   used match user_action: and case 'add' etc before the if loop

    if user_action.startswith("add"):
        todo = user_action[4:]
        todo = todo + "\n"

        todos = functions.get_todos()
        todos.append(todo)

        functions.write_todos(todos_arg=todos, filepath='todos.txt')

    elif user_action.startswith('show'):
        print("Your To-Do's are as follows:")
        functions.todos_print()

    elif user_action.startswith('edit'):
        try:
            number = int(user_action[5:])
            number = number -1

            todos = functions.get_todos()

            new_todo = input("Enter the new to-Do:")
            todos[number] = new_todo + "\n"

            functions.write_todos(todos, 'todos.txt')
            functions.todos_print()
        except ValueError:
            print("Command is invalid, please enter a number.")
            continue
        except IndexError:
            print("The number you entered does not correspond to any To-Do")
            continue


    elif user_action.startswith('complete'):
        # todos_print()
        try:
            todos = functions.get_todos()

            number = int(user_action[9:])
            done_do = todos[number-1].rstrip("\n")
            print(f'The item "{done_do}" has been completed and removed from the ToDo list.')

            todos.pop(number-1)

            functions.write_todos(todos, 'todos.txt')
        except IndexError:
            print("There is no item with that number.")
            continue
        except ValueError:
            print('Please input a number (like "1") .')

    elif user_action.startswith('exit'):
        print("All done, see you later")
        break
    else:
        print("That's not what I asked you to do, please enter one of the listed commands.")