def collect_all_words(words_file):
    # base/corner cases
    if (words_file is None):
        return None

    # main case
    valid_words = set()
    with open(words_file, "r") as f:
        for line in f:
            word = line.rstrip()
            valid_words.add(word)
    return valid_words