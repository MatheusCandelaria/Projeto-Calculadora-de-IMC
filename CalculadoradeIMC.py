def calcula_imc(peso, altura):
    imc = peso / altura**2
    return imc

peso = float(input("Digite o seu peso (em kg): "))
altura = float(input("Digite a sua altura (em metros): "))

imc = calcula_imc(peso, altura)

print("Seu IMC é:", imc)
