import fastf1 as ff1
import matplotlib.pyplot as plt

def GetGraphF1():
    UserSessionY = input("Hello ! Select a year please!")
    UserSessionC = input("Hello ! Select a circuit please!")
    UserSessionE = input("Hello ! Select a session please!")
    race = ff1.get_session(int(UserSessionY),UserSessionC, UserSessionE)
    race.load()
    UserDriver = input("Pick a driver! AAA")


race = ff1.get_session(2024,'Monza','R')
race.load()
