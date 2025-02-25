# -*- coding: utf-8 -*-
"""csp_water_jug.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1fbgKrX9OBMTr9Btl7aPP764bslUOxjNc
"""

from collections import deque

class WaterJugProblem:
    def __init__(self, capacity_1:int, capacity_2:int, goal:tuple, start=(0,0)):
        self.X              =   capacity_1
        self.Y              =   capacity_2
        self.goal           =   goal
        self.tree           =   {start:{'parent':None, 'children':[]}}
        self.queue          =   deque([start])

    def isVisited(self, state:tuple):
        return state in self.tree

    def addChild(self, parent:tuple, child:tuple):
        if not self.isVisited(child):
          self.tree[child] = {'parent':parent, 'children':[]}
          self.tree[parent]['children'].append(child)
          self.queue.append(child)
          if child == self.goal:
            return True
        return False

    # operation-1
    def fill_X(self, state:tuple):
        x, y        =   state
        new_state   =   (self.X, y)
        return(self.addChild(state, new_state))

    # operation-2
    def fill_Y(self, state:tuple):
        x, y        =   state
        new_state   =   (x, self.Y)
        return(self.addChild(state, new_state))

    # operation-3
    def empty_X(self, state:tuple):
        x, y        =   state
        new_state   =   (0, y)
        return(self.addChild(state, new_state))

    # operation-4
    def empty_Y(self, state:tuple):
        x, y        =   state
        new_state   =   (x, 0)
        return(self.addChild(state, new_state))

    def transfer_X_to_Y(self, state:tuple):
        x, y        =   state
        amount      =   min(x, self.Y-y)
        new_state   =   (x-amount, y+amount)
        return(self.addChild(state, new_state))

    def transfer_Y_to_X(self, state:tuple):
        x, y        =   state
        amount      =   min(y, self.X-x)
        new_state   =   (x+amount, y-amount)
        return(self.addChild(state, new_state))

    def generateNeighbours(self, state:tuple):
        if self.fill_X(state):
            return True
        elif self.fill_Y(state):
            return True
        elif self.empty_X(state):
            return True
        elif self.empty_Y(state):
            return True
        elif self.transfer_X_to_Y(state):
            return True
        elif self.transfer_Y_to_X(state):
            return True
        else:
          return False

    def generatePath(self):
        path = []
        current_state = self.goal
        while current_state is not None:
            path.append(current_state)
            current_state = self.tree[current_state]['parent']
        return path[::-1]

    def start(self):
        while self.queue:
            current_state = self.queue.popleft()
            status = self.generateNeighbours(current_state)
            if status:
                print(self.generatePath())
                return status
        print("No solution found")
        #print(self.tree)
        return False

#obj = WaterJugProblem(4,3,(2,0))
Y = 5
X = 3
goal=(2,0)
obj = WaterJugProblem(Y,X,goal)
print(obj.start())