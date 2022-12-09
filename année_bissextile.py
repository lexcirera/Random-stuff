e=1
while e==1:
    #défintition de l'année cherchée"
    x=int(input("Donner l'année"))
    a=x/4
    b=x/100
    c=x/400
    #divisibilité par 4
    if a==int(a):
        print ("L'année est bissextile")
    else:
    #divisibilité par 100
        if b==int(b):
        #divisibilité par 400
            if c==int(c):
                print ("L'année est bissextile")
            else:
                print ("L'année n'est pas bissextile")
        else:
            print ("L'année n'est pas bissextile")
    y=input("Chercher une autre année")
    if y=="oui":
        e=1
    else:
        e=2
