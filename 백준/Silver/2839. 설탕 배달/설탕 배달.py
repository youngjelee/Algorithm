def min_sugar_bags(N):
    bags = 0
    while N >= 0:
        if N % 5 == 0:  # 5kg 봉지로 먼저 나누어 떨어지는지 확인
            bags += N // 5
            return bags
        N -= 3  # 5로 나눠떨어지지 않으면 3kg 봉지 하나 사용
        bags += 1
    return -1  # 정확하게 나누어지지 않으면 -1 반환

# 입력
N = int(input())

# 결과 출력
print(min_sugar_bags(N))
