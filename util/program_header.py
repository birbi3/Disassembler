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


def p_type(ph):
	p_type = list()
	p_type.append(ph[0])
	p_type.append(ph[1])
	p_type.append(ph[2])
	p_type.append(ph[3])
	return p_type

def p_flags_64(ph, arch):
	if arch == "64Bit":
		flags = list()
		flags.append(ph[4])
		flags.append(ph[5])
		flags.append(ph[6])
		flags.append(ph[7])
		return flags
	else:
		print("this is p_flag for 64 bit")
		sys.exit(0)

def p_offset(ph, arch):
	offset = list()
	if arch == "32Bit":
		offset.append(ph[4])
		offset.append(ph[5])
		offset.append(ph[6])
		offset.append(ph[7])
	if arch == "64Bit":
		offset.append(ph[8])
		offset.append(ph[9])
		offset.append(ph[10])
		offset.append(ph[11])
		offset.append(ph[12])
		offset.append(ph[13])
		offset.append(ph[14])
		offset.append(ph[15])
	return offset

def p_vaddr(ph, arch):
	vaddr = list()
	if arch == "32Bit":
		vaddr.append(ph[8])
		vaddr.append(ph[9])
		vaddr.append(ph[10])
		vaddr.append(ph[11])
	if arch == "64Bit":
		vaddr.append(ph[15])
		vaddr.append(ph[16])
		vaddr.append(ph[17])
		vaddr.append(ph[18])
		vaddr.append(ph[19])
		vaddr.append(ph[20])
		vaddr.append(ph[21])
		vaddr.append(ph[21])
	return vaddr

def p_paddr(ph, arch):
	paddr = list()
	if arch == "32Bit":
		paddr.append(ph[12])
		paddr.append(ph[13])
		paddr.append(ph[14])
		paddr.append(ph[15])
	if arch == "64Bit":
		paddr.append(ph[22])
		paddr.append(ph[23])
		paddr.append(ph[24])
		paddr.append(ph[25])
		paddr.append(ph[26])
		paddr.append(ph[27])
		paddr.append(ph[28])
		paddr.append(ph[29])
	return paddr

def p_filesz(ph, arch):
	filesz = list()
	if arch == "32Bit":
		filesz.append(ph[16])
		filesz.append(ph[17])
		filesz.append(ph[18])
		filesz.append(ph[19])
	if arch == "64Bit":
		filesz.append(ph[30])
		filesz.append(ph[31])
		filesz.append(ph[32])
		filesz.append(ph[33])
		filesz.append(ph[34])
		filesz.append(ph[35])
		filesz.append(ph[36])
		filesz.append(ph[37])
	return filesz

def p_memsz(ph, arch):
	memsz = list()
	if arch == "32Bit":
		memsz.append(ph[20])
		memsz.append(ph[21])
		memsz.append(ph[22])
		memsz.append(ph[23])
	if arch == "64Bit":
		memsz.append(ph[38])
		memsz.append(ph[39])
		memsz.append(ph[40])
		memsz.append(ph[41])
		memsz.append(ph[42])
		memsz.append(ph[43])
		memsz.append(ph[44])
		memsz.append(ph[45])
	return memsz

def p_flags_32(ph, arch):
	if arch == "32Bit":
		flags = list()
		flags.append(ph[24])
		flags.append(ph[25])
		flags.append(ph[26])
		flags.append(ph[27])
		return flags
	else:
		print("This is the p_flags function for 32 bit binaries")
		sys.exit(0)

def p_align(ph, arch):
	align = list()
	if arch == "32Bit":
		align.append(ph[28])
		align.append(ph[29])
		align.append(ph[30])
		align.append(ph[31])
	if arch == "64Bit":
		align.append(ph[46])
		align.append(ph[47])
		align.append(ph[48])
		align.append(ph[49])
		align.append(ph[50])
		align.append(ph[51])
		align.append(ph[52])
		align.append(ph[53])
	return align