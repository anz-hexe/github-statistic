import streamlit as st
from github.Repository import Repository


def pulls_info(repo: Repository):
    def pulls_all(repo):
        pulls = repo.get_pulls()
        st.title("Pull requests in the repository: ")
        for pr in pulls:
            st.markdown(f":rainbow[Number] {pr.number}")
            st.markdown(f":rainbow[Title] {pr.title}")
            st.markdown(f":rainbow[State] {pr.state}")
            st.markdown(
                f":rainbow[Updated at] {(pr.updated_at).strftime("%d/%m/%Y, %H:%M:%S")}"
            )
            st.markdown(f":rainbow[User] {pr.user.login}")
            st.markdown(f":rainbow[Head] {pr.head.sha}")
            st.markdown(f":rainbow[Body] {pr.body}")
            st.markdown(f":rainbow[Merge commit sha] {pr.merge_commit_sha}")
            st.markdown(f":rainbow[Merged at] {pr.merged_at}")
            st.markdown(f":rainbow[Changed files] {pr.changed_files}")
            st.divider()

    pulls_all(repo)
