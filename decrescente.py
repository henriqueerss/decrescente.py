decrescente = True
valorAnterior = int(input("Digite o número da sequência: "))

valor = 1


while valor != 0 and decrescente:
    valor = int(input("Digite o próximo número da sequência: "))  
    if valor > valorAnterior:
        decrescente = False
    valorAnterior = valor

if decrescente:
    print("\nA sequência está em ordem decrescente.\n")
else: 
    print("\nA sequência não está em ordem decrescente.\n")
