import requests
html = requests.get('https://dev.to/rly').text
from bs4 import BeautifulSoup
soup = BeautifulSoup(html, 'html.parser')

import re

for tag in soup.select('.color'):
	code = tuple(map(int,re.findall(r'\d+',tag['style'])))
	#숫자가 1회이상 반복되는것을 뽑아라
	print(code)

for idx, tag in enumerate(soup.select('.animal img'), 1):
	image_url = tag['src']
	image_data = requests.get(image_url).content
	image_name = '{}.png'.format(idx)
	with open(image_name, 'wb') as f:
		f.write(image_data)
		print('{} bytes'.format(len(image_data)))