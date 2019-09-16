from flask import  Flask, render_template
import os, sqlite3

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
    conn = sqlite3.connect('cron_db.db')
    c = conn.cursor()
    c.execute('SELECT * FROM cron_table_01')
    res = c.fetchall()

    return render_template('showtime.html', res = res)





if __name__ == '__main__':
    # app.run(host='localhost', port=80, debug = True)
    app.run(host='0.0.0.0', port=port)