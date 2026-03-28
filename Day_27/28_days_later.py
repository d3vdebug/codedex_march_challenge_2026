from collections import deque
def days_to_infect(city):
  # Write code below 💖
  queue = deque()
  humans = 0
  days = 0

  adjacents = [(-1,0), (1,0), (0,-1), (0,1)]

  for row in range(len(city)):
    for col in range(len(city[0])):
      if city[row][col] == '🧟':
        queue.append((row, col))
      elif city[row][col] == '👤':
        humans += 1

  while queue and humans > 0:
    for _ in range(len(queue)):
      row, col = queue.popleft()

      for ar, ac in adjacents:
        nr = row + ar
        nc = col + ac

        if 0 <= nr < len(city) and 0 <= nc < len(city[0]):
          if city[nr][nc] == '👤':
            city[nr][nc] = '🧟'
            humans -= 1
            queue.append((nr, nc))
    days += 1

  return days if humans == 0 else -1