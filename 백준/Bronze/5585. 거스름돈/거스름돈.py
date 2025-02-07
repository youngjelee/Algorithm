change = 1000 - int(input())
coins = [500,100,50,10,5,1]

minChangeCount = 0
for coin in coins :

    if change <= 0 :
        break

    if change // coin > 0 :
        minChangeCount += change // coin
        change %= coin

print(minChangeCount)
