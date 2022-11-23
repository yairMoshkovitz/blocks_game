import random
import pygame
from io import BytesIO
import requests



red = (255, 0, 0)                    # grapic vars
pink = (255, 174, 201)
white= (255,255,255)


try:
    wight = int(input('screen wight:'))
except:
    wight = 1200
try:
    hight = int(input('screen hight:'))
except:
    hight = 650

t = 40            # hight of block
z = wight//(t//3)  # wight of block, by the sceen




url = 'https://github.com/yairMoshkovitz/blocks_game/raw/main/b.png'

IMAGE = ''
while not IMAGE:      # try to load image from my git
    try:
        res_con = requests.get(url).content
        IMAGE = BytesIO(res_con)
        
        
    except:     # load dawnload image from user path
        print('you\'re not conect')
        IMAGE= input('input your b.png path (if it in the same folder that the game file is press enter):')+'b.png' 



level = ''
while not level:     # get the client level

    try:
        level = int(input("your level is (1-10, try 5): ",))
        if level >  10 or level < 1:
            level = ''
            erorr
    except:
        level = int(input("try again, your level is (1-10): ",))
print("press on mouse to start, and don't forget in the end to see your scors 'here' in the end ")




class  CARD():        # take the class CARD from memory game
    def __init__(self,x,y,color,t =30 ,z=40):
       
        self.color = color
        self.x = 50+x
        self.y = 20+y
        pygame.draw.line(screen, white , [self.x ,self.y], [self.x, self.y+30], 40)
        #pygame.display.flip()
        self.open = 0
        self.z = z  # wight of block
        self.t = t  # hight of block
       
    def close(self):
        self.open = 0
        pygame.draw.line(screen, white , [self.x ,self.y], [self.x, self.y+30], 40)
               
           
    def check(self,a,b):
        if self.x-(self.z/2) < a <self.x+self.z and self.y <b < self.y+self.t :
            self.open = 1
            return True

    def check_left(self,a,b):
        if self.x-(self.z/2) < a <self.x and self.y < b < self.y+self.t :
            return True

    def check_right(self,a,b):
        if self.x+(self.z/2) > a >self.x and self.y < b < self.y+self.t :
            return True
           

class BLOCK (CARD):  
    def __init__(self,x,y,color,t =t ,z=z):
       
        self.color = color
        self.open = 0
        self.z = z
        self.t = t
        self.x =x
        self.y =y
       
        pygame.draw.line(screen, color , [self.x ,self.y], [self.x, self.y+t], z)
        #pygame.display.flip()

       
    def check_ball(self,x,y,r):  # check if the ball touch the block 
        for i in range((r*2)):
            if self.check(x,y+i) or self.check(x+i,y) or self.check(x+(r*2),y+i) or self.check(x+i,y+(r*2)):
                return True
                
    def check_ball2(self,x,y,r):  # check if the ball touch the buttum_face in right or left side
        #for i in range((r*2)):
            if self.check_right(x,y) or self.check_right(x+(r*2),y) or self.check_right(x,y+r) or self.check_right(x+r*2,y+r):
                return 3
            elif self.check_left(x,y) or self.check_left(x+r*2,y) or self.check_left(x+(r*2), y+r) or self.check_left(x,y+r):
                return 2
               
    def check_all_balls(self,all_balls) :
        
       
        for ball in all_balls:
            if BLOCK.check_ball(self,ball.x,ball.y,ball.r) : # if the ball 
               
                ball.vy = -ball.vy
           
                if ball.y < 0:  # if the ball loss the screen
                    ball.y -= t//2
                else:
                    ball.y += t//2
             
           
       
    def check_all_balls2(self,all_balls) :
#        ball_num = 0
        for ball in all_balls:
            open_self =  BLOCK.check_ball2(self,ball.x,ball.y,ball.r*2)
            if open_self == 2:
                   
                ball.vy = -(ball.vy+level)-1
                if ball.vx>0:
                     ball.vx = -ball.vx-level-2

            elif open_self == 3:
                ball.vy = -(ball.vy+level)-1
                if ball.vx <0:
                       ball.vx = -ball.vx+level+2              
           
  
           
class Ball(pygame.sprite.Sprite):
    def __init__(self,x,y,level):
        super(Ball,self).__init__()
        self.x = x
        self.y = y
        self.r = 18
        self.vx = level
        self.vy = level
       
        try:
            self.image=pygame.image.load(IMAGE).convert()
            self.image.set_colorkey(pink)

        except:
            try:
                self.image= all_balls[0].image
            except:
                print('error maybe your path is rong')
                pygame.quit()


            
game_over =False          

screen = pygame.display.set_mode((wight, hight))

clock = pygame.time.Clock()

pygame.display.set_caption("yair game")


num_of_row =4
all_balls = [Ball(10+t*num_of_row,10+t*num_of_row,level) ]
  
x=  t//2
y=0
blocks2 =[]
pygame.init()
time = 0
p = time
num_of_blocks = 0
len_mistach = 300 -level *7
down = 0


def line_of_blocks():
    x= z//2 # 
    y=0
    new_blocks =[]
    while x < wight-20 :
    
        rand_color = tuple([random.randint(0,255) for i in range(3)])
        block = BLOCK(x,y,rand_color)
        new_blocks += [block]
       
        x += z # the the hight of block start position

    return new_blocks
   
blocks2 = line_of_blocks()   # made num of rows
for i in range(num_of_row-1):
    for blok in blocks2:
        blok.y += t
    blocks2 += line_of_blocks()    
clock.tick(0.2)


# pos = True

while True:
    mouse = pygame.mouse.get_pos()                       # start when pres mouse
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
       
            while True:
                if time > 70:                            # slow the game loop 
                    time = 50

                for event in pygame.event.get():                # stop when press quit
                    mouse = pygame.mouse.get_pos()
                    if event.type == pygame.QUIT:
                        pygame.quit()

               
                try:                                        # if there is a new size of buttum_face
                    if all_balls[0].vy < 0:   
                        mistah_short.y  -= all_balls[0].vy
                        mistah_long.y -= all_balls[0].vy
                    else:
                        mistah_long.y += all_balls[0].vy
                        mistah_short.y += all_balls[0].vy

                    mistah_long = BLOCK(mistah_long.x,mistah_long.y,mistah_long.color,20,len_mistach+50)
                    mistah_short = BLOCK(mistah_short.x,mistah_short.y,mistah_short.color,20,len_mistach-50)
                 #   pygame.display.flip()
                    if mistah_long.y+15 > mistah.y and mistah_long.x+mistah_long.z//2> mistah.x-mistah.z//2 and mistah_long.x - mistah_long.z//2< mistah.x+mistah.z//2 and mistah_long.color != red:
                        len_mistach +=50                    # the buttum_face catch the new buttum_face
                        mistah_long.color = red                 # to be shur that it's chang only one time
                    elif mistah_long.y > mistah.y :
                        mistah_long.color = red
                    if mistah_short.y+15 > mistah.y and mistah_short.x+mistah_short.z//2> mistah.x-mistah.z//2 and mistah_short.x - mistah_short.z//2< mistah.x+mistah.z//2 and mistah_short.color != red:
                        len_mistach -=50
                        mistah_short.color = red
                    elif mistah_short.y > mistah.y :
                        mistah_short.color = red
                except:
                     pass
                   
                   
                for ball in all_balls:
                    if ball.vx ==0:
                        ball.vx = 1
                    if ball.vy ==0:
                        ball.vy = 1
                   
                    ball.x += ball.vx   # add the speed
                    ball.y += ball.vy
                   
                    screen.blit(ball.image,[ball.x,ball.y])
                   

                       
                    if ball.vx > 14.9 :             # if the speed is too mach get it down and turn all the loop faster
                       
                        for a_ball in all_balls:
                            if a_ball.vy > 4 :
                                a_ball.vy = a_ball.vy//3     # because the loop faster the speed need to be slower
                            if a_ball.vx > 4 :
                                a_ball.vx = a_ball.vx//3
                        time +=5
                       
                    if ball.vy > 14.5 : # ...
                        for a_ball in all_balls:
                            a_ball.vy = a_ball.vy//3
                            a_ball.vx = a_ball.vx//2
                        time +=5
                       

         


                    if  ball.x >( wight - ball.r*5):             # turn vx to anther side when x thoch the end
                        ball.x =( wight - ball.r*5)
                        ball.vx = -ball.vx - 2
                    elif  ball.x <( ball.r):                 # ...thoch the start
                        ball.x =( ball.r)
                        ball.vx = -ball.vx + 2
                    if  ball.y <( ball.r):                   # turn vy to ?down when y thoch the ?
                        ball.y =( ball.r)
                        ball.vy = -ball.vy
               
                mistah = BLOCK(mouse[0], hight-21, white, 20, len_mistach)
                
                num_ball = mistah.check_all_balls2(all_balls)


                if time > (p):                              # new size of buttum_face and add new line when vy is bigger
                    p += time + 9
                    if time < 10:
                        mistah_long = BLOCK(mouse[0],150,white,20,len_mistach+50)
                        mistah_short = BLOCK(mouse[0]+400,-100,white,20,len_mistach-50)
                    elif mistah_long.color != white:
                        mistah_long = BLOCK(mouse[0],150,white,20,len_mistach+50)
                    if mistah_short.color != white:  
                        mistah_short = BLOCK(mouse[0]+400,-100,white,20,len_mistach-50)
                   
                    blocks2 += line_of_blocks()
                    
                    for blok in blocks2: 
                        blok.y +=t
                        if blok.y > hight:
                            game_over = True 

                    

               
                if time > 30 * len(all_balls):                                      # add more ball
                        all_balls += [Ball(10+t*num_of_row,10+t*num_of_row,-level) ]

                   
                if game_over or True in[ball.y > hight for ball in all_balls] : # game over when you lose the ball or the blok thoch the end
                    screen.fill((255,255,255))
                    pygame.display.flip()
                    print(f"game over your scors is: {num_of_blocks*level**2}")
                    clock.tick(1)
                    pygame.quit()


                i = 0
                del_blocks=[]
                for block in blocks2: # remove the "thochs" blooks

                    block_new = BLOCK(block.x, block.y, block.color) # bilt the blocks

                    block.check_all_balls(all_balls)

                    if block.open == 1 :
                        del_blocks += [i]
                        num_of_blocks += 1
                        down += 1
                    i+=1

                if down > 0 :  # if ball thoch any blook turn the ball down
                    
                    for i in range(down):
                         del blocks2[del_blocks.pop()]

                    down = 0


                pygame.display.flip()
                clock.tick(20+time)

                screen.fill((0,0,0))
               
