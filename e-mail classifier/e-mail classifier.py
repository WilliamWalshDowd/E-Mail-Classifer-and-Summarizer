import json
import webbrowser
import nltk
import spacy
from spacy import displacy
from nameparser.parser import HumanName
from transformers import pipeline

INPUT = ""
LABELS = ['education verification', 'translation request', 'payments or fees', 'Start Dates', 'Replace ID Card', 'ID Card First Issue', 'other']

#---------- test data loader--------------------------
file = open('testdata.json')
data = json.load(file)
INPUT = data['testdata'][5]['raw']
#-----------------------------------------------------

#----------template loader--------------------------
templatefile = open('templateOutputs.json')
templatedata = json.load(templatefile)
Templates = templatedata['Templates']
#-----------------------------------------------------

#-------------------------------------------- text simplifier --------------------------------------------------
def get_summary(text):    
    summarizer = pipeline("summarization", model="facebook/bart-large-cnn")
    summarisedText = summarizer(text, max_length=200, min_length=20, do_sample=False)[0]['summary_text']
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

#------------------------------------------- document output --------------------------------------------------
def getEntities(text):
    roberta_nlp = spacy.load("en_core_web_trf")
    # Create a document 
    document = roberta_nlp(text)
    # Entity text & label extraction
    return document.ents
        
def visualize_entities(text):
    roberta_nlp = spacy.load("en_core_web_trf")
    # Create a document 
    document = roberta_nlp(text)
    # Show entities in pretty manner
    displacy.serve(document, style='ent')
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
print("----------------entitys-----------------")
entites = getEntities(INPUT)
for entity in entites:
    print(entity.text + '->', entity.label_)
#visualize_entities(INPUT)
#--------------------------------------------------------------------------------------------------------------

#-----------------------------------e-mail response creator----------------------------------------------------
print("----------------email data-------------------")
top_topic = topics[0]
print( "Most likley topic" + top_topic)
def switch(topic_val):
    if "education verification" in topic_val:
        return Templates[0]['education verification']
    elif "translation request" in topic_val:
        return Templates[0]['translation request']
    elif "Start Dates" in topic_val:
        return Templates[0]['Start Dates']
    elif "Replace ID Card" in topic_val:
        return Templates[0]['Replace ID Card']
    elif "ID Card First Issue" in topic_val:
        return Templates[0]['ID Card First Issue']
    elif "other" in topic_val:
        return Templates[0]['other']
    else: return "none"

chosenTemplate = switch(top_topic)
print(chosenTemplate)

# add names to top and bottom
MostLikelySenderName = str(entites[-1])
returnName = "William"

chosenTemplate = chosenTemplate.replace("(RECIPIENT NAME)", MostLikelySenderName)
chosenTemplate = chosenTemplate.replace("(SENDER NAME)", returnName)

f = open('htmlOutput.html', 'w')
html = chosenTemplate

f.write(html)
f.close()

webbrowser.open('htmlOutput.html')
#--------------------------------------------------------------------------------------------------------------