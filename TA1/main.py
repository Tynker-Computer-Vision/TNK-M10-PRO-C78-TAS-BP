
import pygame,math
import neat

pygame.init()
screen = pygame.display.set_mode((1067,600))

pygame.display.set_caption("Car racing")
background_image = pygame.image.load("track.png").convert()
player_image = pygame.image.load("car.png").convert_alpha()

player=pygame.Rect(170,300,20,20)

WHITE=(255,255,255)
xvel=2
yvel=3
angle=0
change=0

distance=2
forward=False

font = pygame.font.Font('freesansbold.ttf', 12)

def newxy(x,y,distance,angle):
  angle=math.radians(angle+90)
  xnew=x+(distance*math.cos(angle))
  ynew=y-(distance*math.sin(angle))
  return xnew,ynew


gen=0
angle =0
  
# Create a function eval_fitness which is called automaticalling   

    # Use global keyword as we are writing the game code inside a function, and in python global is required when accessing the global variables inside a function
    
    
    # Gen count to show which generation is this (Can be given as boiler to uncomment)
    
    # Genome count to show which genome is running (can be given as boiler to uncomment)
    
    # Run the game code for each genome in the generation
        
        # Print the text on game screen (Can be given as boiler to uncommnet)

# Make it part of eval_fitness() function             
while True:
          screen.blit(background_image,[0,0])
          pygame.draw.rect(screen,(0,0,0), [400, 0, 210, 78])
          # Uncomment this line
          #screen.blit(infoText, (402, 20))
         
          for event in pygame.event.get():
            if event.type == pygame.QUIT:
              pygame.quit()
              
            if event.type == pygame.KEYDOWN:
               if event.key == pygame.K_LEFT:
                  change = 5
               if event.key ==pygame.K_RIGHT:
                change = -5 
               if event.key == pygame.K_UP:
                forward = True
                
            if event.type == pygame.KEYUP:
              if event.key ==pygame.K_LEFT or event.key == pygame.K_RIGHT:
                  change = 0
              if event.key == pygame.K_UP:
                forward = False 
            
          if forward:
              player.x,player.y=newxy(player.x, player.y, 3, angle)  

          angle = angle + change
          
          newimage=pygame.transform.rotate(player_image,angle) 
          pygame.draw.rect(screen,(0, 255, 0), player)
          screen.blit(newimage ,player)
         
              
          pygame.display.update()
          pygame.time.Clock().tick(30)
       
# Load NN configuration    

# Create a population according to the configuration

# Run the genetic algorithm for 10 generations

