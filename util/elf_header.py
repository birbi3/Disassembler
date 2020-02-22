from bin_tools import *

def e_shstrndx(binary, arch):
	sh_index = list()
	if arch == "32Bit":
		sh_index.append(binary[46])
		sh_index.append(binary[47])
	if arch == "64Bit":
		sh_index.append(binary[49])
		sh_index.append(binary[50])
	return(sh_index)

def e_shnum(binary, arch):
	sec_size = list()
	if arch == "32Bit":
		sec_size.append(binary[44])
		sec_size.append(binary[45])
	if arch == "64Bit":
		sec_size.append(binary[47])
		sec_size.append(binary[48])
	return(sec_size)

def e_shentsize(binary, arch):
	sh_size = list()
	if arch == "32Bit":
		sh_size.append(binary[42])
		sh_size.append(binary[43])
	if arch == "64Bit":
		sh_size.append(binary[45])
		sh_size.append(binary[46])
	return(sh_size)	

def e_phentsize(binary, arch):
	ph_size = list()
	if arch == "32Bit":
		ph_size.append(binary[40])
		ph_size.append(binary[41])
	if arch == "64Bit":
		ph_size.append(binary[43])
		ph_size.append(binary[44])
	return(ph_size)

def e_ehsize(binary, arch):
	e_header = list()
	if arch == "32Bit":
		e_header.append(binary[40])
		e_header.append(binary[41])
	if arch == "64Bit":
		e_header.append(binary[43])
		e_header.append(binary[44])
	return(e_header)

def e_flag(binary, arch):
	flag = list()
	if arch == "32Bit":
		flag.append(binary[36])
		flag.append(binary[37])
		flag.append(binary[38])
		flag.append(binary[39])
	if arch == "64Bit":
		flag.append(binary[39])
		flag.append(binary[40])
		flag.append(binary[41])
		flag.append(binary[42])
	return(flag)

def e_shoff(binary, arch, enndian):
	section_header = list()
	if arch == "32Bit":
		section_header.append(binary[32])
		section_header.append(binary[33])
		section_header.append(binary[34])
		section_header.append(binary[35])
	if arch == "64Bit":
		section_header.append(binary[41])
		section_header.append(binary[42])
		section_header.append(binary[43])
		section_header.append(binary[44])
		section_header.append(binary[45])
		section_header.append(binary[46])
		section_header.append(binary[47])
		section_header.append(binary[48])
	if enndian == "Big Endian":
		offset =(big_endian(section_header))
	if enndian == "Little Endian":
		offset = (little_endian(section_header))
	return(offset)

def e_phoff(binary, arch):
	program_header = list()
	if arch == "32Bit":
		program_header.append(binary[28])
		program_header.append(binary[29])
		program_header.append(binary[30])
		program_header.append(binary[31])
	if arch == "64Bit":
		program_header.append(binary[32])
		program_header.append(binary[34])
		program_header.append(binary[35])
		program_header.append(binary[36])
		program_header.append(binary[37])
		program_header.append(binary[38])
		program_header.append(binary[39])
		program_header.append(binary[40])
	return(program_header)

def e_entry(binary, arch):
	entry = list()
	if arch == "32Bit":
		entry.append(binary[24])
		entry.append(binary[25])
		entry.append(binary[26])
		entry.append(binary[27])
	if arch == "64Bit":
		entry.append(binary[24])
		entry.append(binary[25])
		entry.append(binary[26])
		entry.append(binary[27])
		entry.append(binary[28])
		entry.append(binary[29])
		entry.append(binary[30])
		entry.append(binary[31])
	return(entry)	

def e_machine(binary):
	values = {
	"0x0": "None Specificed",
	"0x2": "SPARC",
	"0x3": "x86",
	"0x8": "MIPS",
	"0x14": "PowerPC",
	"0x16": "S390",
	"0x28": "ARM",
	"0x2a": "SuperH",
	"0x32": "IA-64",
	"0x3e": "amd64",
	"0xb7": "AArch64",
	"0xf3": "RISC-V"
	}
	return(values.get(binary[18]))

def e_type(binary):
	val = ""
	values = {
	"0x0": "NULL",
	"0x1": "ET_REL: Relocatable File",
	"0x2": "ET_EXEC Executable File",
	"0x3": "ET_DYN Shared Object File",
	"0x4": "ET_CORE Core file",
	"0xff": "ET_LOPROC Processor-Specific",
	"0xffff": "ET_HIPROC Processor-Specific"
	}
	if binary[17] == "0x0":
		return(values.get(binary[16]))
	else:
		byte_one = binary[16].split("x")[1]
		byte_two = binary[17].split("x")[1]
		val = "0x"+byte_one+byte_two
		return(values.get(val))

def os_detect(binary):
	values ={
	"0x0": "System V",
	"0x1": "HP-UX",
	"0x2": "NetBSD",
	"0x3": "Linux",
	"0X4": "GNU Hurd",
	"0x6": "Solaris",
	"0x7": "AIX",
	"0x8": "IRIX",
	"0x9": "FreeBSD",
	"0xa": "Tru64",
	"0xb": "Novell Modesto", 
	"0xc": "OpenBSD",
	"0xd": "OpenVMS",
	"0xe": "NonStop Kernel",
	"0xf": "AROS",
	"0x10": "Fenix OS",
	"0x11": "CloudABI",
	}
	return(values.get(binary[6]))

def bin_detect(binary):
	if binary[0] == "0x7f":
		if binary[1] == "0x45": 
			if binary[2] == "0x4c":
				if binary[3] == "0x46":
					return("ELF")

def bin_bit(binary):
	if binary[4] == "0x1":
		return("32Bit")
	if binary[4] == "0x2":
		return("64Bit")

def bin_endian(binary):
	if binary[5] == "0x1":
		return("Little Endian")
	if binary[5] == "0x2":
		return("Big Endian")

