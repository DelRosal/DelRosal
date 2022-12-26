#LIBRARIES
import arcade
import random

#SCREEN

screen_w=925
screen_h=600
screen_tittle="Solitaire"

#CARDS

card_scale=0.6
card_w=140*card_scale
card_h=190*card_scale

mat_scale=1.25
mat_w=int(card_w*mat_scale)       
mat_h=int(card_h*mat_scale)       
       
margin_percent=0.10

bottom_y=mat_h/2+mat_h*margin_percent     
start_x=mat_w/2+mat_w*margin_percent  

top_y= screen_h - mat_h / 2 - mat_h * margin_percent
middle_y= top_y - mat_h - mat_h * margin_percent
x_spacing= mat_w + mat_w * margin_percent

card_values=['A','2','3','4','5','6','7','8','9','10','J','Q','K']   
card_suits=["Clubs","Hearts","Spades","Diamonds"]

class Card(arcade.Sprite):
    
    def __init__(self, suit, value, scale=1):
        self.suit=suit
        self.value=value
        self.image_file_name= f":resources:images/cards/card{self.suit}{self.value}.png"
        
        self.is_face_up=False
        
        super().__init__(facedown_cards, scale, hit_box_algorithm="None")
    
    def facedown(self):
        self.texture=arcade.load_texture(facedown_cards)
        self.is_face_up=False
    
    def faceup(self):
        self.texture=arcade.load_texture(self.image_file_name)
        self.is_face_up=True
        
    @property 
    def is_face_down(self):
        return not self.is_face_up
    
#PILES

count=13
bottom_facedown=0
bottom_faceup=1
play1= 2 
play2= 3 
play3= 4 
play4= 5 
play5= 6 
play6= 7 
play7= 8
top1 = 9 
top2 = 10 
top3 = 11 
top4 = 12 
card_offset= card_h * card_scale * 0.3

facedown_cards=":resources:images/cards/cardBack_red2.png"

#GAME CLASS
class Game(arcade.Window):
    
    def __init__(self):
        super().__init__(screen_w,screen_h,screen_tittle)
        self.card_list=None
        arcade.set_background_color(arcade.color.AMAZON)
        
        self.held_cards=None
        self.held_cards_original_pos=None
        
        self.pile_mat_list=None
        
        self.piles=None
      
    def setup(self):
        self.held_cards=[]
        self.held_cards_original_pos=[]
        
        self.pile_mat_list: arcade.SpriteList = arcade.SpriteList()
        pile= arcade.SpriteSolidColor(mat_w, mat_h, arcade.csscolor.DARK_OLIVE_GREEN)
        pile.position=start_x,bottom_y
        self.pile_mat_list.append(pile)
        
        pile= arcade.SpriteSolidColor(mat_w, mat_h, arcade.csscolor.DARK_OLIVE_GREEN)
        pile.position=start_x + x_spacing , bottom_y
        self.pile_mat_list.append(pile)
        
        for i in range (7):
            pile=arcade.SpriteSolidColor(mat_w,mat_h,arcade.csscolor.DARK_OLIVE_GREEN)
            pile.position= start_x + i * x_spacing , middle_y
            self.pile_mat_list.append(pile)
       
        for i in range (4):
            pile=arcade.SpriteSolidColor(mat_w,mat_h,arcade.csscolor.DARK_OLIVE_GREEN)
            pile.position= start_x + i * x_spacing , top_y
            self.pile_mat_list.append(pile) 
                
        self.card_list=arcade.SpriteList()
        
        
        for suit in card_suits:
            for value in card_values:
                card=Card(suit,value,card_scale)
                card.position= start_x,bottom_y
                self.card_list.append(card)
        
        for initial in range (len (self.card_list)):
            final=random.randrange(len(self.card_list))
            self.card_list.swap(initial,final)
            
        self.piles=[[] for x in range (count)]
        for card in self.card_list:
            self.piles[bottom_facedown].append(card)
            
        for pile_i in range (play1,play7+1):
            for y in range (pile_i - play1+1):
                card=self.piles[bottom_facedown].pop()
                self.piles[pile_i].append(card)
                card.position=self.pile_mat_list[pile_i].position
                self.pull_to_top(card)
                
        for i in range (play1, play7 + 1 ):
            self.piles[i][-1].faceup()
                
    
    def on_draw(self):
        self.clear()
        self.pile_mat_list.draw()
        self.card_list.draw()
        
    def pull_to_top(self, card: arcade.Sprite()):
        self.card_list.remove(card)
        self.card_list.append(card) 
           
    def on_mouse_press(self, x, y, button, modifiers):
        cards= arcade.get_sprites_at_point((x,y), self.card_list)
        if len(cards)>0:
            
            primary_card=cards[-1]
            assert isinstance(primary_card,Card)
            
            pile_index= self.get_pile_card(primary_card)
            
            if pile_index == bottom_facedown:
                for i in range (3):
                    if len(self.piles[bottom_facedown])== 0:
                        break
                    card= self.piles[bottom_facedown][-1]
                    card.faceup()
                    card.position= self.pile_mat_list[bottom_faceup].position
                    self.piles[bottom_facedown].remove(card)
                    self.piles[bottom_faceup].append(card)
                    self.pull_to_top(card)
                    
            elif primary_card.is_face_down:
                primary_card.faceup()
            else:
                self.held_cards=[primary_card]
                self.held_cards_original_pos=[self.held_cards[0].position]
                self.pull_to_top(self.held_cards[0])
            
                card_index= self.piles[pile_index].index(primary_card)
                for i in range (card_index + 1, len (self.piles[pile_index])):
                    card=self.piles[pile_index][i]
                    self.held_cards.append(card)
                    self.held_cards_original_pos.append(card)
                    self.pull_to_top(card)
        else:
            mats= arcade.get_sprites_at_point((x,y), self.pile_mat_list)
            if len(mats)>0: 
                mat=mats[0]
                mat_index= self.pile_mat_list.index(mat)
                
                if mat_index == bottom_facedown and len(self.piles[bottom_facedown]) == 0:
                    tmp_list= self.piles[bottom_faceup].copy()
                    for card in reversed(tmp_list):
                        card.facedown()
                        self.piles[bottom_faceup].remove(card)
                        self.piles[bottom_facedown].append(card)
                        card.position= self.pile_mat_list[bottom_facedown].position
                    
            
                
            
    def on_mouse_motion(self, x: float, y: float, dx: float, dy: float):
        for card in self.held_cards:
            card.center_x += dx
            card.center_y += dy
            
    def on_mouse_release(self, x: float, y: float, button: int, modifiers: int):
        if len(self.held_cards)==0:
            return
        
        pile, dist= arcade.get_closest_sprite(self.held_cards[0], self.pile_mat_list)
        reset_pos=True
        
        if arcade.check_for_collision(self.held_cards[0], pile):
            pile_index=self.pile_mat_list.index(pile)
            card_t=self.held_cards[0].suit

            if (self.held_cards[0].value== "A"):
                card_v=1
            elif (self.held_cards[0].value== "J"):
                card_v=11
            elif (self.held_cards[0].value== "Q"):
                card_v=12
            elif (self.held_cards[0].value== "K"):
                card_v=13
            else:
                card_v= int(self.held_cards[0].value)
            
            if (self.piles[pile_index] != []):
                base_t=self.piles[pile_index][-1].suit
                if (self.piles[pile_index][-1].value=="A"):
                    base_v=1
                elif (self.piles[pile_index][-1].value=="J"):
                    base_v=11
                elif (self.piles[pile_index][-1].value=="Q"):
                    base_v=12
                elif (self.piles[pile_index][-1].value=="K"):
                    base_v=13
                else:
                    base_v=int(self.piles[pile_index][-1].value)
            else:
                base_v=0
                base_t=card_t
                      
            if (base_t == "Clubs" or base_t=="Spades"):
                base_color=0
            else:
                base_color=1

            if (card_t == "Clubs" or card_t=="Spades"):
                card_color=0
            else:
                card_color=1
            
            if pile_index == self.get_pile_card(self.held_cards[0]):
                pass
            
            elif play1 <= pile_index <= play7 and (base_v == card_v+1 or base_v==0) and card_color==base_color:
                if len(self.piles[pile_index])> 0 :
                    top_card= self.piles[pile_index][-1]
                    
                        
                    
                    for i, card in enumerate (self.held_cards):
                        card.position= top_card.center_x, top_card.center_y - card_offset * (i+1)
                else:
                    for i, card in enumerate (self.held_cards):
                        card.position= pile.center_x, pile.center_y - card_offset * i
                
                for card in self.held_cards:
                    self.move_card(card, pile_index)
                    
                reset_pos=False
            
            elif top1 <= pile_index <= top4 and len(self.held_cards) == 1 and base_v == card_v-1 and card_t==base_t:
                self.held_cards[0].position= pile.position
                for card in self.held_cards:
                    self.move_card(card, pile_index)
                    
                reset_pos=False
                
                    
        
        if reset_pos:
            for index, card in enumerate (self.held_cards):
                card.position=self.held_cards_original_pos[index]
                
            
        self.held_cards=[]
    
    def get_pile_card (self, card):
        for index, pile in enumerate(self.piles):
            if card in pile:
                return index
    
    def remove_card(self, card):
        for pile in self.piles:
            if card in pile:
                pile.remove(card)
                break
            
    def move_card(self, card, pile_index):
        self.remove_card(card)
        self.piles[pile_index].append(card)
    
    def on_key_press(self, symbol: int, modifiers: int):
        if symbol == arcade.key.R:
            self.setup() 
           
   
#MAIN
def main():
    window=Game()
    window.setup()
    arcade.run()


    
main()
