from transaction import Transaction
from wallet_db import Database
import account

class Wallet:

	def __init__(self):
		self.accounts = []
		self.db = Database()
		self.load_data()
		self.update_accounts()

	def load_data(self):
		for acc in self.accounts:
			del acc
		self.load_accounts()
		self.load_ledgers()

	def load_accounts(self):
		for acc in self.db.get_accounts():
			self.accounts.append(account.Account(acc[1], acc[2]))

	def load_ledgers(self):
		for acc in self.accounts:
			ledger = self.db.get_ledger(acc.name)
			for t in ledger:
				py_t = Transaction(t[1], t[2], t[3], t[4])
				acc.ledger.add_transaction(py_t)

	def add_transaction(self, acc, date, value, is_depot, desc):
		t = Transaction(date, value, desc, is_depot)
		acc.ledger.add_transaction(t)
		self.db.add_transaction(acc.ledger, t)
		if is_depot:
			acc.add_value(value)
		else:
			acc.remove_value(value)

	def update_accounts(self):
		for acc in self.accounts:
			acc.update_account()

	def get_accounts(self):
		return (self.accounts)

	def create_account(self, name, init_value):
		acc = account.Account(name, init_value)
		self.accounts.append(acc)
		self.db.create_account(acc)

	def get_wallet_balance(self):
		self.update_accounts()
		total_value = 0
		for acc in self.accounts:
			total_value = total_value + acc.value
		return (total_value)
