def check_palindrome(sequence):
  # Write code below 💖
  text = sequence.replace(" ", "").lower()
  return text == text[::-1]
