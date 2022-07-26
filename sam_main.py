import FNT
# import sam
import sam
import datetime

FNT_NODE_PATH = "FNT_Nodestxt"

# FNT_NODE_PATH = "FNT_Nodestxt_colored.csv"

# Read and create FNT Nodes
nodefile = open(FNT_NODE_PATH, 'r')
lines = nodefile.readlines()
results = []
# Interate the file
count = 0
# linenew = [lines[57],lines[61]]
now = datetime.datetime.now()

for line in lines:
    print("No.",count)
    count += 1
    elements = line.split(",")
    data = elements[9:19]
    packet = FNT.Packet(999, elements[1], elements[4], elements[5], elements[6] + "&" + elements[7], elements[8], data,
                        999, 999)
    sensorid = packet.get_sid()
    sensorstatus = packet.get_status()
    sensorlocation = packet.get_location()
    timestamp = packet.get_timestamp()
    datatype = packet.get_datatype()
    datapayload = packet.get_data()
    print("Packet Flag:", elements[19])
    print("FNT", timestamp, sensorid, sensorstatus, sensorlocation, datatype, datapayload)
    sam.fnt_decoder(packet)
    result = elements[19]
    results.append(int(result[0]))
    print("=====================================================================================\n")

end = datetime.datetime.now()
print("Start date and time : ")
print(now.strftime("%Y-%m-%d %H:%M:%S"))
print("End date and time : ")
print(end.strftime("%Y-%m-%d %H:%M:%S"))
# print(results)
