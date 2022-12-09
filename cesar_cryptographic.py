
def cesar (n):
    alphabet="abcdefghijklmnopqrstuvwxyz"
    mess=input("Que voulez vous crypter ?\n")
    mess_crypte=""
    for i in range (len(mess)):
        if mess[i].isalpha():
            caractere=mess[i]
            m=alphabet.index(caractere)
            decalage=(m+n)%26
            mess_crypte=mess_crypte+alphabet[decalage]
        else:
            mess_crypte=mess_crypte+mess[i]
    return mess_crypte

def decesar():
    alphabet="abcdefghijklmnopqrstuvwxyz"
    mess_crypte=input("Que voulez vous decrypter ?\n")
    for n in range (26):
        mess=""
        for i in range (len(mess_crypte)):
            if mess_crypte[i].isalpha():
                caractere=mess_crypte[i]
                m=alphabet.index(caractere)
                decalage=(m-n)%26
                mess=mess+alphabet[decalage]
            else:
                mess=mess+mess_crypte[i]
        print("Pour n= " + str(n)+":"+mess)
    return
