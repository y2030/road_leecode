# my_list = [2, 4, 1, 34, 98, 5, 10, 101]
# my_list = [1, 2, 3, 4, 5, 6, 7]
# my_list = [7, 6, 5, 4, 3, 2, 1]
# max_num = my_list[0]
# s_num = my_list[0]
# for n in my_list:
#   if max_num == s_num and max_num > n:
#     s_num = n
#   if n < max_num and n < s_num: continue
#   if s_num < n < max_num: sum = n
#   if max_num < n :
#     s_num, max_num = max_num, n
# print(max_num, s_num)



def find_jishu(arr):
  count = 0
  for i in arr:
    if i % 2 != 0: count += 1
  return count

print(find_jishu([1, 2, 3, 4, 5, 6, 7, 7, 7, 7]))

arr = [2, 5, 1, 3, 10, 5, 98, 9, 7 , 0]

def partition(arr, left_idx, right_idx):
  base_value = arr[right_idx]
  i = left_idx
  for idx in range(left_idx, right_idx):
    if arr[idx] < base_value:
      arr[i], arr[idx] = arr[idx], arr[i]
      i += 1
  arr[i], arr[right_idx] = arr[right_idx], arr[i]
  return i

def quick_sort(arr, left_idx, right_idx):
  if left_idx < right_idx:
    mid_idx = partition(arr, left_idx, right_idx)
    quick_sort(arr, left_idx, mid_idx - 1)
    quick_sort(arr, mid_idx + 1, right_idx)

# quick_sort(arr, 0, len(arr) - 1)
# print(arr)

def merge(left, right):
  merged_l = []
  left_idx, right_idx = 0, 0
  while left_idx < len(left) and right_idx < len(right):
    if left[left_idx] < right[right_idx]:
      merged_l.append(left[left_idx])
      left_idx += 1
    else:
      merged_l.append(right[right_idx])
      right_idx += 1
  if left_idx <= len(left):
    merged_l.extend(left[left_idx:])
  if left_idx <= len(right):
    merged_l.extend(right[right_idx:])
  return merged_l


def merge_sort(arr):
  length = len(arr)
  if length <= 1: return arr
  mid = length // 2
  left = merge_sort(arr[:mid])
  right = merge_sort(arr[mid:])
  merged_list = merge(left, right)
  return merged_list

# print(arr)
# print(merge_sort(arr))

def build_heap(arr, node_idx, max_idx):
  left_idx = node_idx * 2 + 1
  right_idx = node_idx * 2 + 2
  largest_idx = node_idx
  if right_idx <= max_idx and arr[right_idx] > arr[largest_idx]:
    largest_idx = right_idx
  if largest_idx != node_idx:
    arr[node_idx], arr[largest_idx] = arr[largest_idx], arr[node_idx]
    build_heap(arr, largest_idx, max_idx)

def heap_sort(arr):
  length = len(arr)
  for node_idx in range(length // 2 - 1, -1, -1):
    build_heap(arr, node_idx, length - 1)
  for max_idx in range(length - 1, 0, -1):
    arr[max_idx], arr[0] = arr[0], arr[max_idx]
    build_heap(arr, 0, max_idx - 1)

# heap_sort(arr)
# print(arr)


def sort_121(arr):
  cur_idx = 0
  for next_idx in range(1, len(arr)):
    if arr[cur_idx] > arr[next_idx]:
      cur_idx += 1
      break
    cur_idx += 1
  for i in range(cur_idx, len(arr)):
    j = i - 1
    while j >= 0:
      print(i, j)
      if arr[j + 1] < arr[j]:
        arr[j + 1], arr[j] = arr[j], arr[j + 1]
      j -= 1
# sort_121([1, 2, 3, 4, 5, 4, 3, 2, 1])


def compare_version(v1, v2):
  if len(v1) > len(v2):
    v2.extend(["0" for _ in range(len(v1) - len(v2))])
  if len(v2) > len(v1):
    v1.extend(["0" for _ in range(len(v2) - len(v1))])
  idx = 0
  print(v1, v2)
  while idx < len(v1):
    print(idx, len(v1), len(v2))

    if v1[idx].isdigit() and v2[idx].isdigit():
      if v1[idx] > v2[idx]:
        return 1
      elif v2[idx] > v1[idx]:
        return -1
    else:
      vv1 = [str(ord(i)) for i in list(v1[idx])]
      vv2 = [str(ord(i)) for i in list(v2[idx])]
      res = compare_version(vv1, vv2)
      if res != 0: return res
    idx += 1
  return 0

v1 = "1.11.11a"
v2 = "1.11.11b"
v1, v2 = v1.split("."), v2.split(".")
print(compare_version(v1, v2))
