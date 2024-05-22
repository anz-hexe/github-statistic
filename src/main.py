from functools import partial

import streamlit as st
from github import Auth, Github

from config import GITHUB_REPO, GITHUB_TOKEN
from intro import intro
from issues_info import issues_info
from pulls_info import pulls_info
from repo_info import repo_info

if __name__ == "__main__":
    token = Auth.Token(GITHUB_TOKEN)
    github_instance = Github(auth=token)
    repo = github_instance.get_repo(GITHUB_REPO)

    issues_info_for_repo = partial(issues_info, repo)
    repository_info = partial(repo_info, repo)
    repository_intro = partial(intro, repo)
    pull_requests_info = partial(pulls_info, repo)

    st.set_page_config(
        page_title="GitHub statistic",
        page_icon="👾",
    )

    page_names_to_funcs = {
        "—": repository_intro,
        "About issues": issues_info_for_repo,
        "About repo": repository_info,
        "About pulls": pull_requests_info,
    }

    demo_name = st.sidebar.selectbox("Choose a demo", page_names_to_funcs.keys())
    page_names_to_funcs[demo_name]()
