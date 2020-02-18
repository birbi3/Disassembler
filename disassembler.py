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
	sh_offset = e_shoff(binary, arch)
	sh_size = e_shnum(binary, arch)


	print(sh_offset)
	print(sh_size)

if __name__ == '__main__':
	main(sys.argv[1])