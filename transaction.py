import datetime

class Transaction():

	def __init__(self, date, value, description, is_depot):
		self.date = date
		self.dateobj = datetime.datetime.strptime(str(date), "%d%m%Y")
		self.value = value
		self.description = description
		self.is_depot = is_depot

	def __str__(self):
		txt = f"{self.dateobj.strftime('%d/%m/%Y')} | {self.description} | "
		if (self.is_depot):
			txt = txt + "+"
		else:
			txt = txt + "-"
		txt = txt + f"{self.value:.2f}"
		return (txt)

if __name__ == "__main__":
	t = Transaction(24031999, 420, "McDo", 1)
	print(t.dateobj)
	print(t)
