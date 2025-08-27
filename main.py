import pygame

pygame.init()
tela= pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
rodando = True
 
fonte = pygame.font.Font(None, 128)

titulo = 'How Many Cookies ?'

titulo_tranformado = fonte.render(titulo, True, "black")

pote_quase_cheio = pygame.image.load('Biscoitos/bote_quase_cheio.png').convert_alpha()

vidas = 5

while rodando:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            rodando = False

    tela.fill((222, 184, 135))

    tela.blit(titulo_tranformado, (220, 10))

    tela.blit(pote_quase_cheio, (500, 20))

    pygame.display.flip()

    clock.tick(60)  

pygame.quit()