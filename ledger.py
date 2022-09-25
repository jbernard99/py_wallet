import datetime
from transaction import Transaction

class Ledger():

	def __init__(self, name):
		self.name = name
		self.transactions = []

	def __str__(self):
		tstr = (f"			  Ledger : {self.name}\n"
				"			________________________\n")

		for transaction in self.transactions:
			tstr = tstr + str(transaction) + "\n"

		tstr = tstr + "	_________________________________________________\n\n"
		return (tstr)

	def add_transaction(self, transaction):
		self.transactions.append(transaction)

		