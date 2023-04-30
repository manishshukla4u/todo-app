import functions
import PySimpleGUI as gui
import time
import os

if not os.path.exists("todo.txt"):
    with open("todo.txt", "w") as file:
        pass

clock = gui.Text("", key="Clock")
label = gui.Text("Type in a to-do")       ## This is label to the text box
input_box = gui.InputText(key='todo')    ## This is suggestion text appear when we hover cursor on text-box in window
add_button = gui.Button("Add", key="Add")       ## To add button in the window + Add image to button
list_box = gui.Listbox(values=functions.get_todo(), key="items",
                       enable_events=True, size=[45, 10])
edit_button = gui.Button("Edit")
complete_button = gui.Button("Complete", key="Complete")
exit_button = gui.Button("Exit")

## Windows method to create a GUI window, So we use read/close methods to open/close the window
window = gui.Window("My To-Do App",
                    layout=[[clock],
                            [label],
                            [input_box, add_button],
                            [list_box, edit_button, complete_button],
                            [exit_button]],
                    font=('Helvetica', 20))

while True:
    event, values = window.read(timeout=200)   # This timeout would refresh the windows.read after every 200 Micro-seconds to update time-clock on gui window
    window["Clock"].update(value=time.strftime("%b %d, %Y %H:%M:%S"))
    print(event)
    print(values)
    match event:
        case "Add":
            todos = functions.get_todo()
            new_todo = values['todo'] + "\n"
            todos.append(new_todo)
            functions.write_todos(todos)
            window["items"].update(values=todos)
            window["todo"].update(value="")
        case "Edit":
            try:
                todo_to_edit = values["items"][0]
                new_todo = values["todo"] + "\n"

                todos = functions.get_todo()
                index = todos.index(todo_to_edit)
                todos[index] = new_todo
                functions.write_todos(todos)
                window["items"].update(values=todos)      ### Here, we are updating todo list to display in edit box, we selected "items" key from windows refresh/update that with new todos list
                window["todo"].update(value="")
            except IndexError:
                gui.popup("Please select an item first", font=("Helventica", 15))
        case "Complete":
            try:
                todo_to_complete = values["items"][0]
                todos = functions.get_todo()
                todos.remove(todo_to_complete)
                functions.write_todos(todos)
                window["items"].update(values=todos)
                window['todo'].update(value="")
            except IndexError:
                gui.popup("Please select an item first", font=("Helventica", 15))
        case "items":
            window["todo"].update(value=values["items"][0])
        case "Exit":
            break
        case gui.WIN_CLOSED:
            break


window.close()


