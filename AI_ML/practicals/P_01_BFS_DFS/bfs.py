from collections import defaultdict

def BFS(graph, src, e):
	visited = defaultdict(list)
	queue = []
	path  = [];        
	for node in graph:
		visited[node] = False

	queue.append(src)
	visited[src] = True
	while queue:
		s = queue.pop(0)
		path.append(s)
		if s==e:
			return(path)
		unVisitedNodes = list(filter(lambda i:not visited[i], graph[s] ))
		for i in unVisitedNodes:
			queue.append(i)
			visited[i] = True
	return([])
   
adjList_1 = { 
	'1': ['2', '5'],
	'2': ['1', '5', '3'],
	'3': ['2', '4', '5'],
    '4': ['3', '5'],
    '5': ['1', '2', '3', '4']
}

path = BFS(adjList_1,'1', '5')
print(path)