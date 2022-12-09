from math import *
from numpy import *
import random as rd
import matplotlib.pyplot as plt

##
a=[1,2,3,4,5]
b=[5,4,3,2,1]
c=[2,3,1,5,4]

plt.close()
plt.figure()
ax=plt.axes(projection="3d")
ax.plot3D(a,b,c)
plt.show()
##

def f(x, y):
    return sin(sqrt(x ** 2 + y ** 2))

x = linspace(-10, 10, 30)
y = linspace(-10, 10, 30)

X, Y = meshgrid(x, y)
Z = f(X, Y)

##
def f(x, y):
    return -x**7+9*y**6-4*y**5-x**6+x**4+-9*y**3+x**2-4*y+3*x

x = linspace(-20, 20, 50)
y = linspace(-26, 26, 50)

X, Y = meshgrid(x, y)
Z = f(X, Y)






##

plt.close()
fig = plt.figure()
ax = plt.axes(projection='3d')
ax.contour3D(X, Y, Z, 50, cmap='binary')
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('z')
ax.view_init(60, 35)
fig
plt.show()

##

plt.close()
fig = plt.figure()
ax = plt.axes(projection='3d')
ax.plot_wireframe(X, Y, Z, color='black')
ax.set_title('wireframe')
plt.show()

##

plt.close()
plt.figure()
ax = plt.axes(projection='3d')
ax.plot_surface(X, Y, Z, rstride=1, cstride=1,
                cmap='viridis', edgecolor='none')
ax.set_title('surface')
plt.show()

##

plt.close()
fig = plt.figure()
plt.axes(projection='3d').plot_wireframe(X, Y, Z, color='black')
plt.title('wireframe')
plt.show()

##
I=4
J=4
a,b,c,d=[],[],[],[]
for i in range (I+1):
    a1=[]
    for j in range (J+1):
        a2=rd.randint(-7,7)
        a1.append(a2)
    a.append(a1)

for i in range (I):
    b1=[]
    c1=[]
    d1=[]
    for j in range(J):
        b1.append(a[i+1][j])
        c1.append(a[i][j+1])
        d1.append(a[i+1][j+1])
    b.append(b1)
    c.append(c1)
    d.append(d1)


##
taille=5*I
nb_points=10*I

def S(l):
    return 3*l**2-2*l**3

def f(x,z,i,j):
    return a[i][j]+(b[i][j]-a[i][j])*S(x-i)+(c[i][j]-a[i][j])*S(z-j)+(a[i][j]-b[i][j]-c[i][j]+d[i][j])*S(x-i)*S(z-j)

##
Z=[]
x = linspace(-taille, taille, nb_points)
y = linspace(-taille, taille, nb_points)
X, Y = meshgrid(x, y)
for i in range(0,I):
    Z1=[]
    print("sf")
    for j in range(0,J):
        print("dd")
        Z1=f(X,Y,i,j)
        print(Z1)
    Z=Z+Z1

##
Z=[]
x = linspace(-taille, taille, nb_points)
y = linspace(-taille, taille, nb_points)
X, Y = meshgrid(x, y)
Z=f(X,Y,3,0)

##
liste_x=[]
liste_z=[]
for i in range(1,I+1):
    x = linspace(2*(i-1),2*i , int(nb_points/I))
    z = linspace(2*(i-1),2*i , int(nb_points/J))
    liste_x.append(x)
    liste_z.append(z)

##
Z=[]

for i in range (I):
    for j in range(J):
        Z1=[]
        x=liste_x[i]
        z=liste_z[j]
        X,Y=meshgrid(x,z)
        Z1=f(X,Y,i,j)
        Z.append(Z1)

##
plt.figure()
plt.axes(projection='3d').plot_wireframe(X, Y, Z, color='black')
plt.show()











