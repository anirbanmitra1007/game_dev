import math, pygame, sys
pygame.init()

display_width,display_height=800,600 #size

black ={0,0,0}
white ={0,0,0}
gameDisplay = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption('A racey game')
clock=pygame.time.Clock()
carImg=pygame.image.load('ball.png')

def car(x,y):
	gameDisplay.blit(carImg,(x,y))

x=(display_width*.5)
y=(display_height*.8)
crashed = False
while not crashed:

	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			crashed = True
	gameDisplay.fill(black)	
	car(x,y)
	pygame.display.update()
	# define frames per second
	clock.tick(60) #gives a delay
pygame.quit()
quit()
