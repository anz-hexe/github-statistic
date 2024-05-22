from datetime import datetime, timedelta

import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import streamlit as st
from github.Repository import Repository


def issues_info(repo: Repository):
    def issues_labeled(repo):
        issues = repo.get_issues()

        labeled = len(list(filter(lambda issue: bool(issue.labels), issues)))
        unlabeled = len(list(filter(lambda issue: not bool(issue.labels), issues)))

        data = {
            "labeled": labeled,
            "unlabeled": unlabeled,
        }

        df = pd.Series(data)
        df = pd.DataFrame(list(data.items()), columns=["Type", "Count"])

        fig = go.Figure(data=[go.Pie(labels=df["Type"], values=df["Count"])])
        fig.update_layout(title="Labeled and unlabeled issues in repository")

        st.plotly_chart(fig, theme=None, use_container_width=True)

        fig = px.bar(df, x=df["Type"], y=df["Count"])

        st.plotly_chart(fig, theme=None, use_container_width=True)

        labeled = repo.get_labels()

    def issues_commented(repo):
        issues = repo.get_issues()

        commented = len(list(filter(lambda issue: bool(issue.comments), issues)))
        no_comments = len(list(filter(lambda issue: not bool(issue.comments), issues)))

        data = {
            "Issues commented": commented,
            "Issues no comments": no_comments,
        }

        df = pd.Series(data)
        df = pd.DataFrame(list(data.items()), columns=["Type", "Count"])

        fig = go.Figure(data=[go.Pie(labels=df["Type"], values=df["Count"])])
        fig.update_layout(title="Issues with and without comments in repository")

        st.plotly_chart(fig, theme=None, use_container_width=True)

    def issues_assigned(repo):
        issues = repo.get_issues()[:100]

        assigned = len(list(filter(lambda issue: bool(issue.assignee), issues)))
        unassigned = len(list(filter(lambda issue: not bool(issue.assignee), issues)))

        data = {
            "Assigned issues": assigned,
            "Unassigned issues": unassigned,
        }

        df = pd.Series(data)
        df = pd.DataFrame(list(data.items()), columns=["Type", "Count"])

        fig = go.Figure(data=[go.Pie(labels=df["Type"], values=df["Count"])])
        fig.update_layout(title="Assigned and unassigned issues in repository")
        st.plotly_chart(fig, theme=None, use_container_width=True)

    def issues_recent(repo):
        issues = repo.get_issues()[:200]

        today = datetime.now().date()
        yesterday = today - timedelta(days=1)

        filtered_issues_today = len(
            [issue.id for issue in issues if issue.created_at.date() in [today]]
        )

        filtered_issues_yesterday = len(
            [issue.id for issue in issues if issue.created_at.date() in [yesterday]]
        )

        data = {
            "New issues (yesterday):": filtered_issues_yesterday,
            "New issues (today):": filtered_issues_today,
        }

        df = pd.Series(data)
        df = pd.DataFrame(list(data.items()), columns=["Type", "Count"])

        fig = go.Figure(
            data=[
                go.Scatter(
                    x=df["Type"],
                    y=df["Count"],
                    mode="markers",
                    marker_size=[filtered_issues_today, filtered_issues_yesterday],
                )
            ]
        )

        st.plotly_chart(fig, theme=None, use_container_width=True)

        fig = px.histogram(
            df, x=df["Type"], y=df["Count"], color_discrete_sequence=["#A075AE"]
        )

        st.plotly_chart(fig, theme=None, use_container_width=True)

    def issues_milestone(repo):
        issues = repo.get_issues()
        milestones = len(list(filter(lambda issue: bool(issue.milestone), issues)))

        st.metric(label="milestone", value=milestones, delta_color="inverse")

    def issues_pull_request(repo):
        issues = repo.get_issues()[:500]

        pull_requested = len(
            list(filter(lambda issue: bool(issue.pull_request), issues))
        )
        no_pull_requested = len(
            list(filter(lambda issue: not bool(issue.pull_request), issues))
        )

        data = {
            "total issues by pull requests": pull_requested,
            "total issues by not pull requests": no_pull_requested,
        }

        df = pd.Series(data)
        df = pd.DataFrame(list(data.items()), columns=["Type", "Count"])

        fig = go.Figure(data=[go.Pie(labels=df["Type"], values=df["Count"])])
        fig.update_layout(title="Pull requests by issues")

        st.plotly_chart(fig, theme=None, use_container_width=True)

    def issues_locked(repo):
        issues = repo.get_issues()

        locked = list(filter(lambda issue: bool(issue.locked), issues))
        active_lock_reason = list(
            filter(lambda issue: bool(issue.active_lock_reason), issues)
        )

        st.write("Locked issues", locked)
        st.write("Active lock reason issues", active_lock_reason)

    def get_comments_in_issues(repo):
        issues = repo.get_issues()

        for issue in issues:
            st.write("ID issue", issue.id)
            st.write("Comments", list(issue.get_comments()))
            comments = issue.get_comments()
            for comment in comments:
                st.write("Comments ID ", comment.id)
                st.write("Link to issue ", comment.issue_url)
            st.divider()

    def get_event_in_issues(repo):
        issues = repo.get_issues()
        for issue in issues:
            st.write("Issue ID", issue.id)
            events = issue.get_events()
            st.write(list(events))
            for event in events:
                st.write("Issue event", event.issue)
                st.write("ID event", event.id)
                st.write("Event", event.event)

    tab1, tab2, tab3, tab4, tab5, tab6, tab7, tab8, tab9 = st.tabs(
        [
            "Labels",
            "Commented",
            "Assigned",
            "Latest",
            "Milestones",
            "Pull request",
            "Locked",
            "Comments",
            "Events",
        ]
    )

    with tab1:
        st.header("Labeled and unlabeled issues in repository")
        issues_labeled(repo)

    with tab2:
        st.header("Issues with and without comments")
        issues_commented(repo)

    with tab3:
        st.header("Assigned and unassigned issues")
        issues_assigned(repo)

    with tab4:
        st.header("Latest issues in repository")
        issues_recent(repo)

    with tab5:
        st.header("Milestones in repository")
        issues_milestone(repo)

    with tab6:
        st.header("Pull requests in repository")
        issues_pull_request(repo)

    with tab7:
        st.header("Locked issues")
        issues_locked(repo)

    with tab8:
        st.header("Comments in issues")
        get_comments_in_issues(repo)

    with tab9:
        st.header("Events in issues")
        get_event_in_issues(repo)
