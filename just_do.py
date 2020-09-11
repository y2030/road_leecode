def compare_version(v1, v2):
  """比较版本号大小"""
  idx = 0
  len1, len2 = len(v1), len(v2)
  if len1 > len2:
    v2.extend([0 for _ in range(len1-len2)])
  if len2 > len1:
    v1.extend([0 for _ in range(len2-len1)])
  while idx < len1:
    item1, item2 = str(v1[idx]), str(v2[idx])
    if item1.isdigit() and item2.isdigit():
      if v1[idx] > v2[idx]:
        return 1
      elif v1[idx] < v2[idx]:
        return -1
    else:
      items1 = [ord(i) for i in list(item1)]
      items2 = [ord(i) for i in list(item2)]
      res = compare_version(items1, items2)
      if res != 0: return res
    idx += 1
  return 0

v1 = "1.11.11a"
v2 = "1.11.11c"
# print(compare_version(v1.split("."), v2.split(".")))

def kill_man(n, m, start_idx):
  """ 约瑟夫问题， 未解决  有bug"""
  print(n, m)
  while len(n) > 1:
    print(len(n))
    for i in range(m):
      if i == m - 1:
        print("------------------")
        print(i)
        print(n)
        print("杀掉", n[start_idx])
        n.remove(n[start_idx])
        print(n)
        if start_idx >= len(n) - 1:
          start_idx = 0
      else:
        if start_idx >= len(n) - 1:
          start_idx = 0
        else:
          start_idx += 1
  return n[0]

count  = 10
n = [i for i in range(count)]
# print(kill_man(n, 17, 0))

def get_max_amount(stock_prices):
  """股票交易"""
  max_amount = 0
  for idx in range(0, len(stock_prices) - 1):
    for i in range(idx + 1, len(stock_prices)):
      if stock_prices[i] - stock_prices[idx] > max_amount:
        max_amount = stock_prices[i] - stock_prices[idx]
  return max_amount
print(get_max_amount([10, 7, 5, 8, 11, 9]))

def get_max_amount(stock_prices):
  """股票交易"""
  max_amount = 0
  max_prize = stock_prices[-1]
  for idx in range(len(stock_prices) - 2, -1, -1):
    if max_prize - stock_prices[idx] > max_amount:
      max_amount = max_prize - stock_prices[idx]
    if stock_prices[idx] > max_prize:
      max_prize = stock_prices[idx]
  return max_amount
print(get_max_amount([10, 7, 5, 8, 11, 9]))


class Solution70(object):
  def climbStairs(self, n):
    """
    70. 爬楼梯
    假设你正在爬楼梯。需要 n 阶你才能到达楼顶。
    每次你可以爬 1 或 2 个台阶。你有多少种不同的方法可以爬到楼顶呢？
    注意：给定 n 是一个正整数。
    """
    if n == 1: return 1
    if n == 2: return 2
    pre = 1
    cur = 2
    i = 3
    while i <= n:
      pre, cur = cur, pre + cur
      i += 1
    return cur

s70 = Solution70()
print(s70.climbStairs(4))