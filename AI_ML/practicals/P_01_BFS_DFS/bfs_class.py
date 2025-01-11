from collections import defaultdict

class BFS:
    def __init__(self, src, e, aList):
        self.graph = aList
        self.root = src
        self.item = e
        self.path  = []
        #print("hello")

    def start(self):
        queue, visited = ([] , defaultdict(list))
        
        visited = dict([(key[0],False) for key in dic_01]) 
        
        #for node in self.graph:
            #visited[node] = False
        
        visited[self.root] = True
        queue.append(self.root)
        
        while queue:
            curNode = queue.pop(0)
            self.path.append(curNode)

            if curNode == self.item:
                break

            for adjNode in self.graph[curNode]:
                if not visited[adjNode]:
                    queue.append(adjNode)
                    visited[adjNode] = True


adjList_1 = { 
	'1': ['2', '5'],
	'2': ['1', '5', '3'],
	'3': ['2', '4', '5'],
    '4': ['3', '5'],
    '5': ['1', '2', '3', '4']
}

obj = BFS('1', '5', adjList_1)
obj.start()
print(obj.path)