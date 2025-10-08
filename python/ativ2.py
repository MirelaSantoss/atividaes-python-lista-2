nota1 = float(input("Digite a primeira nota:\n"))
nota2 = float(input("Digite a segunda nota:\n"))

media = (nota1+nota2)/2

if media  >= 6: 
    print(f"Vocẽ foi aprovado com nota: {media:.2f}")

else:  
    ex =float(input("Digite a nota do exame:"))

    novam = (media+ex) /2

if novam >= 5:

        print(f"Você foi aprovado em exame com nota: {novam: .2f}")

else: 
      print(f"Você foi reprovado com nota:{novam:.2f}")



