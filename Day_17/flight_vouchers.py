def pick_voucher(vouchers, delays, max_wait):
  # Write code below 💖
  index = -1
  best_rate = -1

  for i in range(len(vouchers)):
      if delays[i] <= max_wait:
        rate = vouchers[i] / delays[i]

        if rate > best_rate:
          best_rate = rate
          index = i
          
  return index