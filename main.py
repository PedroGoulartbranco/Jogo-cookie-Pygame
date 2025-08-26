import pygame

pygame.init()
tela= pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
rodando = True
 
while rodando:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            rodando = False

    tela.fill((222, 184, 135))

    pygame.display.flip()

    clock.tick(60)  

pygame.quit()