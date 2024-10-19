# ARTIFICIAL INTELLIGENCE CIA 1 & CIA 2
```
Name: Shanmathi Ganesan
Registration number: 22011103052
```

## CIA 1
Implement 12 AI search algorithms.

## ALGORITHMS

### British Museum Search Algorithm(BMS)

- **Goal**: The algorithm explores **all possible paths** from the start node to the goal node in a **Depth-First Search (DFS)** manner.
- **Path Tracking**: It keeps track of the current path in the recursive calls and appends the valid path to the `all_paths` list when the goal node is reached.
- **Multiple Paths**: Instead of stopping after finding the first path, the algorithm continues to explore all unvisited neighbors.
- **Recursive Nature**: Each recursive call has its own copy of the `visited` set to avoid interference between different paths.
- **Result**: The function returns all the possible paths from the start node to the goal as a list of paths.

### Breadth-First Search (BFS) Algorithm
- **Goal**: BFS explores all possible paths level-by-level, starting from the root node, until it finds the shortest path to the goal.
- **Queue-based**: It uses a queue to maintain the current path being explored, ensuring that nodes closer to the start are visited first.
- **FIFO Order**: Nodes are visited in the order they are added to the queue (First In, First Out).
- **Shortest Path**: Since BFS explores level by level, it guarantees finding the shortest path in terms of the number of edges.
- **Result**: It returns the first path found to the goal node, which is the shortest one.

### Depth-First Search (DFS) Algorithm
- **Goal**: DFS explores as deeply as possible along each branch before backtracking to explore other branches.
- **Stack-based/Recursive**: DFS can be implemented using a stack or recursively, where the deepest unexplored nodes are visited first.
- **LIFO Order**: Nodes are processed in a Last In, First Out manner.
- **No guarantee of shortest path**: DFS does not guarantee finding the shortest path and may not explore all nodes if not designed to do so.
- **Result**: Returns a valid path to the goal node, though not necessarily the shortest.

### Hill Climbing Algorithm
- **Goal**: This greedy local search algorithm chooses the neighbor with the best heuristic value at each step to move closer to the goal.
- **Heuristic-driven**: It selects neighbors based on a heuristic function that estimates the cost to reach the goal.
- **Risk of Local Maxima**: It may get stuck in local maxima or plateaus, where no better neighboring state exists.
- **No backtracking**: Hill Climbing only moves forward and does not reconsider previously visited nodes.
- **Result**: Returns the path to the goal if successful, but may fail if it gets stuck in a local maximum.

### Beam Search Algorithm
- **Goal**: A heuristic-based algorithm that expands only a limited number of the most promising paths (K-best) at each level.
- **Heuristic-driven**: Like Hill Climbing, it uses a heuristic to select the most promising paths.
- **Limited Exploration**: Beam search keeps track of only the top K paths at any time, potentially missing optimal solutions if K is too small.
- **More efficient than BFS/DFS**: It balances between breadth and depth, exploring less but more promising nodes.
- **Result**: Returns one of the top-K paths to the goal, if found.

### Oracle Algorithm
- **Goal**: The Oracle algorithm directly returns a predefined optimal path to the goal, assuming prior knowledge.
- **No Search**: It does not perform any exploration or computation but relies on pre-existing knowledge of the best path.
- **Efficiency**: This is the most efficient in terms of time and computation but only works when the correct path is already known.
- **Result**: Immediately returns the optimal path provided by the "oracle."

### Branch and Bound Algorithm
- **Goal**: Branch and Bound explores all possible paths but uses cost estimates to prune branches that can't lead to better solutions.
- **Cost-based Pruning**: It eliminates branches that exceed the current best-known cost (bound).
- **Breadth-first/Depth-first hybrid**: It can combine DFS or BFS techniques with cost limits.
- **Optimal Path**: It ensures finding the optimal solution but can be slow for large graphs.
- **Result**: Returns the optimal path to the goal, with unnecessary paths pruned.

### Branch and Bound + Extended Algorithm
- **Goal**: Similar to Branch and Bound but avoids revisiting already explored nodes using an extended list (Dead Horse).
- **Avoids Redundancy**: By tracking visited nodes, it avoids cycles and redundant computations.
- **More Efficient**: Reduces the overall number of paths explored by pruning duplicate paths.
- **Optimal Path**: Ensures finding the optimal path more efficiently than plain Branch and Bound.
- **Result**: Returns the optimal path, efficiently avoiding cycles.

### Branch and Bound + Heuristic Algorithm
- **Goal**: Uses both cost (like Branch and Bound) and a heuristic to prioritize promising paths for faster exploration.
- **Heuristic-driven Pruning**: Incorporates a heuristic function to guide the exploration toward more promising nodes.
- **Improved Efficiency**: Combines the benefits of Branch and Bound with the heuristic-driven approach of A*.
- **Optimal Path**: Prunes non-optimal paths while improving exploration efficiency.
- **Result**: Returns the optimal path, using both cost and heuristics.

### A* Algorithm
- **Goal**: Combines the actual cost of reaching a node and the estimated cost (heuristic) to guide the search toward the goal.
- **Heuristic and Cost**: Uses both the path cost so far (g) and the estimated cost to goal (h) to find the optimal solution.
- **Efficient Search**: A* balances exploration and optimality, usually faster than plain BFS/DFS.
- **Optimal Path**: Guarantees finding the optimal path if the heuristic is admissible (never overestimates).
- **Result**: Returns the shortest/optimal path to the goal, combining cost and heuristic.

## SAMPLE GRAPH

<img src="https://cdn.discordapp.com/attachments/1131576059498876961/1296998232450400286/graph_min_max_alpha.png?ex=6714533b&is=671301bb&hm=5c9e3e6f4cb341e2f215cb294f919550425fef9c184bbee783d644ff1fa01a08&">

<div style="page-break-after: always;"></div>

## CIA 2
Implement min-max and alpha-beta pruning algorithms.

## ALGORITHM

### Min-max Algorithm

- **Goal**: Minimax is used in decision-making for two-player games, where one player tries to maximize the score while the other minimizes it.
- **Recursive Search**: It recursively explores all possible moves (game tree) to evaluate the best move for both players.
- **Maximizing and Minimizing**: At each level, the algorithm alternates between maximizing (player's turn) and minimizing (opponent's turn) the score.
- **No Pruning**: The entire game tree is searched, making it computationally expensive for deep or large trees.
- **Result**: Returns the optimal move for the maximizer, assuming the opponent plays optimally.

### Alpha-Beta Pruning Algorithm
- **Goal**: Alpha-Beta Pruning is an optimization of the Minimax algorithm that reduces the number of nodes evaluated by pruning suboptimal branches.
- **Alpha and Beta**: Alpha represents the best value the maximizer can secure, while Beta represents the best value the minimizer can secure.
- **Pruning**: If a branch is found that can't possibly improve the result, further exploration of that branch is cut off (pruned).
- **Efficiency**: It significantly reduces the time complexity of Minimax without affecting the outcome.
- **Result**: Returns the same optimal move as Minimax but faster by pruning irrelevant branches.

## SAMPLE GRAPH
<img src="https://cdn.discordapp.com/attachments/1131576059498876961/1296998232941006848/graph_search.png?ex=6714533b&is=671301bb&hm=fb8454dc2c1b0022a683c464850129e1a568657d07054e5ea98e0f0275e1e8b2&">
