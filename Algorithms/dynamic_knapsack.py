import math

profits = []
weights = []

capacity = 16



def knapsack(profits, weights, capacity, i = 0, lookup=None):
    # Initializes a lookup table
    if lookup == None:
        lookup = {}
    
    if i >= len(profits):
        return 0
    
    if capacity < 0:
        return -math.inf
    

    # Recursive Step
    left = profits[i] + knapsack(profits, weights, capacity - weights[i], i + 1, lookup)
    right = knapsack(profits, weights, capacity, i + 1, lookup)
    
    lookup[(i, capacity)] = max(left, right)
    
    return lookup[(i, capacity)]
        