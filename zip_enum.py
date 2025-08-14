names = ["Alice", "Bob", "Charlie"]
scores = [85, 92, 78]
ranked = sorted(zip(names, scores), key=lambda x: x[1], reverse=True)
ranked_with_pos = list(map(lambda t: (t[0], t[1], f"Rank {t[2]+1}"), 
                           ((n, s, i) for i, (n, s) in enumerate(ranked))))

print(ranked_with_pos)
# [('Bob', 92, 'Rank 1'), ('Alice', 85, 'Rank 2'), ('Charlie', 78, 'Rank 3')]
