import random
import re

class MarkovChain():
    def __init__(self, source_text):
        self.source_text = self.read_source_text(source_text)
    
    def read_source_text(self, source_text):
       
        with open(str(source_text)) as text:
            text = text.read()
            text = text.split()
        return text
    
    '''
    takes text and converts it to lists
    '''


    def generate_starting_point(self):

        word_list = self.source_text
        starting_words = []
        for word in word_list:
            if word[0].isupper() == True:
                starting_words.append(word) 
        return random.choice(starting_words)
    '''
    creates a list of capitalized words and makes one a starting point
    '''

    def generate_ending_point(self):
    
        word_list = self.source_text
        ending_words = []
        for word in word_list:
            if word[-1] == "." or word[-1] == "?" or word[-1] == "!":
                ending_words.append(word)
        return random.choice(ending_words)

    '''
    creates a list of words that end in '.' '?' '!'
    '''
    
    def generate_sentence(self, max_words):
        '''
        generates a sentence based on words following the starting point and ends on the ending point
        '''
        map = self.build_map()
        starting_point = self.generate_starting_point()
        ending_point = self.generate_ending_point()

        sentence = [starting_point]
        next_word = starting_point
        max_words -= 2 # offset for starting and ending words being appended to sentence

        for count, _ in enumerate(map, start=1):
            # try catch except for rare case when the next word has no value inside of map
            try:
                next_word = random.choice(map[next_word])
            except:
                return " ".join(sentence) + f" {ending_point}"

            sentence.append(next_word)
            if next_word == ending_point or count == max_words:
                completed_sentence = " ".join(sentence) + f" {ending_point}"
                return re.sub(r"[\(\)\{\}]", "", completed_sentence)
                # return re.sub(r"\s*[.:•]\s*|\b(?:[A-Z]{2,}|[A-Z]+\b(?!\.[A-Z]))\b|[()\{\}]|\s{2,}", "", completed_sentence)


            
    def build_map(self):
        '''
        made a dictionary with the key being a word and its value being a list of words followed by the key word
        '''
        words = self.source_text
        map = {}
        for i in range(len(words) - 1):
            next_word = words[i + 1]
            if words[i] in map:
                map[words[i]].append(next_word)
            else:
                map[words[i]] = [next_word]
        return map
                
if __name__ == "__main__":
    source_text = "./data/WhiteFang.txt"
    markov = MarkovChain(source_text)
    print(markov.generate_sentence(10))