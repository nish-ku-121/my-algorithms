def count_concatenated_word(concat_word, valid_words):
    # base/corner cases
    if valid_words is None:
        return 0
    if concat_word is None:
        return 0
    if len(concat_word) == 0:
        return 0
    
    # main case
    counter = [0] * len(concat_word)
    for i in range(0, len(concat_word)):
        word1 = concat_word[0:i+1]
        if ((_is_in_dict(word1, valid_words)) or (counter[i] > 0)):
            counter[i] = max(counter[i], 1);
            for j in range(i+1, len(concat_word)):
                word2 = concat_word[i+1:j+1]
                if (_is_in_dict(word2, valid_words)):
                    counter[j] = max(counter[j], counter[i] + 1)
                else: # for readability
                    continue
        else: # for readability
            continue
    return counter[-1]



def _is_in_dict(word, valid_words):
    # base/corner cases
    if valid_words is None:
        return False

    # main case
    if word in valid_words:
        return True
    else:
        return False