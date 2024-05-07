import pygame
import sys

# Interface de Jeu
class GameGUI:
    def __init__(self, field_width, field_height):
        pygame.init()

        # Dimensions du terrain
        self.field_width = field_width
        self.field_height = field_height
        self.field_margin = 50

        # Couleurs
        self.WHITE = (255, 255, 255)
        self.GREEN = (0, 128, 0)
        self.RED = (255, 0, 0)
        self.BLUE = (0, 0, 255)
        self.YELLOW = (255, 255, 0)

        # Initialisation de la fenêtre
        self.screen_width = self.field_width + 2 * self.field_margin
        self.screen_height = self.field_height + 2 * self.field_margin
        self.screen = pygame.display.set_mode((self.screen_width, self.screen_height))
        pygame.display.set_caption("Football Q-learning")
        self.clock = pygame.time.Clock()

    def draw_field(self, env):
        self.screen.fill(self.GREEN)  # Fond vert pour le terrain de football

        # Les lignes du terrain
        pygame.draw.rect(self.screen, self.WHITE, (self.field_margin, self.field_margin, self.field_width, self.field_height), 2)  # Bord du terrain
        self.draw_goals()
        self.draw_midline()
        self.draw_center_circle()
        
        # Env
        self.draw_env(env)
        
    def draw_env(self, env):
        for row in range(len(env.terrain)):
            for col in range(len(env.terrain[row])):
                if env.terrain[row][col] == 1:  # Si la case est occupée
                    pygame.draw.circle(self.screen, self.WHITE, (col * 100 + self.field_margin + 50, row * 100 + self.field_margin + 50), 20)
                    
        # Agent
        agent_x, agent_y = env.agent_position
        pygame.draw.circle(self.screen, self.RED, (agent_x * 100 + self.field_margin + 50, agent_y * 100 + self.field_margin + 50), 15)
        
        # Adversary
        adv_x, adv_y = env.adversary_position
        pygame.draw.circle(self.screen, self.BLUE, (adv_x * 100 + self.field_margin + 50, adv_y * 100 + self.field_margin + 50), 15)
        
        # ball
        ball_x, ball_y = env.ball_position
        pygame.draw.circle(self.screen, self.YELLOW, (ball_x * 100 + self.field_margin + 50, ball_y * 100 + self.field_margin + 50), 10)


    def draw_goals(self):
        # But gauche
        pygame.draw.rect(self.screen, self.WHITE, (self.field_margin, self.field_margin + self.field_height // 3, 50, self.field_height // 3), 2)
        # But droit
        pygame.draw.rect(self.screen, self.WHITE, (self.field_margin + self.field_width - 50, self.field_margin + self.field_height // 3, 50, self.field_height // 3), 2)

    def draw_midline(self):
        pygame.draw.line(self.screen, self.WHITE, (self.field_margin + self.field_width // 2, self.field_margin), (self.field_margin + self.field_width // 2, self.field_margin + self.field_height), 2)

    def draw_center_circle(self):
        pygame.draw.circle(self.screen, self.WHITE, (self.field_margin + self.field_width // 2, self.field_margin + self.field_height // 2), 50, 2)

    def update_display(self):
        pygame.display.flip()
        self.clock.tick(60)

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
