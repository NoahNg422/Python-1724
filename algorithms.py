import math


def binary_search(target, arr, count=0):  # O(lg n) very good!
  if target in arr:
    while len(arr) > 1:
      count += 1
      mid = len(arr) // 2
      # print(arr)
      if target == arr[mid]:
        return f'{target} found after {count} iteration(s).'
      elif target > arr[mid]:
        arr = arr[mid:]
      else:
        arr = arr[:mid]
  return f'{target} not found!'


def binary_recursive(target, arr, mid, count=0):  # O(lg n) very good!
  # print(arr)
  if arr[mid] == target:
    count += 1
    return f'{target} found after {count} recursive call(s).'
  elif target not in arr:
    return f'{target} not found!'
  if target > arr[mid]:
    return binary_recursive(target, arr[mid:], mid//2, count+1)
  elif target < arr[mid]:
    return binary_recursive(target, arr[:mid], mid//2, count+1)


def complete(graph):  # O(n**2) bad.
  for edges in graph:
    point = graph[edges]
    for j in point:
      print(j)
  return j not in point and edges not in point


def CompleteConstant(graph):  # O(1) excellent!
  n = len(graph)
  return graph == (n(n+1) / 2)


def exponent(coe, n):  # O(lg n) very good!
  if n == 0:
    return 1
  elif n % 2 == 0:
    exponent(coe, n//2) ** 2
  else:
    coe * exponent(coe, n-1 // 2) ** 2


def factorial(index):  # O(n) OK
  answer = index
  if index <= 0:
    return 1
  while index > 1:
    index -= 1
    answer *= index
  return answer


def find_gcd(left, right) -> float:  # O(lg n) very good!
  assert left >= 0 and right >= 0
  while right != 0:
    remainder = left % right
    left = right
    right = remainder
  return left


def is_prime(number):  # O(sqrt(n)) good
  for i in range(2, int(math.sqrt(number))):
    # print(number % i)
    if number % i == 0:
      return False
  return True


def prime_sieve(num):  # O(n**2) bad
  arr = []
  out = []
  for n in range(2, num+1):
    arr.append(n)
  for p in range(1, int(math.sqrt(num))):
    p += 1
    if p > 0:
      j = p**2
      while j <= num:
        if arr[j-2] > 0:
          arr[j-2] = 0
        j += p
  for q in range(len(arr)):
    if arr[q] != 0:
      out.append(arr[q])
  print(out)


def br_force_match(sub, string):  # O(m*n) not good
  for i in range(len(string)-len(sub)):
    j = 0
    while j < len(sub) and sub[j] == string[i+j]:
      j += 1
    if j == len(sub):
      return f'"{sub}" is within "{string}" at position {i+1}.'
  return f'"{sub}" is not in "{string}".'
  

def towers(size, start, end, extra):  # O(2**n) very bad!
  if size == 1:
    movedisknfromstarttoend = None
  else:
    towers(size-1, start, extra, end)
    movedisknfromstarttoend
    towers(size-1, extra, end, start)


def substring_begin_end(string, a, b, count=[]):  # O(n**2) bad
  for i in range(len(string)):
    j = len(string)
    while j > i+1:
      sub = string[i:j]
      j -= 1
      if sub[0] == a and sub[-1] == b:
        count.append(sub)
        # print(sub)
  return count


def coin_row(arr):  # O(n) OK
  pick = []
  pick.append(arr[0])
  for i in range(1, len(arr)-1):
    pick.append(max(arr[i] + pick[i-2], pick[i-1]))
  return pick[len(arr)-2]


# The best of algorithms part 1: sorting!


def selection(arr, steps=0):  # O(n**2) bad
  for i in range(len(arr)):
    min = i
    for j in range(i+1, len(arr)):
      if arr[j] < arr[min]:
        min = j
      steps += 1
    arr[i], arr[min] = arr[min], arr[i]
    # print(steps)
  return arr


def bubble(arr, steps=0):  # O(n**2) bad
  for i in range(len(arr) - 1):
    for j in range(len(arr) - 1 - i):
      if arr[j+1] < arr[j]:
        arr[j+1], arr[j] = arr[j], arr[j+1]
      steps += 1
    # print(steps)
  return arr


def mystery_sort(arr, out=[]):
  highest = arr[0]
  for i in range(1, len(arr)-1):
    if arr[i] > highest:
      highest = arr[i]
  for j in range(highest+1):
    if j in arr:
      out.append(j)
  return out


def insertion(arr):  # O(n**2) bad
  for i in range(1, len(arr)):
    n = arr[i]
    j = i - 1
    while j >= 0 and arr[j] > n:
      arr[j+1], arr[j] = arr[j], arr[j+1]
      j -= 1
  return arr


def merge(arr2, arr3, arr1):
  i, j, k, = 0, 0, 0
  s1, s2 = len(arr2), len(arr3)
  while i < s1 and j < s2:
    if arr2[i] <= arr3[j]:
      arr1[k] = arr2[i]
      i += 1
    else:
      arr1[k] = arr3[j]
      j += 1
    k += 1
  if i == s1:
    arr1[k:s1+s2] = arr3[j:s2]
  else:
    arr1[k:s1+s2] = arr2[i:s1]


def mergesort(arr):
  n = len(arr)
  if n > 1:
    arr2 = arr[:n//2]
    arr3 = arr[n//2:]
    mergesort(arr2[:n//2])
    mergesort(arr3[:n//2])
    merge(arr2, arr3, arr)


def split_array(arr):
  left = 0
  right = len(arr) - 1
  partition = arr[left]
  i = left
  j = right
  while i < j:
    if arr[i] < partition:
      i += 1
    if arr[j] > partition:
      j -= 1
    arr[i], arr[j] = arr[j], arr[i]
  arr[i], arr[j] = arr[j], arr[i]
  arr[left], arr[i] = arr[i], arr[left]
  return j


def quicksort(arr):
  left, right = 0, len(arr)-1
  if left < right:
    split = split_array(arr[left:right])
    quicksort(arr[left:split-1])
    quicksort(arr[split+1:right])
  

def heapsort(arr):
  if len(arr) == 1:
    return arr


def countsort(arr, min, max, dist=[], final=[]):
  assert max > min
  for j in range(max - min):
    dist.append(0)
  for i in range(len(arr) - 1):
    dist.append(dist[arr[i] - min] + 1)
  for k in range(1, max - min):
    dist[k] = dist[k-1] + dist[k]
  o = len(arr) - 1
  while o > 0:
    o -= 1
    n = arr[o] - min
    final.append(arr[o])
    dist[n] = dist[n] - 1
  return final


def main():  # O(n**2) based on max string-function
  numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32]

  print(f'From the list {numbers}: ')
  print(f'{binary_search(12, numbers)}')
  print(f'{binary_recursive(12, numbers, len(numbers)//2)}\n')

  top = 10
  print(f'{top}! == {factorial(top)}\n')

  n1, n2 = 80, 32
  print(f'Greatest common divisor of {[n1, n2]}: {find_gcd(n1, n2)}')

  lcm = n1 * n2 // find_gcd(n1, n2)
  print(f'Least common multiple of {[n1, n2]} is {lcm} \n')

  number = 2147483647

  print(f'is {number} prime? {is_prime(number)}\n')

  prime_sieve(100)

  print(f'\n{br_force_match("b", "youtube")}')

  print(f"\nWhat substrings begin with a and end with b? {substring_begin_end('cabbage is a vegetable', 'a', 'b')}\n")

  unsorted = [11, 5, 12, 3, 7, 1, 10, 9, 6, 4, 8, 2]

  print(f'How many coins? {coin_row(unsorted)}')

  sort = 'selectio'
  
  revers = [12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
  near_sorted = [1, 2, 3, 4, 9, 5, 6, 7, 8, 10, 12, 11]

  if sort == 'selection':
    print(f'\nUnsorted list:               {unsorted}')
    print(f'Reversed list:               {revers}')
    print(f'Almost sorted list:          {near_sorted}')
    print(f'\nSelection sorting algorithm: {selection(unsorted)}')
    print(f'Sorting reversed:            {selection(revers)}')
    print(f'After sorting:               {selection(near_sorted)}')
  elif sort == 'bubble':
    print(f'\nUnsorted list:            {unsorted}')
    print(f'Reversed list:            {revers}')
    print(f'Almost sorted list:       {near_sorted}')
    print(f'\nBubble sorting algorithm: {bubble(unsorted)}')
    print(f'Sorting reversed:         {bubble(revers)}')
    print(f'After sorting:            {bubble(near_sorted)}')
  elif sort == 'insertion':
    print(f'\nUnsorted list:               {unsorted}')
    print(f'Reversed list:               {revers}')
    print(f'Almost sorted list:          {near_sorted}')
    print(f'\nInsertion sorting algorithm: {insertion(unsorted)}')
    print(f'Sorting reversed:            {insertion(revers)}')
    print(f'After sorting:               {insertion(near_sorted)}')
  else: 
    print(f'\nUnsorted list:             {unsorted}')
    mergesort(unsorted)
    print(f'Merge sort: {unsorted}')
    quicksort(revers)
    print(f'Quick sort algorithm: {revers}')


main()
