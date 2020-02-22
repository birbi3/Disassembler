def little_endian(mem):
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
	offset = "0x"
	for _row in mem:
		_por = _row.split("x")[1]
		offset = offset + _por
	offset = offset.split("0")[1].split("x")[1]
	addr = "0x" + offset
	return addr