
N = int ( input()) # 배열 개수 받음

arrA =  sorted(map(int , input().split())) # arrayInputA -> sort
arrB  =  sorted ( map(int,  input().split()), reverse=True)# arrayInputB ->sort reverse

result = 0
for i in range(N) :
    result += arrA[i] * arrB[i]

print(result)