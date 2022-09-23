from wallet_db import Database
from account import Account

class Wallet:

	def __init__(self):
		self.accounts = []
		self.db = Database()

	def create_account(self, name, value, init_value):
		acc = Account(name, value, init_value)
		self.accounts.append(acc)
		self.db.create_account(acc)

	def load_all_transactions(self):
		pass

	def load_ledger_transactions(self):
		pass
