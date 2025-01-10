from collections import defaultdict
from utils import Graph
from utils import Stack

def DFS(graph, src, e):
	visited = defaultdict(list)
	stack = Stack()
	path  = [];       

	for node in graph.adjList:
		visited[node] = False

	stack.push(src)
	visited[src] = True
	while not stack.isEmpty():
		s = stack.pop()
		path.append(s)
		if s==e:
			return(path)
		unVisitedNodes = list(filter(lambda i:not visited[i], graph.adjList[s] ))
		for i in unVisitedNodes:
			stack.push(i)
			visited[i] = True
	return(path)
   
adjList_1 = { 
	'1': ['2', '5', '6', '8'],
	'2': ['1', '5', '3'],
	'3': ['2', '4', '5'],
    '4': ['3', '5'],
    '5': ['1', '2', '3', '4'],
    '6': ['1', '7'],
    '7': ['6'],
    '8': ['1']
}

g1 = Graph(adjList_1)
path = DFS(g1, '1', '5')
print(path)