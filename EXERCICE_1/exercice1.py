chaine = input('Entrer une chaine de caractere svp : ')
a = len(chaine)

if a%2 == 1:
    b = chaine[:int(a/2)] + "-"
    c = chaine[int(a/2)+1:]
    resultat = b+c
    print("Resultat : ",resultat)
else:
    resultat = chaine[:int(a/2)]+ "-" + chaine[int(a/2):]
    print("Resultat : ",resultat)
