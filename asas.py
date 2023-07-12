import pygame

color_azul = (0,100,255) 
color_amarillo = (225,225,0)
color_verde = (0, 250, 0)
posicion_circulo = [250,250]
posicion_rectangulo = [100,5,100,200]
ANCHO_VENTANA = 500
LARGO_VENTANA = 500
pygame.init()
imagen_omori = pygame.image.load("omori.png")
imagen_omori = pygame.transform.scale(imagen_omori,(80,80))

timer_segundos = pygame.USEREVENT #custom event
pygame.time.set_timer(timer_segundos,100)


pantalla = pygame.display.set_mode((ANCHO_VENTANA,LARGO_VENTANA))
pygame.display.set_caption("War thunder 2")
flag_Correr = True
while flag_Correr:
    lista_eventos = pygame.event.get()
    for evento in lista_eventos:
        if evento.type == pygame.QUIT:
            flag_Correr = False
        if evento.type == pygame.MOUSEBUTTONDOWN:
            imagen_omori 



    pantalla.fill(color_azul)
    pygame.draw.circle(pantalla,color_amarillo,posicion_circulo,80)
    pygame.draw.rect(pantalla,color_verde,posicion_rectangulo)
    #mostrar los cambios en la pantalla
    pygame.display.flip()


pygame.quit()