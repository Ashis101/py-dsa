# calculate shortest path in undirected graph using bfs

from collections import deque

def findkey(my_dict):
    key_list = list(my_dict.keys())
    val_list = list(my_dict.values())
    
    # print key with val 100
    position = val_list.index(100)
    return key_list[position]

def shortestPath(s,d,parent,path):

    if d == s:
        return 
    path.append(d)
    if parent[d] != s:
        shortestPath(s,parent[d],parent,path)

def bfs(adj,s,from_vertex,to_vertex):
    spath=[]
    visited=[False]*len(adj)
    parent={}
    q=deque()
    q.append(s)
    visited[s]=True
    if s not in parent.keys():
        parent[s]=-1

    while q:
        vertex=q.popleft()

        for i in adj[vertex]:
            if visited[i] == False:
                q.append(i)
                visited[i]=True
                if i not in parent.keys():
                    parent[i]=vertex


    shortestPath(from_vertex,to_vertex,parent,spath)
    spath.append(from_vertex)
    spath.reverse()
    print(spath)
a=[[1,2],[0,2,3],[0,1,3,4],[1,2,4],[2,3]]
bfs(a,0,0,4)



