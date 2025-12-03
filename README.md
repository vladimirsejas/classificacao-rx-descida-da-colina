# classificacao-rx-descida-da-colina
🩻 Classificação de Radiografias (Bacia x Tórax) usando Pixels e Descida da Colina

Este projeto demonstra, de forma simples e didática, como uma Inteligência Artificial pode classificar radiografias usando apenas:

quantidade de pixels brancos (ossos)

quantidade de pixels pretos (ar)

uma reta aprendida automaticamente pelo computador

Tudo foi feito com Python puro, sem bibliotecas avançadas de IA, para que qualquer aluno do primeiro semestre compreenda.

🎯 Objetivo do Projeto

Separar automaticamente dois tipos de radiografias:

Bacia → possui muito osso (mais pixels brancos)

Tórax → possui muito ar nos pulmões (mais pixels pretos)

Cada radiografia é transformada em um ponto no gráfico (X = pixels brancos, Y = pixels pretos).
Depois, uma reta é ajustada pela IA para dividir corretamente os dois tipos.

🧠 Como o computador entende a imagem?

Cada RX é convertida para escala de cinza.
O programa conta quantos pixels são claros e quantos são escuros.

Pixels brancos (osso) → eixo X

Pixels pretos (ar) → eixo Y

Assim, cada imagem vira um ponto no plano cartesiano.

Isso permite uma classificação simples usando apenas uma reta.

⛰️ Como a IA aprende? (Descida da Colina)

O computador começa com uma reta aleatória.

Depois ele faz milhares de tentativas, sempre procurando melhorar:

Testa uma nova reta

Conta quantos erros ela comete

Se a nova reta erra menos → ele substitui

Repete o processo até encontrar a melhor solução

Esse processo se chama:

✔️ Descida da Colina (Hill Climbing)

É um método simples de otimização usado para melhorar uma solução passo a passo.

📊 Gráfico Final

O projeto possui um gráfico que mostra:

🔵 Pontos azuis → Radiografias de Bacia

🔴 Pontos vermelhos → Radiografias de Tórax

🟢 Reta verde → fronteira de decisão aprendida pela IA

Fica visível que:

✔️ Pontos acima da reta → Tórax
✔️ Pontos abaixo da reta → Bacia

🎥 Demonstração: A Reta se Movendo

Incluímos também um exemplo visual onde a reta:

sobe

desce

e mostra como a classificação mudaria

Isso ajuda a entender como o modelo separa as classes no gráfico.
É uma excelente ferramenta didática.

🗂️ Estrutura do Projeto
├── leitor_pixels.py                      # Converte RX para pixels e cria a base de dados
├── classificador_bacia_torax_descida_colina.py
│                                          # IA que aprende a reta usando descida da colina
├── colina_grafico.py                      # Gera gráfico final com pontos e reta
├── reta_movendo.py                        # Demonstração da reta se movendo no plano
└── imagens_rx/                            # Radiografias utilizadas (Bacia e Tórax)

▶️ Como Executar
1) Instale o Python 3
2) Instale o matplotlib:
pip install matplotlib

3) Rode cada arquivo conforme a função:

leitor_pixels.py → extrai pixels das RX

classificador_bacia_torax_descida_colina.py → treina a reta (IA)

colina_grafico.py → mostra o gráfico com a divisão das classes

reta_movendo.py → demonstra a reta subindo/descendo (visual didático)

📚 Conclusão

Este projeto mostra que é possível criar um classificador real de radiografias usando:

matemática simples

contagem de pixels

uma reta

e uma técnica básica de otimização

É uma forma acessível e didática de entender como modelos lineares de IA funcionam na prática.
