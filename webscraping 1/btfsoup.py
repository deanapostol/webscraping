from bs4 import BeautifulSoup
from urllib.request import urlopen
from openpyxl import Workbook


#enter link that we search
url = "https://www.delfax.com/"
page = urlopen(url)
html = page.read().decode("utf-8")
soup = BeautifulSoup(html, "html.parser")

      #INPUT HERE#
string_to_find = "dolars"
all_text = soup.get_text()



#find all p in the soup
allpsoup = soup.find_all("p")
#print(allpsoup)
comments = soup.findAll('div','comment')
print(comments)
#find all div
alldivsoup = soup.find_all("div class")
for div in alldivsoup:
   print(div.prettify())


#find all h in the soup
allhsoup = soup.find_all(['h1','h2','h3','h4','h5','h6'])
#print(allhsoup)


#counts how many times i see a word inside#
word_count = all_text.lower().count(string_to_find.lower())



#checks  and writes
if_true = string_to_find.lower() in all_text.lower() 
#print(f"'{string_to_find}' {'was' if if_true else 'was not'} found in the HTML.")

#exel things
workbook = Workbook()
sheet = workbook.active

sheet["A1"] = "Run New Search Code"
sheet["B4"] = "Web Site:"
sheet["D4"] = url
sheet["B7"] = "Word to look for:"
sheet["D7"] = string_to_find
sheet["B10"] = "Result:"
sheet["D10"] = if_true
sheet["B13"] = "Times found:"
sheet["D13"] = word_count

workbook.save(filename="Run New Search Code.xlsx")

#adds all the code into a text.file
lines = [str(soup)]
with open('Run New Search Code.txt','w',encoding='utf-8') as f:
   f.writelines(lines)

#adds all the <p> in a text.file
lines = [str(allpsoup)]
with open('all text.txt','w',encoding='utf-8') as f:
   f.writelines(lines)

#adds all the <h1-h6> in a text.file
lines = [str(allhsoup)]
with open('all h1-h6.txt','w',encoding='utf-8') as f:
   f.writelines(lines)