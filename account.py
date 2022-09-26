from ledger import Ledger

class Account():

	def __init__(self, name, initial_value):
		self.name = name
		self.value = initial_value
		self.initial_value = initial_value
		self.ledger = Ledger(name)

	def __str__(self):
		return (f"{self.name}")

	def add_value(self, value):
		self.value = self.value + value

	def remove_value(self, value):
		self.value = self.value - value

	def update_account(self):
		for t in self.ledger.transactions:
			if t.is_depot:
				self.add_value(t.value)
			else:
				self.remove_value(t.value)