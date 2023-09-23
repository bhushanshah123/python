d={'A':['B','C'],
'B':['D','E'],
'C':['F','G'],
'D':[],
'E':[],
'F':['H','I'],
'G':[],
'H':[],
'I':[]}

visited =set()
def dfs (d,visited,node):
	if node not in visited:
		print (node)
		visited.add(node)
		for neigh in d[node]:
			dfs (d,visited,neigh)
print("DFS travarsal")	
dfs(d,visited,'A')
	 
