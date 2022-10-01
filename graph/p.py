# BFS for connected graph 
s=0
# adj=[[1,2],[0,3],[0,3],[1,2],[5,6],[4,5]]
# adj=[[1,2],[0,2,3],[0,1,3,4],[1,2,4],[2,3]]
adj=[[0,1],[1,2],[2,3]]
from collections import deque

# def dfs(adj,s,visited):

#     visited[s]=True
#     print(s)
#     for i in adj[s]:
#         if visited[i] == False:
#             dfs(adj,i,visited)


# def dfs_rec(adj,s):
#     visited=[False]*len(adj)
#     for i in range(len(adj)):
#         if visited[i] == False:

#             dfs(adj,s,visited)

# dfs_rec(adj,s)

def bfs(adj,s,visited):
    parent={}

    for i in range(len(adj)):
        parent[i]=0

    q=deque()
    q.append(s)
    visited[s]=True
    parent[s]=-1
    while q:
        s=q.popleft()
        for i in adj[s]:
            if visited[i] == True and i != parent[s]:
                return True
             
            elif visited[i] == False and parent[i] == 0:
                q.append(i)
                visited[i]=True
                parent[i]=s

    return False


def bfs_rec(adj):
    visited=[False]*len(adj)
    for i in range(len(adj)):

        if(visited[i] == False):

            ans=bfs(adj,i,visited)
            if ans == True:
                return "Got"
            else : return "nothing"

print(bfs_rec(adj))
