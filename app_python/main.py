from flask import Flask, render_template
from datetime import datetime
import pytz
import os

app = Flask(__name__)

TIME_FORMAT = "%Y-%m-%d %H:%M:%S"
TIMEZONE = "Europe/Moscow"
VISITS_FILE_PATH = "data/visits"


def get_time(timezone):
    return datetime.now(timezone)


def format_time(time, time_format):
    return time.strftime(time_format)


@app.get("/visits")
def get_visits():
    with open(VISITS_FILE_PATH, "r") as file:
        visits = int(file.read())
    return {"visits": visits}


def update_visits():
    try:
        with open(VISITS_FILE_PATH, "r+") as file:
            visits = int(file.read())
            visits += 1
            file.seek(0)
            file.write(str(visits))
    except FileNotFoundError:
        init_value = 1
        with open(VISITS_FILE_PATH, "w+") as file:
            file.write(str(init_value))


@app.route('/')
def moscow_time_show():
    update_visits()
    timezone = pytz.timezone(TIMEZONE)
    time = get_time(timezone)

    time_format = format_time(time, TIME_FORMAT)
    return render_template('index.html', time=time_format)


if __name__ == '__main__':
    app.run(debug=True)
