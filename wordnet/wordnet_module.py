from nltk import word_tokenize
from nltk.corpus import wordnet
from unidecode import unidecode
from text_normalizer.normalizer import Normalizer
from utils import paths

class WordNet(object):

    @staticmethod
    def get_word_synonyms_from_sent(word, sent):
        word_synonyms = []
        for synset in wordnet.synsets(word):
            for lemma in synset.lemma_names():
                if lemma in sent and lemma != word:
                    word_synonyms.append(lemma)
        return word_synonyms

    @staticmethod
    def array_tokenizer(phrase_array):
        tokenizer = []
        for phrase in phrase_array:
            tokenizer.append(word_tokenize(phrase))
            return tokenizer

    def join_words_with_syns(self,candidate_words):
        true_pairs = []
        unusual_words = []
        for word in candidate_words:
            word_synonyms = self.get_word_synonyms_from_sent(word, candidate_words)
            if len(word_synonyms) == 0:
                unusual_words.append(word)
            for syn in set(word_synonyms):
                syn = str(unidecode(syn))
                true_pairs.append((word, syn))
        return true_pairs

    def create_syns_dict(self, true_pairs):
        syns_dict = []
        for i in range(0, len(true_pairs)):
            word = true_pairs[i][0]
            syns = []
            for j, k in true_pairs:
                if word == j:
                    syns.append(k)
            syns_dict.append(word + ' => '+','.join(syns))

        return syns_dict

    @staticmethod
    def save_file(path, text_list):
        file = open(path, 'w')
        for pairs in text_list:
            file.write(pairs + '\n')

if __name__ == '__main__':

    wn = WordNet()
    data = open(paths.DOCUMENTS_FILE_PATH, 'r').read()
    text_normalized = Normalizer().normalize(data)
    tokens_set = list(set(text_normalized))
    true_pairs = wn.join_words_with_syns(tokens_set)
    pairs = list(set(true_pairs))
    wn.save_file(paths.THESAURUS_FILE_PATH,wn.create_syns_dict(pairs))


















