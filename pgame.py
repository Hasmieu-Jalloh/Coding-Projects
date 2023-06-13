import pygame

pygame.init()


HEIGHT = 800
WIDTH = 400

screen = pygame.display.set_mode((HEIGHT, WIDTH))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
    #Drawing all our elements
    #Update everything
    pygame.display.update()
