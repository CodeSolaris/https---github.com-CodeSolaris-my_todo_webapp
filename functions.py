FILEPATH: str = "todos.txt"


def window_update(todo_list: list, window: object) -> None:
    """
    Update the todo_list in the window with the given values.

    Args:
        todo_list: The list of todos.
        window: The window object to update.
    """
    window["todo_list"].update(values=todo_list)
    window["todo"].update(value="")


def get_position(action: str, prompt: str) -> int:
    """
    Get the position based on the given action and prompt.

    Args:
        action: The action to perform.
        prompt: The prompt to display.

    Returns:
        The position.
    """
    if action == "edit" or action == "complete":
        number = int(input(prompt)) - 1
    else:
        number = int(action.replace("edit", "").replace("complete", "").strip()) - 1
    return number


def write_todo_list(todo_list: list, file_path: str = FILEPATH) -> None:
    """
    Write the todo_list to the file with the given file_path.

    Args:
        todo_list: The list of todos.
        file_path: The file path to write to.
    """
    with open(file_path, "w") as file:
        file.writelines(todo_list)


def get_todo_list(file_path: str = FILEPATH) -> list:
    """
    Get the todo_list from the file with the given file_path.

    Args:
        file_path: The file path to read from.

    Returns:
        The list of todos.
    """
    with open(file_path, "r") as file:
        todo_list = file.readlines()
    return todo_list


def add_todo(todo: str, file_path: str = FILEPATH) -> None:
    """
    Add a todo to the todo_list.

    Args:
        todo: The todo to add.
        file_path: The file path to write to.
    """
    if todo:
        todo_list = get_todo_list(file_path)
        todo = todo.capitalize() + "\n"
        if todo not in todo_list:
            todo_list.append(todo)
        write_todo_list(todo_list, file_path)


def display_todo_list() -> None:
    """
    Display the todos in the todo_list.
    """
    todo_list = get_todo_list()
    for index, item in enumerate(todo_list):
        print(f"{index + 1}. {item.strip()}")


def edit_todo(action: str) -> None:
    """
    Edit a todo based on the given action.

    Args:
        action: The action to perform.
    """
    number = get_position(
        action, "Please, enter a position to edit (must be a number): "
    )
    try:
        todo_list = get_todo_list()
        new_todo = input("Enter a new todo: ")
        todo_list[number] = new_todo.capitalize() + "\n"
        write_todo_list(todo_list)
    except ValueError:
        print("Please, enter a valid number.")


def complete_todo(action: str) -> None:
    """
    Complete a todo based on the given action.

    Args:
        action: The action to perform.
    """
    number = get_position(
        action, "Please, enter a position to complete (must be a number): "
    )
    try:
        todo_list = get_todo_list()
        todo_to_complete = todo_list.pop(number).strip()
        message = f"You have completed {todo_to_complete}"
        print(message)
        write_todo_list(todo_list)
    except IndexError:
        print("Please, enter a valid position.")
