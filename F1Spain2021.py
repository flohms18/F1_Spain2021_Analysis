import fastf1 as ff1
import matplotlib.pyplot as plt

race = ff1.get_session(2023,'Sahkir','Q')
race.load()


MaxTelem = race.laps.pick_drivers('VER').pick_fastest()
print(MaxTelem['LapTime'])
