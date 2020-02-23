from bin_tools import *

def get_executable(binary, entry, section):
	"""
	Will get all of the excuteable data for binary
	args:
		entry (string): the entry point of the binary 
		section (string): the section header offset
	"""
	return mem_space(binary, entry, section)