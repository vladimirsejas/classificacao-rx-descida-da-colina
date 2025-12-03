import random

# =====================================================================
# BLOCO 1: DADOS DAS IMAGENS (A MATÉRIA-PRIMA)
# =====================================================================
# X = quantidade de pixels brancos (osso)
# Y = quantidade de pixels pretos (ar)

dados_rx = [
    # --- BACIAS (X Alto / Branco) ---
    [47117, 52882, "Bacia"],  # 3L.jpg
    [46483, 53516, "Bacia"],  # 3J.jpg
    [37977, 62022, "Bacia"],  # 3F.jpg
    [41649, 58350, "Bacia"],  # 2K.jpg
    [39735, 60264, "Bacia"],  # 2L.jpg
    [31966, 68033, "Bacia"],  # 3H.jpg
    [43955, 56045, "Bacia"],  # 2C.jpg

    # --- TÓRAX (Y Alto / Preto) ---
    [12500, 85400, "Torax"],  # Torax Real
    [13200, 88500, "Torax"],  # Simulado 1
    [11800, 92100, "Torax"],  # Simulado 2
    [14500, 81000, "Torax"],  # Simulado 3
    [12900, 86300, "Torax"],  # Simulado 4
    [15100, 79800, "Torax"],  # Simulado 5
]

# =====================================================================
# BLOCO 2: O JUIZ – Conta quantos erros uma reta comete
# =====================================================================

def contar_erros(a, b):
    erros = 0

    for rx in dados_rx:
        x = rx[0]      # pixels brancos
        y = rx[1]      # pixels pretos
        classe_real = rx[2]

        # valor da reta
        y_reta = a * x + b

        # regra de classificação
        chute = "Torax" if y > y_reta else "Bacia"

        # se errou, soma 1 erro
        if chute != classe_real:
            erros += 1

    return erros

# =====================================================================
# BLOCO 3: DESCIDA DA COLINA (Hill Climbing)
# =====================================================================

print("\n--- INICIANDO TREINAMENTO ---")

# chute inicial
melhor_a = 1.0
melhor_b = 0.0
melhor_erro = contar_erros(melhor_a, melhor_b)

print(f"Chute inicial: a={melhor_a:.4f}, b={melhor_b:.2f}, erros={melhor_erro}")

# tenta melhorar a reta por 5000 iterações
for tentativa in range(5000):

    if melhor_erro == 0:
        print(f"\nAprendizado perfeito na tentativa {tentativa}!")
        break

    # cria uma reta vizinha aleatória
    novo_a = melhor_a + random.uniform(-0.5, 0.5)
    novo_b = melhor_b + random.uniform(-1000, 1000)

    erro_vizinho = contar_erros(novo_a, novo_b)

    # se a vizinha for melhor, substitui
    if erro_vizinho < melhor_erro:
        melhor_a = novo_a
        melhor_b = novo_b
        melhor_erro = erro_vizinho
        print(f"Melhoria: a={novo_a:.4f}, b={novo_b:.2f}, erros={erro_vizinho}")

print("\n--- RESULTADO FINAL ---")
print(f"Melhor reta: y = {melhor_a:.4f}x + {melhor_b:.2f}")
print(f"Erros finais: {melhor_erro}\n")

# =====================================================================
# BLOCO 4: PROVA REAL (Classificação Final)
# =====================================================================

def classificar(a, b, x, y):
    return "Torax" if y > a*x + b else "Bacia"

print("Classificação Final:\n")

for rx in dados_rx:
    x = rx[0]
    y = rx[1]
    real = rx[2]

    chute = classificar(melhor_a, melhor_b, x, y)

    print(f"X={x:6d}, Y={y:6d} -> Modelo: {chute:6s} | Real: {real}")
