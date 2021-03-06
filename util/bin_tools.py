def little_endian(mem):
	"""
	Returns memory address formatted in little endian 
	"""
	addr = list()
	lil_addr = "0x"
	i = len(mem) - 1
	while i >= 0:
		addr.append(mem[i])
		i -=  1
	for _row in addr:
		_row = _row.split("x")[1]
		lil_addr = lil_addr + _row

	return lil_addr	


def big_endian(mem):
	"""
	Returns memory address formatted in big endian
	"""
	offset = "0x"
	for _row in mem:
		_por = _row.split("x")[1]
		offset = offset + _por
	offset = offset.split("0")[1].split("x")[1]
	addr = "0x" + offset
	return addr

def mem_space(binary, start, end):
	"""
	Grabs all data from binary from start to end .
	"""
	mem = list()
	i = start
	while i <= end:
		mem.append(binary[i])
		i += 1
	return mem


def int_mem(addr):
	"""
	Returns an int version of the memory address
	"""
	return int(addr, 0)