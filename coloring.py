# Function to check if the current color assignment is safe for vertex v
def is_safe(v, graph, colors, color):
    for i in range(len(graph)):
        if graph[v][i] == 1 and colors[i] == color:
            return False
    return True

# Recursive function to solve the graph coloring problem
def graph_coloring(graph, num_colors, colors, v):
    # Base case: If all vertices are assigned a color, return True
    if v == len(graph):
        return True

    # Try assigning each color (from 1 to num_colors) to vertex v
    for color in range(1, num_colors + 1):
        # Check if this color can be assigned to vertex v
        if is_safe(v, graph, colors, color):
            colors[v] = color  # Assign color to vertex v

            # Recursively assign colors to the rest of the vertices
            if graph_coloring(graph, num_colors, colors, v + 1):
                return True

            # Backtrack: Remove the assigned color
            colors[v] = 0

    return False  # Return False if no color can be assigned to this vertex

# Function to initiate graph coloring
def solve_graph_coloring(graph, num_colors):
    # Initialize all vertices with no color (0)
    colors = [0] * len(graph)

    # Start coloring from vertex 0
    if graph_coloring(graph, num_colors, colors, 0):
        # Print the solution
        print("Solution found with the following color assignments:")
        for v in range(len(graph)):
            print(f"Vertex {v} --> Color {colors[v]}")
    else:
        print("No solution exists with the given number of colors.")

# Example usage
# Adjacency matrix of the graph
graph = [
    [0, 1, 1, 1],
    [1, 0, 1, 0],
    [1, 1, 0, 1],
    [1, 0, 1, 0]
]
num_colors = 3  # Number of colors

solve_graph_coloring(graph, num_colors)