from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def hello():
    return render_template("canvas/draw.html")


@app.route('/test')
def test():
    return "Hello"


if __name__ == '__main__':
    app.run(host='0.0.0.0')
