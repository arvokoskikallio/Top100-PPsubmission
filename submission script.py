from io import StringIO
from html.parser import HTMLParser
import bs4 as bs
import urllib.request
import lxml

class MLStripper(HTMLParser):
    def __init__(self):
        super().__init__()
        self.reset()
        self.strict = False
        self.convert_charrefs= True
        self.text = StringIO()
    def handle_data(self, d):
        self.text.write(d + "\n")
    def get_data(self):
        return self.text.getvalue()

def strip_tags(html):
    s = MLStripper()
    s.feed(html)
    return s.get_data()

f = open("output.txt", "w")
f.write("")
f.close()


url = input("Enter the URL of the top 100: ")
source = urllib.request.urlopen(url).read()
soup = bs.BeautifulSoup(source,'lxml')
table = soup.find_all('table')
block=table[-2]
print(block, file=open("block.txt", "w", encoding='utf-8'))
	
############################### Practical code ######################################## DO NOT TOUCH IT WORKS OK

track = input("Give the category name: ")
f = open("block.txt", "r")
stuff = f.read()
x = stuff.split("\n")

for i in range(100):
 splicer = strip_tags(x[i+3])
 splice = splicer.split("\n")
 
 if "-" in splice[5]:
  print("Date: " + splice[5] + "\nName: " + splice[1] + "\n\n" + track + ": " + splice[3] + " ", file=open("output.txt", "a"))
  print(" ", file=open("output.txt", "a"))
 
 

f.close()