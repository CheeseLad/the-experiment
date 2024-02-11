FROM python:3.11-slim-buster

WORKDIR /app

RUN python3 -m pip install -U discord.py
RUN python3 -m pip install requests

CMD [ "python3", "main.py" ]
