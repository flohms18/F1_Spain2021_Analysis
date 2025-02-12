import matplotlib.pyplot as plt
import ergast_py

e = ergast_py.Ergast()

plt.figure(figsize=(20, 6))


standings = e.season(2024).round(24).get_constructor_standings()


for constructor in standings:
    for team in constructor.constructor_standings:
        TeamName = team.constructor.name
        TeamPoints = team.points
        plt.bar(TeamName, TeamPoints, color='blue')
        plt.gca().invert_yaxis()
        
plt.xlabel("Team Name")
plt.ylabel("Points")

plt.title("F1 24 Constructor Standings after Round 24")
plt.legend()
plt.grid(True)
plt.show()
        
        






