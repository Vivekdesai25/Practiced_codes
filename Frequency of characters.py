s = "example"
freq = {}
for c in s:
    freq[c] = freq.get(c, 0) + 1
for char, count in freq.items():
    print(f"{char}: {count}")
