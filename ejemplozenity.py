# ejemploso.so

import os

text = 'Hola a todos Aprender Python es Bueno!'

def buildWarning(text):
    command = 'zenity --warning --text \''+text+'\''
    return command
    
def buildQuestion(text):
    command = 'zenity --question --text \''+text+'\''
    return command    

def buildInput(text):
    command = 'zenity --entry --text \''+text+'\''
    return command

os.system(buildWarning(text))









