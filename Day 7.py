# def generate(numRows):
#     triangle = []
#     for i in range(numRows):
#         row = [1] * (i + 1)
#         for j in range(1, i):
#             row[j] = triangle[i-1][j-1] + triangle[i-1][j]
#         triangle.append(row)
#     return triangle
# numRows = int(input("Enter number of rows: "))
# result = generate(numRows)
# for row in result:
#     print(row)



# def getRow(rowIndex):
#     row = [1]
#     for i in range(rowIndex):
#         row = [1] + [row[j] + row[j+1] for j in range(len(row)-1)] + [1]
#     return row
# rowIndex = int(input("Enter row index: "))
# print(getRow(rowIndex))



# def romanToInt(s: str) -> int:
#     roman_map = {
#         'I': 1, 'V': 5, 'X': 10,
#         'L': 50, 'C': 100, 'D': 500, 'M': 1000
#     }
    
#     total = 0
#     for i in range(len(s)):
#         # If current value < next value, subtract
#         if i + 1 < len(s) and roman_map[s[i]] < roman_map[s[i + 1]]:
#             total -= roman_map[s[i]]
#         else:
#             total += roman_map[s[i]]
#     return total



# class Solution:
#     def maximumProduct(self, nums: list[int]) -> int:
#         nums.sort()
#         option1 = nums[-1] * nums[-2] * nums[-3]
#         option2 = nums[0] * nums[1] * nums[-1]
#         return max(option1, option2)
# if __name__ == "__main__":
#     sol = Solution()
#     test_cases = [
#         [1,2,3],
#         [1,2,3,4],
#         [-10,-10,5,2],
#         [-1,-2,-3,-4],
#         [0,0,2,3]
#     ]
#     for nums in test_cases:
#         print(f"{nums} -> {sol.maximumProduct(nums)}")



# def plusOne(digits):
#     return [int(x) for x in str(int("".join(map(str, digits))) + 1)]
# print(plusOne([9,9,9]))




# class Solution:
#     def removeDuplicates(self, nums: list[int]) -> int:
#         if not nums:
#             return 0
#         k = 1
#         for i in range(1, len(nums)):
#             if nums[i] != nums[i - 1]:
#                 nums[k] = nums[i]
#                 k += 1
#         return k
# if __name__ == "__main__":
#     sol = Solution()
#     test_cases = [
#         [1,1,2],
#         [0,0,1,1,1,2,2,3,3,4],
#         [1,2,3,4,5],
#         [1,1,1,1,1],
#         []
#     ]
#     for nums in test_cases:
#         k = sol.removeDuplicates(nums)
#         print(f"Input: {nums}")
#         print(f"Unique count: {k}, Array after removal: {nums[:k]}")
#         print("-" * 40)




# def detectCapitalUse(word: str) -> bool:
#     return word.isupper() or word.islower() or word.istitle()
# print(detectCapitalUse("USA"))       
# print(detectCapitalUse("leetcode"))  
# print(detectCapitalUse("Google"))     
# print(detectCapitalUse("FlaG"))