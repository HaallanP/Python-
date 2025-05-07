# Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto

n = float(input("Digite o preço de um produto: \nR$"))
desconto = n * 5 / 100
print(
    "Na liquidação da loja, esse produto de R${:.2f} está com desconto de 5%, \nou seja, vai custar só R${:.2f}.".format(
        n, n - desconto
    )
)

# Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento
salario = float(input("Digite seu salário: \nR$"))
aumento = salario * 15 / 100
print(
    "O salário do funcionário, que é de R${:.2f}, vai subir para R${:.2f} com o aumento de 15%.".format(
        salario, salario + aumento
    )
)

# Conversor de temperaturas: escreva um programa que converta uma temperatura digitada em ºC para ºF

celsius = float(input("Digite a temperatura em Celsius: \n"))
farenheit = (1.8 * celsius) + 32
print("{}ºC correspondem a {:.1f}ºF.".format(celsius, farenheit))

# Aluguel de carros:

# Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e a quantidade de dias pelos quais ele foi alugado

# Calcule o preço a pagar, sabendo que o carro custa R$ 60 por dia e R$ 0.15 por km rodado

dias = int(input("Por quantos dias o carro foi alugado: \n"))  # 8 dias
km = float(input("Quantos km o carro rodou: \n"))  # 720km

custo_dias = dias * 60
custo_km = km * 0.15

print(
    "Você andou {}km por {} dias, então o preço a pagar é R${:.2f}.".format(
        km, dias, (custo_km + custo_dias)
    )
)

# tem que dar R$ 588.00

# Faça um programa que leia um número inteiro e mostre na tela o seu sucessor e seu antecessor:

n = int(input("Digite um número: \n"))
print("O antecessor do número {} é: {}.".format(n, n - 1))
print("O sucessor do número {} é: {}.".format(n, n + 1))
