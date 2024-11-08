def longestConsecutive(nums):
    nums_set = set(nums)
    longest_seq = 0

    for num in nums_set:
        
        # Check if num is the start point of the sequence
        if num - 1 not in nums_set:
            current_num = num
            current_seq = 1
            
            while current_num + 1 in nums_set:
                current_num += 1
                current_seq += 1

            longest_seq = max(longest_seq, current_seq)
    return longest_seq

# Example usage
nums = [100, 4, 200, 1, 3, 2]
print(longestConsecutive(nums))  # Output should be 4, as [1, 2, 3, 4] is the longest consecutive sequence.

# Algorithm:
# 1. Create an empty hash (in this case, a set in Python for O(1) lookup).
# 2. Insert all array elements into the hash to ensure unique elements and quick lookups.
# 3. Loop through every element in the hash.
# 4. Check if this element is the starting point of a subsequence.
#    To do this, check if num - 1 is NOT in the hash. 
#    If num - 1 is not present, then num is the first element of a new sequence.
# 5. If this element is the start, count the number of elements in the consecutive sequence
#    starting with this element. Continue to the next number (current_num + 1) as long as it is in the hash.
# 6. If the count of this current sequence is greater than the previous longest sequence,
#    update the longest_seq variable.
