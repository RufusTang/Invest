# -*- coding:utf-8 -*-
import pandas as pd
from numpy import *
import os

def FileMerge(Filename,Dataset):
    DataTemp = pd.DataFrame()
    DataTemp = pd.read_csv(str(os.getcwd()) + "\\" + Filename)

    Dataset = pd.concat([Dataset, DataTemp])

    return Dataset

if __name__ == "__main__":
    Dataset = pd.DataFrame()

    for i in range(1,13,1):
        Dataset = FileMerge(("sample" + str(i) + ".csv"),Dataset)

    Dataset.to_csv('sample.csv')