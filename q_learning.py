# Agent Q-learning
class QAgent:
    def __init__(self, actions):
        self.actions = actions
        self.learning_rate = 0.1
        self.discount_factor = 0.9
        self.epsilon = 0.1
        self.q_table = {}
        
    def get_q_value(self, state, action):
        pass
    
    def update_q_value(self, state, action, value):
        pass
    
    def choose_action(self, state):
        pass
    
    def learn(self, state, action, reward, next_state):
        pass