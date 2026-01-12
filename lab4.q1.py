# Function to perform Best First Search
from heapq import heappush, heappop

def bestFirstSearch(edges, src, target, n):
    
    # create the adjacency list
    adj = [[] for _ in range(n)]
    for edge in edges:
        adj[edge[0]].append([edge[1], edge[2]])
        adj[edge[1]].append([edge[0], edge[2]])
    
    # create a visited array to 
    # keep track of visited nodes
    visited = [False] * n
    
    # create the min heap to store the nodes
    # based on the cost
    pq = []
    
    # push the source node in the min heap
    heappush(pq, [0, src])
    
    # mark the source node as visited
    visited[src] = True
    
    # to store the path   
    path = []
    
    # loop until the min heap is empty
    while pq:
        # get the top element of the min heap
        x = heappop(pq)[1]
        
        # push the current node in the path
        path.append(x)
        
        # if the current node is the target node
        # break the loop
        if x == target:
            break
        
        # loop through the edges of the current node
        for edge in adj[x]:
            if not visited[edge[0]]:
                # mark the node as visited
                visited[edge[0]] = True
                # push the node in the min heap
                heappush(pq, [edge[1], edge[0]])
    
    return path

if __name__ == "__main__":
    n = 14
    edgeList = [
        [0, 1, 3], [0, 2, 6], [0, 3, 5],
        [1, 4, 9], [1, 5, 8], [2, 6, 12],
        [2, 7, 14], [3, 8, 7], [8, 9, 5],
        [8, 10, 6], [9, 11, 1], [9, 12, 10],
        [9, 13, 2]
    ]
    source = 0
    target = 9
    path = bestFirstSearch(edgeList, source, target, n)
    for i in range(len(path)):
        print(path[i], end = " ")