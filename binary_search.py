def two_point_search(nums, target):
    left_bound, right_bound = 0, len(nums) - 1
    # nums.sort()
    # print(type(nums))  # 还是list
    while left_bound <= right_bound:
        mid = (left_bound + right_bound) // 2
        # print(mid)
        if target == nums[mid]:
            return mid
        elif target > nums[mid]:
            left_bound = mid + 1
        else:
            right_bound = mid - 1
    return -1  # low < mid
