import streamlit as st
import functionz

def add_todo():
    new_todo = st.session_state["new_todo"] + '\n'
    todos.append(new_todo)
    functionz.write_todos(todos)
todos = functionz.get_todos()

st.title("My todo app")
for index, todo in enumerate(todos):
    checkbox = st.checkbox(todo, key=todo)
    if checkbox:
        todos.pop(index)
        functionz.write_todos(todos)
        del st.session_state[todo]
        st.experimental_rerun()

st.text_input(label="something", label_visibility='collapsed',
              placeholder="Enter a todo...",
              on_change=add_todo,
              key="new_todo")
print("todo1", "todo2")