bif="images.jpg"
baif="ball.png"
mif="mover.png"

import pygame,sys
from pygame.locals import *

pygame.init()

screen=pygame.display.set_mode((658,485),0,32)

background=pygame.image.load(bif).convert()
k1=pygame.image.load(baif).convert()
k2=pygame.image.load(mif).convert()

k=1
x=3
y=0
m=0
n=0
l=1

clock = pygame.time.Clock()
speedx=100
speedy=100

while k:
    for event in pygame.event.get():
        if event.type== QUIT:
            pygame.quit()
            sys.exit()
            
    x, y = pygame.mouse.get_pos()

    if l%3==0:
        speedx+=30
        speedy+=30
    
    time_passed = clock.tick(30)
    print time_passed
    time_passed_seconds = time_passed / 1000.0
    m=m+speedx*time_passed_seconds
    n=n+speedy*time_passed_seconds
    
    screen.blit(background,(0,0))
    screen.blit(k1,(m,n))
    screen.blit(k2,(x,445))

    if m>=656 or m<0:
        speedx=-speedx

    if n<0:
        speedy=-speedy

    if (n<443 and n>438) and (m-x<59 or x-m<34):
        speedy=-speedy
        l=l+1
    
    if n>480:
        pygame.quit()
        print 'you lose the match'
    
    pygame.display.update()

    
