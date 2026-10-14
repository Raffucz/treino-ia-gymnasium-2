from stable_baselines3 import PPO
from agente2 import agente2

ambiente = agente2()
# Carrega sem treinar
modelo = PPO.load("cerebro_agente")

obs, _ = ambiente.reset()
done = False
traducao = {0: "Cima", 1: "Baixo", 2: "Direita", 3: "Esquerda"}

print("Iniciando a partida:")
while not done:
    action, _ = modelo.predict(obs, deterministic=True)
    obs, reward, done, _, _ = ambiente.step(action)
    print(f"Ação: {traducao[int(action)]} -> Posição: ({int(obs[0])}, {int(obs[1])})")
    if reward == 20:
        print("Tesouro encontrado!")
    elif reward == -15:
        print("Monstro encontrado!")
    elif done:
        print("Fim da partida!")