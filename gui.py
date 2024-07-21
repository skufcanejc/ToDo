import functions
import PySimpleGUI as sg

label = sg.Text("Type in a To-Do")
input_box = sg.InputText(tooltip='Enter To-Do')
add_button = sg.Button("Add")

window = sg.Window("My To-Do app", layout=[[label], [input_box], [add_button]])
window.read()

# This print function shows the app is only executed until here on open.
print("Hello")

window.close()