# Name: Michael Mclean
# OSU Email: mcleamic@oregonstate.edu
# Course: CS325 - Analysis of Algorithms
# Assignment: 2
# Due Date: 2024-04-15
# Description: A function that returns the kth element of 2 merged, sorted lists.

def kthElement(Arr1, Arr2, k):
    length1 = len(Arr1)
    length2 = len(Arr2)
    if length1 + length2 <= k:
        return "k too large"
    elif k <= 0:
        return "k too small"

    if length1 == 0:
        return Arr2[k-1]
    if length2 == 0:
        return Arr1[k-1]
    if k == 1:
        if Arr1[0] < Arr2[0]:
            return Arr1[0]
        else:
            return Arr2[0]

    if length1 < k // 2:
        Arr1_index = length1
    else:
        Arr1_index = k // 2

    if length2 < k // 2:
        Arr2_index = length2
    else:
        Arr2_index = k // 2

    if Arr1[Arr1_index - 1] > Arr2[Arr2_index - 1]:
        return kthElement(Arr1, Arr2[Arr2_index:], k - Arr2_index)
    else:
        return kthElement(Arr1[Arr1_index:], Arr2, k - Arr2_index)


if __name__ == "__main__":

    arr1 = [1, 2, 3, 5, 6]
    arr2 = [3, 4, 5, 6, 7]

    print(kthElement(arr1, arr2, 5))