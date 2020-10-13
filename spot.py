import board

class Spot:
	def __init__ (self, x, y, x_max, y_max):
		self.x = x
		self.y = y
		if x == x_max - 1:
			self.x_options = [-1, 0]
		elif x == 0:
			self.x_options = [0, 1]
		else:
			self.x_options = [-1, 0, 1]

		if y == y_max - 1:
			self.y_options = [-1, 0]
		elif y == 0:
			self.y_options = [0, 1]
		else:
			self.y_options = [-1, 0, 1]
		#print("spot \t x:" , self.x, "\t x_op:", self.x_options, "\t y:", self.y, "\t y_op:", self.y_options)
	
	def get_x_options(self):
		return self.x_options

	def get_y_options(self):
		return self.y_options
	
	def get_x(self):
		return self.x
	
	def get_y(self):
		return self.y
