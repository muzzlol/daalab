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

class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = defaultdict(list)
        self.time = 0

    def add_edge(self, u, v):
        self.graph[u].append(v)

    def scc_util(self, u, low, disc, stack_member, stack, scc):
        disc[u] = self.time
        low[u] = self.time
        self.time += 1
        stack_member[u] = True
        stack.append(u)

        for v in self.graph[u]:
            if disc[v] == -1:
                self.scc_util(v, low, disc, stack_member, stack, scc)
                low[u] = min(low[u], low[v])
            elif stack_member[v]:
                low[u] = min(low[u], disc[v])

        w = -1
        if low[u] == disc[u]:
            scc.append([])
            while w != u:
                w = stack.pop()
                scc[-1].append(w)
                stack_member[w] = False

    def scc(self):
        disc = [-1] * self.V
        low = [-1] * self.V
        stack_member = [False] * self.V
        stack = []
        scc = []

        for i in range(self.V):
            if disc[i] == -1:
                self.scc_util(i, low, disc, stack_member, stack, scc)

        return scc


# Create a directed graph with 5 vertices
g = Graph(5)

# Add directed edges
g.add_edge(1, 0)
g.add_edge(0, 2)
g.add_edge(2, 1)
g.add_edge(0, 3)
g.add_edge(3, 4)

# Find and print strongly connected components
scc = g.scc()
print("Strongly Connected Components:")
for component in scc:
    print(component)

