# Agente Caçador de Tesouros em Ambiente 2D com Gymnasium e PPO

Este projeto implementa um ambiente customizado em grade 2D utilizando **Gymnasium** e treina um agente de Aprendizagem por Reforço com **PPO (Proximal Policy Optimization)** via **Stable-Baselines3**. 

O agente aprende a navegar no mapa para encontrar um **tesouro** sorteado aleatoriamente, enquanto evita um **monstro** e minimiza o número de passos.

---

## 🎮 Sobre o Ambiente (`agente2`)

O ambiente consiste em uma grade 2D ($5 \times 5$, coordenadas de 0 a 4) com elementos gerados em posições aleatórias a cada episódio:

* **Espaço de Ações (`Action Space`):** Discreto (`4` direções)
  * `0`: Cima (`y += 1`)
  * `1`: Baixo (`y -= 1`)
  * `2`: Direita (`x += 1`)
  * `3`: Esquerda (`x -= 1`)

* **Espaço de Observação (`Observation Space`):** Vetor contínuo de 6 posições `[x, y, tesouro_x, tesouro_y, monstro_x, monstro_y]`, permitindo que o agente conheça sua posição atual e as posições do tesouro e do monstro.

* **Recompensas e Finalização (`Reward System`):**
  * **Passo normal:** `-1` (para incentivar a encontrar o menor caminho).
  * **Encontrar o Tesouro:** `+20` e o episódio finaliza (Sucesso).
  * **Encontrar o Monstro:** `-15` e o episódio finaliza (Derrota).
  * **Limite de Passos:** `30` passos máximos por episódio.

---

## 📁 Estrutura do Projeto

* **`agente2.py`**: Classe do ambiente customizado que herda de `gym.Env`, definindo a lógica de movimento, posições randômicas, visão e recompensas.
* **`acesso_zip.py`**: Script de treinamento incremental. Verifica se já existe um cérebro salvo (`cerebro_agente.zip`). Se existir, carrega os pesos anteriores e continua o treinamento; caso contrário, cria a IA do zero.
* **`acompanhar.py`**: Script de visualização/inferência. Carrega o modelo treinado sem realizar novos treinos e executa uma partida completa, exibindo no terminal cada passo e decisão do agente.

---

## 🛠️ Tecnologias Utilizadas

* **Python 3**
* **Gymnasium**
* **Stable-Baselines3**
* **NumPy**

---

## 📦 Instalação de Dependências

Certifique-se de ter o Python instalado e rode o comando no terminal:

```bash
pip install gymnasium stable-baselines3 numpy
