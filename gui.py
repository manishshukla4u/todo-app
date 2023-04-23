import functions
import PySimpleGUI as gui

label = gui.Text("Type in a to-do")       ## This is label to the text box
input_box = gui.InputText(key='todo')    ## This is suggestion text appear when we hover cursor on text-box in window
add_button = gui.Button("Add")       ## To add button in the window
#show_button

## Windows method to create a GUI window, So we use read/close methods to open/close the window
window = gui.Window("My To-Do App",
                    layout=[[label, input_box, add_button]],
                    font=('Helvetica', 20))

while True:
    event, values = window.read()
    print(event)
    print(values)
    match event:
        case "Add":
            todos = functions.get_todo()
            new_todo = values['todo'] + "\n"
            todos.append(new_todo)
            functions.write_todos(todos)
        case gui.WIN_CLOSED:
            break

window.close()


