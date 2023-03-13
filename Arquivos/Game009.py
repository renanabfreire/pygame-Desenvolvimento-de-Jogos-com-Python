import pygame

pygame.init()

white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)

gameDisplay = pygame.display.set_mode((800, 600))
pygame.display.set_caption('Joguin')

gameExit = False

lead_x = 300
lead_y = 300
x_change = 0
y_change = 0

clock = pygame.time.Clock()

while not gameExit:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameExit = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                x_change = -10
                y_change = 0
            if event.key == pygame.K_RIGHT:
                x_change = 10
                y_change = 0
            if event.key == pygame.K_UP:
                x_change = 0
                y_change = -10
            if event.key == pygame.K_DOWN:
                x_change = 0
                y_change = 10

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or pygame.K_RIGHT or pygame.K_UP or pygame.K_DOWN:
                x_change = 0
                y_change = 0

    lead_x += x_change
    lead_y += y_change

    gameDisplay.fill(white)
    pygame.draw.rect(gameDisplay, black, [lead_x,lead_y,10,10])

    pygame.display.update()

    clock.tick(30)

pygame.quit()
quit()
