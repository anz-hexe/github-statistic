# GitHub Statistics Dashboard

This project is a Streamlit application that provides detailed statistics and information about a specified GitHub repository. It leverages the GitHub API to fetch data and uses Plotly for interactive visualizations. The application is organized into multiple tabs for easy navigation and a comprehensive view of repository metrics.

## Features

- **Repository Overview**: General information about the repository.
- **Issues Information**: Detailed statistics and insights about the issues in the repository.
- **Pull Requests Information**: Detailed statistics and insights about the pull requests in the repository.

## Installation

### Using Conda

To set up the environment using `conda`, create the environment from the `env.yml` file:

```bash
conda env create -f env.yml
conda activate github-statistic
```

### Using Docker

You can also run the application using Docker. First, build the Docker image:

```bash
docker build -t github-statistics-dashboard .
```

Then, run the Docker container:

```bash
docker run -p 8501:8501 github-statistics-dashboard
```

### Using Python and Pip

If you prefer to use `pip`, install the dependencies using:

```bash
pip install -r requirements.txt
```

## Usage

To start the Streamlit application, run the following command:

```bash
streamlit run main.py
```

If using Docker, the application will be accessible at `http://localhost:8501` once the container is running.

## Modules

### `main.py`

The entry point of the application. It sets up authentication, retrieves the specified repository, and configures the Streamlit app with multiple tabs for different views.

### `intro.py`

Displays introductory information about the repository, including the full name of the repository.

### `issues_info.py`

Provides detailed statistics and insights about the issues in the repository, organized into the following sub-sections:
- **Labeled vs Unlabeled Issues**
- **Commented vs Uncommented Issues**
- **Assigned vs Unassigned Issues**
- **Recent Issues**
- **Milestones**
- **Pull Requests**
- **Locked Issues**
- **Comments**
- **Events**

### `pulls_info.py`

Displays detailed information about the pull requests in the repository, including:
- **Number**
- **Title**
- **State**
- **Updated At**
- **User**
- **Head SHA**
- **Body**
- **Merge Commit SHA**
- **Merged At**
- **Changed Files**

### `repo_info.py`

Provides comprehensive information about the repository, organized into the following sub-sections:
- **General**
  - **Stargazers**
  - **Languages**
  - **Topics**
  - **Contents**
  - **Branches**
- **Labels**
  - **Top 10 Labels**
  - **All Labels**
- **Milestones**
  - **Titles**
  - **Due Dates**
  - **Closed Issues**

## Configuration

Ensure you have the following environment variables set up in a `config.py` file:
- `GITHUB_REPO`: The full name of the GitHub repository (e.g., `username/repo`).
- `GITHUB_TOKEN`: Your GitHub personal access token.