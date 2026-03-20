def cherry_blossoms(temps):
  # Write code below 💖
  for i in range(4, len(temps)):
    window = temps[i-4:i+1]     
    avg_temp = sum(window) / 5  
        
    if avg_temp > 15:
      return i + 1
    
  return -1
