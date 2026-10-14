import os
from stable_baselines3 import PPO
from agente2 import agente2  # Importa o mapa do arquivo 1

caminho = "cerebro_agente.zip"
ambiente = agente2()

# A sua lógica perfeita de verificação:
if os.path.exists(caminho):
    print("Cérebro antigo encontrado! Carregando...")
    modelo = PPO.load("cerebro_agente", env=ambiente, verbose=1)
else:
    print("Criando IA do zero...")
    modelo = PPO("MlpPolicy", ambiente, verbose=1)

print("Treinando...")
modelo.learn(total_timesteps=15000)
modelo.save("cerebro_agente")
print("Cérebro salvo!")