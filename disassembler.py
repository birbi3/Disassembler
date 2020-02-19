#!/usr/bin/env python

import sys
sys.path.append("util/")
from elf_header import *
from program_header import *


def main(argv):
	with open(argv, "rb") as _binary:
		binary = [_row for _row in _binary]
	binary = "".join(binary)
	binary_string = ""
	for _row in binary:
		binary_string += hex(ord(_row))+" "
	binary = binary_string.split(" ")
	
	arch = bin_bit(binary)
	ph_offset = e_phoff(binary,arch)
	ph_size = e_phentsize(binary,arch)
	program_header = get_full_program_header(ph_offset, arch, binary)
	print(program_header)

if __name__ == '__main__':
	main(sys.argv[1])