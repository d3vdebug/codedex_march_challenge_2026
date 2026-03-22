def leaky_pipe(volume, leak, hours, threshold):
  # Write code below 💖
  cur_vol = volume
  for h in range(hours):
    cur_vol = round(cur_vol * (1 - (leak/100)), 2)
  
  if cur_vol < threshold:
    return -1

  return cur_vol