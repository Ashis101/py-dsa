''' Disconected BFS '''
from collections import deque

def bfs(adj,a,visited):
    q=deque
    q.append(a)
    visited[a]=True

    while q:
        s=q.popleft()
        # print(s)

        for i in adj[s]:
            if visited[i] == False:
                q.append(i)
                visited[i]=True
def bfsdis(adj):
    visited=[False]*len(adj)
    count=0
    for u in range(adj):
        if visited[u] == False:
            count+=1
            bfs(adj,u,visited)
    return count
a=[[1,2],[0,2,3],[0,1],[1]]
print(bfsdis())