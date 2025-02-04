import time
import random
import threading

proceed = input("This script will create a 1.37 GB file in the current directory. Type 'stop' to cancel: ")
if proceed.strip().lower() == "stop":
    exit()

start = time.perf_counter()
TARGET = 100_000_000

places = [
    ("Trondheim", 14.2),
    ("Oslo", 12.2),
    ("Bergen", 13.5),
    ("Stavanger", 15.0),
    ("Hardanger", 13.2),
    ("Kristiansand", 11.8),
    ("Fredrikstad", 12.3),
    ("Drammen", 13.4),
    ("Skien", 12.9)
]
places_len = len(places)

choice_cycle = 0
choices = [0,1,2,3,4]
random.shuffle(choices)

data = []
for i in range(TARGET):
    rng = (i + choices[choice_cycle]) % places_len
    name, avg = places[rng]
    data.append(f"{name};{(avg + random.uniform(-20, 15)):.1f}\n")

    if (i+1) % 20_000 == 0:
        print(f"Generating... {i+1:,}/{TARGET:,}", end="\r", flush=True)

print()
print("Concatenating and writing to file...")
with open("measurements.txt", "w") as f:
    f.write("".join(data))

print(f"Done in {time.perf_counter() - start:.2f} seconds")