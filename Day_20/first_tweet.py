def tweet_balance(tweet):
  # Write code below 💖
  char = 140
  words = tweet.split()
  spaces = tweet.count(" ")
  char -= spaces

  for word in words:
    if word.startswith("@"):
      char -= 20
    elif word.startswith("http://") or word.startswith("https://"):
      char -= 23
    else:
      for ch in word:
        if ord(ch) > 10000:
          char -= 2
        else:
          char -= 1

  return char