#The program will use urllib to read the HTML from the data files below, 
#extract the href= vaues from the anchor tags, scan for a tag that is in 
#a particular position relative to the first name in the list, follow that 
#link and repeat the process a number of times and report the last name you find. 

#Actual problem: Start at: http://python-data.dr-chuck.net/known_by_Aseel.html 
#Find the link at position 18 (the first name is 1). Follow that link. 
#Repeat this process 7 times. The answer is the last name that you retrieve.
#Hint: The first character of the name of the last page that you will load is: E


import urllib 
from BeautifulSoup import *

url = 'http://python-data.dr-chuck.net/known_by_Aseel.html' 

position = 0
times = 0

while times < 7:
	
	html = urllib.urlopen(url).read()
	soup = BeautifulSoup(html)
	tags = soup('a')
	
	for link in tags:
		position = position + 1
		if position == 18:
			url = link.get('href', None)
			print url
			position = 0
			break
	times = times + 1