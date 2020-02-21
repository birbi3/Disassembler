#!/usr/bin/env python

import sys
sys.path.append("util/")
from elf_header import *
from program_header import *
from section_header import *


def main(argv):
	with open(argv, "rb") as _binary:
		binary = [_row for _row in _binary]
	binary = "".join(binary)
	binary_string = ""
	for _row in binary:
		binary_string += hex(ord(_row))+" "
	binary = binary_string.split(" ")
	
	print(len(binary))
	arch = bin_bit(binary)
	section_offset = e_shoff(binary, arch)
	print(section_offset)
	#section_header = get_section_header(binary, arch, section_offset)
	#print(section_header)
	

if __name__ == '__main__':
	main(sys.argv[1])