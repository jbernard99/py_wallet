import datetime
import transaction

class Ledger():

	def __init__(self, name):
		self.name = name
		self.transactions = []

	def __str__(self):
		str = ("\n_________________________________________________\n"
		f"Ledger : {self.name}\n"
		"________________________\n")

		for transaction in self.transactions:
			str = str + str(transaction)

		str = str + "_________________________________________________\n\n"
		return (str)

	def add_transaction(self, transaction):
		self.transactions.append(transaction)

		