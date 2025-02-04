def calMinSum(count , strArr):
    arr = strArr.split() #공백을 기준으로 나눔
    arr = [ int(strNum) for strNum in arr]
    arr.sort()
 
    totalMinute = 0 
    cursorVal = 0
 
    for num in arr:
        cursorVal += num
        totalMinute += cursorVal
         
    return totalMinute        



count = input()
str = input()

print(calMinSum(count,str))