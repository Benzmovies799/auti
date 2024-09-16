# Don't Remove Credit @AmRobots_Bots
# Subscribe YouTube Channel For Amazing Bot @AmRobotsTech
# Ask Doubt on telegram @Am_Robots

FROM python:3.10.8-slim-buster

RUN apt update && apt upgrade -y
RUN apt install git -y
COPY requirements.txt /requirements.txt

RUN cd /
RUN pip3 install -U pip && pip3 install -U -r requirements.txt
RUN mkdir /BENZMOVIES-FILTER-BOT
WORKDIR /BENZMOVIES-FILTER-BOT
COPY . /BENZMOVIES-FILTER-BOT
CMD ["python", "bot.py"]
