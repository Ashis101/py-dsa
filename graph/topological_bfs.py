# topological sorting (kahan's algo)
from collections import deque

def topologicalSort(adj):
    V=len(adj) #number of vertices
    in_degree=[0]*V 

    for u in range(V):
        # calculating how many indegree connection mad with this vertices
        for x in adj[u]:
            in_degree[x]+=1
    q=deque() 

    for i in range(V):
        if(in_degree[i] == 0):
            q.append(i)
    ans=[]
    while q:
        vertex=q.popleft()
        ans.append(vertex)
        for x in adj[vertex]:
            in_degree[x]=in_degree[x]-1
            if( in_degree[x] == 0):
                q.append(x)
    return ans

def addEdge(adj,u,v):
    adj[u].append(v)


a=[[] for i in range(5)]

addEdge(a,0,1)
addEdge(a,4,1)
addEdge(a,1,2)
addEdge(a,2,3)
addEdge(a,3,1)
print(topologicalSort(a))
