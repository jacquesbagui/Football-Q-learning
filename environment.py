import numpy as np

# Environnement
class Environment:
    def __init__(self):
        self.field_width = 5
        self.field_height = 5
        self.terrain = np.zeros((self.field_height, self.field_width))  # Grille du Terrain
        self.agent_position = (2, 2)  # Position Initial de L'agent (HomeTeam)
        self.adversary_position = (2, 3)  # Position initiale de l'adversaire (AwayTeam)
        self.ball_position = (3, 3)  # Position initiale du ballon
    
    def step(self, action):
        # Déplacer l'agent
        if action == "UP":
            new_agent_position = (self.agent_position[0], max(0, self.agent_position[1] - 1))
        elif action == "DOWN":
            new_agent_position = (self.agent_position[0], min(self.field_height - 1, self.agent_position[1] + 1))
        elif action == "LEFT":
            new_agent_position = (max(0, self.agent_position[0] - 1), self.agent_position[1])
        elif action == "RIGHT":
            new_agent_position = (min(self.field_width - 1, self.agent_position[0] + 1), self.agent_position[1])
        else:
            new_agent_position = self.agent_position

        # Déplacer l'adversaire
        new_adv_position = (self.adversary_position[0], min(self.field_height - 1, self.adversary_position[1] + 1))

        # Déplacer le ballon
        new_ball_position = (self.ball_position[0], min(self.field_height - 1, self.ball_position[1] + 1))

        # Mettre à jour les positions
        self.agent_position = new_agent_position
        self.adversary_position = new_adv_position
        self.ball_position = new_ball_position

