import functions
import PySimpleGUI as sg
import time

sg.theme('Reddit')

clock = sg.Text('', key='clock')
label = sg.Text("Type in a To-Do")
input_box = sg.InputText(tooltip='Enter To-Do', key="todo")
add_button = sg.Button("Add")
list_box = sg.Listbox(values=functions.get_todos(), key = 'todos_list',
                      enable_events=True, size=[45, 10])
edit_button = sg.Button("Edit")
complete_button = sg.Button("Complete")
exit_button = sg.Button("Exit")

window = sg.Window("My To-Do app", layout=[[clock],
                                           [label], 
                                           [input_box, add_button],
                                           [list_box, edit_button, complete_button],
                                           [exit_button]],
                                    font=("Helvetica", 16))


while True:
    event, values = window.read(timeout=100)
    window['clock'].update(value=time.strftime("%H:%M:%S %d-%m-%Y"))
    # This print function shows the app is only executed until here on open.
    # print(1, "event = ", event)
    # print(2, "values = ", values)
    # print(3, values['todos_list'])
    match event:
        case "Add":
            todos = functions.get_todos()
            new_todo = values['todo'] + "\n"
            todos.append(new_todo)
            functions.write_todos(todos)
            window['todos_list'].update(values=todos)
        case "Edit":
            try:
                todo_to_edit = values['todos_list'][0]
                new_todo = values['todo'] + '\n'
                todos = functions.get_todos()
                index = todos.index(todo_to_edit)
                todos[index] = new_todo
                functions.write_todos(todos)
                window['todos_list'].update(values=todos)
            except IndexError:
                sg.popup("Please select an item first.", font=("Helvetica", 14))
        case "Complete":
            try:
                todo_to_complete = values['todos_list'][0]
                todos = functions.get_todos()
                todos.remove(todo_to_complete)
                functions.write_todos(todos)          
                window['todos_list'].update(values=todos)
                window['todo'].update(value='')  
            except IndexError:
                sg.popup("Please select an item first.", font=("Helvetica", 14))
        case "Exit":
            break
        case "todos_list":
            window['todo'].update(value=values['todos_list'][0])
        case sg.WIN_CLOSED:
            break
window.close()