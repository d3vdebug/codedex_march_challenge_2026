def function(river, hours):
  # Write code below 💖
  result = river[:]

  for i in range(len(river)):
    if river[i] == '☘️':
      for j in range(1, hours + 1):
        drift = i + j
        if drift < len(river):
          result[drift] = '☘️'

  return result
