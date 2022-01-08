#to find the peak height of a hot air balloon
#by Gaurav Gupta

import csv, math;

#constants
a = 1;
b = 1050;
fc = 1;
fc_list = [];
altitude_list = [];
final_altitude = 0;
table = []
file = open("table.csv", 'r')
csvreader = csv.reader(file, delimiter = ',')
for row in csvreader:
    table.append(row)

Vb = float(input("Enter the Volume of the balloon: "))
Mh = float(input("Enter the mass of balloon hardware: "))
Ti = float(input("Enter the inside temperature of balloon: "))
for x in range(1,30): 
    c = math.floor((a+b)*0.5);
    fc = Mh - Vb*float(table[c][2])/287*(1/float(table[c][1])-1/Ti);
    fb = Mh - Vb*float(table[b][2])/287*(1/float(table[b][1])-1/Ti);
    if fc == 0:
        final_altitude = float(table[c][0]);
        break
    elif fb * fc > 0:
        b = c;
    else:
        a = c;
        
    fc_list.append(fc);
    altitude_list.append(float(table[c][0]));
    print(float(table[c][0]), fc)
