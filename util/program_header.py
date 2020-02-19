#TODO fix the value it's off by one
def get_full_program_header(offset, arch, binary):
	offset = int(offset[0], 0)
	if arch == "32Bit":
		size = 0x20
	if arch == "64Bit":
		size == 0x38

	header_end = offset + size
	
	program_header = list()
 	i = int(offset)
 	while i <= header_end:
 		program_header.append(binary[i])
 		i += 1
 	return program_header
