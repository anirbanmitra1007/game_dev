import math,pygame,random,sys,time
from pygame.locals import *

#start of main function
pygame.init()

#size initialization
display_width = 800
display_height = 600 

car_width=50
black = (0,0,0)
white = (255,255,255)

gameDisplay = pygame.display.set_mode((display_width,display_height),0,32)

pygame.display.set_caption('A racey game')

clock = pygame.time.Clock()

carImg = pygame.image.load('ball.png')
#end of main

#defining obstacles
def things(thingx,thingy,thingw,thingh,color):
	pygame.draw.rect(gameDisplay,color,[thingx,thingy,thingw,thingh])
#end of defining obstacles

#displaying car
def car(x,y):
	gameDisplay.blit(carImg,(x,y))
#displaying car

#displaying text

def text_objects(text, font):
	textsurf = font.render(text,True,black)
	return textsurf, textsurf.get_rect()

#defining message to display
def message_display(text):
	largetext = pygame.font.Font('freesansbold.ttf',110 )
	textsurf, textrect = text_objects(text,largetext)
	textrect.center = ((display_width/2),(display_height/2))
	gameDisplay.blit(textsurf,textrect)
	pygame.display.update()
	time.sleep(2)
	game_loop()
# end of message display
# crash function
def crash():
	message_display("You Crashed")
#end of crash function
# game loop
def game_loop():
	x = (display_width*.45)
	y = (display_height*.9)

	thing_starty = -600
	thing_speed = 7
	thing_width = 100
	thing_height = 100
	thing_startx = random.randrange(0,display_width-thing_width)
	gameexit = False
	x_change = 0
	while not gameexit:

		for event in pygame.event.get():
			
			if event.type == pygame.QUIT:
				pygame.quit()
				quit()
			if event.type == KEYDOWN:
				if event.key == K_q:
					pygame.quit()
					quit()

			if event.type == KEYDOWN:
				if event.key == K_LEFT:
					x_change = -5
				elif event.key == K_RIGHT:
					x_change = 5
			elif event.type == KEYUP:
				if event.key == K_LEFT or event.key == K_RIGHT:
					x_change=0

		x =x + x_change			
		gameDisplay.fill(white)	
		things(thing_startx,thing_starty,thing_width,thing_height,black)
		thing_starty += thing_speed
		
		car(x,y)
		if x<0 or x>display_width-car_width:
			crash()
			gameexit = True

		if thing_starty >display_height:
			thing_starty = 0 - thing_height
			thing_startx = random.randrange(0,display_width-thing_width)
		
		if y < thing_starty + thing_height:

			 if x > thing_startx and x< thing_startx + thing_width or x + car_width > thing_startx and x+ car_width < thing_startx + thing_width:
			 	 
			 	 print "crash"
			 	 crash()

		pygame.display.update()
		# define frames per second
		clock.tick(60) #gives a delay
# end of game loop

#start of main
game_loop()
pygame.quit()
quit()
