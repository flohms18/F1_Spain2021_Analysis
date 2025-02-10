import fastf1 as ff1
import matplotlib as matplotlib



race = ff1.get_session(2021,'Spain','R')

drivers = ['HAM','VER']

race.load()

for driver in drivers:
    print(race.laps.pick_drivers(drivers))




    
