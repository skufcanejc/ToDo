def todos_print():
    with open('todos.txt', 'r') as todos:
        new_todos = [item.strip("\n") for item in todos]
        for i, item in enumerate(new_todos):
            row = f"{i + 1} - {item}"
            print(row)

def get_todos(filepath='todos.txt'):
    """Read the text file and return it as a list."""
    with open(filepath,'r') as f:
        todos_local = f.readlines()
    return todos_local

def write_todos(todos_arg, filepath='todos.txt'):
    """Write the to-do list in a text file as separate lines."""
    with open(filepath, 'w') as f:
        f.writelines(todos_arg)


if __name__ == "__main__":
    print("hello")
    print(get_todos())