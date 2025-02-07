
N = int( input()) # N개 입력받음

coinType = [25 , 10 , 5 , 1 ] #코인종류

inputArr = [ int(input()) for i in range(N) ] # [124 ,25,194]

outputArr = []
for idx , val in enumerate(inputArr) :

    tmp =[]

    for i in range(len(coinType)) :

        if val // coinType[i] > 0:
            tmp.append(str(val // coinType[i]))
            val -=  coinType[i] * (val // coinType[i] )
        else:
            tmp.append(str(0))
    outputArr.append( " ".join(tmp))


for r in outputArr :
    print(r)


