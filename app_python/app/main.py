from flask import Flask, render_template
from datetime import datetime
import pytz

app = Flask(__name__)


@app.route('/')
def moscow_time_show():
 # Get the current time in Moscow
 TIMEZONE = 'Europe/Moscow'

 moscow_tz = pytz.timezone(TIMEZONE)
 
 current_time = datetime.now(moscow_tz).strftime('%Y-%m-%d %H:%M:%S')
 return render_template('index.html', time=current_time)

if __name__ == '__main__':
 app.run(debug=True)