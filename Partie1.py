dico = {'A':0,'B':1,'C':2,'D':3,'E':4,'F':5,'G':6,'H':7,'I':8,'J':9,
        'K':10,'L':11,'M':12,'N':13,'O':14,'P':15,'Q':16,'R':17,'S':18,
        'T':19,'U':20,'V':21,'W':22,'X':23,'Y':24,'Z':25}

dico_inv = {0:'A',1:'B',2:'B',3:'C',4:'D',5:'E',6:'F',7:'G',8:'H',9:'I',10:'J',
            10:'K',11:'L',12:'M',13:'N',14:'O',15:'P',16:'Q',17:'R',18:'S',
            19:'T',20:'U',21:'V' ,22:'W',23:'X',24:'Y',25:'Z'}

#========================================================================
#                           CHIFFREMENT
#========================================================================
message = input("Entrer un message a crypt : ").replace(" ","").upper()
a = len(message)
b = range(len(message))
caract_message = []

for i in b:
     caract_message.append(message[i])
     #print(caract_message)

k = int(input("Donner une cle de chiffrement, compris entre 0 et 25 : "))
if k in range(26):
    chiffre = []
    for i in range(0,len(caract_message)):
        c = dico.get(caract_message[i])+k
        #print(c)
        if c >= 26:
            c = c - 26
        chiffre.append(c)
    print("le chiffre : ",chiffre)

    chiffres = []
    Message = ""
    for i in range(0, len(caract_message)):
        message_chiffre = dico_inv.get(chiffre[i])
        #print(message_chiffre)
        chiffres.append(message_chiffre)
        Message = Message + chiffres[i]
    print("Le chiffre du text : ",chiffres)
    print("Le resultat entendu : ",Message)


#========================================================================
#                           DECHIFFREMENT
#========================================================================

Le_chiffre = input("Entrer un message a crypt : ").replace(" ","").upper()
a = len(Le_chiffre )
b = range(len(Le_chiffre ))
caract_Le_chiffre = []

for i in b:
     caract_Le_chiffre .append(Le_chiffre [i])
     #print(caract_message
k_d = int(input("Donner la cle de dechiffrement, compris entre 0 et 25 : "))
if k_d in range(26):
    dechiffre = []
    for i in range(0,len(caract_Le_chiffre)):
        c = dico.get(caract_Le_chiffre[i]) - k_d
        #print(c)
        if c < 0:
            c = c + 26
        dechiffre.append(c)
    print("le chiffre : ",dechiffre)
    dechiffres = []
    MessageD = ""
    for i in range(0, len(caract_Le_chiffre)):
        message_dechiffre = dico_inv.get(dechiffre[i])
        #print(message_chiffre)
        dechiffres.append(message_dechiffre)
        MessageD = MessageD + dechiffres[i]
    print("Le chiffre du text : ",dechiffres)
    print("Le resultat entendu : ",MessageD)