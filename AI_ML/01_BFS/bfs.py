from collections import defaultdict

class Graph:
	def __init__(self, aList = defaultdict(list)):
		self.g = aList
        
	def addEdge(self, node1, node2):
		#print("hello")
		self.g[node1].append(node2)
		self.g[node2].append(node1)
        
	def showGraph(self):
		edges = []
		for node in self.g:
			for adjNode in self.g[node]: 
				edges.append((node, adjNode))

		print(edges)
		#print("hello")
        
	def BFS(self, src, e):
		visited = defaultdict(list)
		queue = []
		path  = [];        
		for node in self.g:
			visited[node] = False

		queue.append(src)
		visited[src] = True
		while queue:
			s = queue.pop(0)
			path.append(s)
			for i in self.g[s]:
				if not visited[i]:
					queue.append(i)
					visited[i] = True
		print(path)
   
adjList_1 = { 
	'1': ['2', '5', '4'],
	'2': ['1', '5', '3'],
	'3': ['2', '5'],
    '4': ['1'],
    '5': ['1', '2', '3']
}
g2 = Graph(adjList_1)
g2.BFS('1', '3')