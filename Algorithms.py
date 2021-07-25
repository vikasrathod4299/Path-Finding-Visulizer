from queue import Queue
import pygame

def bfs(draw,grid,start, end):

	queue=Queue()
	
	parent={spot:None for row in grid for spot in row}


	visited=set()
	visited.add(start)

	queue.put(start)
	
	while not queue.empty():
		for event in pygame.event.get():
		    if event.type == pygame.QUIT:
		        pygame.quit()

		v=queue.get()


		for i in v.neighbors:

			if i not in visited:

				visited.add(i)
				parent[i]=v
				queue.put(i)
				i.make_open()

				if i==end:
					reconstruct_path(draw,parent,end)
					i.make_end()
					return True
				
		draw()

		if v == start:
			continue
		v.make_closed()

	return False 


def dfs(draw,grid,start,end):
	parent={spot:None for row in grid for spot in row}
	
	visited=set()
	visited.add(start)
	
	stack=[]
	stack.append(start)
	
	while len(stack):

		v=stack.pop()

		for i in v.neighbors:
			if i in visited:
				continue
			stack.append(i)
			visited.add(i)
			parent[i]=v
			i.make_open()


			if i==end:
				reconstruct_path(draw,parent,end)
				i.make_end()
				return True

		draw()

		if v!=start:
			v.make_closed()


def reconstruct_path(draw,parent,end):
	while end:
		end.make_path()
		end=parent[end]
		draw()

