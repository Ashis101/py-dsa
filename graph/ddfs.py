''' Disconnected Depth First Search '''

def dfsrec(adj,s,visited):
    visited[s]=True
    print(s)

    for i in adj[s]:
        if visited[i] == False:
            dfsrec(adj,s,visited)

def dfs(adj,s):
    visited=[False]*len(adj)
    for u in range(len(adj)):
        if visited[u] == False:
            dfsrec(adj,s,visited)

a=[[1,2],[0,2,3],[0,1],[1]]
print(dfs(a,0))