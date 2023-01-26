"""
    This Application is intended to give random quotes in the Windows screen
    which can be a refreshing lines for users
"""
import pandas as pd
import random
import pyautogui as pg
source = list(pd.read_csv("Data\\Source.csv")["Quote"])
# pg.prompt('This lets the user type in a string and press OK.')
# pg.alert(text=random.choice(source), title='Quote of the Day', button='Happy')
while True:
    a = pg.confirm(text=random.choice(source), title='Quote of the Day', buttons=['Happy', 'Nope'])
    if a == "Happy":
        break