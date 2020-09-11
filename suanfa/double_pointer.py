# https://github.com/CyC2018/CS-Notes/blob/master/notes/Leetcode%20%E9%A2%98%E8%A7%A3%20-%20%E5%8F%8C%E6%8C%87%E9%92%88.md

class Solution(object):
  """
  1. 有序数组的 Two Sum
  167. 两数之和 II - 输入有序数组 Two Sum II - Input array is sorted (Easy)
  给定一个已按照升序排列 的有序数组，找到两个数使得它们相加之和等于目标数。
  函数应该返回这两个下标值 index1 和 index2，其中 index1 必须小于 index2。
  说明:
  返回的下标值（index1 和 index2）不是从零开始的。
  你可以假设每个输入只对应唯一的答案，而且你不可以重复使用相同的元素。
  示例:
  输入: numbers = [2, 7, 11, 15], target = 9
  输出: [1,2]
  解释: 2 与 7 之和等于目标数 9 。因此 index1 = 1, index2 = 2 。
  """

  def twoSum(self, numbers, target):
    """
    :type numbers: List[int]
    :type target: int
    :rtype: List[int]
    """
    index1, index2 = 1, len(numbers)
    while index1 != index2:
      sum_two = numbers[index1 - 1] + numbers[index2 - 1]
      if sum_two == target:
        return [index1, index2]
      elif sum_two >= target:
        index2 -= 1
      elif sum_two <= target:
        index1 += 1
      continue
    return []


# sol = Solution()
# print(sol.twoSum([2, 7, 11, 15], 9))


class Solution2(object):
  """
  2. 两数平方和
  633.  平方数之和 Sum of Square Numbers (Easy)
  Input: 5
  Output: True
  Explanation: 1 * 1 + 2 * 2 = 5
  题目描述：判断一个非负整数是否为两个整数的平方和。给定一个非负整数 c ，你要判断是否存在两个整数 a 和 b，使得 a2 + b2 = c。
  可以看成是在元素为 0~target 的有序数组中查找两个数，使得这两个数的平方和为 target，
  如果能找到，则返回 true，表示 target 是两个整数的平方和。
  本题和 167. Two Sum II - Input array is sorted 类似，只有一个明显区别：一个是和为 target，一个是平方和为 target。
  本题同样可以使用双指针得到两个数，使其平方和为 target。
  本题的关键是右指针的初始化，实现剪枝，从而降低时间复杂度。
  设右指针为 x，左指针固定为 0，为了使 02 + x2 的值尽可能接近 target，我们可以将 x 取为 sqrt(target)。
  因为最多只需要遍历一次 0~sqrt(target)，所以时间复杂度为 O(sqrt(target))。又因为只使用了两个额外的变量，因此空间复杂度为 O(1)。
  """

  def judgeSquareSum(self, c):
    """
    :type c: int
    :rtype: bool
    """
    import math
    a, b = 0, int(math.sqrt(c))
    while a <= b:
      sqlt_sum = a * a + b * b
      if sqlt_sum == c:
        return True
      elif sqlt_sum >= c:
        b -= 1
      elif sqlt_sum <= c:
        a += 1
    return False


# sol2 = Solution2()
# print(sol2.judgeSquareSum(0))


class Solution3(object):
  """
  3. 反转字符串中的元音字母
  345. 反转字符串中的元音字母 Reverse Vowels of a String (Easy)
  编写一个函数，以字符串作为输入，反转该字符串中的元音字母。
  Given s = "leetcode", return "leotcede"
  使用双指针，一个指针从头向尾遍历，一个指针从尾到头遍历，当两个指针都遍历到元音字符时，交换这两个元音字符。
  为了快速判断一个字符是不是元音字符，我们将全部元音字符添加到集合 HashSet 中，从而以 O(1) 的时间复杂度进行该操作。
  时间复杂度为 O(N)：只需要遍历所有元素一次
  空间复杂度 O(1)：只需要使用两个额外变量
  """

  def reverseVowels(self, s):
    """
    :type s: str
    :rtype: str
    """
    vowels = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}
    list_s = list(s)
    left_index, right_index = 0, len(s) - 1
    while left_index < right_index:
      left_s, right_s = list_s[left_index], list_s[right_index]
      if list_s[left_index] in vowels and list_s[right_index] in vowels:
        list_s[left_index], list_s[right_index] = right_s, left_s
        left_index += 1
        right_index -= 1
        continue
      if left_s not in vowels:
        left_index += 1
      if right_s not in vowels:
        right_index -= 1
    return "".join(list_s)


# sol3 = Solution3()
# print(sol3.reverseVowels("leotcede"))


class Solution4(object):
  """
  4. 回文字符串
  680. 验证回文字符串 Ⅱ Valid Palindrome II (Easy)
  给定一个非空字符串 s，最多删除一个字符。判断是否能成为回文字符串。
  题目描述：可以删除一个字符，判断是否能构成回文字符串。
  所谓的回文字符串，是指具有左右对称特点的字符串，例如 "abcba" 就是一个回文字符串。
  使用双指针可以很容易判断一个字符串是否是回文字符串：令一个指针从左到右遍历，一个指针从右到左遍历，这两个指针同时移动一个位置，每次都判断两个指针指向的字符是否相同，如果都相同，字符串才是具有左右对称性质的回文字符串。
  示例 1:
  输入: "aba"
  输出: True
  本题的关键是处理删除一个字符。在使用双指针遍历字符串时，如果出现两个指针指向的字符不相等的情况，
  我们就试着删除一个字符，再判断删除完之后的字符串是否是回文字符串。
  在判断是否为回文字符串时，我们不需要判断整个字符串，因为左指针左边和右指针右边的字符之前已经判断过具有对称性质，
  所以只需要判断中间的子字符串即可。
  在试着删除字符时，我们既可以删除左指针指向的字符，也可以删除右指针指向的字符。
  """

  def validPalindrome(self, s):
    """
    :type s: str
    :rtype: bool
    """
    if s == s[::-1]:
      return True
    left_idx, right_idx = 0, len(s) - 1
    while left_idx < right_idx:
      if s[left_idx] != s[right_idx]:
        del_left = s[:left_idx] + s[left_idx + 1:]
        del_right = s[:right_idx] + s[right_idx + 1:]
        # del_left = s[left_idx + 1: right_idx + 1]
        # del_right = s[left_idx: right_idx]
        return del_left == del_left[::-1] or del_right == del_right[::-1]
      left_idx += 1
      right_idx -= 1
    return True


# sol4 = Solution4()
# print(sol4.validPalindrome("abcdbza"))


class Solution5(object):
  """
  5. 归并两个有序数组
  88. 合并两个有序数组 Merge Sorted Array (Easy)
  Input:
  nums1 = [1,2,3,0,0,0], m = 3
  nums2 = [2,5,6],       n = 3
  Output: [1,2,2,3,5,6]
  题目描述：把归并结果存到第一个数组上。
  需要从尾开始遍历，否则在 nums1 上归并得到的值会覆盖还未进行归并比较的值。
  给你两个有序整数数组 nums1 和 nums2，请你将 nums2 合并到 nums1 中，使 nums1 成为一个有序数组。
  说明:
  初始化 nums1 和 nums2 的元素数量分别为 m 和 n 。
  你可以假设 nums1 有足够的空间（空间大小大于或等于 m + n）来保存 nums2 中的元素。
  """

  def merge(self, nums1, m, nums2, n):
    """
    :type nums1: List[int]
    :type m: int
    :type nums2: List[int]
    :type n: int
    :rtype: None Do not return anything, modify nums1 in-place instead.
    """
    idx1 = m - 1
    idx2 = n - 1
    total_idx = m + n - 1
    if m == 0: return nums2
    while idx1 >= 0 and idx2 >= 0:
      if nums1[idx1] <= nums2[idx2]:
        nums1[total_idx] = nums2[idx2]
        idx2 -= 1
      else:
        nums1[total_idx] = nums1[idx1]
        idx1 -= 1
      total_idx -= 1
    nums1[:idx2 + 1] = nums2[: idx2 + 1]
    return nums1


# sol5 = Solution5()
# print(sol5.merge([1, 2, 3, 0, 0, 0], 3, [2, 5, 6], 3))
# print(sol5.merge([1], 1, [], 0))
# print(sol5.merge([0], 0, [1], 1))


class Solution6(object):
  """
  6. 判断链表是否存在环
  141. 环形链表 Linked List Cycle (Easy)
  使用双指针，一个指针每次移动一个节点，一个指针每次移动两个节点，如果存在环，那么这两个指针一定会相遇。
  给定一个链表，判断链表中是否有环。
  为了表示给定链表中的环，我们使用整数 pos 来表示链表尾连接到链表中的位置（索引从 0 开始）。
  如果 pos 是 -1，则在该链表中没有环。
  进阶：
  你能用 O(1)（即，常量）内存解决此问题吗？
 
  """

  def hasCycle(self, head):
    """
    :type head: ListNode
    :rtype: bool
    """
    fast, slow = head, head
    while fast and fast.next:
      fast, slow = fast.next.next, slow.next
      if fast == slow:
        return True
      return False


# sol6 = Solution6()
# print(sol6.hasCycle([3, 2, 0, -4], 1))


class Solution7(object):
  """
  7. 最长子序列
  524. 通过删除字母匹配到字典里最长单词 Longest Word in Dictionary through Deleting (Medium)
  Leetcode / 力扣
  Input:
  s = "abpcplea", d = ["ale","apple","monkey","plea"]
  Output:
  "apple"
  题目描述：删除 s 中的一些字符，使得它构成字符串列表 d 中的一个字符串，找出能构成的最长字符串。
  如果有多个相同长度的结果，返回字典序的最小字符串。
  通过删除字符串 s 中的一个字符能得到字符串 t，可以认为 t 是 s 的子序列，
  我们可以使用双指针来判断一个字符串是否为另一个字符串的子序列。

  给定一个字符串和一个字符串字典，找到字典里面最长的字符串，该字符串可以通过删除给定字符串的某些字符来得到。
  如果答案不止一个，返回长度最长且字典顺序最小的字符串。如果答案不存在，则返回空字符串。
  说明:
  所有输入的字符串只包含小写字母。
  字典的大小不会超过 1000。
  所有输入的字符串长度不会超过 1000。
  """

  def findLongestWord(self, s, d):
    """
    :type s: str
    :type d: List[str]
    :rtype: str
    """
    d.sort(key=lambda x: [-len(x), x])
    for word in d:
      s_idx, word_idx = 0, 0
      while s_idx < len(s) and word_idx < len(word):
        if s[s_idx] == word[word_idx]:
          s_idx += 1
          word_idx += 1
        else:
          s_idx += 1
      if len(word) == word_idx:
        return word
    return ""


# sol7 = Solution7()
# print(sol7.findLongestWord(s="abpcplea", d=["ale", "apple", "monkey", "plea"]))

