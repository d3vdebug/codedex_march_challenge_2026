def wordle_guess(secret, guess):
  count = 0
  for x in range(5):
    if secret[x] == guess[x]:
      count += 1
  return count
