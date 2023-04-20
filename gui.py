import functions
import PySimpleGUI as gui

label = gui.Text("Type in a to-do")       ## This is label to the text box
input_box = gui.InputText(tooltip="Enter todo")    ## This is suggestion text appear when we hover cursor on text-box in window
add_button = gui.Button("Add")       ## To add button in the window

## Windows method to create a GUI window, So we use read/close methods to open/close the window
window = gui.Window("My To-Do App", layout=[[label, input_box, add_button]])
window.read()
window.close()


