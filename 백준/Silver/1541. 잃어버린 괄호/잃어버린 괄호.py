# 55-50+40 -> -35
# 10+20+30+40 -> 100
# 0009-0009 ->

N = input()
splitList = N.split('-') # -기준으로 나눈 리스트 [55 , -50+40]

result = 0

# 첫번째 그룹은 무조건 더한다
result += sum( map(int , splitList[0].split('+') ) )
# 그다음 그룹부터는 모두더한뒤 마이너스 처리한다.
for s in splitList[1:]:
    result -= sum(map(int,s.split('+')))

print(result)