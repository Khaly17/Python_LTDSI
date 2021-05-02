#============================================
#           Exercice 1
#============================================
def elim(L):
    liste = []
    for i in L:
        if i not in liste:
            liste.append(i)
    return print(liste)
#elim("tdsiucaddddddtttt")

#============================================
#           Exercice 2
#============================================

def anagram():
    u = input("valeur 1 : ")
    v = input("valeur 2 : ")
    if len(v) != len(u):
        print("Les deux chaines n'ont pas la meme taille")
        exit()
    for i in range(len(v)):
        if u[i] not in v:
            return False
    return True
#print(anagram())

#============================================
#           Exercice 3
#============================================
def decalage(chaine,entier):
        entier = entier%26
        # chaine ===> chiffre
        dico = {
            'A':0,'B':1,'C':2,'D':3,'E':4,'F':5,'G':6,'H':7,'I':8,'J':9,'K':10,
            'L':11,'M':12,'N':13,'O':14,'P':15,'Q':16
            ,'R':17,'S':18,'T':19,'U':20,'V':21,'W':22,'X':23,'Y':24,'Z':25
        }

        # chiffre ===> chaine chiffrer
        dico_inv = {
            0:'A',1:'B',2:'C',3:'D',4:'E',5:'F',6:'G',7:'H',8:'I',9:'J',10:'K',
            11:'L',12:'M',13:'N',14:'O',15:'P',16:'Q',17:'R',18:'S'
        ,19: 'T',20:'U',21:'V',22:'W',23:'X',24:'Y',25:'Z'
        }
        liste1 = []
        liste2 = []
        chaine_decaler = ""
        chaine1 = chaine
        for i in chaine.replace(" ","").upper():
            c = (dico.get(i)+entier)%26
            liste1.append(c)
        for i in range(len(liste1)):
            liste2.append(dico_inv.get(liste1[i]))
            chaine_decaler=  chaine_decaler + liste2[i]

        for i in range(len(chaine1)):
            if chaine1[i] == " ":
                chaine_decaler[i].endswith(" ")

        print( chaine_decaler)
        print(chaine1.split())
#decalage("LICENCES TDSI",3)
#============================================
#           Exercice 4
#============================================

def decalage(ch,n):
    n = n%26
    liste1 = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
    liste2 = []
    ch_decal = []
    position = []
    for i in range(len(liste1)):
        d = (i + n)%26
        liste2.append(liste1[d])
        for i in range(len(ch)):
            position.append(liste1.index(ch[i].upper()))
        #for i in range(len(position)):
            #ch_decal.append(liste1[(position[i]+n)%26])
    print(position)
    print(liste1[(position[i]+n)%26])
#decalage("khaly",3)

#============================================
#           DEVOIR N 1
#============================================

def occurence():
    ch = input("Entrer une chaine")
    for i in range(len(ch)):
        if "e" == ch[i]:
            print('la position de e dans cette chaine est ',i)
            return True
        print("Le caractere e ne se trouve pas dans la chaine")
#occurence()

#============================================
#           EXO 2
#============================================

def verlan(mot):
    mot_inv = ""
    for el in range(len(mot)):
        a = len(mot)-(1+el)
        mot_inv += mot[a]
    print(mot_inv)
#verlan("khaly")

#**** AU cas ou on a Une phrase ,on veut avoir (ex: LICENCE L3 TDSI) ====> TDSI L3 LICENCE ****#

def verlan1(phrase):
    phrase = phrase.split()
    phrase_inverce = []
    for i in range(len(phrase)):
        phrase_inverce.append(phrase[len(phrase)-(1+i)])
    print(phrase_inverce)
verlan1("LICENCE L3 TDSI")

#============================================
#           EXERCICE 3
#============================================

def Authentification():
    addresse_institutionnel = input("Entrer ton addresse institutionnel")


























