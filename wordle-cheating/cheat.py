from collections import Counter

def count_chars(words):
    counts = Counter()
    for word in words:
        for c in set(word):
            counts[c] += 1

    return counts

def score_words(words):
    counts = count_chars(words)
    scores = []
    for word in words:
        score = sum(counts[c] for c in set(word))
        scores.append((word, score))
    
    return scores

def still_valid(word, no, maybe, yes):
    # If the word contains any chars that we have already
    # found don't exist, it's not valid
    if any(c in word for c in no):
        return False
    
    # If a word contains a different letter in a place where
    # we already know the letter, it's not valid
    if any(word[i] != c for c, i in yes):
        return False
    
    # For every position we have the character in the wrong place
    # if the word has that character in that place, or if the word _doesn't_
    # contain that character, it's not valid
    for c, positions in maybe:
        if any(word[i] == c for i in positions):
            return False
        
        if c not in word:
            return False
    
    return True

def main():
    with open('sorted_words.txt', 'r') as f:
        words = [l.strip() for l in f.readlines()]
    
    scores = score_words(words)
    
    best_word = max(scores, key=lambda s: s[1])
    disallowed_chars = []
    maybe_chars = []
    yes_chars = []
    while len(scores) > 1:
        word, _ = best_word
        print(word, "{}/{}".format(len(scores), len(words)))
        result = input().strip()

        for i in range(len(result)):
            if result[i] == 'n':
                disallowed_chars.append(word[i])
            elif result[i] == 'm':
                maybe_chars.append((word[i], [i]))
            elif result[i] == 'y':
                yes_chars.append((word[i], i))

        scores = [(word, score) for word, score in scores if still_valid(word, disallowed_chars, maybe_chars, yes_chars)]
        best_word = max(scores, key=lambda s: s[1])


if __name__ == "__main__":
    main()