import pygame, sys
import random

pygame.init()


sfondo = pygame.image.load('immagini/sfondo.png') # C:\Programmare\Python\pygame-imparare-1 + immagini/sfondo.png 
uccello = pygame.image.load('immagini/mazinga z.png')
base = pygame.image.load('immagini/base.png')
gameover = pygame.image.load('immagini/gameover.png')
tubo_giu = pygame.image.load('immagini/tubo z - Copia (2).png')
tubo_su = pygame.transform.flip(tubo_giu,False,True)

altezza_schermo = 512

SCHERMO = pygame.display.set_mode((288,altezza_schermo))
FPS = 60/1
FLY_UP = -4.5
DIFFICOLTA = 1
VEL_AVANZ = 2.5
clock = pygame.time.Clock()
FONT = pygame.font.SysFont('Comic Sans MS', 25 , bold = True)     


class tubi_classe:
    def __init__(self):
        self.x = 300
        self.y = random.randint(-75,150)

    def avanza_e_disegna (self):
        self.x -= VEL_AVANZ

        SCHERMO.blit(tubo_giu, (self.x, self.y + 200))
        SCHERMO.blit(tubo_su, (self.x, self.y - 210))
        

    def collisione(self, uccello, uccellox, uccelloy):  

        tolleranza = 2
        uccello_lato_dx = uccellox + uccello.get_width() - tolleranza
        uccello_lato_sx = uccellox + tolleranza
        tubi_lato_dx = self.x + tubo_giu.get_width()
        tubi_lato_sx = self.x
        uccello_lato_su = uccelloy + tolleranza
        uccello_lato_giu = uccelloy + uccello.get_height() - tolleranza

        # disegnamo l'area dove sta il pennuto
        color = (255,0,0)
        pygame.draw.rect(SCHERMO, color, pygame.Rect(uccello_lato_sx, uccello_lato_su, uccello.get_width(), uccello.get_height()), 2)

        tubi_lato_su = self.y + 110
        tubi_lato_giu = self.y + 210

        if uccello_lato_dx > tubi_lato_sx and uccello_lato_sx < tubi_lato_dx: 
            if uccello_lato_su < tubi_lato_su or uccello_lato_giu > tubi_lato_giu:
                print(f"uccello_lato_su: {uccello_lato_su}")
                print(f"tubi_lato_su: {tubi_lato_su}")
                print(f"uccello_lato_giu: {uccello_lato_giu}")
                print(f"tubi_lato_giu: {tubi_lato_giu}")                
                hai_perso ()

def disegna_oggetti():    
    SCHERMO.blit(sfondo, (0,0))
    for tubo in tubi:
        tubo.avanza_e_disegna()

    SCHERMO.blit(uccello, (uccellox, uccelloy))

    SCHERMO.blit(base, (basex,400))
    punteggio =FONT.render("0", 1 , (0,0,0))
    SCHERMO.blit(punteggio,( 10, altezza_schermo - 50))

def aggiorna() :
    pygame.display.update()
    clock.tick(FPS)

def inizzializza():
    global uccellox, uccelloy, uccello_vely  # definisco 3 variabili globali
    global basex
    global tubi
    global punti
    uccellox, uccelloy = 60, 150  # imposto la posizione iniziale
    uccello_vely = 0       
    basex = 0 
    punti = 0
    tubi = []
    tubi.append(tubi_classe())

def hai_perso():
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
    basex -= VEL_AVANZ
    if basex < -45: basex = 0

    uccello_vely += 0.3 * DIFFICOLTA
    uccelloy += uccello_vely
    print(f"y: {uccelloy}")
    
    # quando la y ?? piu di 380 lo rimettiamo a 380 (cosi non va sotto la base)
    # se uccelloy ?? maggiore 380 allora: impostiamo uccelloy a 380

    spiaccicato = False
    if uccelloy > 380:          
        uccelloy = 380
        spiaccicato = True    
     
    for event in pygame.event.get(): # get = prendi  set = imposta
        if (event.type == pygame.KEYDOWN and event.key == pygame.K_UP): # evento di tipo "tasto schiacciato" e tasto "freccia su"
            uccello_vely = FLY_UP
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if uccelloy > 380:
            hai_perso()

    if tubi[-1].x < 150: tubi.append(tubi_classe())
    for t in tubi:
        t.collisione(uccello, uccellox, uccelloy)

    disegna_oggetti()
    aggiorna()

    if spiaccicato:
        hai_perso()