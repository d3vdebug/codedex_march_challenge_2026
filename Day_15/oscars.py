def oscar_pool(predictions):
  # Write code below 💖
  oscars = ["One Battle After Another", "Michael B. Jordan", "Jessie Buckley", "Paul Thomas Anderson"]
  best_prediction = -1
  best_predictor = ""
  tie = False
  for predict in predictions:
    name = predict[0]
    guesses = predict[1:]
    score = 0

    for i in range(len(oscars)):
      if guesses[i] == oscars[i]:
        score += 1

    if score > best_prediction:
      best_prediction = score
      best_predictor = name
      tie = False
    elif score == best_prediction:
      tie = True

  return "Tie" if tie else best_predictor
