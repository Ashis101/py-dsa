# bfs in graph

from collections import deque


def bfs(adj,s,visited):
    q=deque()
    q.append(s)
    visited[s]=True

    while q:
        vertex=q.popleft()
        for v in adj[vertex]:
            if(visited[v] == False):
                q.append(v)
                visited[v]=True

def bfs_dis(adj,s):
    visited=[False]*len(adj)
    counter=0
    for i in range(len(adj)):
        if visited[i] ==False:
            counter+=1
            bfs(adj,s,visited)

    print(counter)
a=[[1,2],[0,2,3],[0,1],[1]]
bfs_dis(a,0)