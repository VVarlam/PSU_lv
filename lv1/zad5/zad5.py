fhand = open('song.txt', encoding='utf-8')

brojRijeci = {}

for line in fhand:
    line = line.rstrip()

    for rijec in line.split():
        rijec = rijec.lower()

        if rijec in brojRijeci:
            brojRijeci[rijec] += 1
        else:
            brojRijeci[rijec] = 1

fhand.close()

for rijec in brojRijeci:
    broj = brojRijeci[rijec]
    if broj == 1:
        print(rijec)