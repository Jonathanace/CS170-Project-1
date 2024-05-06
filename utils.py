import numpy as np

# Criteria definitions
def uniform_cost(state, goal): 
    return 1

def misplaced_tile(state: np.ndarray, goal: np.ndarray):
    crit = np.sum(state != goal)
    if crit > 0: 
        crit -= 1
    return crit

def euclidean_distance(state: np.ndarray, goal: np.ndarray):
    crit = np.linalg.norm(state - goal)
    return  crit

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

fifteen_puzzle = [[1,2,0,4],
                  [5,7,3,12],
                  [10,6,8,11],
                  [9,13,14,15]]

# Define premade initial states
start_states = {
    'trivial': trivial,
    'very_easy': very_easy,
    'easy': easy,
    'doable': doable,
    'oh_boy': oh_boy,
    # 'fifteen_puzzle': fifteen_puzzle
}

criterium = {
    'uniform_cost': uniform_cost,
    'misplaced_tile': misplaced_tile,
    'euclidean_distance': euclidean_distance,
}



if __name__ == '__main__':
    print(np.array([[1,2,3],[4,5,6],[7,8,9]]).shape)