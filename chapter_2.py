# 1. take definitions.json, read it in as our data, and use a spaced repeition algorithm to create a long list where each word is encountered less and less often, thus increasing the spacing between encounters as we strengthen our knowledge of the word

import json
import csv



# 1.1 is to read in the defintions file, and process it
def load_vocab_from_json(file_path):
    '''Load vocab data from a json file'''
    with open(file_path, 'r') as f:
        data = json.load(f)

    # use a for loop, to loop over every word and instnatiate a new instance of the class for that word, and add it to the dictionary
    result = {}
    for word, definition in data.items():
        result[word] = VocabCard(word, definition) 
    return result 

def write_list_to_csv(words_list, output_file):
    '''Writes a list of words to a csv file with each word wrapped in double quotes'''
    with open(output_file, mode="w", newline='', encoding='utf-8') as file:
        writer = csv.writer(file, quoting=csv.QUOTE_ALL)
        for word in words_list:
            writer.writerow([word])

# 1.2 create a complex object that keeps track of a whole lot of properties about the word, or attributes / therefore we need to define a class for this object
# 1.2.1 we're going to need to define a bunch of methods (functions specific to a class that are kind of like actions - such as a method, that we can use to automatically handle a word encounter)
# 1.3 instantiate this class/object for every word
class VocabCard:
    '''Represents a single vocab card'''
    def __init__(self, word, defintion, repetitions=0, interval=1, ease_factor=2.5, review_counter=0, is_new=True):
        '''This method defines the arguments or properties expected when we create an instance of this class i.e a vocab card'''
        self.word = word
        self.definition = defintion
        self.repetitions = repetitions
        self.interval = interval
        self.ease_factor = ease_factor
        self.review_counter = review_counter # when this reaches 0, the word is due for review
        self.is_new = is_new
    
    def update_card(self):
        '''This method is responsible for handling an encounter with the word and updating when we should encounter it next and a few other things'''
        if self.repetitions == 0:
            self.interval = 2
        elif self.repetions == 1:
            self.repetitions = 4
        else:
            self.interval = round(self.interval * self.ease_factor)
        
        self.repetitions +=1
        
        self.is_new = False
        self.ease_factor = max(1.3, self.ease-factor + 0.1)
        
        self.review_counter = self.interval
        

    def is_learned(self, max_repetitions=9):
        '''telling is if this word is learned completely (which is based off a max_repetitions parameter that we will define later)'''
       return self.repetitions >= max_repetitions


# 1.4 we can create the spaced repetition algorithm that we'll use to create this long list that cleverly introduces new words, and tests old words at the appropriate intervals
def show_word-status(vocab_cards):
    '''Displays the current status of the words and also returns the due words which is a list'''
    
    due_words = []
    for card in vocab_cards.values():
        #is the car due for review? if yes then add it to the array
        if card.review_counter <= 0 and not card.is_new:
            due_words.append(card)
    return due_words
def review_session(vocab_cards, max_repetitions=9):
    '''Reviews words until all are oredered / mastered'''
    history = [] #tracks the order of words reviewd or introduced
    total_words_reviewed = 0
    
    #write spcaced repetition algorithm
    while True:
        #Reduce the review counter for all words
        for card in vocab_cards.values():
            if card.review_counter > 0:
               card.review_counter -= 1 
        #get the words due for review
        due_words = show_word_status(vocab_cards)
        # if no due words inroduce, inroduce a new word as a filler
        if not due_words:
            filler_word = None
            for card in vocab_cards.values():
                if card.is_new:
                    filler_word = card
                    break
            if filler_word:
                filler_word.is_new = False #mark as no longer new
                history.append(filler_word.word)
                total_words_reviewed += 1
                continue
        #Review the due words
    
    # write out our history list to a csv file


if __name__ == '__main__':
    vocab_cards = load_vocab_from_json('definitions.json')
    print('Starting vocab learning session...')
    review_session(vocab_cards)