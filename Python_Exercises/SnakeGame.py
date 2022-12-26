#LIBRARIES
import pygame as game
import random
import time

#COLOR CODING
black=(0,0,0)           #Background
white=(255,255,255)     #Food
orange=(255,100,10)     #Food
blue=(0,255,255)        #Snake 
green=(0,255,170)       #Score

#SCREEN
Screen_x=600
Screen_y=800

#SNAKE SETTINGS
S_speed=15

#START SCREEN
game.init()
game.display.set_caption('Snake Game <3')
Screen=game.display.set_mode((Screen_x,Screen_y))
clock=game.time.Clock()

#SCORE
score=0
def Score(score,color):
    font=game.font.SysFont('Lucida Console',25)
    Mess=font.render('Score: '+str(score),True,color)
    Score_pos=Mess.get_rect()
    Screen.blit(Mess,Score_pos)

#GAME OVER
def GameOver():
    font=game.font.SysFont('Lucida Console',30)
    Mess=font.render('Final Score: '+str(score),True,white)
    Mess_pos=Mess.get_rect()
    Screen.blit(Mess,Mess_pos)
    game.display.flip()
    time.sleep(1)
    
    game.quit()
    quit()


#DEFAULT SNAKE
S_pos=[200,300]
S_body=[[200,300],[190,300],[180,300],[170,300]]

#SNAKE DIRECTION
S_dir='RIGHT'
change_to=S_dir

#FRUIT
F_pos=[random.randrange(1,(Screen_x//10))*10,random.randrange(1,(Screen_y//10))*10]
F_spawn=True

#MAIN CODE
while True:
    #SNAKE KEYS
    for event in game.event.get():
        if event.type==game.QUIT:
                game.quit()
                quit()
        if event.type==game.KEYDOWN:
            if(event.key==game.K_UP):
                change_to='UP'
            if(event.key==game.K_DOWN):
                change_to='DOWN'
            if(event.key==game.K_LEFT):
                change_to='LEFT'
            if(event.key==game.K_RIGHT):
                change_to='RIGHT'
    
    #DIAGONAL
    if change_to=='UP' and S_dir!='DOWN':
        S_dir='UP'
    if change_to=='DOWN' and S_dir!='UP':
        S_dir='DOWN'
    if change_to=='LEFT' and S_dir!='RIGHT':
        S_dir='LEFT'
    if change_to=='RIGHT' and S_dir!='LEFT':
        S_dir='RIGHT'

    #SNAKE MOVEMENT
    if change_to=='UP':
        S_pos[1]-=10
    if change_to=='DOWN':
        S_pos[1]+=10
    if change_to=='LEFT':
        S_pos[0]-=10
    if change_to=='RIGHT':
        S_pos[0]+=10

    #SNAKE GROWTH
    S_body.insert(0,list(S_pos))
    if S_pos[0]==F_pos[0] and S_pos[1]==F_pos[1]:
        score+=1
        F_spawn=False
    else:
        S_body.pop()

    if F_spawn==False:
        F_pos=[random.randrange(1,(Screen_x//10))*10,random.randrange(1,(Screen_y//10))*10]

    F_spawn=True
    Screen.fill(black)

    for pos in S_body:
        game.draw.rect(Screen,blue,game.Rect(pos[0],pos[1],10,10))

    game.draw.rect(Screen,orange,game.Rect(F_pos[0],F_pos[1],10,10))

    #GAME OVER CONDITIONS
    if S_pos[0]<0 or S_pos[0]>Screen_x or S_pos[1]<0 or S_pos[1]>Screen_y:
        GameOver()
    for block in S_body[1:]:
        if S_pos[0]==block[0] and S_pos[1]==block[1]:
            GameOver()

    #SCORE DURING GAME
    Score(score,green)

    #REFRESH
    game.display.update()
    clock.tick(S_speed)
