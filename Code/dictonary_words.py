import random
with open('/usr/share/dict/words', 'r') as dictionary:
    dict_list = dictionary.read().splitlines()


word_nums = int(input("How many words should I display?"))

def random_dict():
    random_words = []
    for n in range(word_nums):
        random_word = random.choice(dict_list)
        random_words.append(random_word)

    random_string = ' '.join(random_words)
    return random_string
print(random_dict())