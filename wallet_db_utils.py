import sqlite3

def account_is_double(data, name):
	for account in data:
		if (account[1] == name.lower()):
			return (1)
	return (0)

def is_account_in_db(data, name):
	for account in data:
		if (account[1] == name):
			return (1)
	return (0)


