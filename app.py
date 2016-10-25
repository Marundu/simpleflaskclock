from flask import Flask, render_template
import time

app=Flask(__name__)

@app.route('/')
def current_date_and_time():
	time_now=time.strftime('%I:%M%p %Z')
	date_now=time.strftime('%A %B %Y')
	return render_template('time.html', time_now=time_now, date_now=date_now)

if __name__=='__main__':
	app.run(debug=True, port=7096)