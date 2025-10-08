nota1 = float(input("Digite a primeira nota:\n"))
nota2 = float(input("Digite a segunda nota:\n"))
nota3 = float(input("Digite a terceira nota:\n"))

media = (nota1+nota2+nota3)/3

if media  >= 6: 
    print(f"Vocẽ foi aprovado com nota: {media:.2f}")

else:  
    print(f"Você foi reprovado com nota:{media:.2f}")