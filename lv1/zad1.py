def total_euro(radniSati, placaPoSatu):
    return radniSati * placaPoSatu

radniSati = float(input("Unesite broj radnih sati: "))
placaPoSatu = float(input("Unesite placu po satu: "))

ukupno = total_euro(radniSati, placaPoSatu)
print(ukupno)