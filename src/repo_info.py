from collections import OrderedDict
from datetime import datetime

import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import streamlit as st
from github.Repository import Repository


def repo_info(repo: Repository):
    def topics(repo):
        repository_topics = repo.get_topics()
        st.title("Topics of this repo: ")
        for topic in repository_topics:
            st.markdown(topic)

    def contents(repo):
        repository_contents = repo.get_contents("")
        st.title("All of the contents of the root directory of the repository: ")
        for content in repository_contents:
            st.markdown(content.path)

    def stargazers(repo):
        repository_stargazers = repo.stargazers_count
        st.title("Stars of the repository: ")
        st.markdown(f":star: {repository_stargazers}")

    def repo_labels(repo):
        repository_labels = repo.get_labels()
        labels = list(map(lambda label: label.name, repository_labels))

        st.title("All labels: ")
        for label in labels:
            st.text(label)

    def top_10_lables(repo):
        repository_labels = repo.get_labels()
        labels = list(map(lambda label: label.name, repository_labels))

        labels_count = {word: 0 for word in labels}

        issues = repo.get_issues()

        for issue in issues:
            labs = issue.labels
            for label in labs:
                for respite_word in labels:
                    if respite_word in label.name:
                        labels_count[respite_word] += 1

        top_10_labels = OrderedDict(
            sorted(
                labels_count.items(),
                key=lambda item: item[1],
                reverse=True,
            )
        )
        top = dict(list(top_10_labels.items())[:10])

        df = pd.Series(top)
        df = pd.DataFrame(list(top.items()), columns=["Type", "Count"])
        df.index = df.index + 1

        st.table(df)

        fig = go.Figure(data=[go.Pie(labels=df["Type"], values=df["Count"])])
        fig.update_layout(title="Top 10 labels")

        st.plotly_chart(fig, theme=None, use_container_width=True)

        fig = px.bar(df, x=df["Type"], y=df["Count"])

        st.plotly_chart(fig, theme=None, use_container_width=True)

    def repo_milestones(repo):
        repository_milestones = repo.get_milestones()
        milestones = list(
            filter(
                lambda milestone: milestone.title,
                repository_milestones,
            )
        )
        for milestone in milestones:
            st.write("Milestone ", milestone.title)
            st.metric(label="Due on", value=(milestone.due_on).strftime("%B %d, %Y"))
            st.metric(label="Closed issues", value=milestone.closed_issues)

            st.metric(
                label="Milestone updated at",
                value=str(
                    datetime.now((milestone.updated_at).tzinfo) - milestone.updated_at
                ),
            )
            st.divider()

    def branches_in_project(repo):
        branches = repo.get_branches()
        st.title("Branches of the repository: ")
        for branche in branches:
            st.markdown(branche.name)

    def languages_in_project(repo):
        languages = repo.language
        st.title("Languages in the repository: ")
        st.markdown(languages)

    tab1, tab2, tab3 = st.tabs(["General", "Labels", "Milestones"])

    with tab1:
        st.header("General")
        stargazers(repo)
        languages_in_project(repo)
        topics(repo)
        contents(repo)
        branches_in_project(repo)

    with tab2:
        st.header("Labels")
        top_10_lables(repo)
        repo_labels(repo)

    with tab3:
        st.header("Milestones")
        repo_milestones(repo)
