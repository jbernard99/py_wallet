import datetime

class Transaction():

	def __init__(self, date, value, description, is_in):
		self.date = date
		self.value = value
		self.description = description
		self.is_depot = is_in

	def __str__(self):
		return (f"{self.date} | {self.value} | {self.description}\n")
