s = "vivek desai"

# reversed_each_word = " ".join(word[::-1] for word in s.split())
# reversed_word_order = " ".join(s.split()[::-1])
# fully_reversed = " ".join(word[::-1] for word in s.split()[::-1])

reversed_each_word = " ".join("".join(reversed(word)) for word in s.split())
reversed_word_order = "".join(" ".join(reversed(s.split())))
fully_reversed = " ".join("".join(reversed(word)) for word in reversed(s.split()))


print(reversed_each_word)    # Output: keviv iased
print(reversed_word_order)   # Output: desai vivek
print(fully_reversed)        # Output: iased keviv

