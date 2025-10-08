import math


a = float (input("Digiote o valor de a:"))
b = float (input("Digiote o valor de b:"))
c = float (input("Digiote o valor de c:"))

d = b**2 - 4*a*c

print(d)
if d == 0:
    r1 = -b + math.sqrt(d) / 2*a
    print("A raiz e = ", r1)

elif d > 0:
    r1 = -b + math.sqrt(d) / 2*a
    r2 = -b - math.sqrt(d) / 2*a
    print("A duas raizes sao: ", r1, r2)

else: 
        print("Não a raizes.")