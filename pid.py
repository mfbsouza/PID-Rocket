class PID:
	def __init__(self, kp, ki, kd, setpoint, out_min_value, out_max_value) -> None:

		# initial values
		self.Kp = kp
		self.Ki = ki
		self.Kd = kd

		self.setpoint = setpoint
		self.out_min_value = out_min_value
		self.out_max_value = out_max_value

		# compute variables
		self.i_error = 0
		self.output = 0
		self.prev_time = 0
		self.prev_error = 0
	
	def update_gains(self, kp, ki, kd):
		self.Kp = kp
		self.Ki = ki
		self.Kd = kd
		
	def update_setpoint(self, setpoint):
		self.setpoint = setpoint

	def update_output_limits(self, min_value, max_value):
		self.out_max_value = max_value
		self.out_min_value = min_value

	def __map(self, value):
		slope = (self.out_max_value - self.out_min_value)/(1.0 * self.setpoint)
		mapped_value = (slope * value) + self.out_min_value
		return mapped_value
	
	def compute(self, current_time, measurement):

		# time variation since last compute
		delta_time = current_time - self.prev_time

		# error signal
		error = self.setpoint - measurement

		# proportional error
		p_error = self.Kp * error

		# integral error
		# TODO: implement better way to avoid integral wind-up
		if error < 20 and error > -20:
			self.i_error = self.i_error + (self.Ki * error)
		else:
			self.i_error = 0

		# derivative error
		# TODO: implment anti derivative kick
		d_error = self.Kd * (error - self.prev_error)/delta_time

		self.output = p_error + d_error + self.i_error
		self.output = self.__map(self.output)

		# clamp the output
		if self.output > self.out_max_value:
			self.output = self.out_max_value

		elif self.output < self.out_min_value:
			self.output = self.out_min_value
		
		# remember some variables for next time
		self.prev_error = error
		self.prev_time = current_time

		return self.output

