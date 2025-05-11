# 👉Bubble sort:-
# 👉Bubble sort is the unsorted element to be sorted

# first of all smallest value

# 5 3 8 6 7 2
# 3 5 8 6 7 2
# 3 5 8 6 7 2
# 3 5 6 8 7 2
# 3 5 6 7 8 2
# 3 5 6 7 2 8
# 3 5 6 2 7 8
# 3 5 2 6 7 8
# 3 2 5 6 7 8
# 2 3 5 6 7 8   <- final sort


def sort(nums):
    for i in range(len(nums)-1,0,-1):
        for j in range(i):
            if nums[j] > nums[j+1]:
                temp = nums[j]
                nums[j] = nums[j+1]
                nums[j+1] = temp

nums = [5,3,2,4,6,7,8]
sort(nums)
print(nums)
