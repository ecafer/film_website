from flask import Flask, render_template, request


app = Flask(__name__)


@app.route('/movie_entry', methods=['GET', 'POST'])
def enter_movie():
    if request.method == "GET":
        return render_template('homepage.html')
    elif request.method == "POST":
        print(request.form)
        title = request.form.get('title')
        print(title)
        return render_template('homepage.html')
    else:
        print('UNKNOWN HTTP REQUEST')
