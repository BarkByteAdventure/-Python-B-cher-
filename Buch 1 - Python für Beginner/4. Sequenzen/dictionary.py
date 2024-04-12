dictionary = {"Name":"Alex", "Alter":25, "Groesse":1.80}

# gibt den Namen der Person aus
print(dictionary["Name"])

# gibt den Alter der Person aus
print(dictionary["Alter"])

# gibt die Groesse der Person aus
print(dictionary["Groesse"])


# Dictionaryfunktionen

print(len(dictionary))      # gibt die Anzahl der Elemente in einem Dictionary zurück

print(str(dictionary))      # gibt das Dictionary als String zurück


# Dictionarymethoden

dictionary.copy()
print(dictionary)           # kopiert das Dictionary

dictionary.fromkeys(["Name", "Alter", "Groesse"])
print(dictionary)           # etstellt ein Dictionary mit den Keys und 'None' Werte

dictionary.get("Name")
print(dictionary)           # gibt den Wert für den Key 'Name' aus

dictionary.items()
print(dictionary)           # gibt ein Tuple mit den Key-Value-Paaren aus

dictionary.setdefault("Name")
print(dictionary)           # setzt den Wert für den Key 'Name' aus

dictionary.update({"Alter": 28, "Groesse": 1.70})
print(dictionary)           # aktualisiert das Dictionary

dictionary.values()
print(dictionary)           # gibt alle Werte einer Dictionary aus

dictionary.clear()
print(dictionary)           # kopiert das Dictionary