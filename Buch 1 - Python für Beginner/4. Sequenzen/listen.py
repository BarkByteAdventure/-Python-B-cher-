liste = [10, "Hans", 8.9, True, 29, False]

# gibt das erste Element der Liste aus
print(liste[0])

# gibt das vierte Element der Liste aus
print(liste[3])

# Ändert den Wert beim Index 1
liste[1] = "Peter"

# Ändert den Wert bei dem Index 3
liste[3] = 102

print(liste)

# len
for i in range(len(liste)):
    liste[i] = 10

# alle Elemente in der Liste sind 10
print(liste)
# die Anzahl der Elemente in der Liste ist 6
print(len(liste))

# Listenoperatoren

print(liste + [100, 200, 300, 400])   # fügt 100, 200, 300 und 400 hinzu

print(liste * 3)   # fügt 3 mal die Elemente der Liste hinzu

print(liste * 3 + [1000, 2000, 3000])   # fügt 3 mal die Elemente der Liste und 1000, 2000 und 3000 hinzu

print([12, "Hey"] * 3)   # fügt 3 mal [12, "Hey"] hinzu

# Listenfunktionen

liste = [10, 20, 30, 40, 50]

print(max(liste))   # gibt den höchsten Wert einer Liste zurück

print(min(liste))   # gibt den niedrigsten Wert einer Liste zurück

print(sum(liste))   # gibt die Summe aller Elemente einer Liste zurück

print(len(liste))   # gibt die Anzahl der Elemente in einer Liste zurück

print(sum(liste) / len(liste))      # gibt die Mittelwert aller Elemente einer Liste zurück


# Listenmethoden

liste.append(60)   
print(liste)                        # fügt 60 hinzu

liste.count(liste)
print(liste)                        # gibt die Anzahl der Elemente in einer Liste zurück

liste.extend([1000, 2000, 300])
print(liste)                        # fügt 1000, 2000 und 300 hinzu

liste.index(1000)
print(liste)                        # gibt das Index eines Elementes in einer Liste zurück

liste.insert(0, 1000)
print(liste)                        # fügt 1000 an den Anfang der Liste ein

liste.remove(1000)
print(liste)                        # entfernt 1000 aus der Liste

liste.reverse()
print(liste)                        # umwandelt die Reihenfolge der Elemente in einer Liste

liste.sort()
print(liste)                        # sortiert die Elemente in einer Liste


# Erweitertes Indexieren

print(liste[-2])    # gibt das zweite Element von rechts aus

print(liste[:4])    # gibt alle Elemente bis zum vierten Index aus

print(liste[1:3])   # gibt alle Elemente von Index 1 bis 3 aus

print(liste[2:])    # gibt alle Elemente von Index 2 bis zum Ende