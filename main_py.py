import pygame

pygame.init()

pygame.display.set_caption("Snace_game")

screen = pygame.display.set_mode((600, 700))

icon = pygame.image.load("C:\\Users\\asaly\\PycharmProjects\\modul_7\\img.png")
pygame.display.set_icon(icon)

white = pygame.Color("blue")
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        screen.fill(white)
        pygame.display.update()

pygame.quit()
