import pygame,sys,math,time
from pygame.locals import *
pygame.init()

setDisplay=pygame.display.set_mode((400,300),0,32)
pygame.display.set_caption("Cool Game")
white = (255,255,255)
black=(0,0,0)
red=(255,0,0)
green=(0,255,0)
blue=(0,0,255)
yellow=(255,255,0)
cyan =(0,255,255)
purple = (255,0,255)

clock = pygame.time.Clock()
img= pygame.image.load('../images/ball.png')
imgx=20
imgy=20
pixMove= 5
movement= "down"	
# start of functions
def exitgame():
	pygame.quit()
	quit()
	sys.exit()

# main
while True:

	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			exitgame()
		elif event.type == KEYDOWN:
			if event.key == K_q:
				exitgame()

	if movement == "down":
		imgy += pixMove
		if imgy > 200:
			movement = "right"
	elif movement == "right":
		imgx += pixMove
		if imgx > 300:
			movement= "up"
	elif movement == "up":
		imgy -=pixMove
		if imgy < 30 :
			movement ="left"
	elif movement == "left":
		imgx -= pixMove
		if imgx < 30:
			movement = "down"

	setDisplay.fill(black)
	setDisplay.blit(img,(imgx,imgy))			
	pygame.display.update()
	clock.tick(60)
