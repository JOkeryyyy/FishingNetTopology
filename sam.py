import datetime
import data_predictor
import FNT

SENSOR_LISt = [["8202250", "000", "-63.50001389&44.88001667", "60", "2022-07-10T00:00"]]
TIMESTAMP_DEVIATION_THDV = 2
DATA_DEVIATION_THDE_PRCT = 0.1
NORMAL_SENSOR_STATUS = 000
MLP_PATH = "./myMLP"
RF_PATH = "./rf.joblib"
result_list = []
MODEL = "MLP"


def timestamp_to_datetime(timestamp):
    realyear = timestamp[0:4]
    realmonth = timestamp[5:7]
    realday = timestamp[8:10]
    realhour = timestamp[11:13]
    realmin = timestamp[14:-1]
    last_packet_date = datetime.date(int(realyear), int(realmonth), int(realday))
    last_packet_time = datetime.time(int(realhour), int(realmin))
    last_packet = datetime.datetime.combine(last_packet_date, last_packet_time)
    return last_packet


def year_month_day_hour_vs_datetime(year, month, day, hour, timestamp):
    year = int(year)
    month = int(month)
    day = int(day)
    hour = int(hour)
    realyear = int(timestamp[0:4])
    realmonth = int(timestamp[5:7])
    realday = int(timestamp[8:10])
    realhour = int(timestamp[11:13])
    if (year == realyear and month == realmonth and day == realday and hour == realhour):
        return True
    else:
        return False


def search_list(myList, v):
    for i, x in enumerate(myList):
        if v in x:
            return i, x.index(v)

# Adapter Functions
def fnt_decoder(fntnode):
    if fntnode is None:
        print("Empty packet detected!")
        return False

    if not isinstance(fntnode, FNT.Packet):
        return False

    sensorid = fntnode.get_sid()
    sensorstatus = fntnode.get_status()
    sensorlocation = fntnode.get_location()
    timestamp = fntnode.get_timestamp()
    datatype = fntnode.get_datatype()
    datapayload = fntnode.get_data()

    verifier("FNT", timestamp, sensorid, sensorstatus, sensorlocation, datatype, datapayload)
def verifier(dltname, timestamp, sensorid, sensorstatus, sensorlocation, datatype, datapayload):
    if dltname == "FNT":
        fnt_verifier(timestamp, sensorid, sensorstatus, sensorlocation, datatype, datapayload)
        return True
    else:
        print("DLT not support yet")
# SAM Verifier
def fnt_verifier(timestamp, sensorid, sensorstatus, sensorlocation, datatype, datapayload):
    initialverify = initial_verifier(timestamp, sensorid, sensorstatus, sensorlocation, SENSOR_LISt)
    if initialverify == 0:
        print("Initial verify passed")
        #     Update the last_packet time

        dataverify = data_verifier(datatype, datapayload)

        if dataverify == 0:
            print("initial verify  passed")
            print("Packet verified, attach to FNT")
            result_list.append(dataverify)
            print(result_list)
            realidindex = search_list(SENSOR_LISt, sensorid)
            SENSOR_LISt[realidindex[0]][4] = timestamp
            return dataverify
        else:
            print("data verifier Failed")
            result_list.append(dataverify)
            print(result_list)
            return dataverify
    else:
        print("Initial verifier Failed")
        result_list.append(initialverify)
        print(result_list)
        return initialverify
# Initial Verifier
def initial_verifier(timestamp, sensorid, sensorstatus, sensorlocation, sensorlist):
    # Check if the sensor id exist in the sensor list

    print("Initial Verif start")

    realidindex = search_list(sensorlist, sensorid)
    if realidindex is None:
        # Fail case
        print("ERROR: SENSOR ID NOT EXIST, Detaching the node... ")
        return 1

    # Check is the timestamp matches the expected value "2022-07-01T00:00"

    # Convert freq to seconds
    print(sensorlist)
    freq = int(sensorlist[realidindex[0]][3]) * 60
    # Extract the date from input string
    last_packet = timestamp_to_datetime(sensorlist[realidindex[0]][4])
    this_packet = timestamp_to_datetime(timestamp)
    print("last ", last_packet, " this ", this_packet)
    time_diff = (this_packet - last_packet).seconds
    print(time_diff, " ", (time_diff % freq), freq)
    # Check is time_diff is greater than time freq plus a deviation
    # if not ((freq - TIMESTAMP_DEVIATION_THDV) <= time_diff <= (freq + TIMESTAMP_DEVIATION_THDV)):
    if (time_diff % freq) > TIMESTAMP_DEVIATION_THDV:
        # Fail case

        print("ERROR: ABNORMAL TIMESTAMP, Detaching the node... Except", (freq - TIMESTAMP_DEVIATION_THDV), " to ",
              (freq + TIMESTAMP_DEVIATION_THDV), " Actual ", time_diff)
        return 2

    # Is the sensor status normal?
    realSensorStatus = sensorlist[realidindex[0]][1]
    if realSensorStatus != sensorstatus:
        # Fail case
        print("ERROR: ABNORMAL SENSOR STATUS, Detaching the node...")
        return 3

    # Does the sensor's location matches the record in sensors list?
    realSensorLoaction = sensorlist[realidindex[0]][2]
    # realSensorLoaction = realSensorLoaction.split("&")
    # reallongtitude = realSensorLoaction[0]
    # reallatitude = realSensorLoaction[1]
    # inputsensorlocation = sensorlocation.split("&")
    if realSensorLoaction != sensorlocation:
        # False case
        print("ERROR:INVALID SENSOR LOCATION , Detaching the node...")
        return 4
    print("Initial Verif completed")
    return 0
# Data Verifier
def data_verifier(datatype, datapayload):
    print("data Verif start")
    # 1. Extract the data type and data value: Datatype and data payload
    input_data_value = -999
    predValue = -999
    if (datatype == "weather"):
        predValue = data_predictor.predict_weather(
            month=datapayload[1],
            day=datapayload[2],
            hour=datapayload[3],
            dewtemp=datapayload[5],
            humidity=datapayload[6],
            pressure=datapayload[9],
            winddir=datapayload[7],
            windspd=datapayload[8],
            model=MODEL)

        input_data_value = datapayload[4]
        # predValue = (pred1 + pred2) / 2
    else:
        print("Datatype", datatype, "not support yet.")
        return False

    print("data Verif completed")

    #     Check if the data-payload value matches preditc value
    if (input_data_value != -999 and predValue != -999):
        if (predValue * (1 - DATA_DEVIATION_THDE_PRCT) < float(input_data_value) < predValue * (
                1 + DATA_DEVIATION_THDE_PRCT)):
            print("Data Approved! Attaching to FNT...")
            return 0
        else:
            print("Expect:", predValue, "Actual:", input_data_value, "ERROR:INVALID VALUE: Detaching the node...")
            return 5

    else:
        raise ValueError('Unknown Error')


# 2. Making request to the data predictor


time1 = timestamp_to_datetime("2022-07-01T00:00")
time2 = timestamp_to_datetime("2022-07-01T02:13")
time3 = datetime.time(0, 59)
timeDiff = time2 - time1
