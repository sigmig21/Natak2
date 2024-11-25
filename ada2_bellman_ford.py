# -*- coding: utf-8 -*-
"""ADA2 Bellman Ford.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1WkYiWQ9xGD8XHIKGWH7BIoWONBwB0ypw
"""

graph=[[0,-1,4,'-','-'],
       ['-',0,3,2,2],
       ['-','-',0,'-','-'],
       ['-',1,3,0,'-'],
       ['-','-','-',-3,0]]

def bellman_ford(graph,n,s):
    dist=[]
    for i in range(0,n):
        dist.append(999)
    dist[s]=0
    for _ in range(n-1):
       for u in range(n):
          for v in range(n):
             if graph[u][v]!='-'  and dist[u]+graph[u][v]<dist[v]:
                dist[v]=dist[u]+graph[u][v]
    for u in range(n):
       for v in range(n):
          if graph[u][v]!='-'  and dist[u]+graph[u][v]<dist[v]:
             print("Graph contains negative weight cycle,Bellman ford cannot be applied")
             return
    print("Node     Distance from source")
    print("------------------------------")
    for i in range(0,n):
        print(f"{i}     {dist[i]}")
    return

if __name__=="__main__":
    bellman_ford(graph,5,0)

"""
Space Complexity
Distance Array:

The algorithm maintains a single array dist of size n to store the shortest distances.
Graph Representation:

The graph is represented as an adjacency matrix, which takes O(n square) space.
Thus, the total space complexity is: O(n square)

Time complexity : O(n cube)
as total iterations for relaxation are (n-1)(n square)
"""

##Code 2 alternative
def bellman_ford(graph, source):
    # Step 1: Initialize distances
    distances = {vertex: float('inf') for vertex in graph}
    distances[source] = 0

    # Step 2: Relax edges |V| - 1 times
    for _ in range(len(graph) - 1):
        for u in graph:
            for v, weight in graph[u].items():
                if distances[u] != float('inf') and distances[u] + weight < distances[v]:
                    distances[v] = distances[u] + weight

    # Step 3: Check for negative weight cycles
    for u in graph:
        for v, weight in graph[u].items():
            if distances[u] != float('inf') and distances[u] + weight < distances[v]:
                raise ValueError("Graph contains negative weight cycle")

    return distances


# Example
graph = {
    'A': {'B': -1, 'C': 4},
    'B': {'C': 3, 'D': 2, 'E': 2},
    'C': {},
    'D': {'B': 1, 'C': 5},
    'E': {'D': -3}
}
source = 'A'

shortest_distances = bellman_ford(graph, source)
print(shortest_distances)

"""
Time complexity = O(V.E)
dense graphs E=V*V hence time = O(V cube)
sparse graphs V+E hence O(V square)

Space = O(V+E)
"""