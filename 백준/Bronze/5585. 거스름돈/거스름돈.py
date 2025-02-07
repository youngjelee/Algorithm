totalMount = 1000 - int(input())
coins = [500,100,50,10,5,1]

minChangeCount = 0
for coin in coins :

    if totalMount <= 0 :
        break

    if totalMount // coin > 0 :
        minChangeCount += (totalMount // coin )
        totalMount -= coin * (totalMount // coin )

print(minChangeCount)
