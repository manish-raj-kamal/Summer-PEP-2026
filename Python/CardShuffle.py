"""Describe a method for performing a card shuffle of a list of 2n elements, by converting it into 2 lists.
A card shuffle is a permutation where a list L is cut into two lists, L1 and L2, where L1 is the first half of L and L2 is the second half of L,
and then these two lists are merged into one by taking the first element of L1, then the first element of L2, then the second element of L1, 
then the second element of L2, and so on, until all elements are merged back into a single list.
"""

def card_shuffle(L):

    n = len(L) // 2
    L1 = L[:n] 
    L2 = L[n:] 

    shuffled_list = []
    for i in range(n):
        shuffled_list.append(L1[i])  
        shuffled_list.append(L2[i])  

    return shuffled_list

if __name__ == "__main__":
    original_list = [1, 2, 3, 4, 5, 6]
    shuffled = card_shuffle(original_list)
    print("Original list:", original_list)
    print("Shuffled list:", shuffled)