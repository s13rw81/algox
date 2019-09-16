from flask import  Flask, render_template
import os, datetime

app = Flask(__name__)

port = int(os.getenv('PORT', 8000))

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/positions/')
def positions():
    return render_template('positions.html')


@app.route('/holdings/')
def holdings():
    return render_template('holdings.html')


@app.route('/orders/')
def orders():
    return render_template('orders.html')


@app.route('/profile/')
def profile():
    return render_template('profile.html')


@app.route('/showtime/')
def showtime():
    utc = datetime.datetime.utcnow().ctime()
    loc = datetime.datetime.now().ctime()
    return render_template('showtime.html', utc = utc, loc = loc)





if __name__ == '__main__':
    # app.run(host='localhost', port=80, debug = True)
    app.run(host='0.0.0.0', port=port)