from spellchecker import SpellChecker
import csv
import plotly.graph_objects as go
def removespecchar(test):
    """Function to Clean Up Strings.

    Specifically gets rid of quotes,tabs,new lines, and evens out the spaces."""
    import re
    if type(test) == str:
        test=re.sub('\t',' ',test)
        test=re.sub('\"',' ',test)
        test=re.sub('\n',' ',test)
        test=re.sub('\r',' ',test)
        test=re.sub(' +',' ',test)
    return(test)
def spellCheck(text):
    spell = SpellChecker()
    splitText=text.split()
    string1=""
    tempstring1=""
    tempstring2=""
    boolean=False
    for word1 in splitText:
        words=spell.candidates(word1)
        for word in words:
            if(word1!=word):
                tempstring1+=word1+" "
                boolean=True
            if(boolean):
                break
    tempstring2=tempstring1.split()
    for temp in tempstring2:
        string1+="\n"+"("+temp+"):"
        words=spell.candidates(temp)
        for word in words:
            string1+=word+" "
    return (string1)
def correctSpell(text):
    spell = SpellChecker()
    string2=""
    splitText=text.split()
    for word in splitText:
        newText = spell.correction(word)
        if(newText!=word):
            string2+="("+word+"):"+newText+"\n"
    return (string2)
def cleanChart(text):
    Str1=text.split("Notes\n")
    counter=0
    counter2=0
    ChromoList=""
    CytoList=""
    EventList=""
    ClassList=""
    NotesList=""
    Str2=Str1[1].split("\t")
    for word in Str2:
        counter+=1
        if "chr" in word:
            ChromoList+=word+"\n"
        if(counter%7==3):
            CytoList+=word+"\n"
        if(counter%7==5):
            EventList+=word+"\n"
        if(counter%7==0):
            ClassList+=word+"\n"
        if "\n" in word:
            splitWord=word.split("\n")
            NotesList+=splitWord[0]+"\n"
        counter2+=1
    finalList="Chromosomes Region:\n"+ChromoList+"Cytoband:\n"+CytoList+"Event:\n"+EventList+"Classification:\n"+ClassList+"Notes:\n"+NotesList
    fig=go.Figure(data=[go.Table(header=dict(values=['Chromolist','Cytolist','Eventlist','Classlist','Notes'],line_color='darkslategray',fill_color='lightskyblue',align='left'),cells=dict(values=[ChromoList.split(),CytoList.split(),EventList.split("\n"),ClassList.split(),NotesList.split("\n")],line_color='darkslategray',fill_color='lightcyan',align='left'))])
    fig.update_layout(width=1000,height=600)
    fig.show()
    return finalList
