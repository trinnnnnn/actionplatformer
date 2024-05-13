import pygame
import utils.window as window
from utils.fps import FPS
from states.mainmenu import MainMenu
from states.start import Start
from states.newsave import Newsave
from states.scoringtest import Scoringtest

pygame.init()

pygame.mixer.init()

#creating window, caption, and icon
caption = window.caption
screen = window.screen

clock = pygame.time.Clock()

class Game :
    def __init__(self) :
        pygame.init()

        #screen width and height
        self.screen = screen

        #fps
        self.clock = pygame.time.Clock()

        #starting gamestate
        self.gameStateManager = GameStateManager("mainmenu")

        #gamestates to call
        self.mainmenu = MainMenu(self.screen, self.gameStateManager)
        self.start = Start(self.screen, self.gameStateManager)
        self.newsave = Newsave(self.screen, self.gameStateManager)
        self.scoringtest = Scoringtest(self.screen, self.gameStateManager)

        #gamestate dictionary
        self.states = {"mainmenu":self.mainmenu,
                       "start":self.start,
                       "newsave":self.newsave,
                       "scoringtest":self.scoringtest,
                       }
        
    def run(self) :
        
        while True :
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit()

            self.states[self.gameStateManager.get_state()].run()

            pygame.display.update()
            self.clock.tick(FPS)

class GameStateManager :
        def __init__(self, currentState) :
            self.currentState = currentState
            
        def get_state(self) :
            return self.currentState
        
        def set_state(self, state) :
            self.currentState = state

if __name__ == "__main__":
    p = Game()
    p.run()