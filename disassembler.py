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
	print(p_type(program_header))
	print(p_offset(program_header, arch))
	print(p_vaddr(program_header, arch))
	print(p_paddr(program_header, arch))
	print(p_filesz(program_header, arch))
	print(p_memsz(program_header, arch))
	print(p_flags_32(program_header, arch))
	print(p_align(program_header, arch))

if __name__ == '__main__':
	main(sys.argv[1])