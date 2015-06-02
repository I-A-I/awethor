from collections import Counter

# Class for author profile
class Profile:
    def __init__(self, *rest_text):
        self.texts = []
        if rest_text:
            apply(self.add_texts, rest_text)

    # Add a single text
    def add_text(self, new_text):
        # self.texts.append(unicode(new_text,'utf-8'))
        self.texts.append(new_text)

    # For every n-gram between N_GRAM_MIN and N_GRAM_MAX:
        # ... Count n-grams
        # ... Sort descendingly
        # ... Discard frequency to save memory (?)


    # Add multiple textsshell    
    def add_texts(self, *new_texts):
        for new_text in new_texts:
            self.add_text(new_text)
