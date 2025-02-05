#최소코인개수를 구하는 함수 ( 구해야하는 값 , 코인 배열 )
def getMininumCoinCnt( price ,coinArr):
    
    coinCnt = 0 
        
    coinArr = [ x for x in coinArr if price >= x]

    for cursorCoin in coinArr : 
        
        if price <= 0 :
            break
        
        if price / cursorCoin  > 0 :
            tmpCnt = price//cursorCoin
            coinCnt += tmpCnt
            price -= tmpCnt * cursorCoin
            continue
            
    return coinCnt                
                
    
    

#파라미터로 받는 string 을 공백 기준 배열로 split 한다. 10 4200 
arr = input().split()    # ["10","4200"]

# 배열 원소들을 int 형으로 변한한다.
intArr = [ int(strNum) for strNum in arr] #[10,42]

# intArr 의 첫번째 원소만큼 input() 을 반복 요청 후 값 받아서 동전 모음 배열로 집어넣는다. (역순 정렬)
coinArr = sorted( [int(input()) for _ in range(intArr[0])] , reverse=True)


print(getMininumCoinCnt(int (arr[1]), coinArr))
