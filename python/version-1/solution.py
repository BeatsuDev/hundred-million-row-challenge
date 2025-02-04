import sys
from collections import defaultdict


filename = sys.argv[1]

aggregates = defaultdict(lambda: {"min": float('inf'), "max": float('-inf'), "sum": 0, "count": 0})

with open(filename, 'r') as f:
    print("Reading file...")
    for i, line in enumerate(f):
        place, measurement = line.strip().split(";")
        measurement = float(measurement)

        if measurement < aggregates[place]["min"]:
            aggregates[place]["min"] = measurement
        if measurement > aggregates[place]["max"]:
            aggregates[place]["max"] = measurement
        
        aggregates[place]["count"] += 1
        aggregates[place]["sum"] += measurement


        if (i+1) % 100_000 == 0:
            print(f"Processing... {i+1:,}", end="\r", flush=True)
    
    print()


for place, data in aggregates.items():
    print(f"{place:>15}:\t{data['min']}\t{data['sum']/data['count']:.1f}\t{data['max']}")