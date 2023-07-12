import pygame
color_azul = (0,100,255) 
color_amarillo = (225,225,0)
color_verde = (0, 250, 0)
ANCHO_VENTANA = 500
LARGO_VENTANA = 500
lista_posiciones=[0,0]

pygame.init()
pantalla = pygame.display.set_mode((ANCHO_VENTANA,LARGO_VENTANA))
pygame.display.set_caption("War thunder 2")

imagen_omori = pygame.image.load("omori.png")
imagen_omori = pygame.transform.scale(imagen_omori,(80,80))
rect_omori = pygame.Rect(30,100,81,81)

flag_Correr = True
while flag_Correr:
    lista_eventos = pygame.event.get()
    for evento in lista_eventos:
        if evento.type == pygame.QUIT:
            flag_Correr = False
        if evento.type == pygame.MOUSEBUTTONDOWN:
             lista_posiciones  = list(evento.pos) 

    rect_omori[0] =  lista_posiciones[0] #modifico el left del rect
    rect_omori[1] =  lista_posiciones[1] #modifico el top del rect 

    pantalla.fill(color_azul)
    #DIBUJAR el rectangulo para ver cuanto ocupa
    pygame.draw.rect(pantalla, color_amarillo, rect_omori)

    pantalla.blit(imagen_omori,rect_omori)
    pygame.display.flip

pygame.quit()