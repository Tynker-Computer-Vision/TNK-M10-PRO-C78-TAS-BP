
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

# Check if car is outside the track
# Define checkOutOfBounds() function with car parameter

  # Get x, y location and width, height of car in x, y, width, height variables
  
  

  # Inside if conditon call checkpixel(x,y) to check if that pixel is on road or not
  # Do this for points: (x,y), (x+width, y), (x, y+height), (x+width, y+height)
  # If all are true the return True
  
  

# Define checkPixel(x,y) to check color of the pixel      

    # Access global screen
    
    # Inside try block get the color at x,y using screnn.get_at(), if exception occurs then return 1
    
    
    # Check if color equals (137,137,137,255) i.e color of the road and return 0 else return 1
    
    

gen=0
angle =0
  
def eval_fitness(generation, config):
    global angle, gen, forward, change
    
    gen = gen+1
    genomeCount = 1
    
    for gid, genome in generation:        
        
        infoText = font.render('Generation :'+ str(gen)+  ' genomecount: '+str(genomeCount)+"/"+str(len(generation)) , True, (255,255,0))
        
        while True:
          screen.blit(background_image,[0,0])
          pygame.draw.rect(screen,(0,0,0), [400, 0, 210, 78])
          screen.blit(infoText, (402, 20))
         
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

          # Stop the game when player goes out of the race track, call function checkOutOfBounds(player) inside if condition          
          
          
              # Set x and y location of player object to 170 and 300
              
              # Set angle variable to 0
              
              # Increment the genomeCount by 1
              
              # Add break statement to end the current iteration i.e gameplay for current genome
              
          
          angle = angle + change
          
          newimage=pygame.transform.rotate(player_image,angle) 
          pygame.draw.rect(screen,(0, 255, 0), player)
          screen.blit(newimage ,player)

          # Make farward = True so that car always moves forward
          
              
          pygame.display.update()
          pygame.time.Clock().tick(30)
       
config = neat.config.Config(neat.DefaultGenome, neat.DefaultReproduction,neat.DefaultSpeciesSet, neat.DefaultStagnation,'config-feedforward.txt')  
p = neat.Population(config)
winner = p.run(eval_fitness,10) 
