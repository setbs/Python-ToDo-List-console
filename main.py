while True:
    user_action = input("Type add, show, edit, complete or exit: ")
    user_action = user_action.strip()

    if user_action.startswith('add'):
        todo = user_action[4:] + '\n'

        with open('files/todos.txt', 'r') as file:
            todos = file.readlines()

        todos.append(todo)

        with open('files/todos.txt', 'w') as file:
            file.writelines(todos)
    elif user_action.startswith('show'):
        print(f'Here your things to do: \n {'-' * 20}')
        with open('files/todos.txt', 'r') as file:
            todos = file.readlines()


        for index, item in enumerate(todos):
            row = f"{index + 1}-{item.strip('\n')}"
            print(row)
        print('-' * 20)
    elif user_action.startswith('edit'):
        try:
            number = int(user_action[5:])

            with open('files/todos.txt', 'r') as file:
                todos = file.readlines()
            old_todo = todos[number - 1].strip('\n')
            new_todo = input("Enter new todo: ")
            todos[number - 1] = new_todo + '\n'

            with open('files/todos.txt', 'w') as file:
                file.writelines(todos)
            print(f"{'-' * 20}\nYour todo {old_todo} was repased to {new_todo}\n{'-' * 20}")
        except ValueError:
            print(f"{'-' * 20}\n Something went wrong \n Try use a number of todo after exit function \n{'-' * 20}")
            continue
    elif user_action.startswith('complete'):
        try:
            number = int(user_action[9:])
            with open('files/todos.txt', 'r') as file:
                todos = file.readlines()

            todo_to_remove = todos[number - 1].strip('\n')
            todos.pop(number - 1)


            with open('files/todos.txt', 'w') as file:
                file.writelines(todos)

            print(f'Todo "{todo_to_remove}" was removed from the list')
        except IndexError:
            print(f"{'-' * 15}\n Error, List index out of range \n{'-' * 15}")
            continue

    elif user_action.startswith('exit'):
        break
    else:
        print("Command is not valid")

print(f"{'-' * 15} Bye!! {'-' * 15}")
