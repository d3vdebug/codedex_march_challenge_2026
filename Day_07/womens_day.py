def analyze(percentages):
  NCPY = (percentages[-1] - percentages[0]) / (len(percentages) - 1)

  last_3year_avg = sum(percentages[-3:]) / 3
  first_3year_avg = sum(percentages[:3]) / 3

  if last_3year_avg > first_3year_avg:
    trend = "improving"
  elif last_3year_avg == first_3year_avg:
    trend = "stagnating"
  else:
    trend = "declining"
  
  dips = 0
  for i in range(1, len(percentages)):
    if percentages[i] < percentages[i-1]:
      dips += 1
  
  return round(NCPY,4), trend, dips
