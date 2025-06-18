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
    """,
    """
     -----
     |   |
     O   |
    /|\\  |
    / \\  |
    RIP  |
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

def speel_galgje():
    gekozen_woord = random.choice(woordenlijst)
    max_fouten = 7
    fouten = 0
    geraden_letters = []
    foute_letters = []

    while fouten < max_fouten:
        clear_screen()
        print("Welkom bij Galgje!")
        print(f"Je hebt {max_fouten} fouten om het woord te raden.")
        print(f"Het woord bestaat uit {len(gekozen_woord)} letters.\n")

        print(galgje_stappen[fouten])
        print("Huidige status:", toon_geraden_woord(gekozen_woord, geraden_letters))
        print("Fout geraden letters:", " ".join(foute_letters))

        letter = input("Voer een letter in: ").lower()

        if len(letter) != 1 or not letter.isalpha():
            print("Voer alsjeblieft één geldige letter in.")
            input("Druk op Enter om verder te gaan...")
            continue

        if letter in geraden_letters or letter in foute_letters:
            print("Die letter heb je al geprobeerd.")
            input("Druk op Enter om verder te gaan...")
            continue

        if letter in gekozen_woord:
            geraden_letters.append(letter)
            print("Goed zo! De letter komt voor in het woord.")
        else:
            fouten += 1
            foute_letters.append(letter)
            print(f"Helaas, de letter zit niet in het woord. Fouten: {fouten} van {max_fouten}")

        if toon_geraden_woord(gekozen_woord, geraden_letters) == gekozen_woord:
            clear_screen()
            print("Gefeliciteerd! Je hebt het woord geraden:")
            print("Het woord was:", gekozen_woord)
            break
    else:
        clear_screen()
        print("Helaas, je hebt verloren.")
        print(galgje_stappen[fouten])
        print("Het woord was:", gekozen_woord)


while True:
    speel_galgje()
    opnieuw = input("\nDruk op Enter om opnieuw te spelen of typ 'q' om te stoppen: ")
    if opnieuw.lower() == 'q':
        print("Tot de volgende keer!")
        break
