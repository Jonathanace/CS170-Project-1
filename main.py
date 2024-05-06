from puzzle import *
from utils import * 
import timeit

# Helper function to solve a 
def solve(grid, criteria):
    init_state = State(np.array(grid))
    puzzle = Puzzle(init_state, criteria=criteria)
    start = time.time()
    solution = puzzle.solve()
    end = time.time()
    duration = end - start
    return solution

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



if __name__ == "__main__":
    solution = solve([[1,0,3],[4,2,6],[7,5,8]], misplaced_tile)
    for step in solution['path']:
        print(step)

    print(f'Nodes Expanded (Time): {solution['time']}')
    print(f'Max Frontier Size (space): {solution['space']}')
    # print(solve(doable, misplaced_tile))