import random
import matplotlib.pyplot as plt

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
# BLOCO 2: O JUIZ (CONTA OS ERROS)
# =====================================================================

def contar_erros(a, b):
    erros = 0

    for x_branco, y_preto, classe_real in dados_rx:
        # Equação da reta: y = ax + b
        y_reta = a * x_branco + b

        # Regra: se o ponto estiver ACIMA da reta, é Tórax
        chute = "Torax" if y_preto > y_reta else "Bacia"

        if chute != classe_real:
            erros += 1

    return erros

# =====================================================================
# BLOCO 3: O CÉREBRO (DESCIDA DA COLINA)
# =====================================================================

print("--- TREINANDO IA (DESCIDA DA COLINA) ---")

# Chute inicial
melhor_a = 1.0
melhor_b = 0.0
melhor_erro = contar_erros(melhor_a, melhor_b)

print(f"Chute inicial: a={melhor_a:.4f}, b={melhor_b:.2f}, erros={melhor_erro}")

for tentativa in range(5000):
    if melhor_erro == 0:
        print(f"Sucesso! Reta perfeita encontrada na tentativa {tentativa}.")
        break

    # Gera um vizinho
    novo_a = melhor_a + random.uniform(-0.5, 0.5)
    novo_b = melhor_b + random.uniform(-1000, 1000)

    erro_vizinho = contar_erros(novo_a, novo_b)

    if erro_vizinho < melhor_erro:
        melhor_a = novo_a
        melhor_b = novo_b
        melhor_erro = erro_vizinho
        print(f"Melhoria: a={novo_a:.4f}, b={novo_b:.2f}, erros={erro_vizinho}")

print("\n--- RESULTADO FINAL ---")
print(f"Melhor reta: y = {melhor_a:.4f}x + {melhor_b:.2f}")
print(f"Erros finais: {melhor_erro}")

# =====================================================================
# BLOCO 4: GRÁFICO – PONTOS + RETA DA IA
# =====================================================================

# Separa pontos de bacia e tórax
x_bacia  = [d[0] for d in dados_rx if d[2] == "Bacia"]
y_bacia  = [d[1] for d in dados_rx if d[2] == "Bacia"]
x_torax  = [d[0] for d in dados_rx if d[2] == "Torax"]
y_torax  = [d[1] for d in dados_rx if d[2] == "Torax"]

# Gera pontos da reta usando o menor e maior X do conjunto
min_x = min(d[0] for d in dados_rx)
max_x = max(d[0] for d in dados_rx)

xs_linha = [min_x, max_x]
ys_linha = [melhor_a * x + melhor_b for x in xs_linha]

# Configura o tamanho da figura
plt.figure(figsize=(10, 6))

# Plota os pontos
plt.scatter(x_bacia, y_bacia, color="blue", label="Bacia (Mais Osso)")
plt.scatter(x_torax, y_torax, color="red", label="Tórax (Mais Ar)")

# Plota a reta da IA
plt.plot(xs_linha, ys_linha, "g--", label="Classificador IA")

# Títulos e rótulos
plt.title("Classificação Automática: Bacia vs Tórax")
plt.xlabel("Eixo X: Pixels Brancos (Osso)")
plt.ylabel("Eixo Y: Pixels Pretos (Ar)")
plt.legend()

plt.grid(True)
plt.tight_layout()
plt.show()
