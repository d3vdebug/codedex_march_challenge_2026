def blood_moon(time):
  bloodmoon = []
  hour, minute = map(int, time.split(":"))
  start = hour * 60 + minute

  interval = 168
  day = 1440

  for x in range(3):
    moon = (start + interval)%1440
    bloodmoon.append(f"{moon//60:02d}:{moon%60:02d}")
    start = moon
  
  return bloodmoon
