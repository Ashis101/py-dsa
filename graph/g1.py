''' graph represent in adjacency list  '''

''' add/remove in graph  '''
a=[[1,2],[0,2,3],[0,1],[1]]

# my version of directed graph

# def printGraph(a):
#     for i in a:
#         print(i)

# def addEdge(arr,u,v):
#     arr[u].append(v)
#     arr[v].append(u)
#     printGraph(arr)


# addEdge(a,0,3)

# geek for geek version of directed graph

# in python array is dynamic so no need to create array

def addEdge(adj,u,v):
    adj[u].append(v)
    adj[v].append(u)

def printGraph(adj):
    for l in adj:
        print(l)


adj=[[] for i in range(6)] # this is dynamic size array
addEdge(adj,0,1)
addEdge(adj,0,2)
addEdge(adj,1,3)
addEdge(adj,3,5)
addEdge(adj,2,4)
addEdge(adj,4,5)

printGraph(adj)
