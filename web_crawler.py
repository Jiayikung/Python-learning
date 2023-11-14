import requests 
from bs4 import BeautifulSoup


def main():
	url = 'https://www.imdb.com/chart/top'

	headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36'}

	response = requests.get(url, headers=headers)
	print(response)

	html = response.text
	soup = BeautifulSoup(html)
	tags = soup.find_all('div', {'class': 'sc-c7e5f54-8 fiTXuB cli-title-metadata-item'})
	# 'class': 'sc-c7e5f54-7 brlapf cli-title-metadata'
	# class ="sc-c7e5f54-8 fiTXuB cli-title-metadata-item" > 1994 < / span >
	# class ="sc-c7e5f54-8 fiTXuB cli-title-metadata-item" > 1972 < / span >
	d = {}
	for tag in tags:
		info = tag.text
		print(info)
		# year = info[0:4]
		# print(year)
		# if year not in d:
		# 	d[year] = 1
		# else:
		# 	d[year] += 1

	# for year, count in sorted(d.items(), key=lambda element: element[1]):
	# 	print(year, '->', count)



if __name__ == '__main__':
	main()
