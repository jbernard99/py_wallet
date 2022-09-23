import sqlite3
import wallet_db_utils as utls

class DB():

	def __init__(self):
		self.connection = sqlite3.connect("wallet_db.db")
		self.cursor = self.connection.cursor()

	def add_transaction(self, ledger, transaction):
		self.cursor.execute(f"""
			INSERT INTO {ledger} VALUES(
			'{transaction.date}',
			'{transaction.value}',
			'{transaction.description}'
			)""")
		
	def get_ledger(self, name):
		if (self.is_account_in_db(name)):
			return (self.cursor.execute(f"SELECT * FROM {name}").fetchall())

	def create_ledger(self, name):
		self.cursor.execute(f"""
				CREATE TABLE IF NOT EXIST {name}(
				id integer PRIMARY KEY, 
				date text NOT NULL,
				value real NOT NULL,
				description text
				)""")

	def is_account_in_db(self, name):
		data = self.get_accounts()
		for account in data:
			if (account[1] == name):
				return (1)
		return (0)

	def get_accounts(self):
		return (self.cursor.execute("SELECT * FROM accounts").fetchall())
		
	def add_account(self, account):
		if not (utls.account_is_double(self.get_accounts(), account.name)):
			self.cursor.execute(f"""
				INSERT INTO accounts VALUES(
				'{account.name}',
				'{account.value}',
				'{account.initial_value}'
				)""")
			self.create_ledger_table(account.name)
		
if __name__ == "__main__":
	pass
