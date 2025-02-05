# 첫쨰줄에 미팅룸 배열받음
N = int(input())
# N 숫자만큼 String 받아서 공백으로 int 배열 split   [ [1,2] , [2,4] ]
meetings = [ list(map(int , input().split()))  for _ in range(N) ]

# meetings 를 종료시간 / 시작시간 asc 로 sorting
meetings.sort( key=lambda x: (x[1] , x[0]) )

meetingCnt = 0
lastTime = 0

for meeting in meetings :
    if lastTime <= meeting[0] :
        meetingCnt +=1
        lastTime = meeting[1]


print(meetingCnt)