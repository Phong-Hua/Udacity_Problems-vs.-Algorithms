import math

def fastSelect(Arr, k):
    '''TO DO'''
    # Implement the algorithm explained above to find the k^th lasrgest element in the given array
    # step 1
    groups = [Arr[x:x+5] for x in range(0, len(Arr), 5)]

    # step 2
    median_set = []
    for group in groups:
        group.sort()
        middle = len(group)//2-1 if len(group)%2 == 0 else len(group)//2;
        median_set.append(group[middle])


    # step 3
    if len(median_set) == 1:
        pivot = median_set[0]
    elif len(median_set) > 1:
        pivot = fastSelect(median_set, len(median_set)//2)

    # step 4
    Arr_Less_P = []
    Arr_Equal_P = []
    Arr_More_P = []
    for number in Arr:
        if number == pivot:
            Arr_Equal_P.append(number)
        elif number > pivot:
            Arr_More_P.append(number)
        else:
            Arr_Less_P.append(number)
    
    # step 5
    if k <= len(Arr_Less_P):
        return fastSelect(Arr_Less_P, k)
    elif k > (len(Arr_Less_P) + len(Arr_Equal_P)):
        return fastSelect(Arr_More_P, k - len(Arr_Less_P) - len(Arr_Equal_P))
    else:
        return pivot

    # print(groups)
    # print(median_set)

Arr = [6, 80, 36, 8, 23, 7, 10, 12, 42]
k = 5
print(fastSelect(Arr, k))        # Outputs 12

Arr = [5, 2, 20, 17, 11, 13, 8, 9, 11]
k = 5
print(fastSelect(Arr, k))

Arr = [6, 80, 36, 8, 23, 7, 10, 12, 42, 99]
k = 10
print(fastSelect(Arr, k))

print(Arr)