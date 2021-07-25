import pygame
from spot_util_class import Spot
import Algorithms as algo


GREY=(80,80,80)
DARK=(40,40,41)

WIDTH=800
WIN=pygame.display.set_mode((WIDTH,WIDTH))



def make_spot(rows,width):
	gap=width//rows

	grid=[]

	for i in range(rows):
		grid.append([])
		for j in range(rows):
			grid[i].append(Spot(i,j,gap,rows))
	return grid


def draw_spots(win,grid,rows,width):
	
	win.fill(DARK)

	for row in grid:
		for spot in row:
			spot.draw_spot(win)

	make_grid(win,rows,width)
	pygame.display.update()


def get_mouse_pos(pos,rows,width):
	gap=width//rows

	x,y=pos

	row=x//gap
	col=y//gap

	return row, col


def make_grid(win,rows,width):
	gap=width//rows
	for i in range(rows):
		pygame.draw.line(win,GREY,(0,i*gap),(width,i*gap))
		pygame.draw.line(win,GREY,(i*gap,0),(i*gap,width))


def main(win,width):

	rows=50
	grid=make_spot(rows,width)

	run=True
	start=None
	end=None

	while run:
		
		draw_spots(win,grid,rows,width)
		for event in pygame.event.get():
			
			if event.type == pygame.QUIT: 
				run=False

			if pygame.mouse.get_pressed()[0]:
				pos=pygame.mouse.get_pos()
				row,col=get_mouse_pos(pos,rows,width)
				spot=grid[row][col]
				if not start and spot != end:
					start=spot
					spot.make_start() 

				elif not end and spot != start:
					end=spot
					spot.make_end()

				elif spot!=start and spot!=end:
					spot.make_barrier() 


			elif pygame.mouse.get_pressed()[2]:
				pos=pygame.mouse.get_pos()
				row,col=get_mouse_pos(pos,rows,width)
				spot=grid[row][col]
				spot.reset() 
				if spot ==  start:
					start = None
				elif spot == end:
					end = None


			if event.type== pygame.KEYDOWN:
				if event.key==pygame.K_b and start and end:

					#if event.key==pygame.K_SPACE:
					for line in grid:
						for spot in line:
							spot.update_negihbors(grid)

					algo.bfs(lambda: draw_spots(win, grid, rows ,width), grid, start, end)

				if event.key==pygame.K_d:

					#if event.key==pygame.K_SPACE:
					for line in grid:
						for spot in line:
							spot.update_negihbors(grid)

					algo.dfs(lambda: draw_spots(win, grid, rows ,width), grid, start, end)			


				if event.key == pygame.K_c:
					start=None
					end=None
					grid=make_spot(rows,width)

	
	pygame.quit()
	
main(WIN,WIDTH)


