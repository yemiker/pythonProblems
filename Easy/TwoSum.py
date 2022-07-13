""" Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
You may assume that each input would have exactly one solution, and you may not use the same element twice.
You can return the answer in any order.

 Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
 """


class Test:
    def twoSum(self, numbers, target):  # A function that gets 2 values
        required = {}  # Define a variable to a dictionary
        for num in range(len(numbers)):  # loop for 'nums' : numbers of array
            if target - numbers[num] in required:  # if target-nums[num] in nums the index of nums will return
                return [required[target - numbers[num]], num]  # required contains the index and value of numbers
            else:
                required[numbers[num]] = num  # Otherwise the number will remain the same number


nums = [5, 2, 8, 4]
a = Test()
print(a.twoSum(nums, 10))
