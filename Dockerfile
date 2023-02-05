FROM python:3.9

ENV PYTHONUNBUFFERED=1

WORKDIR /app

RUN apt-get update && apt-get install -y cron

COPY requirements.txt requirements.txt

RUN pip3 install --upgrade pip
RUN pip3 install -r requirements.txt


COPY . /app/

# Set up the cron job
# RUN echo "*/5 * * * * root echo '' > /app/app/app.log" > /etc/cron.d/clear-logs
# RUN chmod 0644 /etc/cron.d/clear-logs
# RUN crontab /etc/cron.d/clear-logs


EXPOSE 8000