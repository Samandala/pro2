import json


def weine_laden():
    try:
        with open("./daten/weine.json") as weine_json:#holt Daten aus dem weine.json File.
            weine = json.load(weine_json)
    except:
        return "Keine Daten gefunden"#wenn try nicht funktioniert kommen keine Daten und Programm würde abstürzen.
    return weine

#Daten im weine.json File speichern
def speichern(name, typ, geschmack, herkunft, jahrgang, preis, bewertung):
    weine = weine_laden() #die Weine werden aus der funktion weine_laden geladen.

    eintrag_weine = {
            "name": name,
            "typ": typ,
            "preis": preis,
            "jahrgang": jahrgang,
            "herkunft": herkunft,
            "geschmack": geschmack,
            "bewertung": bewertung
        }  #dict-Eintrag um die Daten später in das weine.json zu laden

    nummer = len(weine.keys())+1 #weil dict in dict. zählt so die keys
    weine[nummer] = eintrag_weine
    with open("./daten/weine.json", "w") as open_file:
        json.dump(weine, open_file)


