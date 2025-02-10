import fastf1 as ff1
import matplotlib.pyplot as mpl

race = ff1.get_session(2024,'Monza','R')
race.load()

drivers = ['LEC','SAI']

for driver in drivers: 
    print(race.laps.pick_drivers(drivers))


