#!/usr/bin/env python

import sys
sys.path.append("util/")
from elf_header import *
from program_header import *
from section_header import *
from executable import *
from bin_tools import *


def main(argv):
	with open(argv, "rb") as _binary:
		binary = [_row for _row in _binary]
	binary = "".join(binary)
	binary_string = ""
	for _row in binary:
		binary_string += hex(ord(_row))+" "
	binary = binary_string.split(" ")
	

	arch = bin_bit(binary)
	endian = bin_endian(binary)
	exec_entry = e_entry(binary, arch)
	exec_entry = little_endian(exec_entry)
	exec_entry = int_mem(exec_entry)
	section_offset = e_shoff(binary, arch, endian)
	section_offset = int_mem(section_offset)
	executable_data = get_executable(binary, exec_entry, section_offset)
	print(executable_data)


if __name__ == '__main__':
	main(sys.argv[1])