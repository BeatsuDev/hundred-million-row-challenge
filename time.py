import time
import os
import sys

start = time.perf_counter()
os.system(" ".join(sys.argv[1:]))
end = time.perf_counter()

print()
print("Time taken: {:.4f} seconds".format(end - start))