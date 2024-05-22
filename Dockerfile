FROM python:3.12

WORKDIR /github-statistic-directory

COPY requirements.txt .

COPY . .

RUN pip install -r requirements.txt


CMD ["streamlit", "run", "src/main.py"]
