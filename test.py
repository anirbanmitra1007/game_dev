class vector(object):

	def __init__(self,list1,list2):
		self.diff = (list2[0]-list1[0],list2[1]-list1[1])

	def distance(self):
			self.a=self.diff[0]
			self.b=self.diff[1]
			return math.sqrt(self.a**2+self.b**2)	

	def unit(self):
		distance=self.distance()
		self.aunit=self.a/distance
		self.bunit=self.b/distance
		return self.aunit,self.bunit


bif="black.jpg"
mif="ball.png"

import pygame, sys , time
from pygame.locals import *

pygame.init()
screen=pygame.display.set_mode((640,360),0,32)
background=pygame.image.load(bif).convert()
ball=pygame.image.load(mif).convert_alpha()

#setting speed for animation
clock = pygame.time.Clock()
x,y,speedx,speedy = 0,0,250,170
#
while True:

	for event in pygame.event.get():
		if event.type == QUIT:
			pygame.quit()
			sys.exit()
		if event.type ==KEYDOWN:
			if event.key == K_q:
				pygame.quit()
				sys.exit()
	screen.blit(background,(0,0))
	screen.blit(ball,(x,y))
	#time for 1 millisecond
	milli=clock.tick() 
	seconds=milli/1000.0
	#distance moved in
	dmx=seconds*speedx
	dmy=seconds*speedy
	# updating
	x+=dmx
	y+=dmy

	if x>=640:
		x=-
	if y>=360:
		y=0
	pygame.display.update()	 