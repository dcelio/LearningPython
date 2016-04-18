#The program will use urllib to read the HTML from the data files below, 
#and parse the data, extracting numbers and compute the sum of the numbers in the file. 
#Actual data: http://python-data.dr-chuck.net/comments_200513.html (Sum ends with 7)

import urllib
from BeautifulSoup import *

url = 'http://python-data.dr-chuck.net/comments_200513.html'

html = urllib.urlopen(url).read()
soup = BeautifulSoup(html)

tags = soup('span')

sum = 0

for tag in tags:
	h = 'SPAN:', tag
	l = list(h[1])

	for i in l:
		x = int(i)
		sum = x + sum
print sum