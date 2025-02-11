import matplotlib.pyplot as plt
import ergast_py

e = ergast_py.Ergast()



standings = e.season(2024).round(24).get_constructor_standings()

for constructor in standings:
    for team in constructor.constructor_standings:
        print(team.points)


