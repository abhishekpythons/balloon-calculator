class balloon:
    def __init__(self, Vb, Mh, Ti):
        self.Vb = Vb
        self.Mh = Mh
        self.Ti = Ti


def peak_height(Vb, Mh, Ti):
    self.fc_list = {}
    self.altitude_list = {}
    a = 1
    b = 1050
    fc = 1
    final_altitude = 0
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
    return [fc_list, altitude_list]

if __name__=='__main__':
    table = []
    file = open("table.csv", 'r')
    csvreader = csv.reader(file, delimiter = ',')
    for row in csvreader:
        table.append(row)




    
