# Challenges
The main challenge I encountered working on this project was working with the state class that represents a single puzzle state. Some of these issues were implementing relational operators and hashing for use with sets. Both of these problems were solved by properly implementing certain class methods such as `__eq__` and `__hash__`.
# Design
The implementation uses two classes: `State` and `Puzzle`. 

`State` represents a given puzzle state, stored as a numpy ndarray, and a `parent`, which optionally points to another `State` instance. `State` has two non-dunder methods: `get_path` and `get_valid_children`. If the current state has no parent (i.e. it is the initial state) get_path returns a one-element list containing the current state's tile configuration. If the current state does have a parent, then `get_path` returns the return value of `get_path` called on its parent, with its own state configuration appended to the end of it. This recursive calling allows us to easily trace the solution from initial state to goal state. 

# Optimizations

# Results

# Miscellaneous
