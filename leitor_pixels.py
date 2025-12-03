from PIL import Image
import os

# ============================================================
# 1. Lista de imagens usadas no experimento
#    (ajuste os nomes dos arquivos para os seus arquivos reais)
# ============================================================
imagens = [
    {"arquivo": "rx_torax_1.png",  "classe": "Torax"},
    {"arquivo": "rx_torax_2.png",  "classe": "Torax"},
    {"arquivo": "rx_torax_3.png",  "classe": "Torax"},
    {"arquivo": "rx_torax_4.png",  "classe": "Torax"},
    {"arquivo": "rx_torax_5.png",  "classe": "Torax"},
    {"arquivo": "rx_bacia_1.png",  "classe": "Bacia"},
    {"arquivo": "rx_bacia_2.png",  "classe": "Bacia"},
    {"arquivo": "rx_bacia_3.png",  "classe": "Bacia"},
    {"arquivo": "rx_bacia_4.png",  "classe": "Bacia"},
    {"arquivo": "rx_bacia_5.png",  "classe": "Bacia"},
]

# ============================================================
# 2. Função que lê a imagem e conta pixels claros e escuros
# ============================================================
def analisar_imagem(nome_arquivo, limiar=128):
    """
    Abre a imagem, converte para escala de cinza e conta
    quantos pixels são claros e quantos são escuros.

    limiar = valor de corte (0 a 255)
    p >= limiar -> considerado "branco"
    p <  limiar -> considerado "preto"
    """
    img = Image.open(nome_arquivo).convert("L")  # escala de cinza
    pixels = list(img.getdata())
    total = len(pixels)

    brancos = sum(1 for p in pixels if p >= limiar)
    pretos = total - brancos

    perc_brancos = (brancos / total) * 100
    perc_pretos = (pretos / total) * 100

    return brancos, pretos, perc_brancos, perc_pretos

# ============================================================
# 3. Gera a tabela na tela e em um arquivo .csv
# ============================================================
print("Gerando tabela de pixels...\n")

# abre arquivo CSV para salvar a tabela
with open("tabela_pixels_rx.csv", "w", encoding="utf-8") as f:
    # cabeçalho
    f.write("arquivo;classe;brancos;pretos;perc_brancos;perc_pretos\n")

    print(f"{'ARQUIVO':<20} | {'CLASSE':<6} | {'% BRANCOS':<10} | {'% PRETOS':<9}")
    print("-" * 60)

    for item in imagens:
        nome = item["arquivo"]
        classe = item["classe"]

        if not os.path.exists(nome):
            print(f"ARQUIVO NÃO ENCONTRADO: {nome}")
            continue

        br, pr, pb, pp = analisar_imagem(nome)

        # imprime na tela
        print(f"{nome:<20} | {classe:<6} | {pb:>9.2f}% | {pp:>8.2f}%")

        # grava no CSV
        linha = f"{nome};{classe};{br};{pr};{pb:.2f};{pp:.2f}\n"
        f.write(linha)

print("\nTabela salva em: tabela_pixels_rx.csv")
print("Use esses valores no seu código de classificação / descida da colina.")
