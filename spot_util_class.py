import pygame

RED=(196,20,66,255)
GREEN=(0,255,0)
BLUE=(0,255,0)
YELLOW=(255,255,0)
WHITE=(255,255,255)
BLACK=(0,0,0)
PURPLE=(128,0,128)
ORANGE=(255,165,0)
GREY=(80,80,80)
TURQUOISE=(64,224,208)
DARK=(40,40,41)

class Spot:
	def __init__(self, row,col,width,total_row):
		self.row=row
		self.col=col
		self.x=row*width
		self.y=col*width
		self.width=width
		self.color=DARK
		self.total_row=total_row


	def get_position(self):
		return self.row,self.col

	def is_open(self):
		return self.color==WHITE
	
	def is_closed(self):
		return self.color==RED

	def is_barrier(self):
		return self.color==GREY

	def is_start(self):
		return self.color==ORANGE

	def is_end(self):
		return self.color==TURQUOISE

	def make_open(self):
		self.color=WHITE

	def make_closed(self):
		self.color=RED

	def make_barrier(self):
		self.color=GREY

	def make_start(self):
		self.color=ORANGE

	def make_end(self):
		self.color=TURQUOISE
	
	def make_path(self):
		self.color=ORANGE

	def draw_spot(self,win):
		pygame.draw.rect(win,self.color,(self.x,self.y,self.width,self.width))

	def reset(self):
		self.color=DARK

	def update_negihbors(self,grid):
		self.neighbors=[]
		if self.row < self.total_row - 1 and not grid[self.row + 1][self.col].is_barrier(): #right
			self.neighbors.append(grid[self.row + 1][self.col])

		if self.row > 0 and not grid[self.row - 1][self.col].is_barrier(): #left
			self.neighbors.append(grid[self.row - 1][self.col])

		if self.col < self.total_row - 1 and not grid[self.row][self.col + 1].is_barrier(): #down
			self.neighbors.append(grid[self.row][self.col + 1])

		if self.col > 0 and not grid[self.row][self.col - 1].is_barrier(): #up
			self.neighbors.append(grid[self.row][self.col - 1])
