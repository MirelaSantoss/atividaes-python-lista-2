c = int(input("Digite o código do curso de 1 a 5:"))

match c:
    case 1:
        print("Engenharia")
    case 2:
        print("Edificações")
    case 3:
        print("Sistemas Elétricos")
    case 4:
        print("Turismo")
    case 5:
        print("Análise de Sistemas")
    case _:
        print("Código inválido")
