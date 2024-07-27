import time
from funcs import is_sorted, print_arr

n = [0, 1]

start = time.time()

while True:
  for i in range(len(n) - 1):
    if n[i] > n[i + 1]:
      temp = n[i + 1]
      n[i + 1] = n[1]
      n[i] = temp
    print_arr(n)

  if is_sorted(n):
    print(f"{len(n)}: {time.time() - start}")
    n.append(len(n))
    start = time.time()