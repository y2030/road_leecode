import heapq, random, time

numbers = [5, 7, 3, 7, 2, 43, 90, 1, 5, 0, 10, 934, 52]

def get_number():
  yield random.randint(-1000, 9000)

class SortFun(object):
  """常见排序算法"""
  """ [5, 7, 3, 6, 7, 43, 90, 1]"""

  def __init__(self, numbers):
    self.numbers = numbers

  def get_time(func):
    def inner(self, *args, **kwargs):
      t1 = time.time()
      res = func(self, *args, **kwargs)
      t2 = time.time()
      print(t2 - t1)
      return res

    return inner
    # 在类里定义一个装饰器

  @get_time
  def bubble_sort(self):
    """冒泡排序 O(n^2) , O(1)"""
    numbers = self.numbers
    length = len(self.numbers)
    for i in range(length - 1):
      for idx in range(length - i - 1):
        if numbers[idx] > numbers[idx + 1]:
          numbers[idx], numbers[idx + 1] = numbers[idx + 1], numbers[idx]
    return numbers

  @get_time
  def select_sort(self):
    """选择排序 O(n^2) , O(1)"""
    numbers = self.numbers
    length = len(numbers)
    for idx in range(length - 1):
      for j in range(idx + 1, length):
        if numbers[j] < numbers[idx]:
          numbers[idx], numbers[j] = numbers[j], numbers[idx]
    return numbers

  @get_time
  def insert_sort(self):
    """插入排序 O(n^2) , O(1)"""
    numbers = self.numbers
    for i in range(1, len(numbers)):
      j = i - 1
      value = numbers[i]
      while j >= 0:
        if numbers[j] > value:
          numbers[j + 1], numbers[j] = numbers[j], value
        j -= 1
    return numbers

  def shell_sort(self):
    """希尔排序 """
    return []

  @get_time
  def quick_sort(self):
    """快速排序 时间复杂度 nlogn, 共有log(n) 层, 每一层的操作都是n"""

    def partition(arr, left, right):
      key = arr[right]
      i = left
      for idx in range(left, right):
        if arr[idx] <= key:
          arr[i], arr[idx] = arr[idx], arr[i]
          i += 1
      arr[i], arr[right] = arr[right], arr[i]
      return i

    def q_sort(arr, left, right):
      if left < right:
        mid = partition(arr, left, right)
        q_sort(arr, left, mid - 1)
        q_sort(arr, mid + 1, right)

    numbers = self.numbers
    q_sort(numbers, 0, len(numbers) - 1)
    return numbers

  @get_time
  def merge_sort(self):
    """归并排序 时间复杂度 nlogn, 共有log(n) 层, 每一层的操作都是n"""

    def merge(left_n, right_n):
      merged_list = []
      left_idx, right_idx = 0, 0
      while left_idx < len(left_n) and right_idx < len(right_n):
        if left_n[left_idx] < right_n[right_idx]:
          merged_list.append(left_n[left_idx])
          left_idx += 1
        else:
          merged_list.append(right_n[right_idx])
          right_idx += 1
      if left_idx < len(left_n):
        merged_list.extend(left_n[left_idx:])
      if right_idx < len(right_n):
        merged_list.extend(right_n[right_idx:])
      return merged_list

    def m_sort(numbers):
      if len(numbers) <= 1: return numbers
      mid = len(numbers) // 2
      left_n = m_sort(numbers[:mid])
      right_n = m_sort(numbers[mid:])
      return merge(left_n, right_n)

    return m_sort(self.numbers)

  @get_time
  def heap_sort(self):
    def build_heap(arr, max_idx, node_idx):
      largest_idx = node_idx
      left_idx, right_idx = node_idx * 2 + 1, node_idx * 2 + 2
      if left_idx < max_idx and arr[left_idx] > arr[largest_idx]:
        largest_idx = left_idx
      if right_idx < max_idx and arr[right_idx] > arr[largest_idx]:
        largest_idx = right_idx
      if largest_idx != node_idx:
        arr[node_idx], arr[largest_idx] = arr[largest_idx], arr[
          node_idx]
        build_heap(arr, max_idx, largest_idx)

    def h_sort(numbers):
      length = len(numbers)
      for node_idx in range(length // 2 - 1, -1, -1):
        build_heap(numbers, length, node_idx)
      for max_idx in range(length - 1, 0, -1):
        numbers[max_idx], numbers[0] = numbers[0], numbers[max_idx]
        build_heap(numbers, max_idx, 0)
      return numbers

    return h_sort(self.numbers)


sort_func = SortFun(numbers=numbers)
# print(sort_func.bubble_sort())
# print(sort_func.select_sort())
# print(sort_func.insert_sort())
# print(sort_func.quick_sort())
# print(sort_func.merge_sort())
# print(sort_func.heap_sort())

def partition(arr, left, right):
  key = arr[right]
  min_idx = left
  for idx in range(left, right):
    if arr[idx] <= key:
      arr[idx], arr[min_idx] = arr[min_idx], arr[idx]
      min_idx += 1
  arr[min_idx], arr[right] = arr[right], arr[min_idx]
  return min_idx

def quick_sort(arr, left, right):
  if left < right:
    mid = partition(arr, left, right)
    quick_sort(arr, left, mid - 1)
    quick_sort(arr, mid + 1, right)
  return arr

length = len(numbers)
# print(quick_sort(numbers, 0, length - 1))


def merge(arr1, arr2):
  idx1, idx2 = 0, 0
  merged_arr = []
  while idx1 <= len(arr1) and idx2 <= len(arr2):
    if arr1[idx1] < arr2[idx2]:
      merged_arr.append(arr1[idx1])
      idx1 += 1
    else:
      merged_arr.append(arr2[idx2])
      idx2 += 1
  if idx1 < len(arr1):
    merged_arr.extend(arr1[idx1:])
  if idx2 < len(arr2):
    merged_arr.extend(arr2[idx2:])

def merge_sort(numbers):
  if len(numbers) <= 1: return numbers
  length = len(numbers)
  mid = length // 2
  merge_sort(numbers[:mid])
  merge_sort(numbers[mid + 1:])
  return numbers

# print(merge_sort(numbers))

def build_heap(arr, max_idx, node_idx):
  left_idx = 2 * node_idx + 1
  right_idx = 2 * node_idx + 2
  largest_idx = node_idx
  if left_idx <= max_idx and arr[left_idx] > arr[largest_idx]:  # 注意不要在上面一起判断
    largest_idx = left_idx
  if right_idx <= max_idx and arr[right_idx] > arr[largest_idx]: # 注意为largest_idx
    largest_idx = right_idx
  if largest_idx != node_idx:
    arr[node_idx], arr[largest_idx] = arr[largest_idx], arr[node_idx]
    build_heap(arr, max_idx, largest_idx)

def heap_sort(arr):
  length = len(arr)
  for no_leaf_idx in range(length // 2 - 1, -1, -1):
    build_heap(arr, length - 1, no_leaf_idx)
  for max_idx in range(length - 1, 0, -1):
    arr[max_idx], arr[0] = arr[0], arr[max_idx]
    build_heap(arr, max_idx - 1, 0)   # 注意 -1
  return arr

print(heap_sort(numbers))


class Solution215(object):
  """
  1. Kth Element  堆
  215. Kth Largest Element in an Array (Medium)
  在未排序的数组中找到第 k 个最大的元素。请注意，你需要找的是数组排序后的第 k 个最大的元素，而不是第 k 个不同的元素。
  示例 1:
  Input: [3,2,1,5,6,4] and k = 2
  Output: 5
  示例 2:
  Input: [3,2,3,1,2,4,5,5,6] 和 k = 4
  Output: 4
  说明:你可以假设 k 总是有效的，且 1 ≤ k ≤ 数组的长度。
  题目描述：找到倒数第 k 个的元素。
  """

  def findKthLargest(self, nums, k):
    """
    :type nums: List[int]
    :type k: int
    :rtype: int
    """
    nums.sort(reverse=True)
    return nums[k - 1]

  def findKthLargest1(self, nums, k):
    """
    :type nums: List[int]
    :type k: int
    :rtype: int
    """
    return heapq.nlargest(k, nums)[-1]
  def findKthLargest2(self, nums, k):
    """
    使用最小堆实现
    """

    def build_heap(arr, max_idx, node_idx):
      left_idx = 2 * node_idx + 1
      right_idx = 2 * node_idx + 2
      small_idx = node_idx
      if left_idx <= max_idx and arr[left_idx] < arr[small_idx]:
        small_idx = left_idx
      if right_idx <= max_idx and arr[right_idx] < arr[
        small_idx]:  # 注意为largest_idx
        small_idx = right_idx
      if small_idx != node_idx:
        arr[node_idx], arr[small_idx] = arr[small_idx], arr[node_idx]
        build_heap(arr, max_idx, small_idx)

    def heap_sort(arr):
      length = len(arr)
      for no_leaf_idx in range(length // 2 - 1, -1, -1):
        build_heap(arr, length - 1, no_leaf_idx)
      for max_idx in range(length - 1, 0, -1):
        arr[max_idx], arr[0] = arr[0], arr[max_idx]
        build_heap(arr, max_idx - 1, 0)  # 注意 -1
      print(arr)
      return arr

    return heap_sort(nums)[k - 1]


# sol215 = Solution215()
# print(sol215.findKthLargest2(nums=[3, 2, 3, 1, 2, 4, 5, 5, 6], k=4))



class Solution347(object):
  """
  1. 出现频率最多的 k 个元素  桶排序
  347. Top K Frequent Elements (Medium)
  给定一个非空的整数数组，返回其中出现频率前 k 高的元素。
  输入: nums = [1,1,1,2,2,3], k = 2
  输出: [1,2]
  输入: nums = [1], k = 1
  输出: [1]
  提示：
  你可以假设给定的 k 总是合理的，且 1 ≤ k ≤ 数组中不相同的元素的个数。
  你的算法的时间复杂度必须优于 O(n log n) , n 是数组的大小。
  题目数据保证答案唯一，换句话说，数组中前 k 个高频元素的集合是唯一的。
  你可以按任意顺序返回答案。
  """

  def topKFrequent(self, nums, k):
    """
    :type nums: List[int]
    :type k: int
    :rtype: int
    """
    d = {}
    for num in nums:
      if num not in d:
        d[num] = 0
      d[num] += 1
    return sorted(d.keys(), key=lambda x: d[x], reverse=True)[:k]


# sol347 = Solution347()
# print(sol347.topKFrequent(nums=[1, 1, 1, 2, 2, 3], k=2))


class Solution75(object):
  """
  1. 按颜色进行排序
  75. Sort Colors (Medium)
  Input: [2,0,2,1,1,0]
  Output: [0,0,1,1,2,2]
  给定一个包含红色、白色和蓝色，一共 n 个元素的数组，原地对它们进行排序，使得相同颜色的元素相邻，并按照红色、白色、蓝色顺序排列。
  此题中，我们使用整数 0、 1 和 2 分别表示红色、白色和蓝色。
  注意:
  不能使用代码库中的排序函数来解决这道题。
  进阶：
  一个直观的解决方案是使用计数排序的两趟扫描算法。
  首先，迭代计算出0、1 和 2 元素的个数，然后按照0、1、2的排序，重写当前数组。
  你能想出一个仅使用常数空间的一趟扫描算法吗？
  """

  def sortColors(self, nums):
    """
    :type nums: List[int]
    :rtype: None Do not return anything, modify nums in-place instead
    """


# sol75 = Solution75()
# print(sol75.topKFrequent(s="tree"))


class Fib:
  def __init__(self, n):
    self.current = 0
    self.next = 1
    self.n = n

  def __iter__(self):
    return self

  def __next__(self):
    if self.n >= 0:
      fib = self.current
      self.current, self.next = self.next, self.current + self.next
      self.n -= 1
      return fib
    else:
      raise StopIteration()


# fibs = Fib(10)
# print([i for i in fibs])

def fibs(n):
  curr_fib, next_fib = 0, 1
  while n >= 0:
    fib = curr_fib
    yield fib
    curr_fib, next_fib = next_fib, curr_fib + next_fib
    n -= 1
# print([f for f in fibs(10)])




