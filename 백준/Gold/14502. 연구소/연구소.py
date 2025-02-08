from collections import deque
from itertools import combinations

X , Y  = list (map(int, input().split()))

original_lab =  [ list(map(int,input().split())) for _ in range(X) ]


empty_positions = [] # 빈 공간 좌표
virus_positions = [] #바이러스공간 좌표

direction = [[1,0] , [0,1] , [-1,0] ,[0,-1] ]

#0 빈공간 , # 1 벽 , # 2 바이러스
for x in range(X) :
    for y in range(Y) :
        if original_lab[x][y] == 0 :
            empty_positions.append( (x,y))
        elif original_lab[x][y] == 2 :
            virus_positions.append((x,y))

max_safe_area = 0

# combinations 이용하여 , 3개를 포함하여 조합만들고 그것으로 모든 경우의수 brute Force Testing
for walls in combinations(empty_positions , 3 )  :
    # original_lab 복사
    copy_lab = [ ol[:] for ol in original_lab]

    for (wx, wy) in walls :
        copy_lab[wx][wy] = 1

    virus_positons_deque = deque(virus_positions)
    while virus_positons_deque :
        qx , qy = virus_positons_deque.popleft()

        for (dx , dy) in direction :
            tx , ty = qx + dx , qy + dy

            # 범위 초과 체크
            if 0 <= tx < X and 0<=ty<Y :
                if copy_lab[tx][ty] == 0 :
                    copy_lab[tx][ty] = 2
                    virus_positons_deque.append( (tx,ty))

    # 이번 walls 세팅으로인한 안전지대 카운트
    cursorSafetyCnt = 0
    # 0 개수 체크
    for x in range(X) :
        for y in range(Y) :
            if copy_lab[x][y] == 0 :
                cursorSafetyCnt += 1

    max_safe_area = max (max_safe_area , cursorSafetyCnt)

print(max_safe_area)


