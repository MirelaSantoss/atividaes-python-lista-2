def arredondarnota(n):
    notaint = int(n)
    resto = n - notaint

    if resto > 0.5:
        return float(notaint + 1)
    else:
        return float(notaint)

n = float(input("Digite a nota do aluno: "))
notaarredondada = arredondarnota(n)


print(f"Nota arredondada: {notaarredondada}")



