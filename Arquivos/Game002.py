import pygame

pygame.init()

gameDisplay = pygame.display.set_mode((800, 600))
pygame.display.set_caption('Nome do Jogo')

pygame.display.update()

while True:
    for event in pygame.event.get():
        print(event)

pygame.quit()
quit()
