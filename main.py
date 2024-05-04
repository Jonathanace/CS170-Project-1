from puzzle import *
from utils import * 

# Helper function to solve a 
def solve(grid, criteria):
    init_state = State(np.array(grid))
    puzzle = Puzzle(init_state, criteria=criteria)
    start = time.time()
    path = puzzle.solve()
    end = time.time()
    duration = end - start
    return {'path': path,
            'duration': duration}

# Function to solve for all starting states and with all criteria
def solve_all():
    for state_name, start_state in start_states.items():
        for criteria_name, criteria in criterium.items():
            print(f'state: {state_name}, criteria: {criteria_name}')
            solution = solve(start_state, criteria)
            print('Solution:')
            for step in solution['path']:
                print(step)
            print(f'runtime: {solution['duration']}')
            print()
        print()



# Define premade initial states
start_states = {
    'trivial': trivial,
    'very_easy': very_easy,
    'easy': easy,
    'doable': doable,
    'oh_boy': oh_boy
}

criterium = {
    'uniform_cost': uniform_cost,
    'misplaced_tile': misplaced_tile,
    'euclidean_distance': euclidean_distance
}

solve(doable, euclidean_distance)
solve_all()