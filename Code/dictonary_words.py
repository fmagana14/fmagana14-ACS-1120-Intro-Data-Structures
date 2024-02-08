import random
dictionary = open('/usr/share/dict/words', 'r')
dict_list = dictionary.readline()
dictionary.close()

random_dict = []
word_nums = int(input("How many words should I display?"))

def random_dict():
    for i in range(word_nums):
        random_dict = random.choice(dict_list).strip()
        random_dict.append(random_dict)

    random_string = ' '.join(random_dict)
    return random_string
print(random_dict())