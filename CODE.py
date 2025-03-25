import pandas as pd
from datetime import datetime
import calendar

# Charger le fichier Excel
file_path = "Asia_Take_JDS JDM X.xlsx"
df = pd.read_excel(file_path, sheet_name="Sheet1")

def get_weekday_name(day, month, year):
    """Retourne le nom du jour de la semaine pour une date donnée."""
    date_obj = datetime(year, month, day)
    return calendar.day_name[date_obj.weekday()]

def get_message(day, month, year):
    """Retourne le message associé à la probabilité pour une date donnée."""
    weekday_fr = {
        "Monday": "Lundi", "Tuesday": "Mardi", "Wednesday": "Mercredi", 
        "Thursday": "Jeudi", "Friday": "Vendredi"
    }
    weekday = get_weekday_name(day, month, year)
    jour_semaine = weekday_fr.get(weekday, None)
    
    if not jour_semaine:
        return "Cette date tombe un week-end."
    
    # Chercher la probabilité
    result = df[(df["JourSemaine"] == jour_semaine) & (df["Jour"] == day)]
    
    if not result.empty:
        proba = result["Valeur"].values[0]
        return "Let's go trading!" if proba <= 30 else "Pas de trade aujourd'hui."
    else:
        return "Aucune donnée pour cette date."

while True:
    date_str = input("Entrez une date (JJ MM AAAA) : ")
    try:
        day, month, year = map(int, date_str.split())
        print(get_message(day, month, year))
    except ValueError:
        print("Format invalide. Veuillez entrer une date sous forme JJ MM AAAA.")
    
    again = input("Voulez-vous entrer une autre date ? (o/n) : ")
    if again.lower() != 'o':
        break
