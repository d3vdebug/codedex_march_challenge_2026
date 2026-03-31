def calculate_descent(altitude):
  layers = [
    (10000, 700, 2000),
    (700, 85, 500),
    (85, 50, 200),
    (50, 12, 75),
    (12, 0, 20)
  ]
  
  if altitude == 0:
    return 0.0

  h = float(altitude)
  total_time = 0

  for top, bottom, rate in layers:
    if h > bottom:
      segment_top = min(h, top)
      segment_bottom = bottom
      drop_km = segment_top - segment_bottom

      if drop_km > 0:
        drop_m = drop_km * 1000
        drop_time = drop_m / rate
        total_time += drop_time
        h = segment_bottom

  return round(total_time, 1)
