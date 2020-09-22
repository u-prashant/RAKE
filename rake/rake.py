import re
import operator

def load_stop_words(stop_words_file_path: str) -> list:
    """Loads stop words from a file and return as a list of words.

    Keyword arguments:
    stop_words_file_path -- filepath of a file containing stop words
    """
    stop_words = []
    for line in open(stop_words_file_path):
        if line.strip()[0:1] != "#":
            for word in line.split(): # in case more than one per line
                stop_words.append(word)
    
    return stop_words


def build_stop_word_regex(stop_words_file_path: str) -> re.Pattern:
    """Builds a regex expression to match any of the stop word.

    Keyword arguments:
    stop_words_file_path -- filepath of a file containing stop words
    """
    stop_words_list = load_stop_words(stop_words_file_path)
    stop_words_regex_list = []
    for word in stop_words_list:
        word_regex = r'\b' + word + r'(?![\w-])'
        stop_words_regex_list.append(word_regex)
    stop_words_pattern = re.compile('|'.join(stop_words_regex_list), re.IGNORECASE)

    return stop_words_pattern


class RAKE(object):
    def __init__(self, stop_words_file_path: str = 'resources/SmartStoplist.txt'):
        self.stop_words_file_path = stop_words_file_path
        self.stop_words_pattern = build_stop_word_regex(stop_words_file_path)

    def exec(self, text: str):
        sentences = self.split_sentences(text)
        phrases = self.generate_candidate_keywords(sentences)
        word_scores = self.calculate_word_scores(phrases)
        keyword_candidates = self.generate_candidate_keyword_scores(phrases, word_scores)
        sorted_keywords = sorted(keyword_candidates.items(), key=operator.itemgetter(1), reverse=True)
        
        return sorted_keywords

    def split_sentences(self, text: str) -> list:
        """Split text into sentences."""
        sentence_delimiters = re.compile(u'[.!?,;:\t\\\\"\\(\\)\\\'\u2019\u2013]|\\s\\-\\s')
        sentences = sentence_delimiters.split(text)

        return sentences

    def generate_candidate_keywords(self, sentences: list) -> list:
        """Returns keyword phrases after removing stopwords from each sentence."""
        phrases_list = []
        for sentence in sentences:
            phrases = re.sub(self.stop_words_pattern, '|', sentence.strip()).split('|')
            for phrase in phrases: 
                phrase = phrase.strip().lower()
                if phrase != "":
                    phrases_list.append(phrase)
        
        return phrases_list

    def is_number(self, s):
        try:
            float(s) if '.' in s else int(s)
            return True
        except ValueError:
            return False

    def separate_words(self, text: str, word_min_size: int = 0) -> list:
        """Return a list of all words of length greater than specified min size.

        Keyword arguments:
        text -- the text that is to be split into words
        word_min_size -- the min. no. of characters a word must have (default 0)
        """
        splitter = re.compile('[^a-zA-Z0-9_\\+\\-/]')
        words = []
        for single_word in splitter.split(text):
            current_word = single_word.strip().lower()
            if len(current_word) > word_min_size \
                and current_word != '' \
                and not self.is_number(current_word):
                words.append(current_word)

        return words

    def calculate_word_scores(self, phrases: list) -> dict:
        """Calculates the word score for all the words in the phrases."""
        word_frequency = {}
        word_degree = {}
        for phrase in phrases:
            words = self.separate_words(phrase)
            words_list_degree = len(words) - 1
            for word in words:
                word_frequency.setdefault(word, 0)
                word_frequency[word] += 1
                word_degree.setdefault(word, 0)
                word_degree[word] += words_list_degree

        for item in word_frequency:
            word_degree[item] = word_degree[item] + word_frequency[item]

        # Calculate word score = def(w) / freq(w)
        word_score = {}
        for item in word_frequency:
            #word_score.setdefault(item, 0):
            word_score[item] = word_degree[item] / (word_frequency[item] * 1.0)

        return word_score

    def generate_candidate_keyword_scores(self, phrases: list, word_score: dict) -> dict:
        """Returns the dict. of candidate keywords with scores."""
        keyword_candidates = {}
        for phrase in phrases:
            keyword_candidates.setdefault(phrase, 0)
            words = self.separate_words(phrase)
            candidate_score = 0
            for word in words:
                candidate_score += word_score[word]
            keyword_candidates[phrase] = candidate_score
        
        return keyword_candidates
