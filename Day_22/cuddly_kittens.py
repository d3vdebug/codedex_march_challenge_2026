def cuddly_kittens(kittens, limit):
  # Write code below 💖
  max_grp = 0

  for i in range(len(kittens)):
    for j in range(i, len(kittens)):
      temp_grp = kittens[i:j+1]

      if max(temp_grp) - min(temp_grp) <= limit:
        max_grp = max(max_grp, len(temp_grp))
      else:
        break

  return max_grp