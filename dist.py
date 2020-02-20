from geopy.distance import geodesic

loc1 = (72.9751973173,19.1857907682)
loc2 = (72.975744488,19.1859440287)
a = geodesic(loc1, loc2).m
print(round(a,2))