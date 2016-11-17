import random

# x=round(x)
heads = 0
tails = 0
count = 0

for x in range(0,5001):
    num = random.random()
    if 0 < num < .5:
        coin = "head"
        heads += 1
        count += 1
    if 1 > num > .5 :
        coin = "tail"
        tails += 1
        count += 1

    print "Attempt {}: Throwing a coin... It's a {}! ... Got {} head(s) so far and {} tail(s) so far".format(x, coin, heads, tails)
