from github.Repository import Repository


def intro(repo: Repository):
    import streamlit as st

    st.title("This is the page about repo")
    st.code(repo.full_name)
