#Snake game

import pygame as py # for game
import time  # for speed and closing time
import random # for generating random position for food 

py.init()   #init is used to import all the modules of pygame.

white = (255, 255, 255)  #pygame provide only RBC color all other are made by combination.
black = (0, 0, 0)
red = (255, 0, 0)
blue = (220, 220, 220)
green = (100, 255, 0)
yellow = (255, 255, 100)


width = 1000 #height and weidth of the surface
height = 1000
dis = py.display.set_mode((width, height)) #for making frame
py.display.set_caption('Snake Game') #this gets print on title

clock = py.time.Clock() #helps track time

snake_size = 10 #by one movement how much does snake move
snake_speed = 20 #speed of snake

#game_over = False




fontstyle = py.font.SysFont(None, 50) #when game ends
score_font = py.font.SysFont(None, 40) #for score
#can add any font if wanted.

def your_score(score):
    val = score_font.render("Your score is :" + str(score), True, green)
    dis.blit(val, [0, 0 ])

def our_snake(snake_size, snake_list):
    for z in snake_list:
        py.draw.rect(dis, black, [z[0], z[1], snake_size, snake_size])




def msg(m, color):
    mesg = fontstyle.render(m, True, color) #render is for writing on new surface
    dis.blit(mesg, [width/100, height/2])


#py.display.update()
def gameloop():
    game_over = False
    game_close = False
    
    x = width / 2
    y = height / 2
    
    x_change = 0
    y_change = 0 #help in holding new updated values of x and y
    
    snake_list = []
    length_of_snake = 1 #initially it is 1
    
    foody = round(random.randrange(0, height - snake_size) / 10 ) * 10 #x any y cordinate of food are randomly gen.
    foodx = round(random.randrange(0, width - snake_size) / 10 ) * 10 #this gives initial food location
    
    
    
   
    
    while not game_over:
        while game_close == True:
            
            dis.fill(white)
            msg("Bad Luck !!!! Press Q to quit and R to play again", red)
            your_score(length_of_snake - 1)
            py.display.update()
            
            for event in py.event.get(): #gets all event of pygame
                if event.type == py.KEYDOWN:
                    if event.key == py.K_q:
                         game_over = True
                         game_close = False
                        
                    if event.key == py.K_r:
                        gameloop()
                        
        for event in py.event.get():
            if event.type == py.QUIT:
                game_over = True
        
            if event.type == py.KEYDOWN: #work of up and down keys
                if event.key == py.K_LEFT:
                    x_change = -snake_size
                    y_change = 0
                elif event.key == py.K_RIGHT:
                    x_change = snake_size
                    y_change = 0
                elif event.key == py.K_UP:
                    x_change = 0
                    y_change = -snake_size
                elif event.key == py.K_DOWN:
                    x_change = 0
                    y_change = snake_size
                    
        if x >= width or x < 0 or y >=height or y < 0: #limit of surface from (0,0) to (weidth, height)
              game_close = True #games gets close i.e. accident by wall
             # msg("accident by wall", red)
              
        x += x_change #new values of x and y after every movement
        y += y_change
        dis.fill(white) #color of diplay at background
        
        py.draw.rect(dis, red, [foodx, foody, snake_size, snake_size]) # about food coordinate and size
        
        snake_head = []
        snake_head.append(x) #adding in snake lenght
        snake_head.append(y)
        snake_list.append(snake_head)
        if len(snake_list) > length_of_snake:
            del snake_list[0]
            
        for z in snake_list[:-1]: # if snake eats itself
            if z == snake_head:
                game_close = True
                
        our_snake(snake_size, snake_list)
        your_score(length_of_snake - 1)
        py.display.update()
        
        
        
        
     #   py.draw.rect(dis, red,[x, y, snake, snake]) #helps in drawing rectangle..... first two are starting point of snake and next two are size.......color of snake is red.
        

        if x == foodx and y == foody:   #when sanke passes through food point it gets equal
             foody = round(random.randrange(0, height - snake_size) / 10 ) * 10
             foodx = round(random.randrange(0, width - snake_size) / 10 ) * 10
             length_of_snake += 1 # after every cross snake length gets increased
           # print("eaten !! on fire")
        clock.tick(snake_speed) #help in mainatining speed of snake...  
        
    py.quit()
    quit()
    
gameloop()    
            
                        
                   
                    
                
            
    
    




                
   
       
                

                
    

    
    
    
    
    
        
