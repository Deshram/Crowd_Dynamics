import matplotlib.pyplot as plt 
from mpl_toolkits.basemap import Basemap
import pandas as pd
import csv
from csv import DictReader
from collections import Counter
from geopy.distance import geodesic
import statistics
from matplotlib.patches import Polygon

fig, ax = plt.subplots(figsize=(8,8))
fig.tight_layout()

data = pd.read_csv("user_data.csv")
uid = pd.DataFrame(data, columns = ['user_id'])

with open("user_data.csv") as f:
	lon = [row["long"] for row in DictReader(f)]
	
with open("user_data.csv") as f:
	lat = [row["lat"] for row in DictReader(f)]

with open("user_data0.csv") as f:
	lon1 = [row["long"] for row in DictReader(f)]

with open("user_data0.csv") as f:
	lat1 = [row["lat"] for row in DictReader(f)]

s = []

for i in range(len(data)):
	loc1 = (lon[i],lat[i])
	loc2 = (lon1[i],lat1[i])
	s.append(int(geodesic(loc1, loc2).m)/10)

#print("average speed :"+str(round(statistics.mean(s),2))+"m/s")
a = "average speed :"+str(round(statistics.mean(s),2))+"m/s"

#print("No of people :"+str(len(data)))
b = "No of people :"+str(len(data))

m = Basemap(resolution= 'c', projection= 'mill', llcrnrlon=72.9750736484, llcrnrlat=19.1854345049, urcrnrlon=72.9770108788, urcrnrlat=19.1867088006)
m.drawmapboundary(fill_color='white')

x1,y1 = m(72.9755345773,19.1856048259)
x2,y2 = m(72.9755082285,19.1856048259)
x3,y3 = m(72.9754348282,19.1858501243)
x4,y4 = m(72.9752014531,19.1857861334)
x5,y5 = m(72.9751754276,19.1858808495)
x6,y6 = m(72.9753974321,19.1859422691)
x7,y7 = m(72.9752942785,19.1863150219)
x8,y8 = m(72.9753279155,19.1863234935)
x9,y9 = m(72.9754288267,19.1859507408)
x10,y10 = m(72.9762249033,19.1861710039)
x11,y11 = m(72.9761217497,19.1865056338)
x12,y12 = m(72.9761486594,19.1865119875)
x13,y13 = m(72.9762540554,19.1861773576)
x14,y14 = m(72.9767182466,19.1863044323)
x15,y15 = m(72.9766195779,19.1866221187)
x16,y16 = m(72.9766464876,19.1866284725)
x17,y17 = m(72.9767451562,19.1863107861)
x18,y18 = m(72.9769559484,19.1863700876)
x19,y19 = m(72.9769783731,19.186289607)
x20,y20 = m(72.9767810357,19.1862324233)
x21,y21 = m(72.9769043716,19.1858639062)
x22,y22 = m(72.9768774619,19.1858575524)
x23,y23 = m(72.9767518836,19.1862218338)
x24,y24 = m(72.97628545,19.1861011127)
x25,y25 = m(72.9764087858,19.185713534)
x26,y26 = m(72.9763818762,19.1857050623)
x27,y27 = m(72.9762562979,19.1860862873)
x28,y28 = m(72.9754602212,19.1858596704)


poly = Polygon([(x1,y1),(x2,y2),(x3,y3),(x4,y4),(x5,y5),(x6,y6),(x7,y7),(x8,y8),(x9,y9),(x10,y10),(x11,y11),(x12,y12),(x13,y13),(x14,y14),(x15,y15),(x16,y16),(x17,y17),(x18,y18),(x19,y19),(x20,y20),(x21,y21),(x22,y22),(x23,y23),(x24,y24),(x25,y25),(x26,y26),(x27,y27),(x28,y28)],edgecolor = 'black',facecolor = 'grey',linewidth=1)

for i in range(len(data)):
	x,y = m(float(lon[i]),float(lat[i]))
	m.plot(x,y,color = 'red', marker = '.')

plt.gca().add_patch(poly)
ax.set_xlabel(a+'\n'+b)
fig.suptitle('Crowd Monitoring', fontsize=20)
plt.show()