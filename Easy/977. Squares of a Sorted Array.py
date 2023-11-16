"""
Given an integer array nums sorted in non-decreasing order, return an array of the squares of each number
sorted in non-decreasing order.



Example 1:

Input: nums = [-4,-1,0,3,10]
Output: [0,1,9,16,100]
Explanation: After squaring, the array becomes [16,1,0,9,100].
After sorting, it becomes [0,1,9,16,100].
Example 2:

Input: nums = [-7,-3,2,3,11]
Output: [4,9,9,49,121]


Constraints:

1 <= nums.length <= 104
-104 <= nums[i] <= 104
nums is sorted in non-decreasing order.


Follow up: Squaring each element and sorting the new array is very trivial, could you find an O(n) solution
using a different approach?
"""


class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        lenght = len(nums)
        res = [0] * lenght
        left = 0
        right = lenght - 1
        while lenght >= 1:
            x1 = abs(nums[left])
            x2 = abs(nums[right])
            if x1 > x2:
                res[lenght - 1] = x1 ** 2
                left += 1

            else:
                res[lenght - 1] = x2 ** 2
                right -= 1
            lenght -= 1
        return res