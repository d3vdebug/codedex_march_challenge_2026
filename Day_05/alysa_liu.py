def calculate_score(elements):
  total_score = 0.0

  for move, base, goe in elements:
    sorted_goe = sorted(goe)
    trimmed_goe = sorted_goe[1:-1]
    avg_goe = sum(trimmed_goe) / 7
    element_score = base + (avg_goe * 0.1 * base)

  total_score += element_score

  return round(total_score,1)
