def flatten(list):
  # Write code below 💖
  result = []
  for item in list:
    if type(item) == type([]):
      result.extend(flatten(item))
    else:
      result.append(item)
  
  return result