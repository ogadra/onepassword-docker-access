FROM python:3

RUN apt-get update -y

ENV LANGUAGE ja_JP.ja \
    LANG ja_JP.UTF-8 \
    LC_ALL=ja_JP.UTF-8
RUN apt-get install -y --no-install-recommends locales && \
    locale-gen ja_JP.UTF-8

COPY . /root/app/
WORKDIR /root/app/

RUN pip install --upgrade pip
RUN pip install --upgrade setuptools

RUN python -m pip install -r requirements.txt
CMD ["python", "main.py"]
