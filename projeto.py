# Projeto: Sistemas de Coordenadas 2D - Algoritmos e Programação I
# Integrantes: Pedro Henrique Leite - Gabriel Nobrega Neri - Cauê Lemos Garcia

# Identificação da parte A do projeto.
print("---------- Parte A ----------")

# Solicita ao usuário as coordenadas da origem transladada.
x = int(input("Digite a coordenada X da origem transladada: "))
y = int(input("Digite a coordenada Y da origem transladada: "))

# Solicita ao usuário a quantidade de pontos a serem processados.
n = int(input("Digite a quantidade de pontos a ser analisada: "))

# Define as variáveis que vão armazenar a quantidade de pontos em cada quadrante e nos eixos de coordenadas X e Y.
quadrante_1 = quadrante_2 = quadrante_3 = quadrante_4 = eixo_x = eixo_y = 0

# Loop para ler cada ponto e determinar em qual quadrante ou eixo o mesmo se encontra.
for i in range(n):
    ponto_x = int(input("Digite a coordenada X do ponto: "))
    ponto_y = int(input("Digite a coordenada Y do ponto: "))

    # Translada o ponto para a origem (0,0)
    ponto_x_transladado = ponto_x - x
    ponto_y_transladado = ponto_y - y

    # Condições encadeadas para verificar o quadrante de cada um dos pontos escolhidos pelo usuário.
    if ponto_x_transladado > 0 and ponto_y_transladado > 0:
        quadrante_1 += 1
        print(f"Ponto ({ponto_x}, {ponto_y}) está no 1º quadrante.")

    elif ponto_x_transladado < 0 and ponto_y_transladado > 0:
        quadrante_2 += 1
        print(f"Ponto ({ponto_x}, {ponto_y}) está no 2º quadrante.")

    elif ponto_x_transladado < 0 and ponto_y_transladado < 0:
        quadrante_3 += 1
        print(f"Ponto ({ponto_x}, {ponto_y}) está no 3º quadrante.")

    elif ponto_x_transladado > 0 and ponto_y_transladado < 0:
        quadrante_4 += 1
        print(f"Ponto ({ponto_x}, {ponto_y}) está no 4º quadrante.")

    elif ponto_x_transladado == 0 and ponto_y_transladado != 0:
        eixo_y += 1
        print(f"Ponto ({ponto_x}, {ponto_y}) está sobre o eixo de coordenadas.")

    elif ponto_x_transladado != 0 and ponto_y_transladado == 0:
        eixo_x += 1
        print(f"Ponto ({ponto_x}, {ponto_y}) está sobre o eixo de coordenadas.")

# Imprime o total de pontos em cada quadrante e nos eixos de coordenadas.
print(f"Total de pontos no 1º quadrante: {quadrante_1} | Total de pontos no 2º quadrante: {quadrante_2} | Total de pontos no 3º quadrante: {quadrante_3} | Total de pontos no 4º quadrante: {quadrante_4}")
print(f"Total de pontos sobre o eixo X: {eixo_x} | Total de pontos sobre o eixo Y: {eixo_y}")

# Identificação da parte B do projeto.
print("---------- Parte B ----------")

# Solicita ao usuário as coordenadas da origem do robô.
x = int(input("Digite a coordenada X do ponto de origem A do robô: "))
y = int(input("Digite a coordenada Y do ponto de origem A do robô: "))

# Define as coordenadas finais com as mesmas coordenadas de origem.
x_final = x
y_final = y

# Solicita ao usuário o tempo que o robô irá caminhar.
quantos_passos = int(input("Digite por quanto tempo o robô irá caminhar: "))

# Define as variáveis de controle de passos do robô.
passo_cima = 1
passo_lado = 0

# Loop que controla os movimentos do robô pelo plano cartesiano.
while quantos_passos > 0:
    if passo_cima == 1 and passo_lado == 0:
        y_final = y_final + 1
        passo_lado = 1
        passo_cima = 0
        quantos_passos = quantos_passos - 1

    elif passo_cima == 0 and passo_lado == 1:
        x_final = x_final + 2
        passo_lado = 0
        passo_cima = 1
        quantos_passos = quantos_passos - 2

    elif passo_cima == 1 and passo_lado == 1 and quantos_passos >= 2:
        x_final = x_final + 2
        y_final = y_final + 1
        passo_lado = 1
        passo_cima = 0
        quantos_passos = quantos_passos - 2

    elif passo_cima == 1 and passo_lado == 1 and quantos_passos == 1:
        x_final = x_final + 1
        y_final = y_final + 1
        quantos_passos = quantos_passos = 1

# Imprime a coordenada final do robô no plano cartesiano.
print(f"Resposta: ao final da caminhada o robô estará no ponto ({x_final}, {y_final}) do plano cartesiano.")

# Identificação do fim do projeto.
print("---------- Fim ----------")