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

These can be changed or added to and will work perfectly with no other information needed

## Example:
  "Sent: 12 June 2023 11:52 From: test; To: test; ; Cc: Subject: Education Verification Request John Cena 12345678 Number of Attachments: 2 Dear Sir/Madam, My name is Dan Anthony and I work for First Advantage who conducts background screening globally. I am trying to verify the education history for John Cena Please find the education questionnaire attached with the information provided, that I am trying to verify. I have also attached a signed letter of consent to release this information. Please complete and return this via email or fax at your earliest convenience. Email: test Phone: 44444444444 Ext. 4444 Fax: +44 (0) 4444 444 444 Thank you for your time Regards Dan Paty SR#:1-122334466 First Advantage "

### Terminal output:
  ![Screenshot 2023-06-19 102835](https://github.com/WilliamWalshDowd/e-mail-Classifer-and-Summarizer/assets/99445178/0c2666d2-0e11-4162-81e6-17592236a618)

### Spacy highlighting output:
![Screenshot 2023-06-19 102806](https://github.com/WilliamWalshDowd/e-mail-Classifer-and-Summarizer/assets/99445178/ee549b57-af98-478c-bf08-cb7666a26287)

## Email Generating
Emails can also be generaed from templates to answer questions with a single answer and no varition. for example the start dates have a generic answer.
![Screenshot 2023-06-20 094229](https://github.com/WilliamWalshDowd/e-mail-Classifer-and-Summarizer/assets/99445178/72932464-5818-4dac-8adb-29c2902ed138)
### HTML
since its a html template it can be formaated in a single line string using tags. this allows a for a nice output when moving o an email envirnment like so.
![Screenshot 2023-06-20 093911](https://github.com/WilliamWalshDowd/e-mail-Classifer-and-Summarizer/assets/99445178/daa58790-28aa-487f-ae2d-7d170e65a005)

