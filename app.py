from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/nvda')
def nvda():

    return render_template('nvda.html')


@app.route('/googl')
def googl():

    return render_template('google.html')


if __name__ == '__main__':
    app.run(debug=True)
