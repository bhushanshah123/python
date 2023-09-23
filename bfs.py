d={'A':['B','C','D'],
'B':['A','D'],
'C':['A','D'],
'D':['A','B','C']}

visited=[]
queue=[]

def bfs(d,visited,node):
	visited.append(node)
	queue.append(node)
	while queue:
		p=queue.pop(0)
		print(p)
		for neigh in d[p]:
			if neigh not in visited:
				visited.append(neigh)
				queue.append(neigh)
print("BFS TRaversal")
bfs(d,visited,'A')

