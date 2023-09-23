d={'A':['B','C'],
'B':['D','E'],
'C':['F','G'],
'D':[],
'E':[],
'F':['H','I'],
'G':[],
'H':[],
'I':[]}

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

