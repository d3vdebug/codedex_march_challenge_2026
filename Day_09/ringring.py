import re
def find_unique_words(transcript):
  text = transcript.lower()
  text = re.sub(r"[^a-z0-9\s]", "", text)
  words = [w for w in text.split() if w]
  return len(set(words))
