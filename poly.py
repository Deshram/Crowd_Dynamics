from mpl_toolkits.basemap import Basemap
import matplotlib.pyplot as plt
from matplotlib.patches import Polygon
from matplotlib import path

m = Basemap(resolution= 'c', projection= 'merc', llcrnrlon=72.9750621252, llcrnrlat=19.1857039515, urcrnrlon=72.9770045055, urcrnrlat=19.1864059784)
m.drawmapboundary(fill_color='white')

x1,y1 = m(72.9752010216,19.1857890148)
x2,y2 = m(72.9751728083,19.1858771526)
x3,y3 = m(72.9769327864,19.1863613385)
x4,y4 = m(72.9769619064,19.1862811227)
x,y = m(72.9767220795,19.1862451387)
poly = Polygon([(x1,y1),(x2,y2),(x3,y3),(x4,y4)],edgecolor = 'black',facecolor = 'grey',linewidth=1)

p = path.Path([(x1,y1),(x2,y2),(x3,y3),(x4,y4)])

if p.contains_points([(x,y)]):
	print("\ninside polygon\n")
else :
	print("\noutside polygon\n")

m.plot(x,y,color = 'red', marker = '.')
plt.gca().add_patch(poly)
plt.show()