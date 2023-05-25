from math import *
from random import *

a=1
b=1
while a<=100:
    b+=1
    a+=b
print("aastat", b,"kingitus", a)
print()


a=randint(1,35)
print("Õpilased:", a)
b=0
for i in range(a):
    c=randint(1,5)
    print("Hind",c,end=" ")
    b=b+c
print(f"keskmine hind on {b/a}")
print()


n=int(input("Sisesta arv: "))
a=int(input("Sisesta arvu aste: "))
for i in range(1,n+1):
   print(i**a)
print()


a=int(input("Sisesta arv 1 kuni 9:"))
for i in range(a):
    print("  -----  ") 
    print("|  3 3  |") 
    print("!  \-/  !") 
    print("  _____  ") 
print()


print("Sisse arv (0-100). 10 katsega")
r=randint(1,100)
n=1
while n<=10:
    o=int(input("Sisesta arv: "))
    if o==r:
        print(f"sa kasutasid {n} katset.")
        break
    elif r>o:
        print("Liiga väike")
    elif o>r:
        print("liiga suur")
    n=n+1
while True:
        n<=10
        print("Püüdlused lõppesid vastus oli",r)
        break
print()
