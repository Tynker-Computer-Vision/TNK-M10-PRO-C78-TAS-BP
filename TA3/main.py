
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

def checkOutOfBounds(car):
  x = car.x
  y = car.y
  width = car.width
  height = car.height

  if(checkPixel(x,y) or checkPixel(x+width, y) or checkPixel(x, y+height) or checkPixel(x+width, y+height)):
      return True
     
def checkPixel(x, y):
    global screen
    try:
        color = screen.get_at((x, y))
    except:
        return 1
    if(color == (137,137,137,255)):
        return 0
    return 1

gen=0
angle =0
  
def eval_fitness(generation, config):
    global angle, gen, forward, change
    
    gen = gen+1
    genomeCount = 1
    
    for gid, genome in generation:
        # Create a neural network using current genome and configuration
        
        
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
                           
          if(checkOutOfBounds(player)):
              player.x = 170
              player.y = 300
              angle =0
              genomeCount = genomeCount +1
              break
          
          angle = angle + change
          
          newimage=pygame.transform.rotate(player_image,angle) 
          pygame.draw.rect(screen,(0, 255, 0), player)
          screen.blit(newimage ,player)
            
          # Make farward = True so that car always moves forward
          
          # Change controlls the left and right turn so set it to 0 so that car moves straight if not decided by NN
          
          # Give input to neural network and get output
          
          # Change value of change variable to turn left or right depending on value of output[0] and output[1]
          
              
          pygame.display.update()
          pygame.time.Clock().tick(30)
       
config = neat.config.Config(neat.DefaultGenome, neat.DefaultReproduction,neat.DefaultSpeciesSet, neat.DefaultStagnation,'config-feedforward.txt')  
p = neat.Population(config)
winner = p.run(eval_fitness,10) 
