import matplotlib.pyplot as plt 
from mpl_toolkits.basemap import Basemap
from matplotlib.patches import Polygon
from matplotlib import path

fig, ax = plt.subplots(figsize=(8,8))
fig.tight_layout()

m = Basemap(resolution= 'c', projection= 'mill', llcrnrlon=72.9748586247, llcrnrlat=19.1852833874, urcrnrlon=72.9771063159, urcrnrlat=19.186187752)
m.drawmapboundary(fill_color='white')

#platform coords
px1,py1 = m(72.9749069045,19.1853986498)
px2,py2 = m(72.9748975168,19.1854315819)
px3,py3 = m(72.9748854468,19.1854708471)
px4,py4 = m(72.9754264149,19.1856193582)
px5,py5 = m(72.9754398259,19.1855762931)
px6,py6 = m(72.9754518958,19.185537028)

px7,py7 = m(72.9761506113,19.1857396868)
px8,py8 = m(72.9761372002,19.1857776853)
px9,py9 = m(72.9761237892,19.1858131506)
px10,py10 = m(72.9770652446,19.1860677403)
px11,py11 = m(72.9770786556,19.1860335417)
px12,py12 = m(72.9770893844,19.1859968099)

#staircase coords
sx1,sy1 = m(72.9751467946,19.1854933296)
sx2,sy2 = m(72.9751414301,19.1855123289)
sx3,sy3 = m(72.9752319547,19.1855357613)
sx4,sy4 = m(72.9752373191,19.1855173954)

sx5,sy5 = m(72.975524986,19.1855933925)
sx6,sy6 = m(72.9755189511,19.1856130251)
sx7,sy7 = m(72.9756865891,19.1856592566)
sx8,sy8 = m(72.9756926241,19.1856408907)

sx9,sy9 = m(72.9761841389,19.1857732522)
sx10,sy10 = m(72.9761774334,19.1857960513)
sx11,sy11 = m(72.9763350132,19.1858378496)
sx12,sy12 = m(72.9763430598,19.1858144172)

sx13,sy13 = m(72.9763631764,19.1858226502)
sx14,sy14 = m(72.9763564708,19.1858422828)
sx15,sy15 = m(72.9765214267,19.185885981)
sx16,sy16 = m(72.9765281322,19.1858657152)

sx17,sy17 = m(72.9766804943,19.1859124464)
sx18,sy18 = m(72.9766747946,19.1859320789)
sx19,sy19 = m(72.9768333802,19.1859748272)
sx20,sy20 = m(72.9768394151,19.1859561446)

#bridge coords
bx1,by1 = m(72.9751514884,19.1853989665)
bx2,by2 = m(72.9750871154,19.185606692)
bx3,by3 = m(72.9751099142,19.1856130251)
bx4,by4 = m(72.9751742872,19.1854052996)

bx5,by5 = m(72.9755341852,19.1855026957)
bx6,by6 = m(72.9754698122,19.185712321)
bx7,by7 = m(72.9754905993,19.1857167541)
bx8,by8 = m(72.9755556428,19.1855090288)

bx9,by9 = m(72.9763670111,19.1857319535)
bx10,by10 = m(72.976301297,19.1859371454)
bx11,by11 = m(72.976328119,19.1859472783)
bx12,by12 = m(72.9763951743,19.1857395532)

bx13,by13 = m(72.9768618786,19.1858674815)
bx14,by14 = m(72.9767934823,19.1860676068)
bx15,by15 = m(72.9768243277,19.1860752064)
bx16,by16 = m(72.9768940651,19.1858776145)

polyp1 = Polygon([(px1,py1),(px2,py2),(px5,py5),(px6,py6)],edgecolor = 'black',linewidth=1,facecolor = 'grey')
polyp2 = Polygon([(px2,py2),(px3,py3),(px4,py4),(px5,py5)],edgecolor = 'black',linewidth=1,facecolor = 'grey')
polyp3 = Polygon([(px6,py6),(px5,py5),(px8,py8),(px7,py7)],edgecolor = 'black',linewidth=1,facecolor = 'grey')
polyp4 = Polygon([(px4,py4),(px5,py5),(px8,py8),(px9,py9)],edgecolor = 'black',linewidth=1,facecolor = 'grey')
polyp5 = Polygon([(px7,py7),(px8,py8),(px11,py11),(px12,py12)],edgecolor = 'black',linewidth=1,facecolor = 'grey')
polyp6 = Polygon([(px8,py8),(px9,py9),(px10,py10),(px11,py11)],edgecolor = 'black',linewidth=1,facecolor = 'grey')
polys1 = Polygon([(sx1,sy1),(sx2,sy2),(sx3,sy3),(sx4,sy4)],edgecolor = 'black',linewidth=0.5,facecolor = '#D3D3D3',linestyle="--")
polys2 = Polygon([(sx5,sy5),(sx6,sy6),(sx7,sy7),(sx8,sy8)],edgecolor = 'black',linewidth=0.5,facecolor = '#D3D3D3',linestyle="--")
polys3 = Polygon([(sx9,sy9),(sx10,sy10),(sx11,sy11),(sx12,sy12)],edgecolor = 'black',linewidth=0.5,facecolor = '#D3D3D3',linestyle="--")
polys4 = Polygon([(sx13,sy13),(sx14,sy14),(sx15,sy15),(sx16,sy16)],edgecolor = 'black',linewidth=0.5,facecolor = '#D3D3D3',linestyle="--")
polys5 = Polygon([(sx17,sy17),(sx18,sy18),(sx19,sy19),(sx20,sy20)],edgecolor = 'black',linewidth=0.5,facecolor = '#D3D3D3',linestyle="--")
polyb1 = Polygon([(bx1,by1),(bx2,by2),(bx3,by3),(bx4,by4)],edgecolor = 'black',linewidth=0.5,facecolor = '#A9A9A9',linestyle="--")
polyb2 = Polygon([(bx5,by5),(bx6,by6),(bx7,by7),(bx8,by8)],edgecolor = 'black',linewidth=0.5,facecolor = '#A9A9A9',linestyle="--")
polyb3 = Polygon([(bx9,by9),(bx10,by10),(bx11,by11),(bx12,by12)],edgecolor = 'black',linewidth=0.5,facecolor = '#A9A9A9',linestyle="--")
polyb4 = Polygon([(bx13,by13),(bx14,by14),(bx15,by15),(bx16,by16)],edgecolor = 'black',linewidth=0.5,facecolor = '#A9A9A9',linestyle="--")

plt.gca().add_patch(polyp1)
plt.gca().add_patch(polyp2)
plt.gca().add_patch(polyp3)
plt.gca().add_patch(polyp4)
plt.gca().add_patch(polyp5)
plt.gca().add_patch(polyp6)
plt.gca().add_patch(polys1)
plt.gca().add_patch(polys2)
plt.gca().add_patch(polys3)
plt.gca().add_patch(polys4)
plt.gca().add_patch(polys5)
plt.gca().add_patch(polyb1)
plt.gca().add_patch(polyb2)
plt.gca().add_patch(polyb3)
plt.gca().add_patch(polyb4)

plt.show()