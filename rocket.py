class Rocket:
    def __init__(self, mass) -> None:
        
        # intial values
        self.y_pos      = 0
        self.speed      = 0
        self.prev_time  = 0

        # Rocket's weight force
        self.mass = mass
        self.gravity = -9.8
        self.weight_force = self.mass * self.gravity
        
        # Rocket's truster
        self.truster_on = True
        self.trust_force = 198

        # test flag
        self.truster_off = False
    
    def __update_truster(self, height):
        if (self.y_pos >= height):
            self.trust_force = 0
            self.truster_on = False
    
    def update(self, current_time):
        # calculating the time variation since last update
        delta_time = current_time - self.prev_time
        self.prev_time = current_time

        # turn off the "truster" at 125m height
        if (self.y_pos >= 125):
            self.trust_force = 0
            self.truster_off = True
        elif (not self.truster_off):
            self.trust_force = 198

        # calculating the resulting forces on the rocket and its acceleration
        resulting_force = self.weight_force + self.trust_force
        accel = resulting_force/self.mass

        # calculating the current position and speed
        new_y = self.y_pos + (self.speed * delta_time) + (0.5 * accel * delta_time**2)
        self.speed = self.speed + (accel * delta_time)

        # floor
        if new_y <= 0:
            self.y_pos = 0
            self.speed = 0
            self.trust_force = - self.weight_force
        else:
            self.y_pos = new_y

        return [self.y_pos, self.speed, accel]

def demo():
    import matplotlib.pylab as plt

    y_vals     = []
    speed_vals = []
    accel_vals = []
    x_vals     = []
    time       = 0.0

    simulation_time = 20.0
    rocket_mass     = 10

    rocket = Rocket(rocket_mass)

    while(time <= simulation_time):
        y, speed, accel = rocket.update(time)
        y_vals.append(y)
        speed_vals.append(speed)
        accel_vals.append(accel)
        x_vals.append(time)
        time = time + 0.01

    # ploting simulation data
    _, ax = plt.subplots()
    ax.plot(x_vals, y_vals, label="height (meters)")
    ax.plot(x_vals, speed_vals, label="speed (m/s)")
    ax.plot(x_vals, accel_vals, label="acceleration (m/s²)")
    ax.set(xlabel='time (s)')
    ax.grid()
    plt.legend()
    plt.show()

if __name__ == "__main__":
    demo()
