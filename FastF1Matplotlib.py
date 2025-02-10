import fastf1 as ff1
import matplotlib.pyplot as plt

race = ff1.get_session(2023,'Sahkir','Q')
race.load()

plt.figure(figsize=(10, 6))

drivers = ['VER']


for driver in drivers:
    car_data = race.laps.pick_drivers(driver).pick_laps(3).get_car_data()
    car_data = car_data.add_distance()
    
    max_speed = car_data['Speed']
    max_distance = car_data['Distance']

    plt.plot(max_distance, max_speed, label=driver)

plt.xlabel("Distance (m)")
plt.ylabel("Vitesse (km/h)")
plt.title("Vitesse de Verstappen - Tour 3 Qualifications Bahreïn 2023")
plt.legend()
plt.grid(True)

plt.show()
