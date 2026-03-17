def calculate_sleep_debt(planned, actual):
  sleep_debts = [max(0, x - y) for x, y  in zip(planned, actual)]
  total_debt = sum(sleep_debts) + 1.0

  longest_streak = 0
  current_streak = 0
  for due in sleep_debts:
    if due > 0:
      current_streak += 1
      longest_streak = max(longest_streak,current_streak)
    else:
      current_streak = 0
  return round(total_debt, 1), longest_streak
