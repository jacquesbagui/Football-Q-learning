import numpy as np
from environment import Environment
from game_gui import GameGUI
import pygame
import sys

from q_learning import QAgent


     
def main():
    gui = GameGUI(700, 500)
    env = Environment()
    agent = QAgent(actions=["UP", "DOWN", "LEFT", "RIGHT"])

    running = True
    while running:
        gui.handle_events()
        gui.draw_field(env)
        gui.update_display()
        
        pygame.time.wait(1000)
        
        # Test Action
        env.step("RIGHT")
        
        
if __name__ == "__main__":
    main()
