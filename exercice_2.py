nombre = int(input("Entrez un nombre "))
for i in range(2,nombre):
    if nombre%i == 0:
        nbrPrem = False
        print(nbrPrem)
        break
    else:
        nbrPrem = True
        print(nbrPrem)
        break