from flask import Flask
from flask import render_template

app = Flask("Hello World")


@app.route('/index')
def startseite():
    return render_template('index.html')

@app.route('/erfassen')
def erfassen():
    return render_template('erfassen.html')


if __name__ == "__main__":
    app.run(debug=True, port=5000)
