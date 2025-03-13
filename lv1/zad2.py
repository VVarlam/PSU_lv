try:
    a = float(input("Unesi ocjenu: "))
    while a < 0.0 or a > 1.0:
        print("Ocjena nije u dobrom rasponu")
        a = float(input("Unesi ocjenu: "))
    if a >= 0.9:
        print('A')
    elif a >= 0.8 and a < 0.9:
        print('B')
    elif a >= 0.7 and a < 0.8:
        print('C')
    elif a >= 0.6 and a < 0.7:
        print('D')
    else:
        print('F')
except:
    print("Niste unjeli broj")