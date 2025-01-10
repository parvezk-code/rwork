from collections import defaultdict

class Graph:
	def __init__(self, aList = defaultdict(list)):
		self.adjList = aList
        
	def addEdge(self, node1, node2):
		#print("hello")
		self.adjList[node1].append(node2)
		self.adjList[node2].append(node1)
        
	def showGraph(self):
		edges = []
		for node in self.adjList:
			for adjNode in self.adjList[node]: 
				edges.append((node, adjNode))

		print(edges)
		#print("hello")
   