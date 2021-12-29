from queue import Queue
import pygame
from queue import PriorityQueue

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

def h(p1,p2):
    x1,y1=p1
    x2,y2=p2
    return abs(x1-x2)+abs(y1-y2)

def a_star(draw, grid, start, end):
    count = 0
    open_set = PriorityQueue()
    open_set.put((0, count, start))
    came_from = {}
    g_score = {spot: float("inf") for row in grid for spot in row}
    g_score[start] = 0
    f_score = {spot: float("inf") for row in grid for spot in row}
    f_score[start] = h(start.get_position(), end.get_position())

    open_set_hash = {start}

    while not open_set.empty():
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

        current = open_set.get()[2]
        open_set_hash.remove(current)

        if current == end:
            reconstruct_path(draw,came_from,end)
            end.make_end()
            return True

        for neighbor in current.neighbors:
            temp_g_score = g_score[current] + 1
            if temp_g_score < g_score[neighbor]:
                came_from[neighbor] = current
                g_score[neighbor] = temp_g_score
                f_score[neighbor] = temp_g_score + h(neighbor.get_position(), end.get_position())
                if neighbor not in open_set_hash:
                    count += 1
                    open_set.put((f_score[neighbor], count, neighbor))
                    open_set_hash.add(neighbor)
                    neighbor.make_open()

        draw()

        if current != start:
            current.make_closed()

    return False



def reconstruct_path(draw,parent,end):
	while end:
		end.make_path()
		end=parent[end]
		draw()