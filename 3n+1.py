import matplotlib.pyplot as plt

##
def next(n):
    if n%2==0:
        return n/2
    else:
        return 3*n+1

def suite(n):
    abs=[]
    ord=[]
    i=1
    abs.append(i)
    ord.append(n)
    while ord[-1] != 1:
        i+=1
        abs.append(i)
        n=next(n)
        ord.append(n)
    print("itérations:", len(abs))
    print(ord)
    plt.close()
    plt.figure()
    plt.plot(abs,ord,"o",markersize=1)
    plt.grid()
    plt.show()

def calc(n):
    abs=[]
    ord=[]
    i=1
    abs.append(i)
    ord.append(n)
    while ord[-1] != 1:
        i+=1
        abs.append(i)
        n=next(n)
        ord.append(n)
    return ord

##
a=[]
b=[]
for i in range(2,100000):
    a.append(i)
    b.append(len(calc(i)))
plt.close()
plt.figure()
plt.plot(a,b,"o",markersize=0.2)
plt.grid()
plt.show()
