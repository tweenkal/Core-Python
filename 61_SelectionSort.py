# 👉Selection sort:-
# 👉First of all find the min value:-

# Selection sort is a simple sorting algorithm that works like this:
# It repeatedly selects the smallest (or largest, depending on the
# order you want) element from the unsorted part of the list and moves
# it to the beginning.
# Here's how it works step-by-step for sorting in ascending order:
# Find the smallest element in the array.
# Swap it with the element at the first position.
# Now, find the smallest element in the rest of the array
# (excluding the first position), and swap it with the second element.
# Continue this process for all elements.


def sort(nums):
    for i in range(5):
        minpos = i
        for j in range(i,6):
            if nums[j] < nums[minpos]:
                minpos = j

        temp = nums[i]
        nums[i] = nums[minpos]
        nums[minpos] = temp

        print(nums)

nums = [5,3,8,6,7,2]
sort(nums)
print(nums)