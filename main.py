import random
#import math
import pygame
#import pygame.mixer
#import klafim
red = (255, 0, 0)
pink = (255, 174, 201)
white= (255,255,255)
IMAGE='b.png'
class klafim():
    def __init__(self,x,y,color,t =30 ,z=40):
       
        #super(klafim, self)._init_()
        self.color = color
        self.x = 50+x
        self.y = 20+y
        pygame.draw.line(screen, white , [self.x ,self.y], [self.x, self.y+30], 40)
        #pygame.display.flip()
        self.open = 0
        self.z = z
        self.t = t
       
    def close(self):
        self.open = 0
        pygame.draw.line(screen, white , [self.x ,self.y], [self.x, self.y+30], 40)
               
           
    def cheak(self,a,b):
        if self.x-(self.z/2) < a <self.x+self.z and self.y <b < self.y+self.t :
            self.open = 1
    def cheak_left(self,a,b):
        if self.x-(self.z/2) < a <self.x and self.y < b < self.y+self.t :
            self.open = 2
    def cheak_right(self,a,b):
        if self.x+(self.z/2) > a >self.x and self.y < b < self.y+self.t :
            self.open = 3
            return True
           
           
           
game_over =False          
           

rohv = 1200
gova = 700


screen = pygame.display.set_mode((rohv, gova))
white =( 255, 255, 255)
clock = pygame.time.Clock()
t = 40
z = rohv//(t//3)


pygame.display.set_caption("yair")




class bloks (klafim):
    def __init__(self,x,y,color,t =t ,z=z):
       
        #klafim.__init__(self,x,y,color)
        self.color = color
        self.open = 0
        self.z = z
        self.t = t
        self.x =x
        self.y =y
       
        pygame.draw.line(screen, color , [self.x ,self.y], [self.x, self.y+t], z)
        #pygame.display.flip()

       
    def cheak_ball(self,x,y,r):
        for i in range((r*2)):
            if self.open == 1:
                return True
            else:
                self.cheak(x,y+i)
                self.cheak(x+i,y)
                self.cheak(x+(r*2),y+i)
                self.cheak(x+i,y+(r*2))
   
    def cheak_ball2(self,x,y,r):
        for i in range((r*2)):
            if self.open < 2 :
                # self.cheak3(x,y+i)
                self.cheak_right(x+i,y)
                self.cheak_right(x+(r*2),y+i)
                self.cheak_right(x+i,y+(r*2))
           
                self.cheak_left(x,y+i)
                self.cheak_left(x+i//2,y)
               # self.cheak2(x+(r*2),y+i)
                self.cheak_left(x+i//2,y+(r*2))
            elif self.open == 3:
                return 3
            else:
                return 2
               
    def cheak_all_balls(self,all_balls) :
        j = 0
       
        for ball in all_balls:
            if bloks.cheak_ball(self,ball.x,ball.y,ball.r) :
               
                all_balls[j].vy = -all_balls[j].vy
           
                if all_balls[j].y < 0:
                    all_balls[j].y -= t//2
                else:
                    all_balls[j].y += t//2
             
            j += 1
       
    def cheak_all_balls2(self,all_balls) :
        k = 0
#        ball_num = 0
        for ball in all_balls:
            open_self =  bloks.cheak_ball2(self,ball.x,ball.y,ball.r*2)
            if open_self ==2:
                   
                all_balls[k].vy = -(all_balls[k].vy+level)-1
                if all_balls[k].vx>0:
                     all_balls[k].vx = -all_balls[k].vx-level

            elif open_self ==3:
                all_balls[k].vy = -(all_balls[k].vy+level)-1
                if all_balls[k].vx <0:
                       all_balls[k].vx = -all_balls[k].vx+level              
           
            k +=1
       # return ball_num
   
   
   
#                     all_balls[num_ball-1].vy = -(all_balls[num_ball-1].vy+level)
#                     if all_balls[num_ball-1].vx>0:
#                         all_balls[num_ball-1].vx = -all_balls[num_ball-1].vx
#                         #print(vx)
#                 elif mistah.open == 3:
#                     all_balls[num_ball-1].vy = -(all_balls[num_ball-1].vy+level)
#                     if all_balls[num_ball-1].vx <0:
#                         all_balls[num_ball-1].vx = -all_balls[num_ball-1].vx
 

   
           
class Ball(pygame.sprite.Sprite):
    def __init__(self,x,y,level):
        super(Ball,self).__init__()
        self.x = x
        self.y = y
        self.r =12
        self.vx = level
        self.vy = level
       

        self.image=pygame.image.load(IMAGE).convert()
        self.image.set_colorkey(pink)


level = ''
while not level:

    try:
        level = int(input("your level is (1-15): ",))
        if level >  15 or level < 1:
            level = ''
            erorr
    except:
        level = int(input("try again, your level is (1-15): ",))
print("press on mause to start, and dot forget in the end to see your scors")

num_of_row =4
all_balls = [Ball(10+t*num_of_row,10+t*num_of_row,level) ]
x=t//2
# all_balls += [Ball(10+t*num_of_row,10+t*num_of_row,-level) ]
y=0
bloks2 =[]
bloks3 =[]
pygame.init()
time = 0
p = time
num_of_blooks = 0
len_mistach =300 -level *7

down = 0


def line_of_blokim():
    x=z//2
    y=0
    new_bloks =[]
    while x < rohv-20 :
        k=[0,0,0]

        for i in range(3):
            k[i] = random.randint(0,255)

        l=tuple(k)

        blok = bloks(x,y,l)
        new_bloks += [blok]
       
        x+=z
       
#    print(vy ,vx)
    return new_bloks
   
bloks2 = line_of_blokim()
for i in range(num_of_row-1):
    for blok in bloks2:
        blok.y += t
    bloks2 += line_of_blokim()    
clock.tick(0.2)
pos = True
# while pos :
#     for event in pygame.event.get():    
#         if event.type == pygame.MOUSEBUTTONUP:
#             pos =False
while True:
    mouse = pygame.mouse.get_pos()
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
       
            while True:
                if time >80:
                    time = 50
                for event in pygame.event.get(): # stop when press quit
                    mouse = pygame.mouse.get_pos()
                    if event.type == pygame.QUIT:
                        pygame.quit()

               
                try:
                    if all_balls[0].vy < 0:
                        mistah_short.y  -= all_balls[0].vy
                        mistah_long.y -= all_balls[0].vy
                    else:
                        mistah_long.y += all_balls[0].vy
                        mistah_short.y += all_balls[0].vy
                    mistah_long = bloks(mistah_long.x,mistah_long.y,mistah_long.color,20,len_mistach+50)
                    mistah_short = bloks(mistah_short.x,mistah_short.y,mistah_short.color,20,len_mistach-50)
                 #   pygame.display.flip()
                    if mistah_long.y+15 > mistah.y and mistah_long.x+mistah_long.z//2> mistah.x-mistah.z//2 and mistah_long.x - mistah_long.z//2< mistah.x+mistah.z//2 and mistah_long.color != red:
                        len_mistach +=50
                        mistah_long.color = red
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
                   
                    ball.x += ball.vx # add the speed
                    ball.y += ball.vy
                   
                    screen.blit(ball.image,[ball.x,ball.y])
                   

                       
                    if ball.vx >19.9 : # if the speed is too mach get it down and turn all the loop paster
                       
                        for a_ball in all_balls:
                            a_ball.vy = a_ball.vy//3
                            a_ball.vx = a_ball.vx//2
                        time +=5
                       
                    if ball.vy >19.5 : # ...
                        for a_ball in all_balls:
                            a_ball.vy = a_ball.vy//3
                            a_ball.vx = a_ball.vx//2
                        time +=5
                       

                #     mistah_long = bloks(mouse[0],50,white,20,300- level*7)
                #     mistah_long.y += vy
                #     mistah_long = bloks(mistah_long.x,mistah_long.y,white,20,300- level*7)
                    if  ball.x >( rohv - ball.r*5): # turn vx to ather side when x thoch the end
                        ball.x =( rohv - ball.r*5)
                        ball.vx = -ball.vx - 2
                    elif  ball.x <( ball.r): # ...thoch the start
                        ball.x =( ball.r)
                        ball.vx = -ball.vx + 2
                    if  ball.y <( ball.r): # turn vy to ?down when y thoch the ?
                        ball.y =( ball.r)
                        ball.vy = -ball.vy
               
                mistah = bloks(mouse[0],gova-21,white,20,len_mistach)
                num_ball = mistah.cheak_all_balls2(all_balls)


#                 if mistah.open == 2 :    # add vy when thoch the mishth
#                     all_balls[num_ball-1].vy = -(all_balls[num_ball-1].vy+level)
#                     if all_balls[num_ball-1].vx>0:
#                         all_balls[num_ball-1].vx = -all_balls[num_ball-1].vx
#                         #print(vx)
#                 elif mistah.open == 3:
#                     all_balls[num_ball-1].vy = -(all_balls[num_ball-1].vy+level)
#                     if all_balls[num_ball-1].vx <0:
#                         all_balls[num_ball-1].vx = -all_balls[num_ball-1].vx
                if time > (p): # add new line when vy is bigger
                    p += time + 9
                    if time<10:
                        mistah_long = bloks(mouse[0],150,white,20,len_mistach+50)
                        mistah_short = bloks(mouse[0]+400,-100,white,20,len_mistach-50)
                    elif mistah_long.color != white:
                        mistah_long = bloks(mouse[0],150,white,20,len_mistach+50)
                    if mistah_short.color != white:  
                        mistah_short = bloks(mouse[0]+400,-100,white,20,len_mistach-50)
                   
                    for blok in bloks2:
                        blok.y +=t
                        if blok.y> gova:
                            game_over = True  
                    bloks2 += line_of_blokim()

               
                if time > 22 * len(all_balls):
                        all_balls += [Ball(10+t*num_of_row,10+t*num_of_row,-level) ]
                   
#                 if True in[ball.y > gova for ball in all_balls] :
#                     print([ (ball.y, ball.y > gova) for ball in all_balls] )
                if game_over or True in[ball.y > gova for ball in all_balls] : # game over when you lose the ball or the blok thoch the end
                    screen.fill((255,255,255))
                    pygame.display.flip()
                    print(f"game over your scors is: {num_of_blooks*level**2}")
                    clock.tick(1)
                    pygame.quit()


                i = 0
                del_bloks=[]
                for blok in bloks2: # remove the thoch's blooks



                    blok2 = bloks(blok.x,blok.y,blok.color)
                    blok.cheak_all_balls(all_balls)

                    if blok.open == 1 :
                        del_bloks+=[i]
                        num_of_blooks += 1
                        down = 1
                    i+=1

                if down==1:  # if ball thoch any blook turn the ball down
                    l = len(bloks2)
                    for i in del_bloks:
                         del bloks2 [-l+i]
                   
                   
                    down = 0


               

                pygame.display.flip()
                clock.tick(20+time)

                screen.fill((0,0,0))

               
