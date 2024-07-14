def todos_print():
    with open('todos.txt', 'r') as todos:
        new_todos = [item.strip("\n") for item in todos]
        for i, item in enumerate(new_todos):
            row = f"{i + 1} - {item}"
            print(row)

while True:
    user_action = input('Type "add", "show", "edit", "complete" or "exit"')
    user_action = user_action.strip().lower()

 #   used match user_action: and case 'add' etc before the if loop

    if user_action.startswith("add"):
        todo = user_action[4:]
        todo = todo + "\n"

        with open('todos.txt', 'r') as file:
            todos = file.readlines()

        todos.append(todo)

        with open('todos.txt', 'w') as file:
            file.writelines(todos)

    elif user_action.startswith('show'):
        print("Your To-Do's are as follows:")
        todos_print()

    elif user_action.startswith('edit'):
        try:
            number = int(user_action[5:])
            number = number -1

            with open('todos.txt', 'r') as file:
                todos = file.readlines()

            new_todo = input("Enter the new to-Do:")
            todos[number] = new_todo + "\n"

            with open('todos.txt', 'w') as file:
                file.writelines(todos)
            todos_print()
        except ValueError:
            print("Command is invalid, please enter a number.")
            continue
        except IndexError:
            print("The number you entered does not correspond to any To-Do")
            continue


    elif user_action.startswith('complete'):
        # todos_print()
        try:
            with open('todos.txt', 'r') as file:
                todos = file.readlines()

            number = int(user_action[9:])
            done_do = todos[number-1].rstrip("\n")
            print(f'The item "{done_do}" has been completed and removed from the ToDo list.')

            todos.pop(number-1)

            with open('todos.txt', 'w') as file:
                file.writelines(todos)
        except IndexError:
            print("There is no item with that number.")
            continue

    elif user_action.startswith('exit'):
        print("All done, see you later")
        break
    else:
        print("That's not what I asked you to do, please enter one of the listed commands.")
