def todos_print():
    with open('todos.txt', 'r') as todos:
        new_todos = [item.strip("\n") for item in todos]
        for i, item in enumerate(new_todos):
            row = f"{i + 1} - {item}"
            print(row)

while True:
    user_action = input('Type "add", "show", "edit", "complete" or "exit"')
    user_action = user_action.strip().lower()

    match user_action:

        case 'add':
            todo = input("Enter a To-Do") +"\n"

            with open('todos.txt', 'r') as file:
                todos = file.readlines()

            todos.append(todo)

            with open('todos.txt', 'w') as file:
                file.writelines(todos)

        case 'show' | 'display':
            print("Your To-Do's are as follows:")
            todos_print()

        case 'edit':
            number = int(input("Whate # element do you want to switch?"))
            number = number -1

            with open('todos.txt', 'r') as file:
                todos = file.readlines()

            new_todo = input("Enter the new to-Do:")
            todos[number] = new_todo + "\n"

            with open('todos.txt', 'w') as file:
                file.writelines(todos)
            todos_print()

        case 'complete':
            todos_print()
            with open('todos.txt', 'r') as file:
                todos = file.readlines()

            number = int(input("Which # item would you like to mark as done?"))
            todos.pop(number-1)

            with open('todos.txt', 'w') as file:
                file.writelines(todos)

        case 'exit':
            print("All done, see you later!")
            break
        case whatever:
            print("That's not what I asked you to do, please enter one of the listed commands.")
