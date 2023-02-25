from flask import Flask, render_template, request
import json
import os


app = Flask(__name__)
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')


with open('my.json') as user_file:
    zodiac = json.load(user_file)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/all")
def all():
    return zodiac


@app.route("/search")
def search():
    query_sign = request.args.get("sign")
    result = zodiac[query_sign]
    return result


if __name__ == '__main__':
    app.run(debug=True)
