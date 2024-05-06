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

Upon initialization, a `frontier` is created for our algorithm, beginning with only the `State` object passed to `init_state`. The frontier is implmeented as a min-heap, which is explained further in the Optimizations section. The puzzle object generates a `goal_state` based on the size of the `init_state`, and creates an empty set `visited` for referencing visited states. 

Puzzle has two functions: `check_end_state` and `get_valid_children`. `check_end_state` is not strictly required to be implemented, but exists purely as a convenience. It returns a boolean value representing whether a state's tile configuration, represented by the `state` argument, is equivalent to the `goal_state`. That is, it detects whether or not a state is a goal state or not. 

Puzzle's other function, `solve`, takes no arguments. It uses a while loop to repeatedly pop the State from the frontier with the lowest score as defined by our puzzle's `criteria`. It checks if that state is an end state, and if so, calls the state's `get_path` method to get the path that led to that final state. Otherwise, it call's the state's `get_valid_children` method and adds the valid children to the puzzle's `frontier` if that child is not in the `visited` set. Then, it adds that child to the `visited` set. Due to the presence of the `visited` set, we can categorize this implementation as a graph solution rather than a tree solution. 

# Optimizations
The main optimization used in this design was the usage of a min-heap as the puzzle's frontier. The way this works is that when pushing a state to the heap using `heapq.heappush` we also include the score as determined by the `criteria` function. Internally, the min-heap keeps its elements sorted from lowest to highest based on a value we pass to the heap when pushing an item. In our case, the heap is sorted by the criteria, or heuristic, of each associated state. Thus, we can simply pop the first element from our heap using `heapq.heappop` without having to iterate through the list to find the element with the best heuristic value. 

# Results
![image](https://github.com/Jonathanace/CS170-Project-1/assets/55035716/4219c621-128f-40af-acdc-c5cbbdf563a8)
![image](https://github.com/Jonathanace/CS170-Project-1/assets/55035716/ce3cf9ee-7573-46d5-91ac-aa029b41281a)

The number of nodes expanded is the total number of nodes added to the frontier. The maximum queue size is the maximum size of the frontier throughout the algorithm's runtime. Interestingly, we can see that the two line graphs have a simlar shape, despite their scales and units being different.

In order to inspect the information more closely we can use a log scale for the y-axis.

![image](https://github.com/Jonathanace/CS170-Project-1/assets/55035716/52ecdc9e-23f0-4bec-883a-4fcef927f40b)

![image](https://github.com/Jonathanace/CS170-Project-1/assets/55035716/5284aa70-6b3c-4046-93d9-5f9aad598539)

As we can see all algorithms perform similarly well on trivial problems, but as the difficulty increases, the difference between uniform cost and the other two heuristics increases. There are, however, exceptions to this rule, as uniform cost performs surprisingly well on the "doable" problem and euclidean distance performs exceptionally worse on the "oh boy" difficulty.

# Miscellaneous
