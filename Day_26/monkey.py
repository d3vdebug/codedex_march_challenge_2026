def infinite_monkey(target, attempt):
    # Write code below 💖
    best_similarity = 0
    best_index = 0

    n = len(target)
    
    for i in range(len(attempt) - n + 1):
        window = attempt[i:n+i]
        match = 0

        for j in range(n):
            if window[j] == target[j]:
                match += 1
        
        similarity = (match / n) * 100

        if similarity > best_similarity:
            best_similarity = similarity
            best_index = i
        
    if best_similarity == 0:
        attempts = None
    else:
        attempts = round((100 / best_similarity) ** n)
    
    return {
        'best_index': best_index,
        'similarity': round(best_similarity, 2),
        'attempts': attempts
    }