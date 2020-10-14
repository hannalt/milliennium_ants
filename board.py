from spot import *
from multipledispatch import dispatch

class Board:
	def __init__ (self, x_width, y_length):
		self.x_width = x_width
		self.y_length = y_length
		self.spots = []
		self.ant_locations = []
		for y in range(y_length):
			for x in range(x_width):
				self.spots.append(Spot(x, y, self))
				
		for spot in self.spots:
			spot.find_valid_spots(self.x_width, self.y_length, self)

	def get_spot(self, x, y):
		return (self.spots[(self.x_width* y) + x])
	
	def get_x_width(self):
		return self.x_width
	
	def get_y_length(self):
		return self.y_length
	
	@dispatch(object)
	def get_spot_index(self, spot):
		return self.spots.index(spot)

	@dispatch(int, int)
	def get_spot_index(self, x, y):
		return (self.x_width * y) + x
	
	def ants_not_on_same_spot(self):
		if len(self.ant_locations) == len(set(self.ant_locations)):
			return True
		return False
	def start_locations(self, spot):
		self.ant_locations.append(self.get_spot_index(spot))
	
	def update_ant(self, old_spot, new_spot):
		index = -1
		old_spot_index = self.get_spot_index(old_spot)
		new_spot_index = self.get_spot_index(new_spot)
		for location in self.ant_locations:
			if old_spot_index == location:
				index = self.ant_locations.index(location) 
		if index == -1:
			self.ant_locations.append(new_spot_index)
		else:
			self.ant_locations[index] = new_spot_index

	def get_ant_locations(self):
		return self.ant_locations
