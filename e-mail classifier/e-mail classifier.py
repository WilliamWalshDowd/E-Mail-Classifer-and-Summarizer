import json
import nltk
from nameparser.parser import HumanName
from transformers import pipeline

INPUT = ""
LABELS = ['education verification', 'translation request', 'other']

#---------- test data loader--------------------------
file = open('testdata.json')
data = json.load(file)
INPUT = data['testdata'][2]['raw']
#-----------------------------------------------------

#-------------------------------------------- text simplifier --------------------------------------------------
def get_summary(text):    
    summarizer = pipeline("summarization", model="facebook/bart-large-cnn")
    summarisedText = summarizer(text, max_length=130, min_length=30, do_sample=False)[0]['summary_text']
    return summarisedText
#---------------------------------------------------------------------------------------------------------------

#--------------------------------------------- topic identifier ------------------------------------------------
def get_topics(input, labels):
    classifier = pipeline("zero-shot-classification", model="facebook/bart-large-mnli")
    output = classifier(input, labels)
    formatedOutout = []
    for i in range(len(labels)):
        formatedOutout.append(output['labels'][i] + ': ' + str(round(output['scores'][i]*100, 3)) + "%")
    
    return formatedOutout
#---------------------------------------------------------------------------------------------------------------

#------------------------------------------- name extractor ----------------------------------------------------
def get_human_names(text):
    tokens = nltk.tokenize.word_tokenize(text)
    pos = nltk.pos_tag(tokens)
    sentt = nltk.ne_chunk(pos, binary = False)
    person_list = []
    person = []
    name = ""
    for subtree in sentt.subtrees(filter=lambda t: t.label() == 'PERSON'):
        for leaf in subtree.leaves():
            person.append(leaf[0])
        if len(person) > 1: #avoid grabbing lone surnames
            for part in person:
                name += part + ' '
            if name[:-1] not in person_list:
                person_list.append(name[:-1])
            name = ''
        person = []

    return (person_list)
#--------------------------------------------------------------------------------------------------------------

#--------------------------------outputs-----------------------------------------------------------------------
print("----------------raw---------------------")
print(INPUT)
print("----------------summary-----------------")
summary = get_summary(INPUT)
print(summary)
print("----------------labels------------------")
topics = get_topics(INPUT, LABELS)
for topic in topics:
    print(topic)
print("----------------names-------------------")
names = get_human_names(INPUT)
print("LAST, FIRST")
for name in names: 
    last_first = HumanName(name).last + ', ' + HumanName(name).first
    print(last_first)
#--------------------------------------------------------------------------------------------------------------