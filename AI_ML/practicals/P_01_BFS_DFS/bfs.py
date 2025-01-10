from collections import defaultdict
from graphUtils import Graph

def BFS(graph, src, e):
	visited = defaultdict(list)
	queue = []
	path  = [];        
	for node in graph.adjList:
		visited[node] = False

	queue.append(src)
	visited[src] = True
	while queue:
		s = queue.pop(0)
		path.append(s)
		if s==e:
			return(path)
		unVisitedNodes = list(filter(lambda i:not visited[i], graph.adjList[s] ))
		for i in unVisitedNodes:
			queue.append(i)
			visited[i] = True
	return([])
   
adjList_1 = { 
	'1': ['2', '5', '4'],
	'2': ['1', '5', '3'],
	'3': ['2', '5'],
    '4': ['1'],
    '5': ['1', '2', '3']
}

g1 = Graph(adjList_1)
path = BFS(g1,'1', '5')
print(path)