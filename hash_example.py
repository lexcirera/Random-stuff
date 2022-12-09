import hashlib as h

p_trav=6
val=p_trav*str(0)
Flag=False
mot='nvnerqd,rhl,wdfb'
a=mot.encode('utf-8')
print(a)
test=1
preuve=1
b=h.sha256(a).hexdigest()
if b[0:p_trav]==val: Flag=True
while Flag==False:
    test+=1
    preuve+=1
    a=mot+str(preuve)
    a=a.encode('utf-8')
    b=h.sha256(a).hexdigest()
    if b[0:p_trav]==val: Flag=True

print("hash: ",b)
print("Nombre de tests: ", test)