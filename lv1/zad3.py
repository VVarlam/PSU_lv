brojevi = []
while True:
    try:
        unos = input("Unesi broj ili napisi done: ")
        if unos.lower() == 'done':
            break
        provjera = float(unos)
        brojevi.append(provjera)
    except:
        print("Niste unjeli broj")

broj = len(brojevi)
srednjaVrijednost = sum(brojevi)/broj
minVrijednost = min(brojevi)
maxVrijednost = max(brojevi)

brojevi.sort()

print(broj)
print(srednjaVrijednost)
print(minVrijednost)
print(maxVrijednost)
print(brojevi)