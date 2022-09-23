def account_is_double(data, name):
	for account in data:
		if (account[1] == name.lower()):
			return (1)
	return (0)