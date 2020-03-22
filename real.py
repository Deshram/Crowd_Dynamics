from firebase import Firebase
import matplotlib.pyplot as plt 
from mpl_toolkits.basemap import Basemap
import pandas as pd
import numpy as np
import csv
from csv import DictReader
from geopy.distance import geodesic
import statistics
from matplotlib.patches import Polygon
from matplotlib import path
import matplotlib.animation as animation
import time
import math

config = {
	"apiKey": "AIzaSyCgiJvJ3bKMAWnSo5LPPBPnY0SX4YeJf6Y",
	"authDomain": "geofence-2bcb6.firebaseapp.com",
	"databaseURL": "https://geofence-2bcb6.firebaseio.com",
	"storageBucket": "geofence-2bcb6.appspot.com"
}

firebase = Firebase(config)
db = firebase.database()
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

def animate(self):
	polyp1 = Polygon([(px1,py1),(px2,py2),(px5,py5),(px6,py6)],edgecolor = 'black',linewidth=1,facecolor = 'grey')
	polyp2 = Polygon([(px2,py2),(px3,py3),(px4,py4),(px5,py5)],edgecolor = 'black',linewidth=1,facecolor = 'grey')
	polyp3 = Polygon([(px6,py6),(px5,py5),(px8,py8),(px7,py7)],edgecolor = 'black',linewidth=1,facecolor = 'grey')
	polyp4 = Polygon([(px4,py4),(px5,py5),(px8,py8),(px9,py9)],edgecolor = 'black',linewidth=1,facecolor = 'grey')
	polyp5 = Polygon([(px7,py7),(px8,py8),(px11,py11),(px12,py12)],edgecolor = 'black',linewidth=1,facecolor = 'grey')
	polyp6 = Polygon([(px8,py8),(px9,py9),(px10,py10),(px11,py11)],edgecolor = 'black',linewidth=1,facecolor = 'grey')
	polyp7 = Polygon([(px10,py10),(px11,py11),(px14,py14),(px15,py15)],edgecolor = 'black',linewidth=1,facecolor = 'grey')
	polyp8 = Polygon([(px12,py12),(px11,py11),(px14,py14),(px13,py13)],edgecolor = 'black',linewidth=1,facecolor = 'grey')
	polys1 = Polygon([(sx1,sy1),(sx2,sy2),(sx3,sy3),(sx6,sy6)],edgecolor = 'black',linewidth=0.5,facecolor = '#D3D3D3',linestyle="--")
	polys2 = Polygon([(sx3,sy3),(sx6,sy6),(sx5,sy5),(sx4,sy4)],edgecolor = 'black',linewidth=0.5,facecolor = '#D3D3D3',linestyle="--")
	polys3 = Polygon([(sx7,sy7),(sx8,sy8),(sx9,sy9),(sx12,sy12)],edgecolor = 'black',linewidth=0.5,facecolor = '#D3D3D3',linestyle="--")
	polys4 = Polygon([(sx9,sy9),(sx12,sy12),(sx11,sy11),(sx10,sy10)],edgecolor = 'black',linewidth=0.5,facecolor = '#D3D3D3',linestyle="--")
	polys5 = Polygon([(sx13,sy13),(sx14,sy14),(sx15,sy15),(sx18,sy18)],edgecolor = 'black',linewidth=0.5,facecolor = '#D3D3D3',linestyle="--")
	polys6 = Polygon([(sx15,sy15),(sx18,sy18),(sx17,sy17),(sx16,sy16)],edgecolor = 'black',linewidth=0.5,facecolor = '#D3D3D3',linestyle="--")
	polys7 = Polygon([(sx19,sy19),(sx20,sy20),(sx21,sy21),(sx24,sy24)],edgecolor = 'black',linewidth=0.5,facecolor = '#D3D3D3',linestyle="--")
	polys8 = Polygon([(sx21,sy21),(sx24,sy24),(sx23,sy23),(sx22,sy22)],edgecolor = 'black',linewidth=0.5,facecolor = '#D3D3D3',linestyle="--")
	polyb1 = Polygon([(bx1,by1),(bx2,by2),(bx3,by3),(bx4,by4)],edgecolor = 'black',linewidth=0.5,facecolor = '#A9A9A9',linestyle="--")
	polyb2 = Polygon([(bx5,by5),(bx6,by6),(bx7,by7),(bx8,by8)],edgecolor = 'black',linewidth=0.5,facecolor = '#A9A9A9',linestyle="--")
	polyb3 = Polygon([(bx9,by9),(bx10,by10),(bx11,by11),(bx12,by12)],edgecolor = 'black',linewidth=0.5,facecolor = '#A9A9A9',linestyle="--")
	polyb4 = Polygon([(bx13,by13),(bx14,by14),(bx15,by15),(bx16,by16)],edgecolor = 'black',linewidth=0.5,facecolor = '#A9A9A9',linestyle="--")
	polyst1 =  Polygon([(fx1,fy1),(fx2,fy2),(fx3,fy3),(fx4,fy4)],edgecolor = 'black',linewidth=0.5,facecolor = 'white',linestyle="--")
	polyst2 =  Polygon([(fx5,fy5),(fx6,fy6),(fx7,fy7),(fx8,fy8)],edgecolor = 'black',linewidth=0.5,facecolor = 'white',linestyle="--")
	polyst3 =  Polygon([(fx9,fy9),(fx10,fy10),(fx11,fy11),(fx12,fy12)],edgecolor = 'black',linewidth=0.5,facecolor = 'white',linestyle="--")

	plt.cla()

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
	plt.gca().add_patch(polyst1)
	plt.gca().add_patch(polyst2)
	plt.gca().add_patch(polyst3)

	p1 = path.Path([(px1,py1),(px2,py2),(px5,py5),(px6,py6)])
	p2 = path.Path([(px2,py2),(px3,py3),(px4,py4),(px5,py5)])
	p3 = path.Path([(px6,py6),(px5,py5),(px8,py8),(px7,py7)])
	p4 = path.Path([(px4,py4),(px5,py5),(px8,py8),(px9,py9)])
	p5 = path.Path([(px7,py7),(px8,py8),(px11,py11),(px12,py12)])
	p6 = path.Path([(px8,py8),(px9,py9),(px10,py10),(px11,py11)])
	p7 = path.Path([(px10,py10),(px11,py11),(px14,py14),(px15,py15)])
	p8 = path.Path([(px12,py12),(px11,py11),(px14,py14),(px13,py13)])
	p9 = path.Path([(sx1,sy1),(sx2,sy2),(sx3,sy3),(sx6,sy6)])
	p10 = path.Path([(sx3,sy3),(sx6,sy6),(sx5,sy5),(sx4,sy4)])
	p11 = path.Path([(sx7,sy7),(sx8,sy8),(sx9,sy9),(sx12,sy12)])
	p12 = path.Path([(sx9,sy9),(sx12,sy12),(sx11,sy11),(sx10,sy10)])
	p13 = path.Path([(sx13,sy13),(sx14,sy14),(sx15,sy15),(sx18,sy18)])
	p14 = path.Path([(sx15,sy15),(sx18,sy18),(sx17,sy17),(sx16,sy16)])
	p15 = path.Path([(sx19,sy19),(sx20,sy20),(sx21,sy21),(sx24,sy24)])
	p16 = path.Path([(sx21,sy21),(sx24,sy24),(sx23,sy23),(sx22,sy22)])
	p17 = path.Path([(bx1,by1),(bx2,by2),(bx3,by3),(bx4,by4)])
	p18 = path.Path([(bx5,by5),(bx6,by6),(bx7,by7),(bx8,by8)])
	p19 = path.Path([(bx9,by9),(bx10,by10),(bx11,by11),(bx12,by12)])
	p20 = path.Path([(bx13,by13),(bx14,by14),(bx15,by15),(bx16,by16)]) 

	n = 0

	all_users = db.child("geofence-2bcb6").get()
	for user in all_users.each():
		userid = user.key()
		lon = db.child("geofence-2bcb6").child(userid).child("longitude").get()
		lat = db.child("geofence-2bcb6").child(userid).child("latitude").get()
		x,y = m(float(lon.val()),float(lat.val()))
		if p17.contains_points([(x,y)]):
			n+=1
			m.plot(x,y, 'ro', markersize=2)
		elif p18.contains_points([(x,y)]):
			n+=1
			m.plot(x,y, 'ro', markersize=2)
		elif p19.contains_points([(x,y)]):
			n+=1
			m.plot(x,y, 'ro', markersize=2)
		elif p20.contains_points([(x,y)]):
			n+=1
			m.plot(x,y, 'ro', markersize=2)
		elif p9.contains_points([(x,y)]):
			n+=1
			m.plot(x,y, 'ro', markersize=2)
		elif p10.contains_points([(x,y)]):
			n+=1
			m.plot(x,y, 'ro', markersize=2)
		elif p11.contains_points([(x,y)]):
			n+=1
			m.plot(x,y, 'ro', markersize=2)
		elif p12.contains_points([(x,y)]):
			n+=1
			m.plot(x,y, 'ro', markersize=2)	
		elif p13.contains_points([(x,y)]):
			n+=1
			m.plot(x,y, 'ro', markersize=2)
		elif p14.contains_points([(x,y)]):
			n+=1
			m.plot(x,y, 'ro', markersize=2)
		elif p15.contains_points([(x,y)]):
			n+=1
			m.plot(x,y, 'ro', markersize=2)
		elif p16.contains_points([(x,y)]):
			n+=1
			m.plot(x,y, 'ro', markersize=2)			
		elif p1.contains_points([(x,y)]):
			n+=1
			m.plot(x,y, 'ro', markersize=2)	
		elif p2.contains_points([(x,y)]):
			n+=1
			m.plot(x,y, 'ro', markersize=2)
		elif p3.contains_points([(x,y)]):
			n+=1
			m.plot(x,y, 'ro', markersize=2)
		elif p4.contains_points([(x,y)]):
			n+=1
			m.plot(x,y, 'ro', markersize=2)
		elif p5.contains_points([(x,y)]):
			n+=1
			m.plot(x,y, 'ro', markersize=2)
		elif p6.contains_points([(x,y)]):
			n+=1
			m.plot(x,y, 'ro', markersize=2)
		elif p7.contains_points([(x,y)]):
			n+=1
			m.plot(x,y, 'ro', markersize=2)
		elif p8.contains_points([(x,y)]):
			n+=1
			m.plot(x,y, 'ro', markersize=2)

	b = "No of people :"+str(n)		
	ax.set_xlabel(b)
	fig.suptitle('Crowd Monitoring', fontsize=20)
	
def bnimate(self):
	pl1 = 0
	pl2 = 0
	pl3 = 0
	pl4 = 0
	pl5 = 0
	pl6 = 0
	pl7 = 0
	pl8 = 0
	s1 = 0
	s2 = 0
	s3 = 0
	s4 = 0
	s5 = 0
	s6 = 0
	s7 = 0
	s8 = 0
	b1 = 0
	b2 = 0
	b3 = 0
	b4 = 0

	p1 = path.Path([(px1,py1),(px2,py2),(px5,py5),(px6,py6)])
	p2 = path.Path([(px2,py2),(px3,py3),(px4,py4),(px5,py5)])
	p3 = path.Path([(px6,py6),(px5,py5),(px8,py8),(px7,py7)])
	p4 = path.Path([(px4,py4),(px5,py5),(px8,py8),(px9,py9)])
	p5 = path.Path([(px7,py7),(px8,py8),(px11,py11),(px12,py12)])
	p6 = path.Path([(px8,py8),(px9,py9),(px10,py10),(px11,py11)])
	p7 = path.Path([(px10,py10),(px11,py11),(px14,py14),(px15,py15)])
	p8 = path.Path([(px12,py12),(px11,py11),(px14,py14),(px13,py13)])
	p9 = path.Path([(sx1,sy1),(sx2,sy2),(sx3,sy3),(sx6,sy6)])
	p10 = path.Path([(sx3,sy3),(sx6,sy6),(sx5,sy5),(sx4,sy4)])
	p11 = path.Path([(sx7,sy7),(sx8,sy8),(sx9,sy9),(sx12,sy12)])
	p12 = path.Path([(sx9,sy9),(sx12,sy12),(sx11,sy11),(sx10,sy10)])
	p13 = path.Path([(sx13,sy13),(sx14,sy14),(sx15,sy15),(sx18,sy18)])
	p14 = path.Path([(sx15,sy15),(sx18,sy18),(sx17,sy17),(sx16,sy16)])
	p15 = path.Path([(sx19,sy19),(sx20,sy20),(sx21,sy21),(sx24,sy24)])
	p16 = path.Path([(sx21,sy21),(sx24,sy24),(sx23,sy23),(sx22,sy22)])
	p17 = path.Path([(bx1,by1),(bx2,by2),(bx3,by3),(bx4,by4)])
	p18 = path.Path([(bx5,by5),(bx6,by6),(bx7,by7),(bx8,by8)])
	p19 = path.Path([(bx9,by9),(bx10,by10),(bx11,by11),(bx12,by12)])
	p20 = path.Path([(bx13,by13),(bx14,by14),(bx15,by15),(bx16,by16)]) 

	all_users = db.child("geofence-2bcb6").get()
	for user in all_users.each():
		userid = user.key()
		lon = db.child("geofence-2bcb6").child(userid).child("longitude").get()
		lat = db.child("geofence-2bcb6").child(userid).child("latitude").get()
		x,y = m(float(lon.val()),float(lat.val()))
		if p17.contains_points([(x,y)]):
			b1+=1
		elif p18.contains_points([(x,y)]):
			b2+=1
		elif p19.contains_points([(x,y)]):
			b3+=1
		elif p20.contains_points([(x,y)]):
			b4+=1
		elif p9.contains_points([(x,y)]):
			s1+=1
		elif p10.contains_points([(x,y)]):
			s2+=1
		elif p11.contains_points([(x,y)]):
			s3+=1
		elif p12.contains_points([(x,y)]):
			s4+=1	
		elif p13.contains_points([(x,y)]):
			s5+=1
		elif p14.contains_points([(x,y)]):
			s6+=1
		elif p15.contains_points([(x,y)]):
			s7+=1
		elif p16.contains_points([(x,y)]):
			s8+=1			
		elif p1.contains_points([(x,y)]):
			pl1+=1	
		elif p2.contains_points([(x,y)]):
			pl2+=1
		elif p3.contains_points([(x,y)]):
			pl3+=1
		elif p4.contains_points([(x,y)]):
			pl4+=1
		elif p5.contains_points([(x,y)]):
			pl5+=1
		elif p6.contains_points([(x,y)]):
			pl6+=1
		elif p7.contains_points([(x,y)]):
			pl7+=1
		elif p8.contains_points([(x,y)]):
			pl8+=1

	cd1 = pl1/100.013
	cd2 = pl2/84.628
	cd3 = pl3/139.031
	cd4 = pl4/155.109
	cd5 = pl5/155.106
	cd6 = pl6/144.753
	cd7 = pl7/141.188
	cd8 = pl8/138.704
	cd9 = s1/4.86
	cd10 = s2/4.851
	cd11 = s3/14.065
	cd12 = s4/12.789
	cd13 = s5/13.935
	cd14 = s6/9.509
	cd15 = s7/11.689
	cd16 = s8/10.19
	cd17 = b1/27.473
	cd18 = b2/31.836
	cd19 = b3/31.128
	cd20 = b4/32.251

	s = []

	if cd1 == 0:
		s1 = 0
		s.append(s1)
	else:
		s1 = 1.34*(1 - math.exp(-1.913*(1/cd1 - 1/5.4)))
		s.append(s1)
	if cd2 == 0:
		s2 = 0
		s.append(s2)
	else:
		s2 = 1.34*(1 - math.exp(-1.913*(1/cd2 - 1/5.4)))
		s.append(s2)
	if cd3 == 0:
		s3 = 0
		s.append(s3)
	else:
		s3 = 1.34*(1 - math.exp(-1.913*(1/cd3 - 1/5.4)))
		s.append(s3)
	if cd4 == 0:
		s4 = 0
		s.append(s4)
	else:
		s4 = 1.34*(1 - math.exp(-1.913*(1/cd4 - 1/5.4)))
		s.append(s4)
	if cd5 == 0:
		s5 = 0
		s.append(s5)
	else:
		s5 = 1.34*(1 - math.exp(-1.913*(1/cd5 - 1/5.4)))
		s.append(s5)
	if cd6 == 0:
		s6 = 0
		s.append(s6)
	else:
		s6 = 1.34*(1 - math.exp(-1.913*(1/cd6 - 1/5.4)))
		s.append(s6)
	if cd7 == 0:
		s7 = 0
		s.append(s7)
	else:
		s7 = 1.34*(1 - math.exp(-1.913*(1/cd7 - 1/5.4)))
		s.append(s7)
	if cd8 == 0:
		s8 = 0
		s.append(s8)
	else:
		s8 = 1.34*(1 - math.exp(-1.913*(1/cd8 - 1/5.4)))
		s.append(s8)
	if cd9 == 0:
		s9 = 0
		s.append(s9)
	else:
		s9 = 1.34*(1 - math.exp(-1.913*(1/cd9 - 1/5.4)))
		s.append(s9)
	if cd10 == 0:
		s10 = 0
		s.append(s10)
	else:
		s10 = 1.34*(1 - math.exp(-1.913*(1/cd10 - 1/5.4)))
		s.append(s10)
	if cd11 == 0:
		s11 = 0
		s.append(s11)
	else:
		s11 = 1.34*(1 - math.exp(-1.913*(1/cd11 - 1/5.4)))
		s.append(s11)
	if cd12 == 0:
		s12 = 0
		s.append(s12)
	else:
		s12 = 1.34*(1 - math.exp(-1.913*(1/cd12 - 1/5.4)))
		s.append(s12)
	if cd13 == 0:
		s13 = 0
		s.append(s13)
	else:
		s13 = 1.34*(1 - math.exp(-1.913*(1/cd13 - 1/5.4)))
		s.append(s13)
	if cd14 == 0:
		s14 = 0
		s.append(s14)
	else:
		s14 = 1.34*(1 - math.exp(-1.913*(1/cd14 - 1/5.4)))
		s.append(s14)
	if cd15 == 0:
		s15 = 0
		s.append(s15)
	else:
		s15 = 1.34*(1 - math.exp(-1.913*(1/cd15 - 1/5.4)))
		s.append(s15)
	if cd16 == 0:
		s16 = 0
		s.append(s16)
	else:
		s16 = 1.34*(1 - math.exp(-1.913*(1/cd16 - 1/5.4)))
		s.append(s16)
	if cd17 == 0:
		s17 = 0
		s.append(s17)
	else:
		s17 = 1.34*(1 - math.exp(-1.913*(1/cd17 - 1/5.4)))
		s.append(s17)
	if cd18 == 0:
		s18 = 0
		s.append(s18)
	else:
		s18 = 1.34*(1 - math.exp(-1.913*(1/cd18 - 1/5.4)))
		s.append(s18)
	if cd19 == 0:
		s19 = 0
		s.append(s19)
	else:
		s19 = 1.34*(1 - math.exp(-1.913*(1/cd19 - 1/5.4)))
		s.append(s19)
	if cd20 == 0:
		s20 = 0
		s.append(s20)
	else:
		s20 = 1.34*(1 - math.exp(-1.913*(1/cd20 - 1/5.4)))
		s.append(s20)

	sc = []

	f = open("output2.txt", "a")
	for i in range(len(s)):
		if (s[i] > 1) | (s[i] == 0):
			sc.append(2)
		elif s[i] > 0.5 :
			sc.append(1)
		else :
			sc.append(0)
		
	print(str(cd1)+"\n"+str(cd2)+"\n"+str(cd3)+"\n"+str(cd4)+"\n"+str(cd5)+"\n"+str(cd6)+"\n"+str(cd7)+"\n"+str(cd8)+"\n"+str(cd9)+"\n"+str(cd10)+"\n"+str(cd11)+"\n"+str(cd12)+"\n"+str(cd13)+"\n"+str(cd14)+"\n"+str(cd15)+"\n"+str(cd16)+"\n"+str(cd17)+"\n"+str(cd18)+"\n"+str(cd19)+"\n"+str(cd20))
	print(s)
	f.write(str(sc[1])+"\n")
	return sc		

ani = animation.FuncAnimation(fig, animate, interval=5000)
bni = animation.FuncAnimation(fig, bnimate, interval=5000)
plt.show()
