from typing import List 
def longestSubSequence(sequence: List[int]) -> int:
    """
        This problem consists of a solution for the famous longest subsequence problem 
        provided that a list it is required to find the maximum subsequence value.
        an implementation using dynamic programming approach with bottom up approach.
    """
    if len(sequence) < 1:
        return 0
    dp_array = [1]*len(sequence) #This is an initial array with length of the sequence.
    max_val = dp_array[0]
    for i in range(1,len(sequence)):
        for j in range(i):
            if sequence[i] < sequence[j]:
                dp_array[i] = dp_array[j] + 1 if dp_array[j] + 1 < dp_array[i] else dp_array[i]
                if dp_array[i] > max:
                    max_val = dp_array[i]
    return max_val




   
