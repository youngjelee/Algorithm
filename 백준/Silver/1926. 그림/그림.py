##1926 번 문제
from collections import deque

X , Y = list ( map(int , input().split()))

# print(X) ; print(Y)

canvas = [ list (map(int , input().split())) for _ in range(X) ]
# print(canvas)

visitedYn=  [[False]*Y for _ in range(X)]
# print(visitedYn)

direction = [[0,1],[1,0],[0,-1],[-1,0]]

def bfs(x, y ) :
    queue = deque([(x,y)])
    paintWidth = 1
    visitedYn[x][y] =  True

    while queue:
        q = queue.popleft()

        for d in direction :
            cursorX = q[0] + d[0]
            cursorY = q[1] + d[1]

            if 0 <= cursorX < X and 0 <= cursorY < Y :
                if canvas[cursorX][cursorY] == 1 and visitedYn[cursorX][cursorY] == False :
                    visitedYn[cursorX][cursorY] = True
                    queue.append((cursorX,cursorY))
                    paintWidth += 1
    return paintWidth


count = 0
maxWidth = 0
for x in range(X) :
    for y in range(Y) :
        if canvas[x][y] ==1 and visitedYn[x][y]==False :
            count += 1
            maxWidth = max( bfs(x,y) , maxWidth)
print(count)
print(maxWidth)