import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

data = pd.read_csv("food_imports.csv", index_col=0).T
xs = data.index.to_list()
ys = data.values.T.tolist()
ylabels = data.columns.values.tolist()


zipped = zip(ylabels, ys)


print(zipped)
#print(data)
#print(xs)
#print(ys)
#print(ylabels)



"""for label, plots in plot.items:
    if plot