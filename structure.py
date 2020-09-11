class SingleNode(object):
  """单链表的结点"""

  def __init__(self, item):
    # item存放数据元素
    self.item = item
    # next是下一个节点的标识
    self.next = None


class SingleLinkList(object):
  """单链表"""

  def __init__(self):
    self._head = None
    self.cur_node = self._head

  def is_empty(self):
    """判断链表是否为空"""
    return self._head is None

  def length(self):
    """链表长度"""
    count = 0
    cur_node = self._head
    while cur_node:
      count += 1
      cur_node = cur_node.next
    return count

  def __iter__(self):
    return self

  def __next__(self):
    if self._head is None:
      StopIteration()
      if not self.cur_node:
        self.cur_node = self._head
      print(self.cur_node, self.cur_node.item, self.cur_node.next.item)
      item, self.cur_node = self.cur_node.item, self.cur_node.next
      print(item)
      return item

  def travel(self):
    """遍历链表"""
    pass

  def get_iter(self):
    cur_node = self._head
    while cur_node:
      yield cur_node.item
      cur_node = cur_node.next

  # 头部添加元素
  def add(self, item):
    """头部添加元素"""
    node = SingleNode(item)
    self._head, node.next = node, self._head

  # 尾部添加元素
  def append(self, item):
    """尾部添加元素"""
    # 先判断链表是否为空，若是空链表，则将_head指向新节点
    # 若不为空，则找到尾部，将尾节点的next指向新节点
    node = SingleNode(item)
    if self.is_empty():
      self._head = node
    else:
      cur_node = self._head
      while cur_node.next:
        cur_node = cur_node.next
      cur_node.next = node

  # 指定位置添加元素
  def insert(self, pos, item):
    """指定位置添加元素"""
    if pos == 0:
      self.add(item)
    elif pos >= self.length():
      self.append(item)
    else:
      node = SingleNode(item)
      pre_node = self._head
      idx = 1
      while idx <= pos:
        pre_node = pre_node.next
        idx += 1
      pre_node.next, node.next = node, pre_node.next

  # 删除节点
  def remove(self, item):
    """删除节点"""
    # node = SingleNode(item)
    # pre_node = self._head
    # cur_node = pre_node.next
    # while cur_node.item == item or cur_node.next is None:
    #   pre_node.next, node.next = node, cur_node.next

    cur_node = self._head
    pre_node = None
    while cur_node.next is not None:
      if cur_node.item == item:
        if pre_node is None:
          self._head = None
        else:
          pre_node.next = cur_node.next
        break
      else:
        pre_node, cur_node = cur_node, cur_node.next

  def search(self, item):
    """链表查找节点是否存在，并返回True或者False"""
    cur_node = self._head
    while cur_node.next is not None:
      if cur_node.item == item: return True
      cur_node = cur_node.next
    return False


# s_list = SingleLinkList()
# print(s_list.is_empty())
# print(s_list.length())
# s_list.add(1)
# s_list.add(8)
# s_list.add(2)
# s_list.add(10)
# print(s_list.is_empty())
# print(s_list.length())
# git = s_list.get_iter()
# print([i for i in git])
# print("-------")
# # print([i for i in s_list])
# s_list.append(1000)
# s_list.append(999)
# s_list.append(888)
# print(s_list.length())
# git = s_list.get_iter()
# print([i for i in git])
#
# s_list.insert(3, 666)
# s_list.insert(3, 777)
# git = s_list.get_iter()
# print([i for i in git])
#
# s_list.remove(1000)
# git = s_list.get_iter()
# print([i for i in git])
#
# print(s_list.search(777))

class SingleNodee(object):
  def __init__(self, item):
    self.item = item
    self.next = None

class JosephNode(object):
  def __init__(self):
    self._head = None

  def is_null(self):
    return self._head is None

  def head(self):
    return self._head

  def length(self):
    count = 0
    if self.is_null():
      return count
    cur_node = self._head
    while cur_node.next != self._head:
      count += 1
      cur_node = cur_node.next
    return count

  def add(self, item):
    node = SingleNode(item)
    if self.is_null():
      self._head = node
      node.next = self._head
    else:
      cur_node = self._head
      while cur_node.next != self._head:
        cur_node = cur_node.next
      cur_node.next, node.next = node, self._head

  def remove(self, item):
    if self.is_null(): return
    if self.length() == 1 and self._head.item == item:
      self._head = None
    cur_node = self._head
    pre_node = None
    while cur_node.next != self._head:
      if cur_node.item == item:
        if pre_node == None:
          self._head = cur_node.next
        else:
          pre_node.next = cur_node.next
          break
      else:
        pre_node, cur_node = cur_node, cur_node.next
    if cur_node.item == item and pre_node != None:
      pre_node.next = cur_node.next


def get_joseph(n, m):
  joseph_node = JosephNode()
  for i in range(1, n + 1):
    joseph_node.add(i)

  while joseph_node.length() > 1:
    print(joseph_node.length())
    cur_node = joseph_node.head()
    for i in range(1, m + 1):
      next_node = cur_node.next
      if i == m:
        print("删除", cur_node.item)
        joseph_node.remove(cur_node.item)
      cur_node = next_node
  return joseph_node.head().item

# print("---------------------------------")
# n = 10
# m = 7
# print(get_joseph(n, m))


# joseph_node = JosephNode()
# for i in range(1, n + 2):
#   joseph_node.add(i)
# print(joseph_node.length())
# joseph_node.remove(4)
# print(joseph_node.length())
#
#



