import statistics
def earthquake_anomaly(readings):
  # Write code below 💖
  if not readings:
    return []
  
  sus = []
  median = statistics.median(readings)
  threshold = median * 1.5

  for i in range(len(readings)):
    if readings[i] > threshold:
      sus.append(i)
  
  return sus