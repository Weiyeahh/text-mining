import urllib.request
from bs4 import BeautifulSoup
from collections import Counter
url = "https://millercenter.org/the-presidency/presidential-speeches/january-19-2019-remarks-about-us-southern-border" 
html = urllib.request.urlopen(url)
html=html.read()
soup = BeautifulSoup(html)

# kill all script and style elements
for script in soup(["script", "style","a","<div id=\"bottom\" >"]):
    script.extract()    # rip it out

text = soup.select('.transcript-inner')[0].get_text()
text=text.replace('Transcript','')
text=text.replace('THE PRESIDENT:','')
linelist=text.strip().replace("\xa0","").replace("\n","").split(".")
wordlist=text.split()
worddic=Counter(wordlist)

