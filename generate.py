#from random import choice
#from random import randint
from random import shuffle

#coin = choice(["heads","tails"])
#print(coin)
#rand = randint(1,6)
#print(rand)

cards = ["jack","queen","king"]
shuffle(cards)
for card in cards:
    print(card)