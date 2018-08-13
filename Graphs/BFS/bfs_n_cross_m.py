# Python3 Program to print BFS traversal
# from a given source vertex. BFS(int s)
# traverses vertices reachable from s.

'''
if input dimensions are n = 3(rows) and m = 4(columns)
it produces a graph like this below:

1 -> 2 -> 3 -> 4
| \  |  \ |  \ |
5 -> 6 -> 7 -> 8
| \  | \  |  \ |
9 -> 10-> 11-> 12

all are unidirectional edges
each node/vertex in connected to its right, down and diagonal node(if possible)
'''
 
# using adjacency list representation

 
# function to add an edge to graph
def addEdge(G,u,v):
    if(u not in G): temp = []
    else: temp = G[u]
    temp.append(v)
    G[u] = temp
    return G
 
# Function to print a BFS of graph
def BFS(G, s):
 
    # Mark all the vertices as not visited
    visited = [False] * (len(G))
 
    # Create a queue for BFS
    queue = []
 
    # Mark the source node as 
    # visited and enqueue it
    queue.append(s)
    visited[s-1] = True
 
    while queue:
 
        # Dequeue a vertex from 
        # queue and print it
        s = queue.pop(0)
        print (s, end = " ")
 
        # Get all adjacent vertices of the
        # dequeued vertex s. If an adjacent
        # has not been visited, then mark it
        # visited and enqueue it
        for i in G[s]:
            if i == None: break
            if visited[i-1] == False:
                queue.append(i)
                visited[i-1] = True
 
# Driver code
 
# Create an empty graph
G = {}

print('press n*m dimensions')
n = int(input('n = '))
m = int(input('m = '))

# adding edges in graph on right, down and diagonally
for i in range(1, n+1):
    for j in range(1, m+1):
        node = j + (i-1)*m
        if(node+1 <= m*i): G = addEdge(G, node, node+1)
        if(node+m <= n*m): G = addEdge(G, node, node+m)
        if(node+m+1 <= m*(i+1) and node+m+1 <= n*m): G = addEdge(G, node, node+m+1)
G = addEdge(G, n*m, None)

print(G)
print()

print ("Following is Breadth First Traversal"
                  " (starting from vertex 1)")

BFS(G, 1)

