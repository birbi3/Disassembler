import requests
import json
from bs4 import BeautifulSoup

#TODO make this work
def main():
	op_data = dict()
	flag = 
	url = "https://www.felixcloutier.com/x86/"
	response = requests.get(url).content
	soup = BeautifulSoup(response, 'html.parser')
	links = [(url + _row.get('href').strip("./")) for _row in soup.find_all('a')]
	for _row in links:
		data = requests.get(_row).content
		instruction_data = BeautifulSoup(data, "html.parser")
		th = instruction_tables = instruction_data.find_all('th')
		instruction_tables = instruction_data.find_all('td')
		if not len(th)%6:
			instruction = list()
			for _row in instruction_tables:

		if not len(th)%5:
			print(len(th))
			print(_row)

def data_obj(op, instruction):
	data = {
	"op": op,
	"instruction": instruction
	}
	return data

if __name__ == "__main__":
	main()