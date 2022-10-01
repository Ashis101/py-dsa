from collections import deque

def bfs(adj,s):
    visited = [False]*len(adj)

    q=deque()
    q.append(s)
    visited[s] = True

    while q:
        s = q.popleft()
        print(s,end=' ')

        for u in adj[s]:
            if visited[u] == False:
                q.append(u)
                visited[u] = True



a=[[1,2],[0,2,3],[0,1,3,4],[1,2,4],[2,3]]
bfs(a,0)

