import pygame,sys,random
from pygame.locals import *
pygame.font.init()
pygame.init()
screen =pygame.display.set_mode((800,600))
done = False
clock = pygame.time.Clock()
display_instructions = True
instuction_page =1
font = pygame.font.Font(None,84)
font1 = pygame.font.Font(None,48)
font.set_bold(True)
while not done and display_instructions:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            done = True
            pygame.quit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            instuction_page += 1
            if instuction_page == 2:
                display_instructions = False
                 
    screen.fill((0,0,0))

    if instuction_page == 1:
        text = font.render("HUNGRY MAN",True,(155,255,0))
        text1 = font1.render("click to start",True,(255,255,255))
        screen.blit(text,(200,200))
        screen.blit(text1,(323,340))
    pygame.display.update()
    clock.tick(60)        
    
foods = []
x=400
score = 0
for i in range(15):
    foods.append(pygame.Rect(random.randint(0,600),random.randint(0,150),20,20))
pygame.key.set_repeat(50,10)    
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if event.type==pygame.KEYDOWN:
              if event.key==pygame.K_LEFT:
                x-=10
              elif event.key==pygame.K_RIGHT:
                x+=10
    screen.fill((0,0,0))
    basicfont = pygame.font.Font(None,48)
    text = basicfont.render("score: "+str(score),True,(255,0,0))
    screen.blit(text,(620,0))
    man = pygame.draw.rect(screen,(100,150,0),(x%800,518,20,40))
    end=pygame.Rect(0,558,800,40)
    pygame.draw.rect(screen,(0,150,0),end)
    for i in range(len(foods)):
        pygame.draw.rect(screen,(255,0,0),foods[i])
        foods[i].move_ip(0,1)
        if (foods[i].colliderect(man)):
            foods[i]=pygame.Rect(random.randint(0,600),random.randint(0,150),20,20)
            score += 5
            print(score)
        elif(foods[i].colliderect(end)):
            foods[i]=pygame.Rect(random.randint(0,600),random.randint(0,150),20,20)
    pygame.display.update()
    clock.tick(60)        

