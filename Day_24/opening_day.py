def streak_counter(games):
  # Write code below 💖
  max_win = 0
  cur_win = 0

  for game in games:
    if game == "W":
      cur_win += 1
    elif game == "R":
      cur_win += 0
    else:
      cur_win = 0

    max_win = max(max_win, cur_win)

  return max_win