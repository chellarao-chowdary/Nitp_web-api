# Coded by Chellarao Chowdary on 25th Oct 2020

from flask import Flask,jsonify,request
from scrape import getNews
from flask_cors import CORS

app=Flask(__name__)
app.secret_key=""
CORS(app)

@app.route('/')
def home():
	return 'NITP Website API is UP! <br><br> <strong> Made with love in  \U0001F1EE\U0001F1F3 by <a href="https://github.com/chellarao-chowdary/">Chellarao Chowdary</a>'


@app.route('/news')
def news():
    if request.method == 'GET':
        return jsonify(getNews(request.args.get('category')))

if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0',port=5000,use_reloader=True)
