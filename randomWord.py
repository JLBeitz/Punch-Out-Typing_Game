import random

class random_word():
    def __init__(self, difficulty):
        match difficulty:
            case 1:
                self.f = open('easy_words.txt', 'r')
            case 2:
                self.f = open('normal_words.txt', 'r')
            case 3:
                self.f = open('hard_words.txt', 'r')        

    def rand_word(self):
        length = int(self.f.readline())

        index = random.randint(2, length + 1)

        for i in range(index):
            word = self.f.readline()

        return word