import functions
import PySimpleGUI as gui

label = gui.Text("Type in a to-do")       ## This is label to the text box
input_box = gui.InputText(key='todo')    ## This is suggestion text appear when we hover cursor on text-box in window
add_button = gui.Button("Add")       ## To add button in the window
list_box = gui.Listbox(values=functions.get_todo(), key="items",
                       enable_events=True, size=[45, 10])
edit_button = gui.Button("Edit")

## Windows method to create a GUI window, So we use read/close methods to open/close the window
window = gui.Window("My To-Do App",
                    layout=[[label, input_box, add_button], [list_box, edit_button]],
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
            window["items"].update(values=todos)
        case "Edit":
            todo_to_edit = values["items"][0]
            new_todo = values["todo"] + "\n"

            todos = functions.get_todo()
            index = todos.index(todo_to_edit)
            todos[index] = new_todo
            functions.write_todos(todos)
            window["items"].update(values=todos)      ### Here, we are updating todo list to display in edit box, we selected "items" key from windows refresh/update that with new todos list
        case "items":
            window["todo"].update(value=values["items"][0])
        case gui.WIN_CLOSED:
            break


window.close()


