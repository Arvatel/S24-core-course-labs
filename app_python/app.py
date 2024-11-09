from flask import Flask, render_template
from datetime import datetime
import pytz

TIME_FORMAT = "%Y-%m-%d %H:%M:%S"
TIMEZONE = "Europe/Moscow"

app = Flask(__name__)

def get_time(timezone):
	return datetime.now(timezone)


def format_time(time, time_format):
	return time.strftime(time_format)

@app.route('/')
def moscow_time_show():
	timezone = pytz.timezone(TIMEZONE)
	time = get_time(timezone)

	time_format = format_time(time, TIME_FORMAT)
	return render_template('index.html', time=time_format)

if __name__ == '__main__':
	app.run(debug=True)
