def hamiltonian_cycle(graph):
    V = len(graph)
    # Initialize path with -1
    path = [-1] * V
    # Start from vertex 0
    path[0] = 0
    solutions = []
    hamiltonian_cycle_util(graph, path, 1, solutions)
    
    if not solutions: 
        print("No solutions exist")
        return False
    
    print(solutions)
    return True

def hamiltonian_cycle_util(graph, path, pos, solutions):
    # Base case: if all vertices are included in the path
    if pos == len(graph):
        # Check if there is an edge from last vertex to first vertex
        if graph[path[pos-1]][path[0]] == 1:
            solutions.append(path.copy())
        return
    
    # Try different vertices as next candidate
    for v in range(1, len(graph)):
        if is_safe(v, graph, path, pos):
            path[pos] = v
            
            hamiltonian_cycle_util(graph, path, pos + 1, solutions)
                
            # If adding vertex v doesn't lead to a solution,
            # remove it (backtrack)
            path[pos] = -1
    

def is_safe(v, graph, path, pos):
    # Check if this vertex is adjacent to the previously added vertex
    if graph[path[pos-1]][v] == 0:
        return False
    
    # Check if the vertex has already been included in the path
    if v in path:
        return False
    
    return True

def print_solution(path):
    print("Hamiltonian Cycle exists:")
    for vertex in path:
        print(vertex, end=" ")
    print(path[0])  # Print first vertex again to show complete cycle

# Example usage:
# square graph ABCD
# graph = [
#     [0, 1, 0, 1],  # A's connections (to B and D)
#     [1, 0, 1, 0],  # B's connections (to A and C)
#     [0, 1, 0, 1],  # C's connections (to B and D)
#     [1, 0, 1, 0]   # D's connections (to A and C)
# ]

# Example graph represented as adjacency matrix
graph = [
    [0, 1, 1, 1, 0],
    [1, 0, 1, 1, 1],
    [1, 1, 0, 0, 1],
    [1, 1, 0, 0, 1],
    [0, 1, 1, 1, 0]
]

hamiltonian_cycle(graph)