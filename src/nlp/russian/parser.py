import stanza
stanza.download("ru")

nlp = stanza.Pipeline("ru")

doc = nlp("В Российской Федерации проживает более 100 миллионов человек.")
print(doc)
print(doc.entities)
