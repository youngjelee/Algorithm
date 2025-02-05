# 첫째 줄에 회의의 제공받음
N = int (input())

# 미팅 배열
meetings  = [ list(map( int ,input().split()))  for _ in range(N) ]

# 미팅 sorting , 1) 종료시간 2) 시작시간
meetings.sort(key=lambda x: [ x[1] , x[0]])


meeting_cnt = 0
end_time = 0

# 그리디 알고리즘 적용
for start, end in meetings:
    if start >= end_time:  # 이전 회의가 끝난 이후에 시작하는 경우
        meeting_cnt += 1
        end_time = end  # 현재 회의가 끝난 시간으로 업데이트

# 결과 출력
print(meeting_cnt)


