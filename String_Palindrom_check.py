def received(s):
    return s == s[::-1]

  #s = ''.join(c.lower() for c in s if c.isalnum())  # clean input
  #return s == ''.join(reversed(s))  # compare with reversed string


print("Palindrome" if received("madam") else "Not a palindrome")
