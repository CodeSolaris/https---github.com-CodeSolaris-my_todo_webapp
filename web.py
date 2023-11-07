import streamlit as st

import functions

todo_list = functions.get_todo_list()


def add_to_webapp_todolist():
    todo = st.session_state["new_todo"]
    functions.add_todo(todo)


st.title("My To-Do App")
st.write("This app is to increase your productivity")

for index, todo in enumerate(todo_list):
    checkbox = st.checkbox(todo, key=todo)
    if checkbox:
        confirm = st.button(
            "Confirm to complete", help="Press confirm to complete this todo"
        )
        if confirm:
            todo_list.pop(index)
            functions.write_todo_list(todo_list)
            del st.session_state[todo]
            st.rerun()


new_todo_input = st.text_input(
    "Add a new todo", key="new_todo", help="Add a new todo to your list",
    on_change=add_to_webapp_todolist
)
