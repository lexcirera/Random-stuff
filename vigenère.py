 def  cleee(str,n):
     a=len(str)
     b=n%a
     a=a-b
     str=str*a
     for i in range(0,b+1):
        str=str+str[i]
     return str

## algo vigenère
def vigenère(mess,cle):
    clecode=cleee(mess,len(cle))
    c=len(mess)
    crypt=""
    for i in range (0,c):
        a=clecode[i]
        alpha="abcdefghijklmnopqrstuvwxyz"
        if a !=" ":
            bb=mess[i]
            k=alpha.append(mess[i])
            v=alpha[(k+i)%26]
            crypt+= v
        else:
            crypt+=" "
    return crypt