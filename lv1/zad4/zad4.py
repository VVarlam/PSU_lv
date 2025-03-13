imeDatoteke = input("Unesite ime tekstualne datoteke: ")

try:
    fhand = open(imeDatoteke)
    ukupnaPouzdanost = 0
    brLinija = 0

    for line in fhand:
        #uklanja suvišne praznine i nove redove na kraju linije
        line = line.rstrip()
        if line.startswith("X-DSPAM-Confidence:"):
            #pronalazak broja
            for rijec in line.split():
                try:
                    broj = float(rijec)
                    ukupnaPouzdanost += broj
                    brLinija += 1
                    break
                except:
                    continue
    fhand.close()

    srednjaVrijednost = ukupnaPouzdanost / brLinija

    if brLinija > 0:
        print("Srednja vrijednost pouzdanosti je: ", srednjaVrijednost)
    else:
        print("Nema pronadjenih vrijednosti")
except:
    print("Datoteka nije pronadjena")
