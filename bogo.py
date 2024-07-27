import random
import time
from funcs import is_sorted, print_arr

n = [0, 1]

start = time.time()

while True:
  random.shuffle(n)
  print_arr(n)
  if is_sorted(n):
    print(f"{len(n)}: {time.time() - start}")
    n.append(len(n))
    start = time.time()