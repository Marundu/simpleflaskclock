from flask import Flask, render_template
import time

app=Flask(__name__)

@app.route('/')
def current_day_and_time():
	time_now=time.strftime('%I:%M %p %Z')
	day_today=time.strftime('%A, %B %d, %Y')
	return render_template('time.html', time_now=time_now, day_today=day_today)

if __name__=='__main__':
	app.run(debug=True, port=7096)