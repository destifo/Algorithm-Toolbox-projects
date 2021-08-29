import random

numlist = list()
#listSize = int(input())


def max_pairwise_product(numlist):
    n = len(numlist)
    max_product = 0
    for first in range(listSize):
        for second in range(first + 1, listSize):
            max_product = max(max_product,
                numlist[first] * numlist[second])

    return max_product

def max_pairwise_product_fast(bigindex1 = None, bigindex2 = None):
    for n in range(len(numlist)):
        if bigindex1 is None or int(numlist[n]) > int(numlist[bigindex1]):
            bigindex1 = n

    for n in range(len(numlist)):
        if (bigindex1 != n) and (bigindex2 is None or int(numlist[n]) > int(numlist[bigindex2])):
            bigindex2 = n

    return int(numlist[bigindex1]) * int(numlist[bigindex2])



x = random.randint()
y = random.randint()

while True:
    for i in range(x%20):
        numlist.append(y%100)
    if max_pairwise_product(numlist) != max_pairwise_product_fast(numlist):
        print("Wrong answer", i, y%100)
        print(max_pairwise_product, max_pairwise_product_fast)
        break
