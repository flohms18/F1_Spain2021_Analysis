import fastf1 as ff1
import matplotlib.pyplot as plt

race = ff1.get_session(2023,'Sahkir','Q')
race.load()


MaxSpeed = race.laps.pick_drivers('VER').pick_laps(3).get_car_data()['Speed']
MaxDistance = race.laps.pick_drivers('VER').pick_laps(3).get_car_data().add_distance()['Distance']


print(MaxSpeed)
print(MaxDistance)