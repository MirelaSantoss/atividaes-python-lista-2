a = float(input("Digite o primeiro número:"))
b = float(input("Digite o segundo número:"))
c = float(input("Digite o terceiro numero:"))

maior = max(a, b, c)
menor = min(a, b, c)
meio = (a + b + c) - maior - menor 

print(f"\na) Maior número: {maior}")
print(f"b) Menor número: {menor}")
print(f"c) Número do meio: {meio}")

    
