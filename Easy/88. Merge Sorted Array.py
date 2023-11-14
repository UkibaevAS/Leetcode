"""
You are given two integer arrays nums1 and nums2, sorted in non-decreasing order, and two integers m and n,
representing the number of elements in nums1 and nums2 respectively.

Merge nums1 and nums2 into a single array sorted in non-decreasing order.

The final sorted array should not be returned by the function, but instead be stored inside the array nums1.
To accommodate this, nums1 has a length of m + n, where the first m elements denote the elements that should be merged,
and the last n elements are set to 0 and should be ignored. nums2 has a length of n.



Example 1:

Input: nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3
Output: [1,2,2,3,5,6]
Explanation: The arrays we are merging are [1,2,3] and [2,5,6].
The result of the merge is [1,2,2,3,5,6] with the underlined elements coming from nums1.
Example 2:

Input: nums1 = [1], m = 1, nums2 = [], n = 0
Output: [1]
Explanation: The arrays we are merging are [1] and [].
The result of the merge is [1].
Example 3:

Input: nums1 = [0], m = 0, nums2 = [1], n = 1
Output: [1]
Explanation: The arrays we are merging are [] and [1].
The result of the merge is [1].
Note that because m = 0, there are no elements in nums1. The 0 is only there to ensure the merge result can fit in nums1.


Constraints:

nums1.length == m + n
nums2.length == n
0 <= m, n <= 200
1 <= m + n <= 200
-109 <= nums1[i], nums2[j] <= 109


Follow up: Can you come up with an algorithm that runs in O(m + n) time?
"""


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:

        if m == 0 and n == 1:
            nums1[m] = nums2[n - 1]
        elif m == n == 1:
            if nums1[m - 1] >= nums2[n - 1]:
                nums1[m - 1], nums1[m] = nums2[n - 1], nums1[m - 1]
            else:
                nums1[m] = nums2[n - 1]
        else:
            i = m - 1
            j = n - 1
            for index in range(m + n - 1, -1, -1):
                if i == -1 and j != -1:
                    nums1[index] = nums2[j]
                    j -= 1
                elif j == -1:
                    break
                elif i != -1:
                    if nums1[i] >= nums2[j]:
                        nums1[index] = nums1[i]
                        i -= 1
                    else:
                        nums1[index] = nums2[j]
                        j -= 1
                else:
                    nums1[index] = nums2[j]
                    j -= 1



"""
Основная мысль:
Списки отсортированы по возрастанию
Список nums1 имеет длину m + n (по условию задачи, все что зарезервировано под слияние со вторым списком заполнено 0)
В цикле двигаемся с конца списка (с индекса (m + n - 1) и сравниваем элементы списков nums1[: m], nums2.
Элементы для сравнения берутся с концов списков.

Исходя из условия, получается если элемент с конца списка №1 >= элемента с конца списка №2,
то он будет максимальным, следовательно перемещается в конец списка №1 по индексу m + n - 1.
Далее в работе этот индекс элемента не участвует 
"""

"""
Решение AbirBandyopadhyay
"""
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        while n > 0:
            if nums1[m - 1] >= nums2[n - 1] and m > 0:
                nums1[m + n - 1] = nums1[m - 1]
                m -= 1
            else:
                nums1[m + n - 1] = nums2[n - 1]
                n -= 1

"""
Решение Amirali Sharifzad
"""
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        a, b, write_index = m - 1, n - 1, m + n - 1
        while b >= 0:
            if a >= 0 and nums1[a] > nums2[b]:
                nums1[write_index] = nums1[a]
                a -= 1
            else:
                nums1[write_index] = nums2[b]
                b -= 1
            write_index -= 1