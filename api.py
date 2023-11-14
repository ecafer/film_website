from flask import Flask, render_template, request


app = Flask(__name__)


@app.route('/movie_entry', methods=['GET', 'POST'])
def enter_movie():

    if request.method == "POST":
        try:
            title = request.form.get('title')
            director = request.form.get('director')
            release_year = request.form.get('releaseYear')
            country = request.form.get('country')
            myRating = request.form.get('myRating')
            short = request.form.get('short')
            print(title, director, release_year, country, myRating, short)
        except KeyError:
            print('Make sure the field exists.')
    return render_template('homepage.html')

