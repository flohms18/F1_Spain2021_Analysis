import fastf1 as ff1
import matplotlib.pyplot as mpl

race = ff1.get_session(2019,'Monza','R')
race.load()
print(race.laps.pick_drivers('LEC'))


