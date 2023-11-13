from flask import Flask, render_template


app = Flask(__name__)


@app.route('/enter_movie')
def enter_movie():
    return render_template('homepage.html')