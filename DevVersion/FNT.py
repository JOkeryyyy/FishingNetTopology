import math


# Sensor: SensorID, Status, Location.
class Sensor(object):

    def __init__(self, sid, status, location):
        self.sid = sid
        self.status = status
        self.location = location


# Dataset: Data Type, Data.
class Dataset(object):

    def __init__(self, datatype, data):
        self.datatype = datatype
        self.data = data


# Packet: PacketID, Timestamp, Auditee, Auditor, Sensor Info, Dataset.
class Packet(Sensor, Dataset):

    def __init__(self, pid, timestamp, sid, status, location, datatype, data, auditee1, auditee2):
        Sensor.__init__(self, sid, status, location)
        Dataset.__init__(self, datatype, data)
        self.pid = pid
        self.timestamp = timestamp
        self.auditee1 = auditee1
        self.auditee2 = auditee2
        self.auditor = []
        self.disable = False

    def get_pid(self):
        return self.pid

    def get_timestamp(self):
        return self.timestamp

    def get_auditee(self):
        adt1 = self.auditee1
        adt2 = self.auditee2
        if adt1 is None and adt2 is None:
            return [None, None]
        elif adt1 is not None and adt2 is None:
            return [adt1.get_pid(), None]
        elif adt2 is not None and adt1 is None:
            return [None, adt2.get_pid()]
        else:
            return [adt1.get_pid(), adt2.get_pid()]

    def get_auditor(self):
        if len(self.auditor) == 0:
            return [None, None]
        if len(self.auditor) == 1:
            return [self.auditor[0].get_pid(), None]
        if len(self.auditor) == 2:
            return [self.auditor[0].get_pid(), self.auditor[1].get_pid()]

    def get_sid(self):
        return self.sid

    def get_status(self):
        return self.status

    def get_location(self):
        return self.location

    def get_datatype(self):
        return self.datatype

    def get_data(self):
        return self.data

    def print_sensor(self):
        print("SensorID: {0}, Status: {1}, Location: {2}".format(self.sid, self.status, self.location))

    def print_dataset(self):
        print("Data: {0} = {1}".format(self.datatype, self.data))

    def print_packet(self):
        print("PacketID: {0}, Timestamp: {1}, Auditee: {2}".format(self.pid, self.timestamp, self.get_auditee()))

    def print_detail(self):
        print("PacketID: {0}, Timestamp: {1}, Auditee: {2}, Auditor: {3}."
              .format(self.pid, self.timestamp, self.get_auditee(), self.get_auditor()),
              "SensorID: {0}, Status: {1}, Location: {2}."
              .format(self.sid, self.status, self.location),
              "Data: {0} = {1}."
              .format(self.datatype, self.data))


class FishingNet(object):
    def __init__(self, rate):
        self.pid = 0
        self.rate = rate
        self.packets = []
        self.auditeeList = []

        self.group = self.rate * 2 - 1  # Each group in FNT contains (rate * 2 - 1) packets.
        self.countInitial = math.comb(self.rate + 1, 2)  # Counting packets in the initial network.

        edges = []  # Special packets on the edge of the initial network.
        for n in range(1, self.rate):
            upper = int(n * (n + 1) / 2)
            lower = upper + n
            edges.append(upper)
            edges.append(lower)
        self.edge = edges

    def on_edge(self):  # Determine whether a packet is on the edge.
        return (self.pid - self.countInitial + 1) % self.group in [0, self.rate]

    def on_top_edge(self):  # Determine whether a packet is on the top edge.
        if (self.pid - self.countInitial + 1) % self.group == self.rate:
            return True
        if (self.pid - self.countInitial + 1) % self.group == 0:
            return False

    def new_packet(self, timestamp, sid, status, location, datatype, data):  # Create a new packet.
        if self.pid == 0:  # First packet #0.
            packet = Packet(self.pid, timestamp, sid, status, location, datatype, data, None, None)

        elif 0 < self.pid < self.countInitial:  # Packets in the initial network.
            if self.pid in self.edge:  # Packets at the initial network edge have only one auditee.
                adt = self.auditee_initial()
                packet = Packet(self.pid, timestamp, sid, status, location, datatype, data, adt, None)
                adt.auditor.append(packet)

            else:  # Other packets at the initial network have two auditee.
                adt1 = self.auditee_initial()
                adt2 = self.auditee_initial()
                packet = Packet(self.pid, timestamp, sid, status, location, datatype, data, adt1, adt2)
                adt1.auditor.append(packet)
                adt2.auditor.append(packet)

        else:  # Packets in the formal network.
            adt1 = self.auditee_formal()[0]
            adt2 = self.auditee_formal()[1]
            packet = Packet(self.pid, timestamp, sid, status, location, datatype, data, adt1, adt2)
            adt1.auditor.append(packet)
            adt2.auditor.append(packet)

        self.auditeeList.append([packet, 0])
        self.packets.append(packet)
        self.pid += 1

    def auditee_initial(self):  # Auditee for the initial network.
        adt = self.auditeeList[0][0]
        self.auditeeList[0][1] += 1

        if self.auditeeList[0][1] >= 2:  # If a packet is approved twice, remove it from the list.
            self.auditeeList.pop(0)

        if self.countInitial < self.pid and self.on_edge():  # Last layer of the initial network.
            adt = (self.packets[self.pid - self.group])
            self.auditeeList[0][1] += 1
        return adt

    def auditee_formal(self):  # Auditee for the formal network.
        if self.on_edge():  # Auditee for packets on the edge.
            if self.on_top_edge():  # On top edge.
                return [self.auditee_initial(), self.packets[self.pid - self.rate + 1]]
            else:  # On bottom edge.
                return [self.auditee_initial(), self.packets[self.pid - self.rate]]

        else:  # Auditee for other packets.
            return [self.packets[self.pid - self.rate], self.packets[self.pid - self.rate + 1]]

    def display_fnt(self):  # Print all nodes
        for i in range(len(self.packets)):
            if self.packets[i].disable is True:
                print("Packet {0} disabled.".format(i))
            else:
                self.packets[i].print_detail()
