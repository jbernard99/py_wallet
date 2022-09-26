import sqlite3
import wallet_db_utils as utls

class Database():
	db_file = "wallet_db.db"

	def __init__(self):
		self.connection = sqlite3.connect(self.db_file)
		self.cursor = self.connection.cursor()
		self.create_account_table()

	def create_account_table(self):
		self.cursor.execute("""
			CREATE TABLE IF NOT EXISTS accounts(
			id integer PRIMARY KEY,
			name text NOT NULL,
			initial_value real
			)""")

	def add_transaction(self, ledger, transaction):
		print(transaction)
		cmd = f"""
			INSERT INTO {ledger.name}(date, value, description, is_depot) VALUES(
			'{transaction.date}',
			'{transaction.value}',
			'{transaction.description}',
			'{transaction.is_depot}'
			)"""
		self.cursor.execute(cmd)
		self.connection.commit()
		
	def get_ledger(self, name):
		if (utls.is_account_in_db(self.get_accounts(), name)):
			return (self.cursor.execute(f"SELECT * FROM {name}").fetchall())

	def create_ledger_table(self, name):
		self.cursor.execute(f"""
				CREATE TABLE IF NOT EXISTS {name}(
				id integer NOT NULL PRIMARY KEY, 
				date text NOT NULL,
				value real NOT NULL,
				description text,
				is_depot integer
				)""")

	def get_accounts(self):
		return (self.cursor.execute("SELECT * FROM accounts").fetchall())
		
	def create_account(self, account):
		if not (utls.account_is_double(self.get_accounts(), account.name)):
			self.cursor.execute(f"""
				INSERT INTO accounts(name, initial_value) VALUES(
				'{account.name}',
				'{account.initial_value}'
				)""")
			self.create_ledger_table(account.name)
			self.connection.commit()
		
if __name__ == "__main__":
	db = Database()
