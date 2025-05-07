# Programa que exibe a tabuada de um número inteiro

n = int(input("Digite um número: "))
print(f"\nTabuada do {n}:")

for i in range(1, 11):
    print(f"{n} x {i} = {n * i}")

# Operações entre dois números
print("\nAgora vamos fazer algumas operações com dois números:")

n1 = int(input("Digite o primeiro valor: "))
n2 = int(input("Digite o segundo valor: "))

s = n1 + n2
m = n1 * n2
d = n1 / n2
di = n1 // n2
e = n1 ** n2

print(f"\nA soma é {s}")
print(f"O produto é {m}")
print(f"A divisão é {d:.3f}")
print(f"Divisão inteira: {di}")
print(f"Potência: {e}")

# Faça um programa que leia a largura e a algura de uma parede em metros, calcule a sua área e a quantidade de tinta necessária para pintá-la, sabendo que cada litro de tinta pinta uma área de 2m²

largura = float(input("Digite a largura: \n"))
altura = float(input("Digite a altura: \n"))
area = largura * altura

print(
    "Sua parede tem a dimensão {}x{} e sua área é de {}m².".format(
        largura, altura, area
    )
)

# Cada litro (L) de tinta pinta uma área de 2m².
tinta_necessaria = area / 2
print(
    "Para pintar essa parede, você precisará de {}L de tinta.".format(tinta_necessaria)
)
# Conferir a resposta porque não sei se entendi o problema. O velho Guilherme continua o mesmo, só que agora com ímpeto suficiente para continuar
