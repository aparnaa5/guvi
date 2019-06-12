g=list(map(int,input().split()))
for j in range(g[0]+1,g[1]):
  if j%2 != 0:
    print(j,end=' ')
