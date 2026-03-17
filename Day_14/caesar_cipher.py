def function(message, shift):
  # Write code below 💖
  decode = ""
  shift = shift % 26

  for c in message:
    if c == " ":
      decode += " "
    else:
      new = ord(c) - shift
      if new < ord('a'):
        new += 26
      decode += chr(new)

  return decode
