from bs4 import BeautifulSoup
from urllib.request import urlopen
from openpyxl import Workbook
import tkinter as tk


#enter link that we search
url = "https://www.delfax.com"
page = urlopen(url)
html = page.read().decode("utf-8")
soup = BeautifulSoup(html, "html.parser")

      #INPUT HERE#
string_to_find = "multinational"
all_text = soup.get_text()

#counts how many times i see a word inside#
word_count = all_text.lower().count(string_to_find.lower())




#checks checks and writes
if_true = string_to_find.lower() in all_text.lower() 
#print(f"'{string_to_find}' {'was' if if_true else 'was not'} found in the HTML.")


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

#adds the text into a text.file
lines = ['Run New Search Code',str(soup)]
with open('Run New Search Code.txt','w',encoding='utf-8') as f:
   f.writelines(lines)




# Function to handle user input and display output
def process_input():
    user_input = input_entry.get()  # Get user input from the Entry widget
    user_input2 = input_entry.get()
    
    string_to_find2 = user_input      
    word_count2 = all_text.lower().count(string_to_find2.lower())     
    output_label.config(text=f"times found: {word_count2}")  # Display the input in a Label widget
    

# Create the main application window
app = tk.Tk()
app.title("Input and Output Display")

# Create an Entry widget for user input
input_label = tk.Label(app, text="Keywords:")
input_label.pack()
input_entry = tk.Entry(app)
input_entry.pack()
