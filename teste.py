# Example file showing a basic pygame "game loop"
import pygame

# pygame setup
pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True

fonte = pygame.font.Font(None, 32)
texto_usuario = ''

pode_digitar = False

caixa_de_texto = pygame.Rect(200, 200, 140, 32)

while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            if caixa_de_texto.collidepoint(event.pos):
                pode_digitar = True 
            else:
                pode_digitar = False

        if event.type == pygame.KEYDOWN:
            if pode_digitar == True:
                if event.key == pygame.K_BACKSPACE:
                    texto_usuario = texto_usuario[:-1] #deleta o ultimo elemento
                else:
                    if event.unicode in "1234567890":
                        texto_usuario += event.unicode #Adiciona na string oque digita
    screen.fill("black")

    pygame.draw.rect(screen, "white", caixa_de_texto, 2)

    texto_surface = fonte.render(texto_usuario, True, (255, 255, 255))
    screen.blit(texto_surface, (caixa_de_texto.x + 5, caixa_de_texto.y + 5))

    caixa_de_texto.w = max(100, texto_surface.get_width() + 10)

    pygame.display.flip()

    clock.tick(60)  # limits FPS to 60

pygame.quit()