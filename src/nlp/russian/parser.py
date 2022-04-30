import stanza
from transformers import YOSO_PRETRAINED_MODEL_ARCHIVE_LIST
stanza.download("ru")


doc = nlp("Чтобы выкрасить забор в лиловый цвет, нужно быть полностью без царя в голове. К тому же совесть не давала беспечно бить баклуши и гнала на работу.")

print(doc)
print(doc.entities)

from typing import Optional, Tuple, List

import nltk
from nltk import SnowballStemmer

from i18n import Language
from models import Mwe
from nlp.parser import Parser


class RussianParser(Parser):
    def __init__(self):
        super(RussianParser, self).__init__()
        self.nlp = stanza.Pipeline("ru")
        self.language = Language.ENGLISH

    def get_sentence_count(self, text: str):

        doc = self.nlp(text)
        return len(doc.sentences)

    def lemmatize(self, text: str, mwe: Optional[Mwe] = None) -> Tuple[List[str], List[str]]:
        oktens = nltk.word_tokenize(text)
        lemmas = [self.english_stemmer.stem(token) for token in tokens]
        return tokens, lemmas

"""
extract lemmas and tokens from output,
create translation.py file for Russian, insert Russian translations for terms
"""