#LIBRERIAS
import pygame as game
import time
import random 

game.init()

#COLOR CODING
white=(255,255,255)
black=(0,0,0)
red=(255,0,0)
blue=(0,255,255)
green=(0,255,0)
yellow=(255,255,102)

#SCREEN
show_width=375
show_height=450
show=game.display.set_mode((show_width,show_height))
game.display.set_caption('Snake Game for UTEPO')
clock=game.time.Clock()

#SNAKE SETTINGS
S_size=10
S_speed=15

#FONTS
font=game.font.SysFont('Lucida Console',30)
Score_font=game.font.SysFont('comicsansms',15)

#SCORE
def Score(score):
    val=Score_font.render('Score: '+ str(score),True,white)
    show.blit(val,[0,0])

#SNAKE BODY
def Snake(S_size,S_list):
    for x in S_list:
        game.draw.rect(show,blue,[x[0],x[1],S_size,S_size])

#MESSAGE 
def Message(msg,color,y):
    Mess=font.render(msg,True,color)
    show.blit(Mess,[show_width/6,y])

#GAME LOOP
def Game_loop():

    game_over=False
    game_close=False

    #SNAKE MOVEMENT
    x=show_width/2
    y=show_height/2

    Xchange=0
    Ychange=0

    #SETTINGS
    S_list=[]
    S_length=1

    #FOOD PLACEMENT
    Food_x=round(random.randrange(0,show_width-S_size)/10.0)*10.0
    Food_y=round(random.randrange(0,show_height-S_size)/10.0)*10.0

    while not game_over:
        
        #PLAY AGAIN
        while game_close==True:
            show.fill(black)
            Message(' --GAME OVER--',white,show_height/6)
            Message('--Press Q-Quit--', red,show_height/4)
            Message(' --C-Continue--',green,show_height/3)
            game.display.update()
            for event in game.event.get():
                    if event.type==game.KEYDOWN:
                        if event.key==game.K_q:
                            game_over=True
                            game_close=False
                        if event.key==game.K_c:
                            Game_loop()

        #GAME 
        for event in game.event.get():
            
            #QUIT SCREEN
            if event.type==game.QUIT:
                game_over=True  
            
            #MOVEMENT
            if event.type==game.KEYDOWN:
                if(event.key==game.K_LEFT):
                    Xchange=-S_size
                    Ychange=0
                elif(event.key==game.K_RIGHT):
                    Xchange=S_size
                    Ychange=0
                elif(event.key==game.K_UP):
                    Xchange=0
                    Ychange=-S_size
                elif(event.key==game.K_DOWN):
                    Xchange=0
                    Ychange=S_size

        #SCREEN LIMITS            
        if (x>=show_width or x<0 or y>=show_height or y<0):
            game_close=True

        x+=Xchange
        y+=Ychange
        show.fill(black)

        #DRAW SNAKE AND FOOD
        game.draw.rect(show,yellow,[Food_x,Food_y,S_size,S_size])

        S_head=[]
        S_head.append(x)
        S_head.append(y)
        S_list.append(S_head)
        
        if len(S_list)>S_length:
            del S_list[0]

        for x in S_list[:-1]:
            if x== S_head:
                game_close=True
        
        Snake(S_size,S_list)
        Score(S_length-1)
        game.display.update()

        if x==Food_x and y==Food_y:
            print('yummy')
            Food_x=round(random.randrange(0,show_width-S_size)/10.0)*10.0
            Food_y=round(random.randrange(0,show_height-S_size)/10.0)*10.0
            S_length+=1

        clock.tick(S_speed)

    game.quit()
    quit()

Game_loop()
