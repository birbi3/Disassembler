#TODO calculate mem address properly

def get_section_header(binary, arch, offset):
	mem_addr = [int(offset[i], 0) for i in range(len(offset))]
	addr = 0
	for _row in mem_addr:
		addr += _row
	print(addr)
	if arch =="32Bit":
		size = 0x28
	if arch == "64Bit":
		size = 0x40
	i = addr
	section_head = list()
	while i <= size:
		section_head.append(binary[i])
		i += 1
	return section_head
