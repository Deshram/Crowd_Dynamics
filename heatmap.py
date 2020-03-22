import matplotlib.pyplot as plt 
from mpl_toolkits.basemap import Basemap
import pandas as pd
from matplotlib.patches import Polygon
from tcs import printfunction

p1,p2,p3,p4,p5,p6,p7,p8,p9,p10,p11,p12,p13,p14,p15,p16,p17,p18,p19,p20 = printfunction()

fig, ax = plt.subplots(figsize=(8,8))
fig.tight_layout()

m = Basemap(resolution= 'c', projection= 'mill', llcrnrlon=72.9750736484, llcrnrlat=19.1854345049, urcrnrlon=72.9770108788, urcrnrlat=19.1867088006)
m.drawmapboundary(fill_color='white')

#platform coords
px1,py1 = m(72.9747986302,19.1856848672)
px2,py2 = m(72.9747838781,19.1857266656)
px3,py3 = m(72.9747718081,19.1857659307)
px4,py4 = m(72.9751768217,19.1858786596)
px5,py5 = m(72.9751902327,19.1858330614)
px6,py6 = m(72.9752023027,19.1857925297)
px7,py7 = m(72.9758594439,19.185976189)
px8,py8 = m(72.9758460328,19.1860217871)
px9,py9 = m(72.9758326218,19.1860610522)
px10,py10 = m(72.9764884219,19.1862409114)
px11,py11 = m(72.9765018329,19.1861991131)
px12,py12 = m(72.976515244,19.1861585815)
px13,py13 = m(72.9771348343,19.186337174)
px14,py14 = m(72.9771214232,19.1863777056)
px15,py15 = m(72.9771106944,19.1864119041)

#staircase coords
sx1,sy1 = m(72.9749691181,19.1857632392)
sx2,sy2 = m(72.9749657654,19.1857759053)
sx3,sy3 = m(72.9750448905,19.1857980711)
sx4,sy4 = m(72.9751334034,19.1858240368)
sx5,sy5 = m(72.9751380973,19.185810104)
sx6,sy6 = m(72.9750469022,19.1857847716)
sx7,sy7 = m(72.9752774045,19.1858545939)
sx8,sy8 = m(72.975270699,19.1858659934)
sx9,sy9 = m(72.9754222438,19.1859115916)
sx10,sy10 = m(72.975579153,19.1859552898)
sx11,sy11 = m(72.9755825058,19.1859438903)
sx12,sy12 = m(72.9754276082,19.1858989254)
sx13,sy13 = m(72.9760837436,19.1860794181)
sx14,sy14 = m(72.9760790497,19.1860952508)
sx15,sy15 = m(72.9762500406,19.1861402156)
sx16,sy16 = m(72.9764163375,19.1861832805)
sx17,sy17 = m(72.9764190197,19.186169981)
sx18,sy18 = m(72.9762527228,19.1861275495)
sx19,sy19 = m(72.9765772701,19.1862212789)
sx20,sy20 = m(72.9765732468,19.1862345783)
sx21,sy21 = m(72.9767415554,19.1862839762)
sx22,sy22 = m(72.9769138873,19.186335274)
sx23,sy23 = m(72.9769165695,19.1863238745)
sx24,sy24 = m(72.9767442376,19.1862706768)

#bridge coords
bx1,by1 = m(72.9750598103,19.1857036918)
bx2,by2 = m(72.974991414,19.1859367492)
bx3,by3 = m(72.9750101894,19.1859405491)
bx4,by4 = m(72.9750826091,19.1857074917)
bx5,by5 = m(72.975440684,19.1858062878)
bx6,by6 = m(72.9753709466,19.1860520112)
bx7,by7 = m(72.9753937453,19.1860558111)
bx8,by8 = m(72.975466165,19.1858100876)
bx9,by9 = m(72.9762721688,19.1860304788)
bx10,by10 = m(72.9761957258,19.1862673356)
bx11,by11 = m(72.9762198657,19.1862736687)
bx12,by12 = m(72.9762963087,19.1860368118)
bx13,by13 = m(72.9767616719,19.1861748728)
bx14,by14 = m(72.9766865701,19.186406663)
bx15,by15 = m(72.9767133922,19.1864117294)
bx16,by16 = m(72.9767871529,19.1861824725)

#stall coords
fx1,fy1 = m(72.9757243276,19.1859684146)
fx2,fy2 = m(72.975716281,19.1860013466)
fx3,fy3 = m(72.9757618785,19.1860114795)
fx4,fy4 = m(72.9757699252,19.1859798142)
fx5,fy5 = m(72.9759845019,19.1860380785)
fx6,fy6 = m(72.9759751141,19.1860672106)
fx7,fy7 = m(72.976011324,19.1860786101)
fx8,fy8 = m(72.9760220528,19.186049478)
fx9,fy9 = m(72.9770493389,19.1863395325)
fx10,fy10 = m(72.9770426333,19.1863648648)
fx11,fy11 = m(72.9770868898,19.1863749977)
fx12,fy12 = m(72.9770935953,19.186350932)

#p = [0,1,1,2,1,0,1,2,0,2,1,0,0,1,1,2,2,0,1,2]
a = 0
b = 0
c = 0
	
if p1[len(p1)-1] == 2:
	polyp1 = Polygon([(px1,py1),(px2,py2),(px5,py5),(px6,py6)],edgecolor = 'black',linewidth=1,facecolor = '#F6CECE',label = 'low'if a == 0 else "")
	a+=1
elif p1[len(p1)-1] == 1:
	polyp1 = Polygon([(px1,py1),(px2,py2),(px5,py5),(px6,py6)],edgecolor = 'black',linewidth=1,facecolor = '#F78181',label = 'medium'if b == 0 else "")	
	b+=1
else:
	polyp1 = Polygon([(px1,py1),(px2,py2),(px5,py5),(px6,py6)],edgecolor = 'black',linewidth=1,facecolor = '#FF2E2E',label = 'high'if c == 0 else "")	
	c+=1

if p2[len(p2)-1] == 2:
	polyp2 = Polygon([(px2,py2),(px3,py3),(px4,py4),(px5,py5)],edgecolor = 'black',linewidth=1,facecolor = '#F6CECE',label = 'low'if a == 0 else "")
	a+=1
elif p2[len(p2)-1] == 1:
	polyp2 = Polygon([(px2,py2),(px3,py3),(px4,py4),(px5,py5)],edgecolor = 'black',linewidth=1,facecolor = '#F78181',label = 'medium'if b == 0 else "")
	b+=1
else:
	polyp2 = Polygon([(px2,py2),(px3,py3),(px4,py4),(px5,py5)],edgecolor = 'black',linewidth=1,facecolor = '#FF2E2E',label = 'high'if c == 0 else "")
	c+=1

if p3[len(p3)-1] == 2:
	polyp3 = Polygon([(px6,py6),(px5,py5),(px8,py8),(px7,py7)],edgecolor = 'black',linewidth=1,facecolor = '#F6CECE',label = 'low'if a == 0 else "")
	a+=1
elif p3[len(p3)-1] == 1:
	polyp3 = Polygon([(px6,py6),(px5,py5),(px8,py8),(px7,py7)],edgecolor = 'black',linewidth=1,facecolor = '#F78181',label = 'medium'if b == 0 else "")
	b+=1
else:
	polyp3 = Polygon([(px6,py6),(px5,py5),(px8,py8),(px7,py7)],edgecolor = 'black',linewidth=1,facecolor = '#FF2E2E',label = 'high'if c == 0 else "")
	c+=1

if p4[len(p4)-1] == 2:
	polyp4 = Polygon([(px4,py4),(px5,py5),(px8,py8),(px9,py9)],edgecolor = 'black',linewidth=1,facecolor = '#F6CECE',label = 'low'if a == 0 else "")
	a+=1
elif p4[len(p4)-1] == 1:
	polyp4 = Polygon([(px4,py4),(px5,py5),(px8,py8),(px9,py9)],edgecolor = 'black',linewidth=1,facecolor = '#F78181',label = 'medium'if b == 0 else "")
	b+=1
else:
	polyp4 = Polygon([(px4,py4),(px5,py5),(px8,py8),(px9,py9)],edgecolor = 'black',linewidth=1,facecolor = '#FF2E2E',label = 'high'if c == 0 else "")
	c+=1

if p5[len(p5)-1] == 2:
	polyp5 = Polygon([(px7,py7),(px8,py8),(px11,py11),(px12,py12)],edgecolor = 'black',linewidth=1,facecolor = '#F6CECE',label = 'low'if a == 0 else "")
	a+=1
elif p5[len(p5)-1] == 1:
	polyp5 = Polygon([(px7,py7),(px8,py8),(px11,py11),(px12,py12)],edgecolor = 'black',linewidth=1,facecolor = '#F78181',label = 'medium'if b == 0 else "")
	b+=1
else:
	polyp5 = Polygon([(px7,py7),(px8,py8),(px11,py11),(px12,py12)],edgecolor = 'black',linewidth=1,facecolor = '#FF2E2E',label = 'high'if c == 0 else "")
	c+=1

if p6[len(p6)-1] == 2:
	polyp6 = Polygon([(px8,py8),(px9,py9),(px10,py10),(px11,py11)],edgecolor = 'black',linewidth=1,facecolor = '#F6CECE',label = 'low'if a == 0 else "")
	a+=1
elif p6[len(p6)-1] == 1:
	polyp6 = Polygon([(px8,py8),(px9,py9),(px10,py10),(px11,py11)],edgecolor = 'black',linewidth=1,facecolor = '#F78181',label = 'medium'if b == 0 else "")
	b+=1
else:
	polyp6 = Polygon([(px8,py8),(px9,py9),(px10,py10),(px11,py11)],edgecolor = 'black',linewidth=1,facecolor = '#FF2E2E',label = 'high'if c == 0 else "")
	c+=1

if p7[len(p7)-1] == 2:
	polyp7 = Polygon([(px10,py10),(px11,py11),(px14,py14),(px15,py15)],edgecolor = 'black',linewidth=1,facecolor = '#F6CECE',label = 'low'if a == 0 else "")
	a+=1
elif p7[len(p7)-1] == 1:
	polyp7 = Polygon([(px10,py10),(px11,py11),(px14,py14),(px15,py15)],edgecolor = 'black',linewidth=1,facecolor = '#F78181',label = 'medium'if b == 0 else "")
	b+=1
else:
	polyp7 = Polygon([(px10,py10),(px11,py11),(px14,py14),(px15,py15)],edgecolor = 'black',linewidth=1,facecolor = '#FF2E2E',label = 'high'if c == 0 else "")
	c+=1

if p8[len(p8)-1] == 2:
	polyp8 = Polygon([(px12,py12),(px11,py11),(px14,py14),(px13,py13)],edgecolor = 'black',linewidth=1,facecolor = '#F6CECE',label = 'low'if a == 0 else "")
	a+=1
elif p8[len(p8)-1] == 1:
	polyp8 = Polygon([(px12,py12),(px11,py11),(px14,py14),(px13,py13)],edgecolor = 'black',linewidth=1,facecolor = '#F78181',label = 'medium'if b == 0 else "")
	b+=1
else:
	polyp8 = Polygon([(px12,py12),(px11,py11),(px14,py14),(px13,py13)],edgecolor = 'black',linewidth=1,facecolor = '#FF2E2E',label = 'high'if c == 0 else "")
	c+=1

if p9[len(p9)-1] == 2:
	polys1 = Polygon([(sx1,sy1),(sx2,sy2),(sx3,sy3),(sx6,sy6)],edgecolor = 'black',linewidth=0.5,facecolor = '#F6CECE',label = 'low'if a == 0 else "",linestyle="--")
	a+=1
elif p9[len(p9)-1] == 1:
	polys1 = Polygon([(sx1,sy1),(sx2,sy2),(sx3,sy3),(sx6,sy6)],edgecolor = 'black',linewidth=0.5,facecolor = '#F78181',label = 'medium'if b == 0 else "",linestyle="--")
	b+=1
else:
	polys1 = Polygon([(sx1,sy1),(sx2,sy2),(sx3,sy3),(sx6,sy6)],edgecolor = 'black',linewidth=0.5,facecolor = '#FF2E2E',label = 'high'if c == 0 else "",linestyle="--")
	c+=1

if p10[len(p10)-1] == 2:
	polys2 = Polygon([(sx3,sy3),(sx6,sy6),(sx5,sy5),(sx4,sy4)],edgecolor = 'black',linewidth=0.5,facecolor = '#F6CECE',label = 'low'if a == 0 else "",linestyle="--")
	a+=1
elif p10[len(p10)-1] == 1:
	polys2 = Polygon([(sx3,sy3),(sx6,sy6),(sx5,sy5),(sx4,sy4)],edgecolor = 'black',linewidth=0.5,facecolor = '#F78181',label = 'medium'if b == 0 else "",linestyle="--")
	b+=1
else:
	polys2 = Polygon([(sx3,sy3),(sx6,sy6),(sx5,sy5),(sx4,sy4)],edgecolor = 'black',linewidth=0.5,facecolor = '#FF2E2E',label = 'high'if c == 0 else "",linestyle="--")
	c+=1

if p11[len(p11)-1] == 2:
	polys3 = Polygon([(sx7,sy7),(sx8,sy8),(sx9,sy9),(sx12,sy12)],edgecolor = 'black',linewidth=0.5,facecolor = '#F6CECE',label = 'low'if a == 0 else "",linestyle="--")
	a+=1
elif p11[len(p11)-1] == 1:
	polys3 = Polygon([(sx7,sy7),(sx8,sy8),(sx9,sy9),(sx12,sy12)],edgecolor = 'black',linewidth=0.5,facecolor = '#F78181',label = 'medium'if b == 0 else "",linestyle="--")
	b+=1
else:
	polys3 = Polygon([(sx7,sy7),(sx8,sy8),(sx9,sy9),(sx12,sy12)],edgecolor = 'black',linewidth=0.5,facecolor = '#FF2E2E',label = 'high'if c == 0 else "",linestyle="--")	
	c+=1

if p12[len(p12)-1] == 2:
	polys4 = Polygon([(sx9,sy9),(sx12,sy12),(sx11,sy11),(sx10,sy10)],edgecolor = 'black',linewidth=0.5,facecolor = '#F6CECE',label = 'low'if a == 0 else "",linestyle="--")
	a+=1
elif p12[len(p12)-1] == 1:
	polys4 = Polygon([(sx9,sy9),(sx12,sy12),(sx11,sy11),(sx10,sy10)],edgecolor = 'black',linewidth=0.5,facecolor = '#F78181',label = 'medium'if b == 0 else "",linestyle="--")
	b+=1
else:
	polys4 = Polygon([(sx9,sy9),(sx12,sy12),(sx11,sy11),(sx10,sy10)],edgecolor = 'black',linewidth=0.5,facecolor = '#FF2E2E',label = 'high'if c == 0 else "",linestyle="--")
	c+=1

if p13[len(p13)-1] == 2:
	polys5 = Polygon([(sx13,sy13),(sx14,sy14),(sx15,sy15),(sx18,sy18)],edgecolor = 'black',linewidth=0.5,facecolor = '#F6CECE',label = 'low'if a == 0 else "",linestyle="--")
	a+=1
elif p13[len(p13)-1] == 1:
	polys5 = Polygon([(sx13,sy13),(sx14,sy14),(sx15,sy15),(sx18,sy18)],edgecolor = 'black',linewidth=0.5,facecolor = '#F78181',label = 'medium'if b == 0 else "",linestyle="--")
	b+=1
else:
	polys5 = Polygon([(sx13,sy13),(sx14,sy14),(sx15,sy15),(sx18,sy18)],edgecolor = 'black',linewidth=0.5,facecolor = '#FF2E2E',label = 'high'if c == 0 else "",linestyle="--")
	c+=1

if p14[len(p14)-1] == 2:
	polys6 = Polygon([(sx15,sy15),(sx18,sy18),(sx17,sy17),(sx16,sy16)],edgecolor = 'black',linewidth=0.5,facecolor = '#F6CECE',label = 'low'if a == 0 else "",linestyle="--")
	a+=1
elif p14[len(p14)-1] == 1:
	polys6 = Polygon([(sx15,sy15),(sx18,sy18),(sx17,sy17),(sx16,sy16)],edgecolor = 'black',linewidth=0.5,facecolor = '#F78181',label = 'medium'if b == 0 else "",linestyle="--")
	b+=1
else:
	polys6 = Polygon([(sx15,sy15),(sx18,sy18),(sx17,sy17),(sx16,sy16)],edgecolor = 'black',linewidth=0.5,facecolor = '#FF2E2E',label = 'high'if c == 0 else "",linestyle="--")
	c+=1

if p15[len(p15)-1] == 2:
	polys7 = Polygon([(sx19,sy19),(sx20,sy20),(sx21,sy21),(sx24,sy24)],edgecolor = 'black',linewidth=0.5,facecolor = '#F6CECE',label = 'low'if a == 0 else "",linestyle="--")
	a+=1
elif p15[len(p15)-1] == 1:
	polys7 = Polygon([(sx19,sy19),(sx20,sy20),(sx21,sy21),(sx24,sy24)],edgecolor = 'black',linewidth=0.5,facecolor = '#F78181',label = 'medium'if b == 0 else "",linestyle="--")
	b+=1
else:
	polys7 = Polygon([(sx19,sy19),(sx20,sy20),(sx21,sy21),(sx24,sy24)],edgecolor = 'black',linewidth=0.5,facecolor = '#FF2E2E',label = 'high'if c == 0 else "",linestyle="--")
	c+=1

if p16[len(p16)-1] == 2:
	polys8 = Polygon([(sx21,sy21),(sx24,sy24),(sx23,sy23),(sx22,sy22)],edgecolor = 'black',linewidth=0.5,facecolor = '#F6CECE',label = 'low'if a == 0 else "",linestyle="--")
	a+=1
elif p16[len(p16)-1] == 1:
	polys8 = Polygon([(sx21,sy21),(sx24,sy24),(sx23,sy23),(sx22,sy22)],edgecolor = 'black',linewidth=0.5,facecolor = '#F78181',label = 'medium'if b == 0 else "",linestyle="--")
	b+=1
else:
	polys8 = Polygon([(sx21,sy21),(sx24,sy24),(sx23,sy23),(sx22,sy22)],edgecolor = 'black',linewidth=0.5,facecolor = '#FF2E2E',label = 'high'if c == 0 else "",linestyle="--")
	c+=1

if p17[len(p17)-1] == 2:
	polyb1 = Polygon([(bx1,by1),(bx2,by2),(bx3,by3),(bx4,by4)],edgecolor = 'black',linewidth=0.5,facecolor = '#F6CECE',label = 'low'if a == 0 else "",linestyle="--")
	a+=1
elif p17[len(p17)-1] == 1:
	polyb1 = Polygon([(bx1,by1),(bx2,by2),(bx3,by3),(bx4,by4)],edgecolor = 'black',linewidth=0.5,facecolor = '#F78181',label = 'medium'if b == 0 else "",linestyle="--")
	b+=1
else:
	polyb1 = Polygon([(bx1,by1),(bx2,by2),(bx3,by3),(bx4,by4)],edgecolor = 'black',linewidth=0.5,facecolor = '#FF2E2E',label = 'high'if c == 0 else "",linestyle="--")
	c+=1

if p18[len(p18)-1] == 2:
	polyb2 = Polygon([(bx5,by5),(bx6,by6),(bx7,by7),(bx8,by8)],edgecolor = 'black',linewidth=0.5,facecolor = '#F6CECE',label = 'low'if a == 0 else "",linestyle="--")
	a+=1
elif p18[len(p18)-1] == 1:
	polyb2 = Polygon([(bx5,by5),(bx6,by6),(bx7,by7),(bx8,by8)],edgecolor = 'black',linewidth=0.5,facecolor = '#F78181',label = 'medium'if b == 0 else "",linestyle="--")
	b+=1
else:
	polyb2 = Polygon([(bx5,by5),(bx6,by6),(bx7,by7),(bx8,by8)],edgecolor = 'black',linewidth=0.5,facecolor = '#FF2E2E',label = 'high'if c == 0 else "",linestyle="--")
	c+=1

if p19[len(p19)-1] == 2:
	polyb3 = Polygon([(bx9,by9),(bx10,by10),(bx11,by11),(bx12,by12)],edgecolor = 'black',linewidth=0.5,facecolor = '#F6CECE',label = 'low'if a == 0 else "",linestyle="--")
	a+=1
elif p19[len(p19)-1] == 1:
	polyb3 = Polygon([(bx9,by9),(bx10,by10),(bx11,by11),(bx12,by12)],edgecolor = 'black',linewidth=0.5,facecolor = '#F78181',label = 'medium'if b == 0 else "",linestyle="--")
	b+=1
else:
	polyb3 = Polygon([(bx9,by9),(bx10,by10),(bx11,by11),(bx12,by12)],edgecolor = 'black',linewidth=0.5,facecolor = '#FF2E2E',label = 'high'if c == 0 else "",linestyle="--")
	c+=1

if p20[len(p20)-1] == 2:
	polyb4 = Polygon([(bx13,by13),(bx14,by14),(bx15,by15),(bx16,by16)],edgecolor = 'black',linewidth=0.5,facecolor = '#F6CECE',label = 'low'if a == 0 else "",linestyle="--")
	a+=1
elif p20[len(p20)-1] == 1:
	polyb4 = Polygon([(bx13,by13),(bx14,by14),(bx15,by15),(bx16,by16)],edgecolor = 'black',linewidth=0.5,facecolor = '#F78181',label = 'medium'if b == 0 else "",linestyle="--")
	b+=1
else:
	polyb4 = Polygon([(bx13,by13),(bx14,by14),(bx15,by15),(bx16,by16)],edgecolor = 'black',linewidth=0.5,facecolor = '#FF2E2E',label = 'high'if c == 0 else "",linestyle="--")
	c+=1

plt.gca().add_patch(polyp1)
plt.gca().add_patch(polyp2)
plt.gca().add_patch(polyp3)
plt.gca().add_patch(polyp4)
plt.gca().add_patch(polyp5)
plt.gca().add_patch(polyp6)
plt.gca().add_patch(polyp7)
plt.gca().add_patch(polyp8)
plt.gca().add_patch(polys1)
plt.gca().add_patch(polys2)
plt.gca().add_patch(polys3)
plt.gca().add_patch(polys4)
plt.gca().add_patch(polys5)
plt.gca().add_patch(polys6)
plt.gca().add_patch(polys7)
plt.gca().add_patch(polys8)
plt.gca().add_patch(polyb1)
plt.gca().add_patch(polyb2)
plt.gca().add_patch(polyb3)
plt.gca().add_patch(polyb4)

plt.legend()
plt.show()