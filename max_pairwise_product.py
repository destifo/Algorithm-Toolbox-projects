numlist = list()
listSize = int(input())

strlist = input()
numlist = strlist.split()

def max_pairwise_product_fast(bigindex1 = None, bigindex2 = None):
    for n in range(len(numlist)):
        if bigindex1 is None or int(numlist[n]) > int(numlist[bigindex1]):
            bigindex1 = n

    for n in range(len(numlist)):
        if (bigindex1 != n) and (bigindex2 is None or int(numlist[n]) > int(numlist[bigindex2])):
            bigindex2 = n

    return int(numlist[bigindex1]) * int(numlist[bigindex2])

solution = max_pairwise_product_fast()
print(solution)
