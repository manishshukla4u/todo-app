# from functions import get_todo, write_todos
# or
import functions
import time

now = time.strftime("%b %d, %Y %H:%M:%S")
print("It is ", now)

while True:
    user_action = input("Enter add, show, edit, complete or exit: ").strip()

    if user_action.startswith("add"):
        todo = user_action[4:] + "\n"

        todos = functions.get_todo()

        # Once user add new entry then save them in the existing list
        todos.append(todo)
        # Then write all content back to the file as open file in write mode
        functions.write_todos(todos, "todo.txt")

    elif user_action.startswith("show"):
        todos = functions.get_todo()

        # Removing extra line from content pulled from file because next print command is adding new line to each
        # iteration We are using list comprehensions below
        new_todos = [item.strip('\n') for item in todos]

        # adding sequence number to print list using enumerate function
        for index, item in enumerate(new_todos):
            print(f"{index + 1}.{item}")

    elif user_action.startswith("edit"):
        try:
            number = int(user_action[5:])
            number = number - 1
            new_value = input("Please enter the new value: ") + "\n"

            todos = functions.get_todo()

            todos[number] = new_value

            functions.write_todos(todos, "todo.txt")

        except ValueError:
            print("Your command is not valid.")
            continue


    elif user_action.startswith("complete"):
        try:
            number = int(user_action[9:])

            todos = functions.get_todo()

            index = number - 1
            todo_to_remove = todos[index].strip("\n")
            todos.pop(index)

            functions.write_todos(todos, "todo.txt")

            message = f"Todo {todo_to_remove} is removed."
            print(message)
        except IndexError:
            print("Please enter correct index value to complete.")
            continue

    elif user_action.startswith("exit"):
        break

    else:
        print("Command is not valid.")
print("Bye")