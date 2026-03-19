def upset_probability(matchups):
  # Write code below 💖
  seeds = []
  for match in matchups:
    if match[1] < match[3]:
      seed = match[1] / (match[1] + match[3])
      seeds.append(round(seed, 2))

    elif match[3] < match[1]:
      seed = match[3] / (match[1] + match[3])
      seeds.append(round(seed, 2))
    
  return seeds