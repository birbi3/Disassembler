
def main():
	with open("test", "rb") as _binary:
		binary = [_row for _row in _binary]
	binary = "".join(binary)
	binary_string = ""
	for _row in binary:
		binary_string += hex(ord(_row))+" "
	binary = binary_string.split(" ")
	
	bin_detect(binary)
	bin_bit(binary)
	bin_endian(binary)
	os_detect(binary)
	

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
	print(values.get(binary[16]))


def bin_detect(binary):
	if binary[0] == "0x7f":
		if binary[1] == "0x45": 
			if binary[2] == "0x4c":
				if binary[3] == "0x46":
					print("ELF")

def bin_bit(binary):
	if binary[4] == "0x1":
		print("32Bit")
	if binary[4] == "0x2":
		print("64Bit")

def bin_endian(binary):
	if binary[5] == "0x1":
		print("Little Endian")
	if binary[5] == "0x2":
		print("Big Endian")

main()