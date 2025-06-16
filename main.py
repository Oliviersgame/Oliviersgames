import random

def toon_geraden_woord(woord, geraden_letters):
    zichtbaar = ""
    for letter in woord:
        if letter in geraden_letters:
            zichtbaar += letter
        else:
            zichtbaar += "-"
    return zichtbaar

woordenlijst = [
    "informatica", "informatiekunde", "spelletje", "aardigheidje",
    "scholier", "fotografie", "waardebepaling", "specialiteit",
    "verzekering", "universiteit", "heesterperk"
]

gekozen_woord = random.choice(woordenlijst)

beurten = 5

geraden_letters = []

print("Welkom bij Galgje!")
print(f"Je hebt {beurten} beurten om het woord te raden.")
print(f"Het woord bestaat uit {len(gekozen_woord)} letters.")

while beurten > 0:

    print("\nHuidige status: ", toon_geraden_woord(gekozen_woord, geraden_letters))

    letter = input("Voer een letter in: ").lower()

    if letter in geraden_letters:
        print("Die letter heb je al geprobeerd.")
        continue

    geraden_letters.append(letter)

    if letter in gekozen_woord:
        print("Goed zo! De letter komt voor in het woord.")
    else:
        beurten -= 1
        print(f"Helaas, de letter zit niet in het woord. Nog {beurten} beurt(en) over.")

    if toon_geraden_woord(gekozen_woord, geraden_letters) == gekozen_woord:
        print("\nGefeliciteerd! Je hebt het woord geraden:", gekozen_woord)
        break

if beurten == 0:
    print("\nJe hebt helaas verloren. Het woord was:", gekozen_woord)
