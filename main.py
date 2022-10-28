
from optparse import Values
from flask import Flask, render_template, request, json
from pandas import value_counts
from movie import get_movies
from bank import getbank
from bike import get_bike, looking_bike

app = Flask(__name__)


@app.route('/')
@app.route('/<name>')
def index(name='GUEST'):
    return render_template('./index.html', name=name, date=getdate())


@app.route('/bank')
def bank():
    date = getdate()
    columns, values, cointime = getbank()

    return render_template('./bank.html', **locals())


@app.route('/movie')
def movie():

    columns, values = get_movies()

    return render_template('./movies.html', **locals())


@app.route('/movie-json', methods=['POST'])
def movie_json():
    columns, values = get_movies()
    titles = [value[0] for value in values]
    expect = [value[1] for value in values]

    return json.dumps({'title': titles, 'expect': expect}, ensure_ascii=False)


@app.route('/date')
def getdate():
    from datetime import datetime
    date = datetime.now()

    return date.strftime('%Y-%m-%d %H:%M:%S')


@app.route('/bike')
def getbike():
    columns, values, site = get_bike()
    return render_template('./bike.html', **locals())


@app.route('/bike-json', methods=['POST'])
def bike_json():
    columns, values = looking_bike()
    titles = [value[0:] for value in values]

    return json.dumps({'title': titles}, ensure_ascii=False)


if __name__ == '__main__':
    movie_json()
    bike_json()
    app.run(debug=True)
