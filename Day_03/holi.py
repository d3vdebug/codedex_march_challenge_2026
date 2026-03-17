def find_missing_colors(grid):
  palette = ["🟥", "🟧", "🟨", "🟩", "🟦", "🟪", "🟫"]
    
  found = []
  for row in grid:
    for color in row:
      if color not in found:   
        found.append(color)

  missing = []
  for color in palette:
    if color not in found:
      missing.append(color)

  return missing
