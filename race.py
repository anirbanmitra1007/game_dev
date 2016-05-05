import math,pygame,random,sys,time
from pygame.locals import *

#start of main function
pygame.init()

#size initialization
display_width = 800
display_height = 600 

crash_sound = pygame.mixer.Sound("crash.wav")
pygame.mixer.music.load("Five_Card_Shuffle.wav")
car_width=50
white=(255,255,255)
black=(0,0,0)
red=(180,0,0)
bright_red=(255,0,0)
green=(0,180,0)
bright_green=(0,255,0)
blue=(0,0,255)
block_color=(128,23,78)

gameDisplay = pygame.display.set_mode((display_width,display_height),0,32)

pygame.display.set_caption('A racey game')

clock = pygame.time.Clock()
carImg = pygame.image.load('ball.png')
pause = False
#end of main
def quitgame():
	pygame.quit()
	quit()

# unpause
def unpause():
	global pause
	pygame.mixer.music.unpause()
	pause = False
#pause
def paused():

	#stop the music
	pygame.mixer.music.pause()
	largetext = pygame.font.Font('freesansbold.ttf',110 )
	textsurf, textrect = text_objects("Paused",largetext)
	textrect.center = ((display_width/2),(display_height/2.5))
	gameDisplay.blit(textsurf,textrect)
	while pause:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				quitgame()
			if event.type == KEYDOWN:
				if event.key == K_q:
					quitgame()
		
		button("Continue!",150,400,100,50,bright_green,green,"unpause")

		button("QUIT!",550,400,100,50,bright_red,red,"quit")
		
		gameDisplay.blit(textsurf,textrect)
		pygame.display.update()
		clock.tick(10)
#end of pause
def button(msg,x,y,width,height,icol,acol,action=None):
	
	mouse = pygame.mouse.get_pos()

	click = pygame.mouse.get_pressed()

	# adding buttons
	if mouse[0]>x and mouse[0]<x+width and mouse[1]>y and mouse[1]<y+height:
		pygame.draw.rect(gameDisplay,acol,(x,y,width,height))
		if click[0] == 1 and action!=None:
			if action == "unpause":
				unpause()
			elif action == "play":
				game_loop()
			elif action == "quit":
				quitgame()
	else:
		pygame.draw.rect(gameDisplay,icol,(x,y,width,height))
	#end
	#displaying text in buttons
	smalltext= pygame.font.Font("freesansbold.ttf",20)
	textsurf,textrect = text_objects(msg,smalltext)

	textrect.center = ((x+width/2),(y+height/2))
	gameDisplay.blit(textsurf,textrect)			

def game_intro():

	intro = True

	while intro:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				quitgame()
			if event.type == KEYDOWN:
				if event.key == K_q:
					quitgame()
		gameDisplay.fill(white)
		largetext = pygame.font.Font('freesansbold.ttf',110 )
		textsurf, textrect = text_objects("A racey game",largetext)
		textrect.center = ((display_width/2),(display_height/2.5))
		gameDisplay.blit(textsurf,textrect)
		
		button("GO!",150,400,100,50,bright_green,green,"play")

		button("QUIT!",550,400,100,50,bright_red,red,"quit")
		
		gameDisplay.blit(textsurf,textrect)
		pygame.display.update()
		clock.tick(10)


#keeping track of scores
def things_dodged(count):

	font= pygame.font.SysFont("comicsansms",25,10,10)
	text = font.render("Dodged: "+str(count),True,black)
	gameDisplay.blit(text,(0,0))

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

	# music playing
	pygame.mixer.music.stop()
	pygame.mixer.Sound.play(crash_sound)

	largetext = pygame.font.Font('freesansbold.ttf',110 )
	textsurf, textrect = text_objects("Paused",largetext)
	textrect.center = ((display_width/2),(display_height/2.5))
	gameDisplay.blit(textsurf,textrect)
	while True:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				quitgame()
			if event.type == KEYDOWN:
				if event.key == K_q:
					quitgame()
		
		button("Play Again!",150,400,115,50,bright_green,green,"play")

		button("QUIT!",550,400,100,50,bright_red,red,"quit")
		
		gameDisplay.blit(textsurf,textrect)
		pygame.display.update()
		clock.tick(10)


#end of crash function
# game loop
def game_loop():

	# music start
	pygame.mixer.music.play(-1)


	global pause
	x = (display_width*.45)
	y = (display_height*.9)

	thing_starty = -600
	thing_speed = 7
	thing_width = 100
	thing_height = 100
	thing_startx = random.randrange(0,display_width-thing_width)
	gameexit = False
	x_change = 0
	car_speed = 8
	#keeping track of scores
	dodged = 0

	while not gameexit:

		for event in pygame.event.get():
			
			if event.type == pygame.QUIT:
				quitgame()
			if event.type == KEYDOWN:
				if event.key == K_q:
					quitgame()
				elif event.key == K_LEFT:
					x_change = -car_speed
				elif event.key == K_RIGHT:
					x_change = car_speed
				elif event.key == K_p:
					pause =True
					paused()
			elif event.type == KEYUP:
				if event.key == K_LEFT or event.key == K_RIGHT:
					x_change=0

		x =x + x_change			
		gameDisplay.fill(white)	
		things(thing_startx,thing_starty,thing_width,thing_height,block_color)
		things(thing_startx,thing_starty,thing_width,thing_height,block_color)
		thing_starty += thing_speed
		
		#start of drawing stuff
		car(x,y)
		things_dodged(dodged)
		#end of drawing
		if x<0 or x>display_width-car_width:
			crash()
			gameexit = True

		if thing_starty >display_height:
			thing_starty = 0 - thing_height
			thing_startx = random.randrange(0,display_width-thing_width)
			dodged+= 1
			thing_speed+=0.5

		if y < thing_starty + thing_height:

			 if x > thing_startx and x< thing_startx + thing_width or x + car_width > thing_startx and x+ car_width < thing_startx + thing_width:
			 	 
			 	 crash()

		pygame.display.update()
		# define frames per second
		clock.tick(60) #gives a delay
# end of game loop

#start of main
game_intro()
game_loop()
quitgame()