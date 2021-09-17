from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import SnowballStemmer
import string


def tokenize_sentence(sentence: str, language='english'):
    snowball = SnowballStemmer(language=language)
    stop_words = stopwords.words(language)
    tokens = word_tokenize(sentence, language=language)
    tokens = [i for i in tokens if i not in string.punctuation]
    tokens = [i for i in tokens if i not in stop_words]
    tokens = [snowball.stem(i) for i in tokens]
    return tokens


def tokenize_sentence_ru(sentence: str):
    return tokenize_sentence(sentence, language='russian')
