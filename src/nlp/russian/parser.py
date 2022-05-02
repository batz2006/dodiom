import stanza
from transformers import YOSO_PRETRAINED_MODEL_ARCHIVE_LIST
stanza.download("ru")
nlp = stanza.Pipeline("ru")

doc = nlp("Чтобы выкрасить забор в лиловый цвет, нужно быть полностью без царя в голове.")
lemma_list = []
for sentence in doc.sentences:
    for word in sentence.words:
        lemma_list.append(word.lemma)
print(lemma_list)
# print(*[f'lemma: {word.lemma}' for sent in doc.sentences for word in sent.words], sep='\n')
# print(doc.entities)

# from typing import Optional, Tuple, List

# import nltk
# from nltk import SnowballStemmer

# from i18n import Language
# from models import Mwe
# from nlp.parser import Parser


# class RussianParser(Parser):
#     def __init__(self):
#         super(RussianParser, self).__init__()
#         self.nlp = stanza.Pipeline("ru")
#         self.language = Language.ENGLISH

#     def get_sentence_count(self, text: str):

#         doc = self.nlp(text)
#         return len(doc.sentences)

#     def lemmatize(self, text: str, mwe: Optional[Mwe] = None) -> Tuple[List[str], List[str]]:
#         oktens = nltk.word_tokenize(text)
#         lemmas = [self.english_stemmer.stem(token) for token in tokens]
#         return tokens, lemmas

# """
# extract lemmas and tokens from output,
# create translation.py file for Russian, insert Russian translations for terms
# """