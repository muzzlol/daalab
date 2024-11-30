from collections import defaultdict
class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = defaultdict(list)
        self.time = 0

    def add_edge(self, u, v):
        self.graph[u].append(v)
        self.graph[v].append(u)

    def bcc_util(self, u, parent, low, disc, stack, bcc):
        children = 0
        disc[u] = self.time
        low[u] = self.time
        self.time += 1

        for v in self.graph[u]:
            if disc[v] == -1:
                parent[v] = u
                children += 1
                stack.append((u, v))
                self.bcc_util(v, parent, low, disc, stack, bcc)

                low[u] = min(low[u], low[v])

                if (parent[u] == -1 and children > 1) or (parent[u] != -1 and low[v] >= disc[u]):
                    bcc.append([])
                    while stack[-1] != (u, v):
                        bcc[-1].append(stack.pop())
                    bcc[-1].append(stack.pop())

            elif v != parent[u] and disc[v] < low[u]:
                low[u] = min(low[u], disc[v])
                stack.append((u, v))

    def bcc(self):
        disc = [-1] * self.V
        low = [-1] * self.V
        parent = [-1] * self.V
        stack = []
        bcc = []

        for i in range(self.V):
            if disc[i] == -1:
                self.bcc_util(i, parent, low, disc, stack, bcc)

        return bcc
    
# Create a graph with 5 vertices
g = Graph(5)

# Add edges
g.add_edge(0, 1)
g.add_edge(1, 2)
g.add_edge(2, 0)
g.add_edge(1, 3)
g.add_edge(3, 4)

# Find and print bi-connected components
bcc = g.bcc()
print("Bi-Connected Components:")
for component in bcc:
    print(component)
from collections import defaultdict

class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = defaultdict(list)
    
    def add_edge(self, u, v):
        self.graph[u].append(v)
    
    def dfs_fill_order(self, v, visited, stack):
        visited[v] = True
        for neighbor in self.graph[v]:
            if not visited[neighbor]:
                self.dfs_fill_order(neighbor, visited, stack)
        stack.append(v)
    
    def get_transpose(self):
        g = Graph(self.V)
        for u in self.graph:
            for v in self.graph[u]:
                g.add_edge(v, u)
        return g
    
    def dfs_util(self, v, visited, component):
        visited[v] = True
        component.append(v)
        for neighbor in self.graph[v]:
            if not visited[neighbor]:
                self.dfs_util(neighbor, component)
    
    def print_sccs(self):
        stack = []
        visited = [False] * self.V
        
        # Fill vertices in stack according to their finishing times
        for i in range(self.V):
            if not visited[i]:
                self.dfs_fill_order(i, visited, stack)
        
        # Create a reversed graph
        gr = self.get_transpose()
        
        # Mark all vertices as not visited for second DFS
        visited = [False] * self.V
        
        # Process all vertices in order defined by the stack
        while stack:
            v = stack.pop()
            if not visited[v]:
                component = []
                gr.dfs_util(v, visited, component)
                print(component)

# Test the implementation
g = Graph(5)
g.add_edge(1, 0)
g.add_edge(0, 2)
g.add_edge(2, 1)
g.add_edge(0, 3)
g.add_edge(3, 4)

print("Strongly Connected Components:")
g.print_sccs()

