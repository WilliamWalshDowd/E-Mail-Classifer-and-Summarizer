# Email-Classifer-and-Summarizer
A simple AI implementation of 2 models to summarize, categorize and extract names from a jumbled mess of raw e-mail.

## INSTALLS
You will need to install a few packages to make this work a its very heavily dependant on 3 main packages.
  - nltk
  - transformers
  - more packages will request to install when atempting to run


## RUN
To run simply write:
  > py '/e-mail classifier.py'


## DATA
The default data its checking is test data in the testdata.json file made from random raw e-mails with 3 main labels:
  - education verification
  - translation request
  - other

These can be changed or added to and will work perfectly with no other information needed.
test data exampls:
  "Sent: 12 June 2023 11:52 From: test; To: test; ; Cc: Subject: Education Verification Request John Cena 12345678 Number of Attachments: 2 Dear Sir/Madam, My name is Dan Anthony and I work for First Advantage who conducts background screening globally. I am trying to verify the education history for John Cena Please find the education questionnaire attached with the information provided, that I am trying to verify. I have also attached a signed letter of consent to release this information. Please complete and return this via email or fax at your earliest convenience. Email: test Phone: 44444444444 Ext. 4444 Fax: +44 (0) 4444 444 444 Thank you for your time Regards Dan Paty SR#:1-122334466 First Advantage "
