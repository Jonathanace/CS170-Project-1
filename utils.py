import numpy as np

# Criteria definitions
def uniform_cost(state, goal): 
    return 1

def misplaced_tile(state: np.ndarray, goal: np.ndarray):
    crit = np.sum(state != goal)
    return crit

def euclidean_distance(state: np.ndarray, goal: np.ndarray):
    return np.linalg.norm(state - goal)

# Starting States
trivial = [
    [1, 2, 3], 
    [4, 5, 6],
    [7, 8, 0],
]

very_easy = [
    [1,2,3],
    [4,5,6],
    [7,0,8]
]

easy = [
    [1,2,0],
    [4,5,3],
    [7,8,6],
]

doable = [
    [0,1,2],
    [4,5,3],
    [7,8,6]
]

oh_boy = [
    [8,7,1],
    [6,0,2],
    [5,4,3]
]