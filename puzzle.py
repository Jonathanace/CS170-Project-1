import numpy as np
from heapq import heappush, heappop
import time

# State Class
class State:
    def __init__(self: np.array, state, parent=None):
        self.parent = parent
        self.size = state.size
        self.shape = state.shape
        self.state = state

    def __str__(self):
        return str(self.state)
    
    def __repr__(self):
        return str(self.state)
    
    def get_path(self):
        if self.parent:
            return self.parent.get_path() + [self.state]
        else:
            return [self.state]
        
    def get_valid_children(self):
        loc = np.concatenate(np.where(self.state == 0))
        res = []
        for dir in [[1,0],[-1,0],[0,1],[0,-1]]:
            child_loc = loc+dir
            if np.all([0 <= child_loc, child_loc < 3]): # Check if child is valid
                new_state = self.state.copy()
                new_state[tuple(loc)] = self.state[tuple(child_loc)]
                new_state[tuple(child_loc)] = self.state[tuple(loc)]
                res.append(State(new_state, parent=self))
        return res
    
    def __hash__(self):
        res = hash(tuple(self.state.ravel()))
        return res
    
    def __eq__(self, other):
        return np.all(self.state == other.state)
    
    def __lt__(self, other):
        return True 
    
# Puzzle Class 
class Puzzle:
    def __init__(self, init_state, criteria):
        self.goal_state = np.append(np.arange(1, init_state.size), 0).reshape(init_state.shape)
        self.frontier = []
        heappush(self.frontier, (criteria(state=init_state.state, goal=self.goal_state), init_state))
        self.criteria = criteria
        self.visited = set()
        print(f'initial state:\n{init_state}')
        print(f'goal state:\n{self.goal_state}')
        print()
    def check_end_state(self, state):
        eq = np.all(self.goal_state == state)
        return eq
    def solve(self):
        while self.frontier:
            cur = heappop(self.frontier)[1]
            # print('Expanding node\n', cur)
            if self.check_end_state(cur.state):
                print('End state found')
                return cur.get_path()

            for child in cur.get_valid_children():                    
                if child not in self.visited:
                    criteria = self.criteria(state=child.state, goal=self.goal_state)
                    heappush(self.frontier, (criteria, child))
                    self.visited.add(child)
                        