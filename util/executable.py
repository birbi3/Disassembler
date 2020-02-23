def get_executable(binary, arch, entry, section):
	"""
	Will get all of the excuteable data for binary
	args:
		entry (string): the entry point of the binary 
		section (string): the section header offset
	"""
	executable_data = list()
	i = entry
	while i <= section:
		executable_data.append(binary[i])
	return executable_data