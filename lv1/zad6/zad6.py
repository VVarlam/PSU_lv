fhand = open('SMSSpamCollection.txt', encoding='utf-8')
brojHamRijeci = 0
brojSpamRijeci = 0
brojHamPoruka = 0
brojSpamPoruka = 0
usklicnik = 0

for line in fhand:
    line = line.rstrip()

    if not line:
        continue

    if line.startswith('ham'):
        oznaka = 'ham'
        #uklanja se ham iz poruke, poruka pocinje od indeksa 4
        poruka = line[4:].strip()
    elif line.startswith('spam'):
        oznaka = 'spam'
        poruka = line[5:].strip()
    else:
        continue

    brojRijeci = len(poruka.split())


    if oznaka == 'ham':
        brojHamRijeci += brojRijeci
        brojHamPoruka += 1
    elif oznaka == 'spam':
        brojSpamRijeci += brojRijeci
        brojSpamPoruka += 1

        if poruka.endswith('!'):
            usklicnik += 1

fhand.close()

if brojHamPoruka > 0:
    prosjekHam = brojHamRijeci / brojHamPoruka
else:
    prosjekHam = 0
if brojSpamPoruka > 0:
    prosjekSpam = brojSpamRijeci / brojSpamPoruka
else:
    prosjekSpam = 0

print(prosjekHam)
print(prosjekSpam)
print(usklicnik)