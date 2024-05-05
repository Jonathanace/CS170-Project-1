# Challenges
The main challenge I encountered working on this project was working with the state class that represents a single puzzle state. Some of these issues were implementing relational operators and hashing for use with sets. Both of these problems were solved by properly implementing certain class methods such as `__eq__` and `__hash__`.
# Design
The implementation uses two classes: `State` and `Puzzle`. 

## State
`State` represents a given puzzle state, stored as a numpy ndarray, and a `parent`, which optionally points to another `State` instance. `State` has two non-dunder methods: `get_path` and `get_valid_children`. It accepts two arguments: `state`, which accepts a nuumpy array representing the tile configuration, and `parent`, which optionally accepts another State object, otherwise it is `None`. 

If the current state has no parent (i.e. it is the initial state) get_path returns a one-element list containing the current state's tile configuration. If the current state does have a parent, then `get_path` returns the return value of `get_path` called on its parent, with its own state configuration appended to the end of it. This recursive calling allows us to easily trace the solution from initial state to goal state. 

## Puzzle
`Puzzle` represents the A* algorithm operating on a given starting state with a given criteria. As such, it accepts two arguments: `init_state`, a `State` object representing the initial state, and `criteria` which accepts a _function_ to be used as our selection criteria. 

# Optimizations

# Results

# Miscellaneous
