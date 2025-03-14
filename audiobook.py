
import PyPDF2
import pyttsx3


book = open('lecture1428551222.pdf', 'rb')
pdfreader=PyPDF2.PdfFileReader(book)
pages= pdfreader.numPages
print(pages)
speaker = pyttsx3.init()
for num in range(7,pages):

     page=pdfreader.getPage(78)
     text=page.extractText()
     speaker.say(text)
     speaker.runAndWait()
