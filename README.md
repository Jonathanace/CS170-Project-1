# Challenges
The main challenge I encountered working on this project was working with the state class that represents a single puzzle state. Some of these issues were implementing relational operators and hashing for use with sets. Both of these problems were solved by properly implementing certain class methods such as `__eq__` and `__hash__`.
# Design
The implementation uses two classes: `State` and `Puzzle`. 

## State
`State` represents a given puzzle state, stored as a numpy ndarray, and a `parent`, which optionally points to another `State` instance. `State` has two non-dunder methods: `get_path` and `get_valid_children`. It accepts two arguments: `state`, which accepts a nuumpy array representing the tile configuration, and `parent`, which optionally accepts another State object, otherwise it is `None`. 

If the current state has no parent (i.e. it is the initial state) get_path returns a one-element list containing the current state's tile configuration. If the current state does have a parent, then `get_path` returns the return value of `get_path` called on its parent, with its own state configuration appended to the end of it. This recursive calling allows us to easily trace the solution from initial state to goal state. 

State's other function `get_valid_children` returns a list of `State` objects for each of its children. A child of the current state is a state that we can reach by making a single move on the current state. A state is considered valid if it is physically possible (e.g. moving a tile from outside the valid board space into the board is considered invalid). 

## Puzzle
`Puzzle` represents the A* algorithm operating on a given starting state with a given criteria. As such, it accepts two arguments: `init_state`, a `State` object representing the initial state, and `criteria` which accepts a _function_ to be used as our selection criteria. 

Upon initialization, a `frontier` is created for our algorithm, beginning with only the `State` object passed to `init_state`. The puzzle object generates a `goal_state` based on the size of the `init_state`, and creates an empty set `visited` for referencing visited states. 

Puzzle has two functions: `check_end_state` and `get_valid_children`. `check_end_state` is not strictly required to be implemented, but exists purely as a convenience. It returns a boolean value representing whether a state's tile configuration, represented by the `state` argument, is equivalent to the `goal_state`. That is, it detects whether or not a state is a goal state or not. 

Puzzle's other function, `solve`, takes no arguments. It uses a while loop to repeatedly pop the State from the frontier with the lowest score as defined by our puzzle's `criteria`. It checks if that state is an end state, and if so, calls the state's `get_path` method to get the path that led to that final state. Otherwise, it call's the state's `get_valid_children` method and adds the valid children to the puzzle's `frontier` if that child is not in the `visited` set. Then, it adds that child to the `visited` set. 
# Optimizations

# Results

# Miscellaneous
