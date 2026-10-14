import gymnasium as gym
import numpy as np
from gymnasium import spaces

class agente2(gym.Env):
    def __init__(self):
        super().__init__()
        self.action_space = spaces.Discrete(4)
        self.observation_space = spaces.Box(low=0, high=4, shape=(6,), dtype=np.float32)

    def pegar_visao(self):
        return np.array([
            self.x, self.y, 
            self.tesouro_x, self.tesouro_y, 
            self.monstro_x, self.monstro_y
        ], dtype=np.float32)

    def reset(self, seed=None):
        self.x, self.y, self.passos = 0, 0, 0
        self.tesouro_x = np.random.randint(1, 4)
        self.tesouro_y = np.random.randint(1, 4)
        self.monstro_x = np.random.randint(1, 4)
        self.monstro_y = np.random.randint(1, 4)
        return self.pegar_visao(), {}

    def step(self, action):
        self.passos += 1
        
        if action == 0 and self.y < 4: self.y += 1
        elif action == 1 and self.y > 0: self.y -= 1
        elif action == 2 and self.x < 4: self.x += 1
        elif action == 3 and self.x > 0: self.x -= 1

        reward, done = -1, False
        
        # AGORA SIM: Verifica se a IA pisou na coordenada sorteada do tesouro
        if self.x == self.tesouro_x and self.y == self.tesouro_y:
            reward, done = 20, True
            
        # Verifica se pisou na coordenada sorteada do monstro
        elif self.x == self.monstro_x and self.y == self.monstro_y:
            reward, done = -15, True
            
        elif self.passos >= 30:
            done = True

        return self.pegar_visao(), reward, done, False, {}