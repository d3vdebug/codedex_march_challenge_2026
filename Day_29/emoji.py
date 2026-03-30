def emoticons_mood(message):
  # Write your code here 💖
  mood = 0
  happy = [":)", ":p", "XD", ":3", "<3", "\m/"]
  sad = [":(",":'(", "t(-.-t)"]

  for emo in happy:
    h = message.count(emo)
    mood += h
  
  for emo in sad:
    s = message.count(emo)
    mood -= s
  
  return mood