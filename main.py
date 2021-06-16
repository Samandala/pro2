from flask import Flask
from flask import render_template

import daten

app = Flask("Hello World")


@app.route('/') # Seitenverlinkung Startseite
def startseite():
    return render_template('index.html')


@app.route('/erfassen') # Seitenverlinkung Erfassen
def erfassen():
    return render_template('erfassen.html')


@app.route('/weinkeller') # Seitenverlinkung Weinkeller
def weinkeller():
    weine = daten.weine_laden()
    return render_template('weinkeller.html', weine=weine)


@app.route("/speichern/<aktivitaet>") # Daten speichern
def speichern(aktivitaet):
    zeitpunkt, aktivitaet = daten.aktivitaet_speichern(aktivitaet)

    return "Gespeichert: " + aktivitaet + " um " + str(zeitpunkt)


@app.route("/liste")
def auflisten():
    aktivitaeten = daten.aktivitaeten_laden()

    aktivitaeten_liste = ""
    for key, value in aktivitaeten.items():
        zeile = str(key) + ": " + value + "<br>"
        aktivitaeten_liste += zeile

    return aktivitaeten_liste

"""
@app.route('/weine/erfassen', methods=['GET', 'POST'])
def erfassen():
    if request.method == 'POST':
        wine_create_data = request.form.to_dict()
        mv.save_wine(movie_create_data)
        return redirect(url_for('movies'))
    return render_template('movie_create.html')
"""



if __name__ == "__main__":
    app.run(debug=True, port=5000)
