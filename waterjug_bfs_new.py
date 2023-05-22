from collections import deque
def bfs(a,b,target):
    m={}
    path=[]
    q=deque([(0,0)])
    while q:
        u=q.popleft()
        if (u[0],u[1]) in m:
            continue
        if u[0]>a or u[1]>b or u[0]<0 or u[1]<0:
            continue
        path.append((u[0],u[1]))
        m[(u[0],u[1])]=1
        if u[0]==target or u[1]==target:
            if u[0]==target and u[1]!=0:
                path.append((u[0],0))
            elif u[1]==target and u[0]!=0:
                path.append((0,u[1]))
            print("Path: ",path)
            return
        q.append((u[0],b))
        q.append((a,u[1]))
        for ap in range(max(a,b)+1):
            c,d=u[0]+ap,u[1]-ap
            if c==a or (d==0 and d>=0):
                q.append((c,d))
            c,d=u[0]-ap,u[1]+ap
            if (c==0 and c>=0) or d==b:
                q.append((c,d))
        q.append((a,0))
        q.append((0,b))
    print("No solution")
j1,j2,target=4,3,2
print("Path from initial state to solution state is: ")
bfs(j1,j2,target)