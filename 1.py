def multi(nums: list[int]) -> list:
    pair = []
    iterations = int(round((len(nums)+1)/2))
    print(iterations)
    for i in range(iterations):
        pair.append(nums[i]*nums[(len(nums)-1-i)])
    return pair


print(multi([2, 3, 4, 5, 6]))