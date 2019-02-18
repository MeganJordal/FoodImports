import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

food_import_data = pd.read_csv("food_imports3.csv", thousands=',')
food_import_data = food_import_data.drop(['Unnamed: 1','Unnamed: 2'], axis=1)
food_import_data = food_import_data.drop([0, 1, 2, 3], axis = 0)
food_import_data = food_import_data.set_index('Unnamed: 0')
year_list = list(food_import_data)
import_values_list = food_import_data.values.tolist()

data = pd.read_csv("food_imports2.csv", index_col=0)


y1=import_values_list[0]
"""print(type(y1[0])
k = 0
int(k)
for k in y1:
    y = y1[k]
    y = float(y)
    y1[k] = y"""
y2=import_values_list[1]

y3=import_values_list[2]

y4=import_values_list[3]

y5=(import_values_list[4])

y6=(import_values_list[5])

y7=(import_values_list[6])

y8=(import_values_list[7])

y9=(import_values_list[8])

y10=(import_values_list[9])

y11=(import_values_list[10])
y12=(import_values_list[11])

y13=(import_values_list[12])

y14=(import_values_list[13])

y15=(import_values_list[14])


x1 = (year_list)

fig, ax = plt.subplots(figsize=(6, 8), dpi = 80, facecolor = 'w', edgecolor = 'k')

ax.set_title('click on points')
line1 = ax.plot(x1, y1, 'o', color = 'darkred', label = 'Live Animals', picker = 5)
line2 = ax.plot(x1, y2, 'o', color = 'indianred', label = 'Meats', picker = 5)
line3 = ax.plot(x1, y3, 'o', color = 'coral', label = 'Fish and Shellfish', picker = 5)
line4 = ax.plot(x1, y4, 'o', color = 'orange', label = 'Dairy', picker = 5)
line5 = ax.plot(x1, y5, 'o', color = 'darkgreen', label = 'Vegetables', picker = 5)
line6 = ax.plot(x1, y6, 'o', color = 'g', label = 'Fruits', picker = 5)
line7 = ax.plot(x1, y7, 'o', color = 'mediumseagreen', label = 'Nuts', picker = 5)
line8 = ax.plot(x1, y8, 'o', color = 'mediumspringgreen', label = 'Coffee, Teas, and Spices', picker = 5)
line9 = ax.plot(x1, y9, 'o', color = 'chartreuse', label = 'Grains', picker = 5)
line10 = ax.plot(x1, y10, 'o', color = 'midnightblue', label = 'Vegetable Oils', picker = 5)
line11 = ax.plot(x1, y11, 'o', color = 'b', label = 'Sugar and Candy', picker = 5)
line12 = ax.plot(x1, y12, 'o', color = 'slateblue', label = 'Cocoa and Chocolate', picker = 5)
line13 = ax.plot(x1, y13, 'o', color = 'cornflowerblue', label = 'Other Edible Products', picker = 5)
line14 = ax.plot(x1, y14, 'o', color = 'gold', label = 'Beverages', picker = 5)
line15 = ax.plot(x1, y15, 'o', color = 'y', label = 'Liquors', picker = 5)

plt.xticks(np.arange(0, 18, 2))
plt.yticks(np.arange(0, 1200, 100))

leg = ax.legend(loc = 'upper left', fancybox = True, shadow = True)

plt.show()

# Define the pick event and print

def showData(event):
    thisline = event.artist
    xdata = thisline.get_xdata()
    ydata = thisline.get_ydata()
    label = thisline.get_label()
    ind = event.ind
    points = tuple(zip(xdata[ind], ydata[ind]))
    print('picked points: ', label, points, event.artist)

fig.canvas.mpl_connect('pick_event', showData)



"""for i in range (len(x1)):
    plt.scatter(x1[i - 1], y1[i-1])

plt.show()
print(x1)
print(import_values_list)
print(food_import_data.index)

#def onclick(event):
#    print('%s click: button=%d, x=%d, y=%d, xdata=%f, ydata=%f' %('double' if event.dblclick))

#cid = fig.canvas.mpl_connect('button_press_event..."""