import pygame
import numpy as np
import os

pygame.init()
pygame.mixer.init()


#Function to display Text on screen
def TextShow(text,color,x,y,size):
    font = pygame.font.SysFont(None,size)
    screen_text = font.render(text,True,color)
    Gamespace.blit(screen_text,[x,y])

#Defining Colors
white = (255,255,255)
Sand = (255,255,220)
red = (255,0,0)
green = (0,255,0)
black = (0,0,0)
blue = (0,0,255)
a = False

#Snake Variables
snake_x = 300
snake_y = 200
size = 20
move = 5
movex = 0
movey = 0
score = 0
L = [[snake_x,snake_y,size,size]]
x = 0
k = False


#food Variables
food = False
food_x = -10
food_y = -10
fsize = 10

#Display Screen
w,h = 1000,700
Gamespace = pygame.display.set_mode((w,h)) #It should be in tuple
pygame.display.set_caption("Snakesss")


#Game Variables
exit = False
game_over = False
Start = True
#Creating a pygame clock
clock = pygame.time.Clock()

#Game LOOP
while not exit:
    while Start:
        Gamespace.fill(Sand)
        TextShow("Welcome to Snakes",green,300,200,70)
        TextShow("Press Space to Play",black,380,260,35)
        TextShow("Backspace to Exit",black,700,500,25)
        pygame.display.update()
        for event in pygame.event.get():  #List of all events in pygame
            #cross = Quit
            if event.type == pygame.QUIT:
                Start = False
                exit = True
                game_over = True
                break
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    Start = False
                    game_over = False
                elif event.key == pygame.K_BACKSPACE:
                    exit = True
                    game_over = True
                    Start = False
        
    while not game_over:
        for event in pygame.event.get():  #List of all events in pygame
            #cross = Quit
            if event.type == pygame.QUIT:
                exit = True
                game_over = True
                break
        
            #Taking Inputs
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    movex = move
                    movey = 0
                if event.key == pygame.K_LEFT:
                    movex = -move
                    movey = 0

                elif event.key == pygame.K_UP:
                    movex = 0
                    movey = -move

                elif event.key == pygame.K_DOWN:
                    movex = 0
                    movey = move
                elif event.key == pygame.K_p:
                    k = True
                    
                #CheatCode
                elif event.key == pygame.K_KP_PLUS:
                    score += 1
                    x = 1
                    food = False
                while k == True:
                    for event in pygame.event.get():
                        if event.key == pygame.K_p:
                            k = False
                            break
        #Movement of snake
        snake_x += movex
        snake_y += movey
    
        #Length of Snake Logic
        L.append([snake_x,snake_y,size,size])
        if x == 0:
            L.pop(0)
        else:
            x = 0   
        
        #Generating Food
        if food == False:
            food_x = np.random.randint(200,770)
            food_y = np.random.randint(55,630)
            food = True
        
    
        # Displaying Things on GameSpace
        Gamespace.fill(white) #Fills colour of sand in whole screen background
        pygame.draw.rect(Gamespace,black,[190,45,620,610])
        pygame.draw.rect(Gamespace,Sand,[200,55,600,590])
        for i in L:
            pygame.draw.rect(Gamespace,green,i) 
        pygame.draw.rect(Gamespace,red,[food_x,food_y,fsize,fsize])
    
        TextShow("Score : "+str(score*10),blue,850,660,40)
        TextShow("Snakess",green,400,10,60)
        pygame.display.update()
    
    
    ##Logic if snake goes from 1 side and comes out of other
        # if(snake_x <0):
        #     snake_x = w-1
        # if(snake_x>1000):
        #     snake_x = 0
        # if(snake_y<0):
        #     snake_y = h-1
        # if(snake_y>700):
        #     snake_y = 0
    
    
    
        #Logic behind Eating Food and showing next    
        if(snake_x-food_x<fsize and snake_x-food_x>-size)and(snake_y-food_y<fsize and snake_y-food_y>-size):
            pygame.mixer.music.load('C:/Users/Saksham Setia/Desktop/Coding/Python/PyGame/TutorialMake/Snakes/beep.mp3')
            pygame.mixer.music.play()
            score += 1
            x = 1
            food = False
        
    
        clock.tick(30+score) #Giving FPS in clock
    
    
        #GameLoose Mechanics
        if(L.count(L[0]) == 2):
            game_over = True

        if(snake_x>193 and snake_x<204)or(snake_x>775 and snake_x<790)or(snake_y>45 and snake_y<60)or(snake_y>620 and snake_y<635):
            game_over = True

    while game_over==True:
        if exit == True or a == True:
            a = False
            break
        
        Gamespace.fill(white)
        TextShow("Game Over",red,250,150,120)
        TextShow("Enter to Main ",green,100,290,80)
        TextShow("Menu",green,150,380,80)
        TextShow("Backspace to",blue,500,290,80)
        TextShow("Exit",blue,580,380,80)
        TextShow("Score : "+str(score*10),red,325,500,60)
        
        pygame.display.update()
        
        for event in pygame.event.get():
            
                
            if event.type == pygame.QUIT:
                exit = True
                game_over = False
                
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    score = 0
                    snake_x = 300
                    snake_y = 200
                    movex = 0
                    movey = 0
                    food = False
                    Start = True
                    exit = False
                    a = True
                    L = [[snake_x,snake_y,size,size]]
                elif event.key == pygame.K_BACKSPACE:
                    exit = True
                    game_over = False
    
print(score)
#Quit Game
pygame.quit()
quit()