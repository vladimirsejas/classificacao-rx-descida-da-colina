import matplotlib.pyplot as plt
import numpy as np

# Pontos (mesmos dados)
dados_rx = [
    [47117, 52882, "Bacia"],
    [46483, 53516, "Bacia"],
    [37977, 62022, "Bacia"],
    [41649, 58350, "Bacia"],
    [39735, 60264, "Bacia"],
    [31966, 68033, "Bacia"],
    [43955, 56045, "Bacia"],
    [12500, 85400, "Torax"],
    [13200, 88500, "Torax"],
    [11800, 92100, "Torax"],
    [14500, 81000, "Torax"],
    [12900, 86300, "Torax"],
    [15100, 79800, "Torax"],
]

# Separando pontos
x_bacia  = [d[0] for d in dados_rx if d[2] == "Bacia"]
y_bacia  = [d[1] for d in dados_rx if d[2] == "Bacia"]
x_torax  = [d[0] for d in dados_rx if d[2] == "Torax"]
y_torax  = [d[1] for d in dados_rx if d[2] == "Torax"]

# Valores de X para desenhar a reta
xs = np.linspace(min(x_bacia + x_torax), max(x_bacia + x_torax), 100)

# Inclinação (a) – você pode brincar com esse valor
a = 1.5

plt.ion()  # modo interativo ligado

fig, ax = plt.subplots(figsize=(10, 6))

for b in range(-50000, 150000, 15000):  # mexe o valor de b (reta sobe/desce)
    ax.clear()

    # pontos
    ax.scatter(x_bacia, y_bacia, color="blue", label="Bacia (Mais Osso)")
    ax.scatter(x_torax, y_torax, color="red", label="Tórax (Mais Ar)")

    # reta
    ys = a * xs + b
    ax.plot(xs, ys, "g--", label=f"Reta: y = {a:.2f}x + {b}")

    ax.set_title("Movimento da Reta Classificadora")
    ax.set_xlabel("Pixels Brancos (X)")
    ax.set_ylabel("Pixels Pretos (Y)")
    ax.legend()
    ax.grid(True)

    plt.tight_layout()
    plt.pause(0.8)  # espera 0.8 segundos antes de atualizar

plt.ioff()
plt.show()

