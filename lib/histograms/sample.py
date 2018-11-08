'''
Module for Stochastic sampling from dictionary based histograms
'''
import random

from . import distogram

def random_sample(histogram):
    '''
        Randomly select a word from a histogram regardless of it's frequency in the histogram
        Assumes that histogram is a dictionary based histogram.
    '''
    histogram_words = list(histogram.keys())
    histogram_length = len(histogram_words)
    random_index = random.randint(0, histogram_length - 1)
    return histogram_words[random_index]

def weighted_sample(histogram, word_count=10):
    '''
        Randomly selects a word from a histogram, however, words are now weighted based on their frequency meaning that
        more frequent words have a higher probability of being returned.
        Assumes that histogram is a dictionary based histogram and that word_count is the amount of words that you'd like to pull randomly
    '''
    word_list = []
    for word, frequency in histogram.items():
        for _ in range(0, frequency):
            word_list.append(word)

    output_list = []

    for _ in range(0, word_count):
        random_index = random.randint(0, len(word_list) - 1)
        output_list.append(word_list[random_index])
    return output_list

def test_sampling(histogram):
    '''
        Testing out both random and weighted sampling to see if our code produces the correct results
        Assumes that histogram is a dictionary based histogram
    '''
    print("Now testing random sample")
    random_words = {}
    for i in range(0, 10000):
        word = random_sample(histogram)

        if word in random_words:
            random_words[word] += 1
        else:
            random_words[word] = 1

    print("Now testing weighted sample")
    weighted_words = {}
    for i in range(0, 10000):
        word = weighted_sample(histogram)

        if word in weighted_words:
            weighted_words[word] += 1
        else:
            weighted_words[word] = 1

    print("Finished testing, here are the results")

    print("-----Randomly sampled words-----")
    for word, times_found in random_words.items():
        print("{} was found: {} times".format(word, times_found))

    print()

    print('-----Randomly sampled words with weights-----')
    for word, times_found in weighted_words.items():
        print("{} was found: {} times".format(word, times_found))


if __name__ == '__main__':
    histogram = distogram.histogram('Hi Hi Hi Hi Hi Hi Hi Hi hello there what is up there hands in the air i dont care', is_file=False)
    test_sampling(histogram)