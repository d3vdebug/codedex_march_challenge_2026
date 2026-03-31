def longest_streak(progress):
  # Write code below 💖
  max_streak = 0
  tmp_streak = 0

  for s in progress:
    if s == '✅':
      tmp_streak += 1
    elif s == '❌':
      tmp_streak = 0
    max_streak = max(max_streak, tmp_streak)
  
  return max_streak