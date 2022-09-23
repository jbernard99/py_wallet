import account

class Wallet():

	def __init__(self):
		self.accounts = []

	def add_accounts(self, name, value, init_value):
		self.accounts.append(account.Account(name, value, init_value))

	def load_all_transactions(self):
		pass

	def load_ledger_transactions(self):
		pass
