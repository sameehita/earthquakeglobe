
import csv
lines0 = csv.reader(open("desktop/1900-1909.csv", "rb"))
lines1 = csv.reader(open("desktop/1910-1919.csv", "rb"))
lines2 = csv.reader(open("desktop/1920-1929.csv", "rb"))
lines3 = csv.reader(open("desktop/1930-1939.csv", "rb"))
lines4 = csv.reader(open("desktop/1940-1949.csv", "rb"))
lines5 = csv.reader(open("desktop/1950-1959.csv", "rb"))
lines6 = csv.reader(open("desktop/1960-1969.csv", "rb"))
lines7 = csv.reader(open("desktop/1970-1979.csv", "rb"))
lines8 = csv.reader(open("desktop/1980-1989.csv", "rb"))
lines9 = csv.reader(open("desktop/1990-1999.csv", "rb"))
lines20 = csv.reader(open("desktop/2000-2007.csv", "rb"))

data0 = []  
data1 = []
data2 = []
data3 = []
data4 = []
data5 = []
data6 = []
data7 = []
data8 = []
data9 = []
data20 = []
for latitude, longitude, magnitude in lines0:
    data0 += (latitude, longitude, str(float(magnitude)))
for latitude, longitude, magnitude in lines1:
    data1 += (latitude, longitude, str(float(magnitude)/10))
for latitude, longitude, magnitude in lines2:
    data2 += (latitude, longitude, str(float(magnitude)/10))
for latitude, longitude, magnitude in lines3:
    data3 += (latitude, longitude, str(float(magnitude)/10))
for latitude, longitude, magnitude in lines4:
    data4 += (latitude, longitude, str(float(magnitude)/10))
for latitude, longitude, magnitude in lines5:
    data5 += (latitude, longitude, str(float(magnitude)/10))
for latitude, longitude, magnitude in lines6:
    data6 += (latitude, longitude, str(float(magnitude)/10))
for latitude, longitude, magnitude in lines7:
    data7 += (latitude, longitude, str(float(magnitude)/10))
for latitude, longitude, magnitude in lines8:
    data8 += (latitude, longitude, str(float(magnitude)/10))
for latitude, longitude, magnitude in lines9:
    data9 += (latitude, longitude, str(float(magnitude)/10))
for latitude, longitude, magnitude in lines20:
    data20 += (latitude, longitude, str(float(magnitude)/10))
print """
[
["1900-1909", [%s]],
["1910-1919", [%s]],
["1920-1929", [%s]],
["1930-1939", [%s]],
["1940-1949", [%s]],
["1950-1959", [%s]],
["1960-1969", [%s]],
["1970-1979", [%s]],
["1980-1989", [%s]],
["1990-1999", [%s]],
["2000-2007", [%s]],
""" % (",".join(data0),
		",".join(data1),
		",".join(data2),
		",".join(data3),
		",".join(data4),
		",".join(data5),
		",".join(data6),
		",".join(data7),
		",".join(data8),
		",".join(data9),
		",".join(data20))
#        ",".join(datacurrent)


