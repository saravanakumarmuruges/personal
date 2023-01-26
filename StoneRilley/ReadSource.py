import pandas as pd
import random


class ReadSource:
    source = []
    morning = []
    procast = []

    def __init__(self):
        sourcedf = pd.read_excel("Data\\Source.xlsx")
        mornigdf = sourcedf[(sourcedf["Category"] == "Morning")]
        procastdf = sourcedf[(sourcedf["Category"] == "Procastination")]
        self.source = sourcedf["Quote"].tolist()
        self.morning = mornigdf["Quote"].tolist()
        self.procast = procastdf["Quote"].tolist()

    def getgeneralquotes(self):
        return random.choice(self.source)

    def getmorningquotes(self):
        return random.choice(self.morning)

    def getprocastquotes(self):
        return random.choice(self.procast)
