import joblib
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import datetime

from windrose import WindroseAxes
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split

from keras.models import Sequential, Model, load_model
from keras.layers import Dense, Dropout, GaussianNoise, Input, BatchNormalization, ELU
from keras.callbacks import EarlyStopping
from tensorflow.keras.optimizers import Adam
from sklearn.metrics import r2_score
from sklearn.preprocessing import StandardScaler

BATCH_SIZE = 1024
MLP_PATH = "./MLModels/myMLP"
RF_PATH = "./MLModels/rf.joblib"
Liner_PATH = "./MLModels/linerregressor.joblib"
DT_PATH = "./MLModels/dt.joblib"


def loadMLP(path):
    my_mlp = load_model(path)
    return my_mlp


def loadJoblib(path):
    rf = rfmodel = joblib.load(path)
    return rf


def predict_weather(month, day, hour, dewtemp, humidity, pressure, winddir, windspd, model):
    if model == "MLP":
        return predict_mlp(month, day, hour, dewtemp, humidity, pressure, winddir, windspd)
    elif model == "randomforest":
        return predict_rf(month, day, hour, dewtemp, humidity, pressure, winddir, windspd)
    elif model == "liner":
        return predict_lr(month, day, hour, dewtemp, humidity, pressure, winddir, windspd)
    elif model == "tree":
        return predict_dt(month, day, hour, dewtemp, humidity, pressure, winddir, windspd)
    else:
        raise ValueError('Unknown Model')


def predict_mlp(month, day, hour, dewtemp, humidity, pressure, winddir, windspd):
    inputarray = [int(month), int(day), int(hour), float(dewtemp), float(humidity), float(pressure), float(winddir),
                  float(windspd)]
    inputarray = [inputarray]
    inputarray = np.array(inputarray)
    # print(inputarray)
    # print(inputarray.shape)

    mlp = loadMLP(MLP_PATH)
    output = mlp.predict(inputarray, batch_size=BATCH_SIZE, verbose=0)
    print(output[0][0])
    return float(output[0][0])


def predict_rf(month, day, hour, dewtemp, humidity, pressure, winddir, windspd):
    rf = loadJoblib(RF_PATH)
    inputarray = [int(month), int(day), int(hour), float(dewtemp), float(humidity), float(pressure), float(winddir),
                  float(windspd)]
    inputarray = [inputarray]
    inputarray = np.array(inputarray)
    output = rf.predict(inputarray)
    print(output[0])
    return float(output[0])


def predict_lr(month, day, hour, dewtemp, humidity, pressure, winddir, windspd):
    lr = loadJoblib(Liner_PATH)
    inputarray = [int(month), int(day), int(hour), float(dewtemp), float(humidity), float(pressure), float(winddir),
                  float(windspd)]
    inputarray = [inputarray]
    inputarray = np.array(inputarray)
    output = lr.predict(inputarray)
    print(output[0])
    return float(output[0])


def predict_dt(month, day, hour, dewtemp, humidity, pressure, winddir, windspd):
    tree = loadJoblib(DT_PATH)
    inputarray = [int(month), int(day), int(hour), float(dewtemp), float(humidity), float(pressure), float(winddir),
                  float(windspd)]
    inputarray = [inputarray]
    inputarray = np.array(inputarray)
    output = tree.predict(inputarray)
    print(output[0])
    return float(output[0])
