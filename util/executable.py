from bin_tools import *

def get_executable(binary, entry, section):
	"""
	Will get all of the excuteable data for binary
	args:
		entry (string): the entry point of the binary 
		section (string): the section header offset
	"""
	return mem_space(binary, entry, section)


def format_32(excuteable):
	i = 0
	data = list()
	format_exec = list()
	for _byte in excuteable:
		if i == 4:
			format_exec.append(data)
			data = list()
			i = 0
		data.append(_byte)
		i +=1
	return format_exec


def format_64(excuteable):
	i = 0
	data = list()
	format_exec = list()
	for _byte in excuteable:
		if i == 8:
			format_exec.append(data)
			data = list()
			i = 0
		data.append(_byte)
		i +=1
	return format_exec