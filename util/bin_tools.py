def little_endian(mem):
	addr = list()
	lil_addr = list()
	i = len(mem) - 1
	while i >= 0:
		print (i)
		addr.append(mem[i])
		i -=  1

	for _row in add:
		if _row == "0x0":
			continue
		else:
			lil_addr.append()

	return addr	


def big_endian(mem):
	offset = "0x"
	for _row in mem:
		_por = _row.split("x")[1]
		offset = offset + _por
	offset = offset.split("0")[1].split("x")[1]
	addr = "0x" + offset
	return addr