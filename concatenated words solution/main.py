import sys
import os
import heapq
from concatenated_word_algo import count_concatenated_word
from file_processor import collect_all_words



def main(words_file):
    # base/corner cases
    if (words_file is None):
        return None, None

    # main case
    longest_words = [(0, ''), (0 , '')] # this will be a min heap containing the longest 2 words
    heapq.heapify(longest_words)

    count_of_concat_words = 0
    valid_words = collect_all_words(words_file)
    for concat_word in valid_words:
        new_word_count = count_concatenated_word(concat_word, valid_words)
        if (new_word_count > 1):
            update_longest((len(concat_word), concat_word), longest_words)
            count_of_concat_words += 1
    return longest_words, count_of_concat_words


def update_longest(new_tuple, longest_words):
    # base/corner cases
    if new_tuple is None:
        return
    if len(longest_words) == 0:
        return

    # main case
    curr_tuple = longest_words[0]
    curr_count = curr_tuple[0]
    if (new_tuple[0] > curr_count):
        # new tuple is larger than the smallest of the largest seen so far, so replace it
        heapq.heapreplace(longest_words, new_tuple)




if __name__ == '__main__':
    if (len(sys.argv) == 0):
        print "please provide file of words as first argument"
        sys.exit(1)

    words_file = sys.argv[1]
    
    if (not os.path.isfile(words_file)):
        print "file argument is not a file!"
        sys.exit(1)

    if (not os.access(words_file, os.R_OK)):
        print "user does not have read access on file!"
        sys.exit(1)

    longest_words, count_of_concat_words = main(words_file)
    print "longest words: %s, concat words count: %s" % (longest_words, count_of_concat_words)



