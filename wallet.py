from wallet_db import Database
from account import Account
import wallet_utils as utls

class Wallet:

	def __init__(self):
		self.accounts = []
		self.db = Database()
		self.load_data()

	def load_data(self):
		for acc in self.accounts:
			del acc
		self.load_accounts()
		self.load_ledgers()

	def load_accounts(self):
		for acc in self.db.get_accounts():
			self.accounts.append(Account(acc[1], acc[2], acc[3]))

	def load_ledgers(self):
		for acc in self.accounts:
			ledger = self.db.get_ledger(acc.name)
			for t in ledger:
				acc.ledger.add_transaction(t[1], t[2], t[3])

	def add_transaction(self, acc_name, date, value, desc):
		for acc in self.accounts:
			if (acc.name == acc_name):
				acc.ledger.add_transaction(date, value, desc)

	def create_account(self, name, value, init_value):
		acc = Account(name, value, init_value)
		self.accounts.append(acc)
		self.db.create_account(acc)

	def load_all_transactions(self):
		pass

	def load_ledger_transactions(self):
		pass
