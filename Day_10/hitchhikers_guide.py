from itertools import combinations

def minimum_components(components):
  target = 42
    
  for r in range(1, len(components) + 1):
    for combo in combinations(components, r):
      if sum(combo) == target:
        return r
                
  return -1
