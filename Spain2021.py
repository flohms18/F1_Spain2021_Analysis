import fastf1 as ff1
import matplotlib.pyplot as plt

race = ff1.get_session(2021,'Spain','R')
race.load()

plt.figure(figsize=(10, 6))

drivers = ['VER','HAM']

for driver in drivers : 
    car_lap = race.laps.pick_drivers(driver)
    LapNumber = car_lap['LapNumber']
    LapTime = car_lap['LapTime'].dt.total_seconds()

    if driver == "VER":
        plt.plot(LapNumber, LapTime, label=driver, color='#0600EF')
    else : 
        plt.plot(LapNumber, LapTime, label=driver, color='#00D2BE')

        

plt.xlabel("Lap")
plt.ylabel("Time")
plt.title("Hamilton v Verstappen")
plt.legend()
plt.grid(True)
plt.show()