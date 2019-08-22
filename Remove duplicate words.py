def remove_duplicate_words(s):
    words = s.split()
    return " ".join(sorted(set(words), key=words.index))