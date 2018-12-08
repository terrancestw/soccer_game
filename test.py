import pygame,sys

pygame.init()

def cropSurface(newWidth,newHeight,cropWidth,cropHeight,image):
    newSurf = pygame.Surface((newWidth,newHeight),
                             pygame.SRCALPHA,32)
    newSurf.blit(image,(0,0),(cropWidth,cropHeight,
                              newWidth,newHeight))
    return newSurf





width = 900
height = 700
screenDim = (width,height)

screen = pygame.display.set_mode(screenDim)
pygame.display.set_caption("Sample Game")

grassImage = pygame.image.load("grass.png").convert() #load faster with convert()
grassImage = pygame.transform.scale(grassImage,(screenDim)) #full screen background image
screen.blit(grassImage,(0,0))

rescale = 3
player = pygame.image.load("characterBody.png").convert_alpha() #convert_alpha make image transparency
playerWidth = player.get_rect().width
playerHeight = player.get_rect().height
player = pygame.transform.scale(player,
                               (playerWidth*rescale,
                                playerHeight*rescale)) #resize player
player = pygame.transform.rotate(player,90) # rotate player 
#screen.blit(player,(0,0))

foot = pygame.image.load("characterFoot.png").convert_alpha()
footWidth = foot.get_rect().width
footHeight = foot.get_rect().height
foot = pygame.transform.scale(foot,
                             (footWidth*rescale,
                             footHeight*rescale))
foot = pygame.transform.rotate(foot,90)
#screen.blit(foot,(0,0))

rescaleBall = 2
ball = pygame.image.load("ball.png").convert_alpha()
ballWidth = ball.get_rect().width
ballHeight = ball.get_rect().height
ball = pygame.transform.scale(ball,
                             (ballWidth*rescaleBall,
                              ballHeight*rescaleBall))
#screen.blit(ball,(0,0))

goalLeft = pygame.image.load("goalLeft.png").convert_alpha()
goalLeft = pygame.transform.scale(goalLeft,(250,270))
goalLeftWidth = goalLeft.get_rect().width
goalLeftHeight = goalLeft.get_rect().height
adjust = 12
goalLeft = cropSurface(goalLeftWidth/2+adjust,
                       goalLeftHeight/2+adjust,
                       goalLeftWidth/2-adjust,
                       goalLeftHeight/2-adjust,
                       goalLeft)
#screen.blit(goalLeft,(0,0))

goalMiddle = pygame.image.load("goalMiddle.png").convert_alpha()
goalMiddle = pygame.transform.scale(goalMiddle,(250,270))
goalMiddleWidth = goalMiddle.get_rect().width
goalMiddleHeight = goalMiddle.get_rect().height
goalMiddle = cropSurface(goalMiddleWidth,
                         goalMiddleHeight/2+adjust,
                         0,
                         goalMiddleHeight/2-adjust,
                         goalMiddle)
#screen.blit(goalMiddle,(0,0))

goalRight = pygame.image.load("goalRight.png").convert_alpha()
goalRight = pygame.transform.scale(goalRight,(250,270))
goalRightWidth = goalRight.get_rect().width
goalRightHeight = goalRight.get_rect().height
goalRight = cropSurface(goalRightWidth/2+adjust,
                        goalRightHeight/2+adjust,
                        0,
                        goalRightHeight/2-adjust,
                        goalRight)
screen.blit(goalRight,(0,0))






finished = False

while finished == False:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True
            pygame.quit()
            sys.exit() # error won't show if sys added
            
            


    pygame.display.flip()
    
