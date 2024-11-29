import heapq

def dijkstra(graph, start):
    V = len(graph)
    dist = [float('inf')] * V
    dist[start] = 0
    pq = [(0, start)]  # (distance, vertex)
    
    while pq:
        d, u = heapq.heappop(pq)
        if d > dist[u]:
            continue
            
        for v, weight in graph[u]:
            if dist[u] + weight < dist[v]:
                dist[v] = dist[u] + weight
                heapq.heappush(pq, (dist[v], v))
    return dist

def bellman_ford(graph, V, start):
    dist = [float('inf')] * V
    dist[start] = 0
    
    for _ in range(V - 1):  # Relax all edges V-1 times
        for u in graph:
            for v, weight in graph[u]:
                if dist[u] + weight < dist[v]:
                    dist[v] = dist[u] + weight
    
    # Check for negative weight cycle
    for u in graph:
        for v, weight in graph[u]:
            if dist[u] + weight < dist[v]:
                print("Graph contains negative weight cycle")
                return None
    return dist

def floyd_warshall(graph, V):
    dist = [[float('inf')] * V for _ in range(V)]
    
    for u in range(V):
        dist[u][u] = 0  # Distance from a node to itself is 0
    
    # Fill initial distances from graph
    for u in graph:
        for v, weight in graph[u]:
            dist[u][v] = weight
    
    # Update distances using Floyd-Warshall algorithm
    for k in range(V):
        for i in range(V):
            for j in range(V):
                dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])
    return dist

# Example usage
graph = {
    0: [(1, 1), (2, 4)],
    1: [(2, 2), (3, 5)],
    2: [(3, 1)],
    3: []
}
V = 4

# Test the algorithms
print("Dijkstra's Algorithm:")
print(dijkstra(graph, 0))

print("\nBellman-Ford Algorithm:")
print(bellman_ford(graph, V, 0))

print("\nFloyd-Warshall Algorithm:")
dist_matrix = floyd_warshall(graph, V)
for row in dist_matrix:
    print(row) 