import sys
import os
import time
import random as rd
import pygame as pg
from math import cos,sin
from PIL import Image

class Point:
	def __init__(self,x,y,z):
		self.x = x
		self.y = y
		self.z = z
		self.color = (255,255,255)

	def draw(self,surface,screenSize):
		pg.draw.circle(surface,self.color,(self.x + (screenSize/2),(self.y* -1) + (screenSize/2)),4)

class Cube:
	def __init__(self,size):
		#front
		self.point1 = Point(-size, size, size)
		self.point2 = Point( size, size, size)
		self.point3 = Point( size,-size, size)
		self.point4 = Point(-size,-size, size)
		#back
		self.point5 = Point(-size, size,-size)
		self.point6 = Point( size, size,-size)
		self.point7 = Point( size,-size,-size)
		self.point8 = Point(-size,-size,-size)

	def draw(self,surface,screenSize):
		self.point1.draw(surface,screenSize)
		self.point2.draw(surface,screenSize)
		self.point3.draw(surface,screenSize)
		self.point4.draw(surface,screenSize)

		self.point5.draw(surface,screenSize)
		self.point6.draw(surface,screenSize)
		self.point7.draw(surface,screenSize)
		self.point8.draw(surface,screenSize)

		pg.draw.line(surface,(255,255,255),(self.point1.x + (screenSize/2),(self.point1.y * -1) + (screenSize/2)),(self.point2.x+ (screenSize/2),(self.point2.y * -1)+ (screenSize/2)))
		pg.draw.line(surface,(255,255,255),(self.point2.x + (screenSize/2),(self.point2.y * -1) + (screenSize/2)),(self.point3.x+ (screenSize/2),(self.point3.y * -1)+ (screenSize/2)))
		pg.draw.line(surface,(255,255,255),(self.point3.x + (screenSize/2),(self.point3.y * -1) + (screenSize/2)),(self.point4.x+ (screenSize/2),(self.point4.y * -1)+ (screenSize/2)))
		pg.draw.line(surface,(255,255,255),(self.point4.x + (screenSize/2),(self.point4.y * -1) + (screenSize/2)),(self.point1.x+ (screenSize/2),(self.point1.y * -1)+ (screenSize/2)))

		pg.draw.line(surface,(255,255,255),(self.point5.x + (screenSize/2),(self.point5.y * -1) + (screenSize/2)),(self.point6.x+ (screenSize/2),(self.point6.y * -1)+ (screenSize/2)))
		pg.draw.line(surface,(255,255,255),(self.point6.x + (screenSize/2),(self.point6.y * -1) + (screenSize/2)),(self.point7.x+ (screenSize/2),(self.point7.y * -1)+ (screenSize/2)))
		pg.draw.line(surface,(255,255,255),(self.point7.x + (screenSize/2),(self.point7.y * -1) + (screenSize/2)),(self.point8.x+ (screenSize/2),(self.point8.y * -1)+ (screenSize/2)))
		pg.draw.line(surface,(255,255,255),(self.point8.x + (screenSize/2),(self.point8.y * -1) + (screenSize/2)),(self.point5.x+ (screenSize/2),(self.point5.y * -1)+ (screenSize/2)))

		pg.draw.line(surface,(255,255,255),(self.point1.x + (screenSize/2),(self.point1.y * -1) + (screenSize/2)),(self.point5.x+ (screenSize/2),(self.point5.y * -1)+ (screenSize/2)))
		pg.draw.line(surface,(255,255,255),(self.point2.x + (screenSize/2),(self.point2.y * -1) + (screenSize/2)),(self.point6.x+ (screenSize/2),(self.point6.y * -1)+ (screenSize/2)))
		pg.draw.line(surface,(255,255,255),(self.point3.x + (screenSize/2),(self.point3.y * -1) + (screenSize/2)),(self.point7.x+ (screenSize/2),(self.point7.y * -1)+ (screenSize/2)))
		pg.draw.line(surface,(255,255,255),(self.point4.x + (screenSize/2),(self.point4.y * -1) + (screenSize/2)),(self.point8.x+ (screenSize/2),(self.point8.y * -1)+ (screenSize/2)))

	def rotateZclockwise(self):
		s = sin(1/30)
		c = cos(1/30)
		x1 = self.point1.x
		y1 = self.point1.y

		self.point1.x = x1 * c - y1 * s
		self.point1.y = x1 * s + y1 * c

		x1 = self.point2.x
		y1 = self.point2.y

		self.point2.x = x1 * c - y1 * s
		self.point2.y = x1 * s + y1 * c

		x1 = self.point3.x
		y1 = self.point3.y

		self.point3.x = x1 * c - y1 * s
		self.point3.y = x1 * s + y1 * c

		x1 = self.point4.x
		y1 = self.point4.y

		self.point4.x = x1 * c - y1 * s
		self.point4.y = x1 * s + y1 * c

		x1 = self.point5.x
		y1 = self.point5.y

		self.point5.x = x1 * c - y1 * s
		self.point5.y = x1 * s + y1 * c

		x1 = self.point6.x
		y1 = self.point6.y

		self.point6.x = x1 * c - y1 * s
		self.point6.y = x1 * s + y1 * c

		x1 = self.point7.x
		y1 = self.point7.y

		self.point7.x = x1 * c - y1 * s
		self.point7.y = x1 * s + y1 * c

		x1 = self.point8.x
		y1 = self.point8.y

		self.point8.x = x1 * c - y1 * s
		self.point8.y = x1 * s + y1 * c

	def rotateZcounterclockwise(self):
		s = sin(-1/30)
		c = cos(-1/30)
		x1 = self.point1.x
		y1 = self.point1.y

		self.point1.x = x1 * c - y1 * s
		self.point1.y = x1 * s + y1 * c

		x1 = self.point2.x
		y1 = self.point2.y

		self.point2.x = x1 * c - y1 * s
		self.point2.y = x1 * s + y1 * c

		x1 = self.point3.x
		y1 = self.point3.y

		self.point3.x = x1 * c - y1 * s
		self.point3.y = x1 * s + y1 * c

		x1 = self.point4.x
		y1 = self.point4.y

		self.point4.x = x1 * c - y1 * s
		self.point4.y = x1 * s + y1 * c

		x1 = self.point5.x
		y1 = self.point5.y

		self.point5.x = x1 * c - y1 * s
		self.point5.y = x1 * s + y1 * c

		x1 = self.point6.x
		y1 = self.point6.y

		self.point6.x = x1 * c - y1 * s
		self.point6.y = x1 * s + y1 * c

		x1 = self.point7.x
		y1 = self.point7.y

		self.point7.x = x1 * c - y1 * s
		self.point7.y = x1 * s + y1 * c

		x1 = self.point8.x
		y1 = self.point8.y

		self.point8.x = x1 * c - y1 * s
		self.point8.y = x1 * s + y1 * c

	def rotateXclockwise(self):
		s = sin(1/30)
		c = cos(1/30)
		z1 = self.point1.z
		y1 = self.point1.y

		self.point1.z = z1 * c - y1 * s
		self.point1.y = z1 * s + y1 * c

		z1 = self.point2.z
		y1 = self.point2.y

		self.point2.z = z1 * c - y1 * s
		self.point2.y = z1 * s + y1 * c

		z1 = self.point3.z
		y1 = self.point3.y

		self.point3.z = z1 * c - y1 * s
		self.point3.y = z1 * s + y1 * c

		z1 = self.point4.z
		y1 = self.point4.y

		self.point4.z = z1 * c - y1 * s
		self.point4.y = z1 * s + y1 * c

		z1 = self.point5.z
		y1 = self.point5.y

		self.point5.z = z1 * c - y1 * s
		self.point5.y = z1 * s + y1 * c

		z1 = self.point6.z
		y1 = self.point6.y

		self.point6.z = z1 * c - y1 * s
		self.point6.y = z1 * s + y1 * c

		z1 = self.point7.z
		y1 = self.point7.y

		self.point7.z = z1 * c - y1 * s
		self.point7.y = z1 * s + y1 * c

		z1 = self.point8.z
		y1 = self.point8.y

		self.point8.z = z1 * c - y1 * s
		self.point8.y = z1 * s + y1 * c

	def rotateXcounterclockwise(self):
		s = sin(-1/30)
		c = cos(-1/30)
		z1 = self.point1.z
		y1 = self.point1.y

		self.point1.z = z1 * c - y1 * s
		self.point1.y = z1 * s + y1 * c

		z1 = self.point2.z
		y1 = self.point2.y

		self.point2.z = z1 * c - y1 * s
		self.point2.y = z1 * s + y1 * c

		z1 = self.point3.z
		y1 = self.point3.y

		self.point3.z = z1 * c - y1 * s
		self.point3.y = z1 * s + y1 * c

		z1 = self.point4.z
		y1 = self.point4.y

		self.point4.z = z1 * c - y1 * s
		self.point4.y = z1 * s + y1 * c

		z1 = self.point5.z
		y1 = self.point5.y

		self.point5.z = z1 * c - y1 * s
		self.point5.y = z1 * s + y1 * c

		z1 = self.point6.z
		y1 = self.point6.y

		self.point6.z = z1 * c - y1 * s
		self.point6.y = z1 * s + y1 * c

		z1 = self.point7.z
		y1 = self.point7.y

		self.point7.z = z1 * c - y1 * s
		self.point7.y = z1 * s + y1 * c

		z1 = self.point8.z
		y1 = self.point8.y

		self.point8.z = z1 * c - y1 * s
		self.point8.y = z1 * s + y1 * c

	def rotateYclockwise(self):
		s = sin(1/30)
		c = cos(1/30)
		z1 = self.point1.z
		x1 = self.point1.x

		self.point1.z = z1 * c - x1 * s
		self.point1.x = z1 * s + x1 * c

		z1 = self.point2.z
		x1 = self.point2.x

		self.point2.z = z1 * c - x1 * s
		self.point2.x = z1 * s + x1 * c

		z1 = self.point3.z
		x1 = self.point3.x

		self.point3.z = z1 * c - x1 * s
		self.point3.x = z1 * s + x1 * c

		z1 = self.point4.z
		x1 = self.point4.x

		self.point4.z = z1 * c - x1 * s
		self.point4.x = z1 * s + x1 * c

		z1 = self.point5.z
		x1 = self.point5.x

		self.point5.z = z1 * c - x1 * s
		self.point5.x = z1 * s + x1 * c

		z1 = self.point6.z
		x1 = self.point6.x

		self.point6.z = z1 * c - x1 * s
		self.point6.x = z1 * s + x1 * c

		z1 = self.point7.z
		x1 = self.point7.x

		self.point7.z = z1 * c - x1 * s
		self.point7.x = z1 * s + x1 * c

		z1 = self.point8.z
		x1 = self.point8.x

		self.point8.z = z1 * c - x1 * s
		self.point8.x = z1 * s + x1 * c

	def rotateYcounterclockwise(self):
		s = sin(-1/30)
		c = cos(-1/30)
		z1 = self.point1.z
		x1 = self.point1.x

		self.point1.z = z1 * c - x1 * s
		self.point1.x = z1 * s + x1 * c

		z1 = self.point2.z
		x1 = self.point2.x

		self.point2.z = z1 * c - x1 * s
		self.point2.x = z1 * s + x1 * c

		z1 = self.point3.z
		x1 = self.point3.x

		self.point3.z = z1 * c - x1 * s
		self.point3.x = z1 * s + x1 * c

		z1 = self.point4.z
		x1 = self.point4.x

		self.point4.z = z1 * c - x1 * s
		self.point4.x = z1 * s + x1 * c

		z1 = self.point5.z
		x1 = self.point5.x

		self.point5.z = z1 * c - x1 * s
		self.point5.x = z1 * s + x1 * c

		z1 = self.point6.z
		x1 = self.point6.x

		self.point6.z = z1 * c - x1 * s
		self.point6.x = z1 * s + x1 * c

		z1 = self.point7.z
		x1 = self.point7.x

		self.point7.z = z1 * c - x1 * s
		self.point7.x = z1 * s + x1 * c

		z1 = self.point8.z
		x1 = self.point8.x

		self.point8.z = z1 * c - x1 * s
		self.point8.x = z1 * s + x1 * c
screenSize = 400

pg.init()
screen = pg.display.set_mode((screenSize,screenSize))
clock = pg.time.Clock()
pg.display.set_caption('Insertion Sort Visualization')

cube = Cube(50)

count = 0
cnt = 0
do = rd.randrange(6)
start = time.time()

while True:
	clock.tick(30)
	for event in pg.event.get():
		if event.type == pg.QUIT: sys.exit()
	screen.fill((0,0,0))

	cube.draw(screen,screenSize)
	if count < 100:
		if do == 0:
			cube.rotateXclockwise()
			count += 1
		elif do == 1:
			cube.rotateXcounterclockwise()
			count += 1
		elif do == 2:
			cube.rotateYclockwise()
			count += 1
		elif do == 3:
			cube.rotateYcounterclockwise()
			count += 1
		elif do == 4:
			cube.rotateZclockwise()
			count += 1
		elif do == 5:
			cube.rotateZcounterclockwise()
			count += 1
	else:
		do = rd.randrange(6)
		count = 0
	count += 1
	pg.display.update()
	'''
				pg.image.save(screen,f"images/frame{cnt}.jpg")
			
				cnt += 1
				if time.time() >= start + 60:
					break
			
			frames = []
			for count, filename in enumerate(os.listdir('images')):
			    frames.append(Image.open(f"images/frame{count}.jpg"))
			
			frameOne = frames[0]
			frameOne.save(f"SelectionSort.gif",format="GIF",append_images=frames,
			    save_all=True, duration=30)'''
