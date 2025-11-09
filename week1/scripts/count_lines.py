file = "./data/sample.txt"   # FIXED: added missing slash

with open(file, 'r') as f:
    lines = f.readlines()
print(f"Total lines: {len(lines)}")
