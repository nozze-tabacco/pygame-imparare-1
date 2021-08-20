import pygame, sys
import random

pygame.init()

sfondo=pygame.image.load('immagini/sfondo.png') # C:\Programmare\Python\pygame-imparare-1 + immagini/sfondo.png 
#sfondo=pygame.image.load('c:/miei file/cartella1/alex//immagini/sfondo.png') percorso assoluto
uccello=pygame.image.load('immagini/uccello.png')
base=pygame.image.load('immagini/base.png')
gameover=pygame.image.load('immagini/gameover.png')
tubo_giu=pygame.image.load('immagini/tubo.png')
tubo_su=pygame.transform.flip(tubo_giu,False,True)

SCHERMO=pygame.display.set_mode((288,512))
FPS=60/1
FLY_UP = -10
DIFFICOLTA = 2
VEL_AVANZ= 3
clock = pygame.time.Clock()

def disegna_oggetti():    
    SCHERMO.blit(sfondo, (0,0) )
    SCHERMO.blit(uccello, (uccellox, uccelloy))
    SCHERMO.blit(base, (basex,400))

def aggiorna() :
    pygame.display.update()
    clock.tick(FPS)

def inizzializza():
    global uccellox, uccelloy, uccello_vely  # definisco 3 variabili globali
    global basex
    uccellox, uccelloy = 60, 150  # imposto la posizione iniziale
    uccello_vely = 0       
    basex =0  

inizzializza()

while True:
    basex-= VEL_AVANZ
    if basex < -45: basex = 0
    print(basex)
    uccello_vely +=0.3 * DIFFICOLTA
    uccelloy += uccello_vely
    numeri = []
  

    for event in pygame.event.get(): # get = prendi  set = imposta
        if (event.type == pygame.KEYDOWN and event.key == pygame.K_UP): # evento di tipo "tasto schiacciato" e tasto "freccia su"
            uccello_vely = FLY_UP
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    
    disegna_oggetti()
    aggiorna()