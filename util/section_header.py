def get_section_header(binary, arch, offset):
	"""
	Returns section header in a list byte by byte
	"""
	offset = int(offset,0)
	print(offset)
	if arch =="32Bit":
		size = 0x28
	if arch == "64Bit":
		size = 0x40
	size = size + offset
	i = offset
	section_head = list()
	while i <= size:
		section_head.append(binary[i])
		i += 1
	return section_head
