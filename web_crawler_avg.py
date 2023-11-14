"""
File: web_crawler_avg.py
Name: Doris
--------------------------
This file demonstrates how to get
averages on www.imdb.com/chart/top
Do you know the average score of 250 movies?
Let's use Python code to find out the answer
"""

import requests 
from bs4 import BeautifulSoup


def main():
	url = 'http://www.imdb.com/chart/top'
	headers = {
		'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36'}
	response = requests.get(url, headers=headers)
	html = response.text
	soup = BeautifulSoup(html)
	tags = soup.find_all('div', {'class': 'sc-e3e7b191-0 iKUUVe sc-c7e5f54-2 hCiLPi cli-ratings-container'})
	total = 0
	for tag in tags:
		target = tag.span['aria-label']
		score = float(target[-3:])
		total += score
	print(total/250)

if __name__ == '__main__':
	main()
