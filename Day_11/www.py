def check_url(address):
  # Write code below 💖
  if not address.startswith(("http://", "https://")):
    return "invalid"

  domain = address.split("://")[1]
  if domain.startswith("www."):
    domain = domain[4:]
  if " " in domain or "." not in domain:
    return "invalid"

  return "valid"
