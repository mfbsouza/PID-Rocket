from rocket import Rocket
from pid import PID
import matplotlib.pylab as plt

def main():

    kp = 1.5
    kd = 2.7
    ki = 0.0115

    height_vals = []
    speed_vals  = []
    accel_vals  = []
    pid_output  = []
    setpoint    = []
    x_vals      = []

    time            = 0.01
    simulation_time = 90.0  # 90 seconds
    rocket_mass     = 10    # 10kg
    target_height   = 125   # 125 meters

    rocket_ship     = Rocket(rocket_mass)
    pid_controller  = PID(kp, ki, kd, target_height, 0.0, 1.0)

    while (time <= simulation_time):
        gas_pedal = pid_controller.compute(time, rocket_ship.get_height())
        height, speed, accel = rocket_ship.update(time, gas_pedal)

        height_vals.append(height)
        speed_vals.append(speed)
        accel_vals.append(accel)
        pid_output.append(100*gas_pedal)
        setpoint.append(target_height)
        x_vals.append(time)

        time = time + 0.01

    # ploting

    _, ax = plt.subplots()
    ax.plot(x_vals, height_vals, label="height (meters)")
    ax.plot(x_vals, speed_vals, label="speed (m/s)")
    ax.plot(x_vals, accel_vals, label="acceleration (m/s²)")
    ax.plot(x_vals, pid_output, label="PID output")
    ax.plot(x_vals, setpoint, label="setpoint")
    ax.set(xlabel='time (s)')
    ax.grid()
    plt.legend()
    plt.show()

if __name__ == "__main__":
    main()

