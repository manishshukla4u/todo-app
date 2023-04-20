# Open the file as file object in read-only mode
# Read all lines in file as list and saved as todos, because we dont want to overwrite the file content in each exexution
def get_todo(filepath="todo.txt"):
    """
    Read a test file and return the list of
    to-do items.
    :param filepath:
    :return:
    """
    with open(filepath, "r") as file_local:
        todos_local = file_local.readlines()
    return todos_local

def write_todos(todos_args, filepath="todo.txt"):
    """
    Write the to-do items in the text file. These are the doc-strings of this function.
    :param todos_args:
    :param filepath:
    :return:
    """
    with open(filepath, "w") as file:
        file.writelines(todos_args)

## If we want to run code during only direct file execution not by calling as module
if __name__ == "__name__":
    print("Hello")
    print(get_todo())