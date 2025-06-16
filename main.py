import os
import random

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def toon_geraden_woord(woord, geraden_letters):
    zichtbaar = ""
    for letter in woord:
        zichtbaar += letter if letter in geraden_letters else "-"
    return zichtbaar

galgje_stappen = [
    """
     -----
     |   |
         |
         |
         |
         |
    =========
    """,
    """
     -----
     |   |
     O   |
         |
         |
         |
    =========
    """,
    """
     -----
     |   |
     O   |
     |   |
         |
         |
    =========
    """,
    """
     -----
     |   |
     O   |
    /|   |
         |
         |
    =========
    """,
    """
     -----
     |   |
     O   |
    /|\\  |
         |
         |
    =========
    """,
    """
     -----
     |   |
     O   |
    /|\\  |
    /    |
         |
    =========
    """,
    """
     -----
     |   |
     O   |
    /|\\  |
    / \\  |
         |
    =========
    """
]

woordenlijst = [
    "informatica", "informatiekunde", "spelletje", "aardigheidje",
    "scholier", "fotografie", "waardebepaling", "specialiteit",
    "verzekering", "universiteit", "heesterperk", "barendrecht",
    "techniek", "programmeren", "python", "informaticus",
    "applicatie", "software", "hardware", "database",
    "netwerk", "server", "client", "browser", "internet",
    "website", "applicatieontwikkeling", "softwareontwikkeling",
    "hardwareontwikkeling", "databank", "netwerkbeheer",
    "serverbeheer", "clientbeheer", "browserbeheer", "internetbeheer",
    "websitebeheer", "applicatiebeheer", "softwarebeheer",
    "hardwarebeheer", "databasebeheer", "netwerkbeheer",
    "autoband", "alex", "olivier", "gijs", "mikala", "martin(thosewhoknow)",
]

gekozen_woord = random.choice(woordenlijst)

max_fouten = len(galgje_stappen) - 1 
fouten = 0
geraden_letters = []

while fouten < max_fouten:
    clear_screen()
    print("Welkom bij Galgje!")
    print(f"Je hebt {max_fouten} fouten om het woord te raden.")
    print(f"Het woord bestaat uit {len(gekozen_woord)} letters.\n")

    print(galgje_stappen[fouten])
    print("Huidige status:", toon_geraden_woord(gekozen_woord, geraden_letters))

    letter = input("Voer een letter in: ").lower()

    if len(letter) != 1 or not letter.isalpha():
        print("Voer alsjeblieft één geldige letter in.")
        input("Druk op Enter om verder te gaan...")
        continue

    if letter in geraden_letters:
        print("Die letter heb je al geprobeerd.")
        input("Druk op Enter om verder te gaan...")
        continue

    geraden_letters.append(letter)

    if letter in gekozen_woord:
        print("Goed zo! De letter komt voor in het woord.")
    else:
        fouten += 1
        print(f"Helaas, de letter zit niet in het woord. Fouten: {fouten} van {max_fouten}")

    if toon_geraden_woord(gekozen_woord, geraden_letters) == gekozen_woord:
        clear_screen()
        print("Welkom bij Galgje!")
        print(galgje_stappen[fouten])
        print("\nGefeliciteerd! Je hebt het woord geraden:", gekozen_woord)
        break

    input("\nDruk op Enter voor de volgende beurt...")

if fouten == max_fouten:
    clear_screen()
    print("Welkom bij Galgje!")
    print(galgje_stappen[fouten])
    print("\nJe hebt helaas verloren. Het woord was:", gekozen_woord)
