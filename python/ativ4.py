a = float (input("Digiote o valor de a:"))
b = float (input("Digiote o valor de b:"))
c = float (input("Digiote o valor de c:"))


if  a<b+c and b<a+c and c<a+b:

    if a==b and b==c and a==c:
        print("e um triangulo equilatero")

    elif a == b or b== c or c==a:

        print("e um triangulo isósceles")

    else: 
        print("e um triangulo escaleno")   

else:
    print("este não é um triangulo") 