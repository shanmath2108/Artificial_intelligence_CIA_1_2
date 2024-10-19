def alpha_beta_pruning(depth, node, is_maximizing, values, alpha, beta, max_depth):
    if depth == max_depth:
        print(f"Depth: {depth}, Returning value: {values[node]}")
        return values[node]

    # Maximizing
    if is_maximizing:
        print(f"Maximizer at depth {depth}, evaluating children of node {node}")
        best_value = float('-inf')

        # Traverse both children
        for child in range(2):
            value = alpha_beta_pruning(depth + 1, node * 2 + child, False, values, alpha, beta, max_depth)
            best_value = max(best_value, value)
            alpha = max(alpha, best_value)
            
            print(f"Maximizer at depth {depth}, node {node}: Alpha = {alpha}, Beta = {beta}")

            if beta <= alpha:
                print(f"Pruning at depth {depth}, node {node}: Alpha = {alpha}, Beta = {beta}")
                break  # Beta cut-off (pruning)

        print(f"Best value for maximizer at depth {depth}: {best_value}\n")
        return best_value

    # Minimizing
    else:
        print(f"Minimizer at depth {depth}, evaluating children of node {node}")
        best_value = float('inf')

        # Traverse both children
        for child in range(2):
            value = alpha_beta_pruning(depth + 1, node * 2 + child, True, values, alpha, beta, max_depth)
            best_value = min(best_value, value)
            beta = min(beta, best_value)

            print(f"Minimizer at depth {depth}, node {node}: Alpha = {alpha}, Beta = {beta}")

            if beta <= alpha:
                print(f"Pruning at depth {depth}, node {node}: Alpha = {alpha}, Beta = {beta}")
                break  # Alpha cut-off (pruning)

        print(f"Best value for minimizer at depth {depth}: {best_value}\n")
        return best_value

# Test case
values = [3, 5, 6, 9, 1, 2, 0, -1]

# Alpha and Beta initial values
alpha = float('-inf')
beta = float('inf')

# Set maximum depth of the tree
max_depth = 3

optimal_value = alpha_beta_pruning(0, 0, True, values, alpha, beta, max_depth)
print("The optimal value is:", optimal_value)
