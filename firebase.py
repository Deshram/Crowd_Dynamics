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

def animate(i):
	x1,y1 = m(72.9751973173,19.1857907682)
	x2,y2 = m(72.9751731775,19.1858768981)
	x3,y3 = m(72.977015855,19.1863784773)
	x4,y4 = m(72.9770507238,19.1862999473)

	#st1 coords
	x5,y5 = m(72.9752691913,19.185848816)
	x6,y6 = m(72.9752638269,19.1858646487)
	x7,y7 = m(72.9755823392,19.1859571117)
	x8,y8 = m(72.9755883742,19.1859393791)

	#st2 coords
	x9,y9 = m(72.976085924,19.18607934)
	x10,y10 = m(72.9760805596,19.1860977059)
	x11,y11 = m(72.9764131535,19.1861863689)
	x12,y12 = m(72.9764185179,19.1861705362)	

	#st3coords
	x13,y13 = m(72.9765787799,19.1862186676)
	x14,y14 = m(72.9765747566,19.1862351335)
	x15,y15 = m(72.9769221026,19.186335196)
	x16,y16 = m(72.9769247848,19.1863193633)

	#br1coords
	x17,y17 = m(72.9755492015,19.1854529549)
	x18,y18 = m(72.9753265782,19.1862230576)
	x19,y19 = m(72.975343342,19.1862255909)
	x20,y20 = m(72.9755706592,19.1854580213)
		
	#br2 coord
	x21,y21 = m(72.9763877732,19.1856730171)
	x22,y22 = m(72.9761391379,19.1864384714)
	x23,y23 = m(72.9761597854,19.1864418522)
	x24,y24 = m(72.9764078898,19.1856793502)

	#br3coord
	x25,y25 = m(72.9768848334,19.1858088696)
	x26,y26 = m(72.9766318607,19.1865688638)
	x27,y27 = m(72.9766557037,19.1865730829)
	x28,y28 = m(72.9769022678,19.1858152027)

	#platform region division coords
	px1,py1 = m(72.975744488,19.1859440287)
	px2,py2 = m(72.9757109604,19.186028892)
	px3,py3 = m(72.9764713666,19.1861428873)
	px4,py4 = m(72.9764405212,19.1862277504)

	#bridge division chords
	bx1,by1 = m(72.9754177733,19.1858988043)	
	bx2,by2 = m(72.9754372193,19.185904504)
	bx3,by3 = m(72.9762402517,19.1861302654)
	bx4,by4 = m(72.9762617094,19.1861378651)
	bx5,by5 = m(72.9767303855,19.1862775021)
	bx6,by6 = m(72.9767525137,19.1862844684)

	polyp1 = Polygon([(x1,y1),(x2,y2),(px2,py2),(px1,py1)],edgecolor = 'black',linewidth=1,facecolor = 'grey')
	polyp2 = Polygon([(px2,py2),(px1,py1),(px3,py3),(px4,py4)],edgecolor = 'black',linewidth=1,facecolor = 'grey')
	polyp3 = Polygon([(px3,py3),(px4,py4),(x3,y3),(x4,y4)],edgecolor = 'black',linewidth=1,facecolor = 'grey')
	poly2 = Polygon([(x5,y5),(x6,y6),(x7,y7),(x8,y8)],edgecolor = 'black',linewidth=0.5,facecolor = '#D3D3D3',linestyle="--")
	poly3 = Polygon([(x9,y9),(x10,y10),(x11,y11),(x12,y12)],edgecolor = 'black',linewidth=0.5,facecolor = '#D3D3D3',linestyle="--")
	poly4 = Polygon([(x13,y13),(x14,y14),(x15,y15),(x16,y16)],edgecolor = 'black',linewidth=0.5,facecolor = '#D3D3D3',linestyle="--")
	polyb1 = Polygon([(x17,y17),(bx1,by1),(bx2,by2),(x20,y20)],edgecolor = 'black',linewidth=0.5,facecolor = '#A9A9A9',linestyle="--")
	polyb2 = Polygon([(bx1,by1),(x18,y18),(x19,y19),(bx2,by2)],edgecolor = 'black',linewidth=0.5,facecolor = '#A9A9A9',linestyle="--")
	polyb3 = Polygon([(x21,y21),(bx3,by3),(bx4,by4),(x24,y24)],edgecolor = 'black',linewidth=0.5,facecolor = '#A9A9A9',linestyle="--")
	polyb4 = Polygon([(bx3,by3),(x22,y22),(x23,y23),(bx4,by4)],edgecolor = 'black',linewidth=0.5,facecolor = '#A9A9A9',linestyle="--")
	polyb5 = Polygon([(x25,y25),(bx5,by5),(bx6,by6),(x28,y28)],edgecolor = 'black',linewidth=0.5,facecolor = '#A9A9A9',linestyle="--")
	polyb6 = Polygon([(bx5,by5),(x26,y26),(x27,y27),(bx6,by6)],edgecolor = 'black',linewidth=0.5,facecolor = '#A9A9A9',linestyle="--")

	plt.gca().add_patch(polyp1)
	plt.gca().add_patch(polyp2)
	plt.gca().add_patch(polyp3)
	plt.gca().add_patch(poly2)
	plt.gca().add_patch(poly3)
	plt.gca().add_patch(poly4)
	plt.gca().add_patch(polyb1)	
	plt.gca().add_patch(polyb2)
	plt.gca().add_patch(polyb3)
	plt.gca().add_patch(polyb4)
	plt.gca().add_patch(polyb5)
	plt.gca().add_patch(polyb6)

	p1 = path.Path([(x1,y1),(x2,y2),(px2,py2),(px1,py1)])
	p2 = path.Path([(px2,py2),(px1,py1),(px3,py3),(px4,py4)])
	p3 = path.Path([(px3,py3),(px4,py4),(x3,y3),(x4,y4)])
	p4 = path.Path([(x5,y5),(x6,y6),(x7,y7),(x8,y8)])
	p5 = path.Path([(x9,y9),(x10,y10),(x11,y11),(x12,y12)])
	p6 = path.Path([(x13,y13),(x14,y14),(x15,y15),(x16,y16)])
	p7 = path.Path([(x17,y17),(bx1,by1),(bx2,by2),(x20,y20)])
	p8 = path.Path([(bx1,by1),(x18,y18),(x19,y19),(bx2,by2)])
	p9 = path.Path([(x21,y21),(bx3,by3),(bx4,by4),(x24,y24)])
	p10 = path.Path([(bx3,by3),(x22,y22),(x23,y23),(bx4,by4)])
	p11 = path.Path([(x25,y25),(bx5,by5),(bx6,by6),(x28,y28)])
	p12= path.Path([(bx5,by5),(x26,y26),(x27,y27),(bx6,by6)])

	b1 = 0
	b2 = 0
	b3 = 0
	b4 = 0
	b5 = 0
	b6 = 0	
	s1 = 0
	s2 = 0
	s3 = 0
	pl1 = 0
	pl2 = 0
	pl3 = 0
	n=0

	all_users = db.child("geofence-2bcb6").get()
	for user in all_users.each():
		userid = user.key()
		lon = db.child("geofence-2bcb6").child(userid).child("longitude").get()
		lat = db.child("geofence-2bcb6").child(userid).child("latitude").get()
		x,y = m(float(lon.val()),float(lat.val()))
		if p7.contains_points([(x,y)]):
			b1+=1
			n+=1
			m.plot(x,y, 'ro', markersize=2)
		elif p8.contains_points([(x,y)]):
			b2+=1
			n+=1
			m.plot(x,y, 'ro', markersize=2)
		elif p9.contains_points([(x,y)]):
			b3+=1
			n+=1
			m.plot(x,y, 'ro', markersize=2)
		elif p10.contains_points([(x,y)]):
			b4+=1
			n+=1
			m.plot(x,y, 'ro', markersize=2)
		elif p11.contains_points([(x,y)]):
			b5+=1
			n+=1
			m.plot(x,y, 'ro', markersize=2)
		elif p12.contains_points([(x,y)]):
			b6+=1
			n+=1
			m.plot(x,y, 'ro', markersize=2)
		elif p4.contains_points([(x,y)]):
			s1+=1
			n+=1
			m.plot(x,y, 'ro', markersize=2)
		elif p5.contains_points([(x,y)]):
			s2+=1
			n+=1
			m.plot(x,y, 'ro', markersize=2)	
		elif p6.contains_points([(x,y)]):
			s3+=1
			n+=1
			m.plot(x,y, 'ro', markersize=2)
		elif p1.contains_points([(x,y)]):
			pl1+=1
			n+=1
			m.plot(x,y, 'ro', markersize=2)
		elif p2.contains_points([(x,y)]):
			pl2+=1
			n+=1
			m.plot(x,y, 'ro', markersize=2)
		elif p3.contains_points([(x,y)]):
			pl3+=1
			n+=1
			m.plot(x,y, 'ro', markersize=2)

	b = "No of people :"+str(n)		
	ax.set_xlabel(b)
	fig.suptitle('Crowd Monitoring', fontsize=20)
	print("\nplatform area 1 contains "+str(pl1)+" people\ncrowd density = "+str(pl1/269.45)+"\n")
	print("platform area 2 contains "+str(pl2)+" people\ncrowd density = "+str(pl2/380.44)+"\n")
	print("platform area 3 contains "+str(pl3)+" people\ncrowd density = "+str(pl3/286.74)+"\n")
	print("bridge 1 area 1 contains "+str(b1)+" people\ncrowd density = "+str(b1/49.63)+"\n")
	print("bridge 1 area 2 contains  "+str(b2)+" people\ncrowd density = "+str(b2/32.01)+"\n")
	print("bridge 2 area 1 contains "+str(b3)+" people\ncrowd density = "+str(b3/50.13)+"\n")
	print("bridge 2 area 2 contains "+str(b4)+" people\ncrowd density = "+str(b4/36.42)+"\n")
	print("bridge 3 area 1 contains "+str(b5)+" people\ncrowd density = "+str(b5/45.12)+"\n")
	print("bridge 3 area 2 contains "+str(b6)+" people\ncrowd density = "+str(b6/36.08)+"\n")
	print("stairs 1 contains "+str(s1)+" people\ncrowd density = "+str(s1/28.29)+"\n")
	print("stairs 2 contains "+str(s2)+" people\ncrowd density = "+str(s2/31.57)+"\n")
	print("stairs 3 contains "+str(s3)+" people\ncrowd density = "+str(s3/27.16)+"\n")
	print("--------------------------------------------------------------")

ani = animation.FuncAnimation(fig, animate, interval=1000)
plt.show()
