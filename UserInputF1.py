import fastf1 as ff1
import matplotlib.pyplot as plt

def GetGraphF1():
    UserSessionY = input("Hello ! Select a year please!")
    UserSessionC = input("Hello ! Select a circuit please!")
    UserSessionE = input("Hello ! Select a session please!")

    drivers = []
    
    UserDriver = input("Pick a driver! AAA ")
    drivers.append(UserDriver)
    print(drivers)
    

    race = ff1.get_session(int(UserSessionY),UserSessionC, UserSessionE)

    race.load()


    for driver in drivers :
       car_lap = race.laps.pick_drivers(driver)
       LapTime = car_lap['LapTime'].dt.total_seconds()
       LapSession = car_lap['Time']

       plt.plot(LapSession,LapTime, label=driver)
    
    plt.xlabel("Time")
    plt.ylabel("Lap")
    plt.legend()
    plt.grid(True)

    plt.show()


GetGraphF1()

