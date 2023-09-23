d={'A':['B','C'],
'B':['A'],
'C':['A','D','E'],
'D':['C','E'],
'E':['C','D']}

visited =set()
def dfs (d,visited,node):
	if node not in visited:
		print (node)
		visited.add(node)
		for neigh in d[node]:
			dfs (d,visited,neigh)
print("DFS travarsal")	
dfs(d,visited,'A')
	 
