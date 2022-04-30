from navec import Navec
from slovnet import NER
from ipymarkup import show_span_ascii_markup as show_markup

text = "Я поехал в Перекрёсток, чтобы купить продукты."

navec = Navec.load('navec_hudlit_v1_12B_500K_300d_100q.tar')
ner = NER.load('slovnet_ner_news_v1.tar')
ner.navec(navec)

markup = ner(text)
show_markup(markup.next, markup.spans)