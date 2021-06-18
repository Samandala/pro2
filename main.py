from flask import Flask, url_for, redirect, request #diese Module werden hier importiert
from flask import render_template

import daten

app = Flask("Weinkeller")


#die Startseite wird hier direkt aufgerufen, da die url route "/" ist.
@app.route('/')  # Seitenverlinkung Startseite
def startseite():
    return render_template('index.html') #die Startseite als index.html wird gerendert.


#die url ruft die Seite weinkeller.html auf.
@app.route('/weinkeller', methods=["GET", "POST"])# Detailseite Wein
def weinkeller():  # gibt id mit

    if request.method == "POST":
        weine = daten.weine_laden()
        wein_id = request.form["wein_id"]
        print(wein_id)
        wein_detail = weine[wein_id]
        wein_jahrgang = weine[wein_id]["jahrgang"]
        wein_typ = weine[wein_id]["typ"]
        wein_herkunft = weine[wein_id]["herkunft"]
        wein_geschmack = weine[wein_id]["geschmack"]
        wein_bewertung = weine[wein_id]["bewertung"]
        wein_preis = weine[wein_id]["preis"]
        wein_name = weine[wein_id]["name"]

        return render_template('detail_wein.html',
                               wein_detail=wein_detail,
                               wein_jahrgang=wein_jahrgang,
                               wein_typ=wein_typ,
                               wein_herkunft=wein_herkunft,
                               wein_geschmack=wein_geschmack,
                               wein_bewertung=wein_bewertung,
                               wein_preis=wein_preis,
                               wein_name=wein_name
                               )

    weine = daten.weine_laden()
    return render_template('weinkeller.html', data=weine)

#auf der Seite erfassen werden die Daten der Weine anhand des Formulars erfasst.
#nachdem das Formular geschickt wurde wird die Seite Weinkeller aufgerufen.
#Variablen werden zusammengenommen und beim rendern dann ausgegeben.
@app.route('/erfassen', methods=['GET', 'POST'])
def erfassen():
    if request.method == 'POST':
        name = request.form["name"]
        typ = request.form["typ"]
        geschmack = request.form["geschmack"]
        herkunft = request.form["herkunft"]
        jahrgang = request.form["jahrgang"]
        preis = request.form["preis"]
        bewertung = request.form["bewertung"]

        daten.speichern(name, typ, geschmack, herkunft, jahrgang, preis, bewertung) #keys mitgeben, damit die funktion weiss von wo er die Daten nehmen muss.

        return redirect(url_for('weinkeller'))
    return render_template('erfassen.html')



if __name__ == "__main__":
    app.run(debug=True, port=5000)


#Quelle:
# https://www.w3schools.com/python/python_json.asp