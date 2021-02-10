FROM python:3.7.1-alpine

WORKDIR /app

ADD . /app

RUN pip install -r requirements.txt

WORKDIR /app/French-CRS

RUN pip install -e .

RUN python -m spacy download fr_core_news_md

WORKDIR /app

CMD ["python","app.py"]