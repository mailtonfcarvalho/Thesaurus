import nltk
import re
import string
from unidecode import unidecode
from utils import paths

class Normalizer(object):

    @staticmethod
    def remove_html(text):
        return unidecode(re.sub(re.compile("<.*?>"), '', text))

    @staticmethod
    def has_digit(sentence):
        return any(char.isdigit() for char in sentence)

    def remove_characteres(self,text):
        text_no_links = self.remove_html(text)
        links = re.findall(r"https?://[\w:/.'\"_%#-]+", text_no_links)
        for link in links:
            text_no_links = text_no_links.replace(link, '')
        chars_to_remove = nltk.word_tokenize(string.punctuation)
        regex = '[' + re.escape(' '.join(chars_to_remove)) + ']'
        clean_text = re.sub(regex, ' ',text_no_links)
        clean_text = ' '.join(
            [
                word for word in clean_text.split()
                if not self.has_digit(word)
            ]
        )
        clean_text = clean_text.lower()
        return clean_text

    @staticmethod
    def remove_stopwords(text):
        STOP_WORDS = open(paths.STOPWORDS_FILE_PATH, 'r').read().split()
        text_tokenize = nltk.word_tokenize(text)
        no_stopwords = ' '.join(
            [
                word.replace('\"', '')
                for word in text_tokenize
                if word not in STOP_WORDS
            ]
        )
        return no_stopwords

    @staticmethod
    def retrieve_nouns_and_verbs(text):
        tokens = nltk.word_tokenize(text)
        words = [n for n, t in nltk.pos_tag(tokens) if t[:2] in ('NN', 'VB')]
        return words

    def normalize(self, text):
        delete_chars = self.remove_characteres(text)
        delete_stopwords = self.remove_stopwords(delete_chars)
        nouns_verbs = self.retrieve_nouns_and_verbs(delete_stopwords)
        return nouns_verbs

if __name__ == '__main__':

    w = Normalizer()
    data = open(paths.DOCUMENTS_FILE_PATH, 'r').read()
    words = w.normalize(data)
    words_list = list(set(words))
    print(words_list)