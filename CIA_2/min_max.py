def min_max(depth, node, is_maximising, values, max_depth):
    if depth == max_depth:
        print("Depth: ", depth, ", Returning value: ", values[node])
        return values[node]

    #Maximising
    if is_maximising:
        print(f"Maximizer at depth {depth}, evaluating children of node {node}")
        print(f"Maximizer at depth {depth}")
        best_value = float('-inf')
        for child in range(2):
            best_value = max(best_value, min_max(depth + 1, child, False, values, max_depth))
        print("Best value: ", best_value, "\n")
        return best_value
    
    #Minimising
    else:
        print(f"Minimizer at depth {depth}, evaluating children of node {node}")
        print(f"Minimizer at depth {depth}")
        best_value = float('inf')
        for child in range(2):
            best_value = min(best_value, min_max(depth + 1, child, True, values, max_depth))
        print("Best value: ", best_value, "\n")
        return best_value
    
# Test case
values = [3, 5, 6, 9, 1, 2, 0, -1]

# Set maximum depth of the tree
max_depth = 3

optimal_value = min_max(0, 0, True, values, max_depth)
print("The optimal value is:", optimal_value)