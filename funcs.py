from os import system

def is_sorted(arr):
  for i in range(len(arr) - 1):
    if arr[i] > arr[i + 1]:
      return False
  return True

def print_arr(arr):
  system('clear')
  for num in arr:
    print("_" * num)
  print()