import requests
import json
from bs4 import BeautifulSoup

def main():
	url = "https://www.felixcloutier.com/x86/"
	response = requests.get(url).content
	soup = BeautifulSoup(response, 'html.parser')
	links = [(url + _row.get('href').strip("./")) for _row in soup.find_all('a')]
	for _row in links:
		data = requests.get(_row).content
		instruction_data = BeautifulSoup(data, "html.parser")
		instruction_tables = instruction_data.find_all('td')
		print("")
		print(instruction_tables)
	"""	
	test_link = requests.get(links[1]).content
	test = BeautifulSoup(test_link, 'html.parser')
	print(test.find_all('td'))
	"""

def data_obj(op, instruction):
	data = {
	"op": op,
	"instruction": instruction
	}
	return data

if __name__ == "__main__":
	main()