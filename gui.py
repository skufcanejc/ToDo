import functions
import PySimpleGUI as sg

label = sg.Text("Type in a To-Do")
input_box = sg.InputText(tooltip='Enter To-Do', key="TODO1")
add_button = sg.Button("Add")

window = sg.Window("My To-Do app", layout=[[label], [input_box], [add_button]],
                   font=("Helvetica", 20))


while True:
    event, values = window.read()
    # This print function shows the app is only executed until here on open.
    print("event = ", event)
    print("values = ", values)
    match event:
        case "Add":
            todos = functions.get_todos()
            new_todo = values['TODO1'] + "\n"
            todos.append(new_todo)
            functions.write_todos(todos)

        case sg.WIN_CLOSED:
            break
window.close()