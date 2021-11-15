class Rocket:
	def __init__(self, mass) -> None:
		
		# intial values
		self.y_pos = 0
		self.speed = 0
		self.accel = 0
		self.prev_time = 0

		# Rocket's weight force
		self.mass = mass
		self.gravity = -9.8
		self.weight_force = self.mass * self.gravity
		
		# Rocket's truster
		self.trust_force = 0
		self.max_trust_force = 5.5 * (-self.weight_force)

	def get_height(self):
		return self.y_pos
	
	def update(self, current_time, gas_pedal):
		# calculating the time variation since last update
		delta_time = current_time - self.prev_time
		self.prev_time = current_time

		# calculating the trust force
		self.trust_force = gas_pedal * self.max_trust_force

		# calculating the resulting forces on the rocket and its acceleration
		resulting_force = self.weight_force + self.trust_force
		self.accel = resulting_force/self.mass

		# calculating the current position and speed
		new_y = self.y_pos + (self.speed * delta_time) + (0.5 * self.accel * delta_time**2)
		self.speed = self.speed + (self.accel * delta_time)

		# floor
		if new_y <= 0:
			self.y_pos = 0
			self.speed = 0
			self.accel = 0
		else:
			self.y_pos = new_y

		return [self.y_pos, self.speed, self.accel]

def demo():
	import matplotlib.pylab as plt

	height_vals = []
	speed_vals = []
	accel_vals = []
	x_vals = []
	time = 0.0
	pedal = 1.0

	simulation_time = 40.0
	rocket_mass = 10

	rocket = Rocket(rocket_mass)

	while (time <= simulation_time):
		height, speed, accel = rocket.update(time, pedal)

		height_vals.append(height)
		speed_vals.append(speed)
		accel_vals.append(accel)
		x_vals.append(time)

		# a bit simulation tests
		if (height >= 125):
			pedal = 0.0
		elif (time >= 21.0 and time < 22.0):
			pedal = 1.0
		time = time + 0.01

	# ploting simulation data
	_, ax = plt.subplots()
	ax.plot(x_vals, height_vals, label="height (meters)")
	ax.plot(x_vals, speed_vals, label="speed (m/s)")
	ax.plot(x_vals, accel_vals, label="acceleration (m/s²)")
	ax.set(xlabel='time (s)')
	ax.grid()
	plt.legend()
	plt.show()

if __name__ == "__main__":
	demo()
