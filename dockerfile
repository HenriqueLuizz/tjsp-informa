FROM python:3

WORKDIR /usr/src/app

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

ENV BOT_TOKEN=''
ENV BOT_CHATID=''

CMD [ "python", "./bot_tjsp.py" ]