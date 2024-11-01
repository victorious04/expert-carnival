import random

def FlippingCoin(x):
    return random.choice(x)

def MainCoinFlipFunc():
    coinChance = ["Heads","Tails"]
    headsInARow = 0
    numOfFlips = 0

    

    while headsInARow != 5:
        coinFlip = FlippingCoin(coinChance)
        if coinFlip == "Heads":
            headsInARow +=1
        else:
            headsInARow = 0
        numOfFlips+=1

    print(f"It took {numOfFlips} coin flips to get five heads in a row.")
    

MainCoinFlipFunc()
