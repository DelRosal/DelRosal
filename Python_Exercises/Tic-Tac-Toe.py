#LIBRARIES
from pydoc import doc
import pandas as pd

#NEW GAME
def New_Game():
    base={'A':['-','-','-'],'B':['-','-','-'],'C':['-','-','-']}
    tictac=pd.DataFrame(base)
    print(tictac)
    return base
    
#X TURN
def x_move():
    print('Player X')
    col,ren=place()
    base[col][ren]='x'
    tictac=pd.DataFrame(base)
    print(tictac)

#O TURN
def o_move():
    print('Player O')
    col,ren=place()
    base[col][ren]='o'
    tictac=pd.DataFrame(base)
    print(tictac)

#ASKS FOR POSITION
def place():
    print('Make your next move')
    ren=int(input('Row: '))
    col=input('Column: ')
    col=col.upper()
    if(base.get(col)[ren]!='-'):
        print('This place is occupied,\nTry Again: ')
        return place()
    return col,ren

#WINNER
def end_game():
    #VERTICAL
    if((base.get('A')[0]==base.get('A')[1] and base.get('A')[1]==base.get('A')[2]) and base.get('A')[0]!='-'):
        return 1
    elif((base.get('B')[0]==base.get('B')[1] and base.get('B')[1]==base.get('B')[2])and base.get('B')[0]!='-'):
        return 1
    elif((base.get('C')[0]==base.get('C')[1] and base.get('C')[1]==base.get('C')[2]) and base.get('C')[0]!='-'):
        return 1
    
    #HORIZONTAL
    elif(base.get('A')[0]==base.get('B')[0] and base.get('B')[0]==base.get('C')[0]) and base.get('A')[0]!='-':
        return 1
    elif(base.get('A')[1]==base.get('B')[1] and base.get('B')[1]==base.get('C')[1]) and base.get('A')[1]!='-':
        return 1
    elif(base.get('A')[2]==base.get('B')[2] and base.get('B')[2]==base.get('C')[2]) and base.get('A')[2]!='-':
        return 1

    #DIAGONAL
    elif(base.get('A')[0]==base.get('B')[1] and base.get('B')[1]==base.get('C')[2]) and base.get('A')[0]!='-':
        return 1
    elif(base.get('A')[2]==base.get('B')[1] and base.get('B')[1]==base.get('C')[0]) and base.get('A')[2]!='-':
        return 1
    else:
        return 0

#START OVER
def again():
    a=input('New Game?? (S/N)')
    if(a== 'S' or a=='s'):
        return 0
    else:
        print('END')
        return 1
   
#PLAYERS TURN
def turno():
    a=0
    while a<9:
        if(a%2==0):
            x_move()
            if (end_game()==1):
                print('TEAM X WINS')
                break
        elif(a%2!=0):
            o_move()
            if (end_game()==1):
                print('TEAM O WINS')
                break
                
        a=a+1
    if a==9:
        print('THATS A TIE')
    print('GAME OVER')
        
#MAIN CODE
cont=0
while cont==0:
    base=New_Game()
    turno()
    cont=again()
