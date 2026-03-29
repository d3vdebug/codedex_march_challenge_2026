def average_time(total, completed):
  # Write code below 💖
  time = total.split(":")
  total_seconds = int(time[0])*60*60 + int(time[1])*60 + int(time[2])
  avg_time = round(total_seconds / completed)
  return avg_time