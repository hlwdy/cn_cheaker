import re,csv

class Radical(object):
    dictionary_filepath = 'radical_data.csv'
    def __init__(self):
        self.read_dictionary()

        self.origin_len = len(self.dictionary)

    def read_dictionary(self):
        self.dictionary = {}

        file = open(self.dictionary_filepath, 'rU',encoding='UTF-8')
        reader = csv.reader(file)

        for line in reader:
            self.dictionary[line[0]] = line[1]

        file.close()

    def get_radical(self,word):
        if word in self.dictionary:
            return self.dictionary[word]
        else:
            return self.get_radical_from_baiduhanyu(word)

    
