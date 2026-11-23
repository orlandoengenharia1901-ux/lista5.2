

# 11. A Tabuada Mágica: Peça ao usuário para digitar um número inteiro. Use um laço for com range(1, 11) para imprimir a tabuada completa desse número (ex: 5 x 1 = 5 até 5 x 10 = 50).

numero = int(input("Digite um número inteiro: "))

print("Tabuada do", numero)

for i in range(1, 11):
    print(f"{numero} x {i} = {numero * i}")


# EXERCÍCIO 12 - O COFRE PERSISTENTE

senha_secreta = "dragao123"
senha = input("Digite a senha do cofre: ")

while senha != senha_secreta:
    print("Senha incorreta, tente novamente!")
    senha = input("Digite a senha: ")

print("Cofre Aberto!")


# EXERCÍCIO 13 - CONTAGEM REGRESSIVA DA NASA

print("Iniciando contagem regressiva!")

for i in range(10, -1, -1):
    print(i)

print("DECOLAR! 🚀")



# EXERCÍCIO 14 - SOMADOR DE MOEDAS

total_ouro = 0

for i in range(1, 6):
    moedas = int(input(f"Moedas do baú {i}: "))
    total_ouro += moedas

print("Total de moedas:", total_ouro)


# EXERCÍCIO 15 - DETECTOR DE NÚMEROS PARES

print("Números pares de 1 até 20:")

for numero in range(1, 21):
    if numero % 2 == 0:
        print(numero)

# EXERCÍCIO 16 - BARRA DE STAMINA

energia = 100

while energia > 0:
    print(f"\nEnergia atual: {energia}")
    acao = input("Correr ou pular? ").lower()

    if acao == "correr":
        energia -= 20
    elif acao == "pular":
        energia -= 15
    else:
        print("Ação inválida!")

print("O herói desmaiou de cansaço!")


# EXERCÍCIO 17 - VALIDADOR DE NOTA ESCOLAR

nota = float(input("Digite uma nota de 0 a 10: "))

while nota < 0 or nota > 10:
    print("Nota inválida!")
    nota = float(input("Digite uma nota válida: "))

print("Nota registrada:", nota)


# EXERCÍCIO 18 - CONTADOR DE LETRAS

palavra = input("Digite uma palavra: ").lower()
contador = 0

for letra in palavra:
    print(letra)

    if letra == "a":
        contador += 1

print("Quantidade de letras 'a':", contador)


# EXERCÍCIO 19 - ESCADA DE ASTERISCOS

n = int(input("Digite o tamanho da escada: "))

print("Escada de asteriscos:")

for i in range(1, n + 1):
    print("*" * i)

# EXERCÍCIO 20 - CAIXA DE SUPERMERCADO

total = 0

while True:
    preco = float(input("Preço do produto (0 para sair): "))

    if preco == 0:
        break

    if preco < 0:
        print("Preço inválido!")
        continue

    total += preco

print(f"Valor total da compra: R$ {total:.2f}")



# EXERCÍCIO 21 - BATALHA DE TURNOS

vida_heroi = 100
vida_goblin = 80

while vida_heroi > 0 and vida_goblin > 0:
    print(f"\nHerói: {vida_heroi} HP")
    print(f"Goblin: {vida_goblin} HP")

    print("1 - Atacar")
    print("2 - Curar")
    escolha = input("Escolha uma ação: ")

    if escolha == "1":
        vida_goblin -= 15
        print("Você causou 15 de dano!")
    elif escolha == "2":
        vida_heroi = min(100, vida_heroi + 10)
        print("Você recuperou vida!")
    else:
        print("Opção inválida!")
        continue

    if vida_goblin > 0:
        vida_heroi -= 12
        print("Goblin atacou! -12 HP")

if vida_heroi > 0:
    print("O Herói venceu!")
else:
    print("O Goblin venceu!")


# EXERCÍCIO 22 - LIMITE DE TENTATIVAS

senha_secreta = "dragao123"
tentativas = 0
senha = ""

while tentativas < 3:
    senha = input("Digite a senha: ")
    tentativas += 1

    if senha == senha_secreta:
        print("Cofre Aberto!")
        break
    else:
        print("Senha incorreta!")

if senha != senha_secreta:
    print("Cartão Bloqueado! Chamando os guardas!")

# EXERCÍCIO 23 - ADIVINHE O NÚMERO SECRETO

numero_secreto = 42
tentativas = 0

while True:
    chute = int(input("Adivinhe o número: "))
    tentativas += 1

    if chute > numero_secreto:
        print("Chutou alto! Tente um menor.")
    elif chute < numero_secreto:
        print("Chutou baixo! Tente um maior.")
    else:
        print("Parabéns! Você acertou!")
        break

print("Total de tentativas:", tentativas)

# EXERCÍCIO 24 - RELÓGIO DIGITAL

print("Simulador de relógio digital")

for hora in range(0, 3):

    for minuto in range(0, 60):
        print(f"{hora:02d}:{minuto:02d}")


# EXERCÍCIO 25 - CAÇADOR DE NÚMEROS PRIMOS

numero = int(input("Digite um número inteiro: "))
divisores = 0

for i in range(1, numero + 1):

    if numero % i == 0:
        divisores += 1

if divisores == 2:
    print("É um Número Primo!")
else:
    print("Não é um Número Primo!")

# EXERCÍCIO 26 - SEQUÊNCIA DE FIBONACCI

n = int(input("Quantos termos deseja gerar? "))

a = 0
b = 1

print("Sequência de Fibonacci:")

for i in range(n):
    print(a)

    proximo = a + b
    a = b
    b = proximo

# EXERCÍCIO 27 - ELEVADOR INTELIGENTE

andar_atual = 0

while True:
    print(f"\nElevador no andar {andar_atual}")
    destino = int(input("Andar desejado (0 a 10, -1 para sair): "))

    if destino == -1:
        print("Elevador desligado!")
        break

    if destino < 0 or destino > 10:
        print("Andar inválido!")
        continue

    if destino > andar_atual:
        for andar in range(andar_atual + 1, destino + 1):
            print("Subindo... Andar", andar)

    elif destino < andar_atual:
        for andar in range(andar_atual - 1, destino - 1, -1):
            print("Descendo... Andar", andar)

    else:
        print("Você já está neste andar!")

    andar_atual = destino
    print("Chegou ao andar", andar_atual)

# EXERCÍCIO 28 - SIMULADOR DE JUROS

saldo = 100
taxa = 0.10

meses = int(input("Quantos meses deseja guardar? "))

print(f"Saldo inicial: {saldo:.2f} moedas")

for mes in range(1, meses + 1):
    saldo = saldo * (1 + taxa)
    print(f"Mês {mes}: {saldo:.2f} moedas")

print(f"Saldo final: {saldo:.2f} moedas")

# EXERCÍCIO 29 - FATORIAL EXPLOSIVO

numero = int(input("Digite um número inteiro positivo: "))

while numero < 0:
    print("Número inválido!")
    numero = int(input("Digite um número positivo: "))

fatorial = 1

for i in range(1, numero + 1):
    fatorial *= i

print(f"O fatorial de {numero} é {fatorial}")


# EXERCÍCIO 30 - SIMULADOR DE FLIPERAMA

import time

fichas = 5

while True:
    print("\n===== FLIPERAMA =====")
    print("Fichas disponíveis:", fichas)
    print("1 - Jogar Corrida (1 ficha)")
    print("2 - Jogar Luta (2 fichas)")
    print("3 - Comprar fichas")
    print("4 - Sair")

    opcao = input("Escolha uma opção: ")

  
    if opcao == "1":
        if fichas >= 1:
            fichas -= 1
            print("Iniciando Corrida!")

            for fase in range(1, 4):
                print(f"Jogando... Fase {fase}")
                time.sleep(1)
        else:
            print("Fichas insuficientes!")

    elif opcao == "2":
        if fichas >= 2:
            fichas -= 2
            print("Iniciando Luta!")

            for fase in range(1, 4):
                print(f"Jogando... Fase {fase}")
                time.sleep(1)
        else:
            print("Fichas insuficientes!")

    elif opcao == "3":
        quantidade = int(input("Quantas fichas deseja comprar? "))

        if quantidade > 0:
            fichas += quantidade
            print("Compra realizada!")
        else:
            print("Quantidade inválida!")

    elif opcao == "4":
        print("Obrigado por jogar!")
        break

    else:
        print("Opção inválida!")

    if fichas == 0:
        resposta = input("Fichas acabaram! Comprar mais? (s/n): ").lower()

        if resposta != "s":
            print("Fim de jogo!")
            break

