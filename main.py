from _typeshed import Self
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


class tubi_classe:
    def __init__(self):
        self.x = 300
        self.y = random.randint(-75,150)
def avanza_e_disegna (self) :
    self.x -= VEL_AVANZ
    SCHERMO.blit(tubo_giu, (self.x,self.y+250))
    SCHERMO.blit(tubo_su, (self.x,self.y-210))
def disegna_oggetti():    
     SCHERMO.blit(sfondo, (0,0) )
     for t in tubi:
         t.avanza_e_disegna()
     SCHERMO.blit(uccello, (uccellox, uccelloy))
     SCHERMO.blit(base, (basex,400))
     
def aggiorna() :
    pygame.display.update()
    clock.tick(FPS)

def inizzializza():
    global uccellox, uccelloy, uccello_vely  # definisco 3 variabili globali
    global basex
    global tubi
    uccellox, uccelloy = 60, 150  # imposto la posizione iniziale
    uccello_vely = 0       
    basex =0 
    tubi = []
    tubi.append(tubi_classe())

def hai_perso ():
    SCHERMO.blit(gameover, (50,180))
    aggiorna ()
    ricominciamo = False
    while not ricominciamo: # vuol dire ricominciamo = False
        for event in pygame.event.get():   
            if (event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE):
                inizzializza ()
                ricominciamo = True
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

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
        if uccelloy > 380:
            hai_perso ()


    disegna_oggetti()
    aggiorna()