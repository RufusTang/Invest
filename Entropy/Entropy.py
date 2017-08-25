# -*- coding:utf-8 -*-
from __future__ import division
import pandas as pd
from numpy import *
import operator
import os
from math import log

import treePlotter as TreePlotter


def Disperse(Dataset):
    valMax = 200
    valMin = -200
    valMedian = 50

    pd.options.mode.chained_assignment = None  # default='warn'


    Dataset["pe_ratio"][Dataset["pe_ratio"] <= 0] = valMin
    Dataset["pe_ratio"][Dataset["pe_ratio"] >= 70] = valMax
    Dataset["pe_ratio"][(Dataset["pe_ratio"] < 70) & (Dataset["pe_ratio"] > 0)] = valMedian



    Dataset["pe_ratio_lyr"][Dataset["pe_ratio_lyr"] <= 0] = valMin
    Dataset["pe_ratio_lyr"][Dataset["pe_ratio_lyr"] >= 70] = valMax
    Dataset["pe_ratio_lyr"][(Dataset["pe_ratio_lyr"] < 70)&(Dataset["pe_ratio_lyr"] > 0)] = valMedian

    Dataset["pb_ratio"][Dataset["pb_ratio"] <= 0] = valMin
    Dataset["pb_ratio"][Dataset["pb_ratio"] >= 4] = valMax
    Dataset["pb_ratio"][(Dataset["pb_ratio"] < 4)&(Dataset["pb_ratio"] > 0)] = valMedian

    Dataset["ps_ratio"][Dataset["ps_ratio"] <= 0] = valMin
    Dataset["ps_ratio"][Dataset["ps_ratio"] >= 4] = valMax
    Dataset["ps_ratio"][(Dataset["ps_ratio"] < 4)&(Dataset["ps_ratio"] > 0)] = valMedian

    Dataset["pcf_ratio"][Dataset["pcf_ratio"] <= 0] = valMin
    Dataset["pcf_ratio"][Dataset["pcf_ratio"] >= 40] = valMax
    Dataset["pcf_ratio"][(Dataset["pcf_ratio"] < 40)&(Dataset["pcf_ratio"] > 0)] = valMedian

    Dataset["roe"][Dataset["roe"] <= 0] = valMin
    Dataset["roe"][Dataset["roe"] >= 5] = valMax
    Dataset["roe"][(Dataset["roe"] < 5)&(Dataset["roe"] > 0)] = valMedian

    Dataset["inc_return"][Dataset["inc_return"] <= 0] = valMin
    Dataset["inc_return"][Dataset["inc_return"] >= 5] = valMax
    Dataset["inc_return"][(Dataset["inc_return"] < 5)&(Dataset["inc_return"] > 0)] = valMedian

    Dataset["roa"][Dataset["roa"] <= 0] = valMin
    Dataset["roa"][Dataset["roa"] >= 3] = valMax
    Dataset["roa"][(Dataset["roa"] < 3)&(Dataset["roa"] > 0)] = valMedian

    Dataset["net_profit_margin"][Dataset["net_profit_margin"] <= 0] = valMin
    Dataset["net_profit_margin"][Dataset["net_profit_margin"] >= 10] = valMax
    Dataset["net_profit_margin"][(Dataset["net_profit_margin"] < 10)&(Dataset["net_profit_margin"] > 0)] = valMedian

    Dataset["gross_profit_margin"][Dataset["gross_profit_margin"] <= 0] = valMin
    Dataset["gross_profit_margin"][Dataset["gross_profit_margin"] >= 25] = valMax
    Dataset["gross_profit_margin"][(Dataset["gross_profit_margin"] < 25)&(Dataset["gross_profit_margin"] > 0)] = valMedian

    Dataset["expense_to_total_revenue"][Dataset["expense_to_total_revenue"] <= 80] = valMin
    Dataset["expense_to_total_revenue"][Dataset["expense_to_total_revenue"] >= 100] = valMax
    Dataset["expense_to_total_revenue"][(Dataset["expense_to_total_revenue"] < 100)&(Dataset["expense_to_total_revenue"] > 80)] = valMedian

    Dataset["operation_profit_to_total_revenue"][Dataset["operation_profit_to_total_revenue"] <= 0] = valMin
    Dataset["operation_profit_to_total_revenue"][Dataset["operation_profit_to_total_revenue"] >= 10] = valMax
    Dataset["operation_profit_to_total_revenue"][(Dataset["operation_profit_to_total_revenue"] < 10)&(Dataset["operation_profit_to_total_revenue"] > 0)] = valMedian

    Dataset["net_profit_to_total_revenue"][Dataset["net_profit_to_total_revenue"] <= 0] = valMin
    Dataset["net_profit_to_total_revenue"][Dataset["net_profit_to_total_revenue"] >= 10] = valMax
    Dataset["net_profit_to_total_revenue"][(Dataset["net_profit_to_total_revenue"] < 10)&(Dataset["net_profit_to_total_revenue"] > 0)] = valMedian


    Dataset["operating_expense_to_total_revenue"][Dataset["operating_expense_to_total_revenue"] <= 2] = valMin
    Dataset["operating_expense_to_total_revenue"][Dataset["operating_expense_to_total_revenue"] >= 5] = valMax
    Dataset["operating_expense_to_total_revenue"][(Dataset["operating_expense_to_total_revenue"] < 5)&(Dataset["operating_expense_to_total_revenue"] > 2)] = valMedian

    Dataset["ga_expense_to_total_revenue"][Dataset["ga_expense_to_total_revenue"] <= 3] = valMin
    Dataset["ga_expense_to_total_revenue"][Dataset["ga_expense_to_total_revenue"] >= 8] = valMax
    Dataset["ga_expense_to_total_revenue"][(Dataset["ga_expense_to_total_revenue"] < 8)&(Dataset["ga_expense_to_total_revenue"] > 3)] = valMedian

    Dataset["financing_expense_to_total_revenue"][Dataset["financing_expense_to_total_revenue"] <= 0] = valMin
    Dataset["financing_expense_to_total_revenue"][Dataset["financing_expense_to_total_revenue"] >= 3] = valMax
    Dataset["financing_expense_to_total_revenue"][(Dataset["financing_expense_to_total_revenue"] < 3)&(Dataset["financing_expense_to_total_revenue"] > 0)] = valMedian

    Dataset["operating_profit_to_profit"][Dataset["operating_profit_to_profit"] <= 80] = valMin
    Dataset["operating_profit_to_profit"][Dataset["operating_profit_to_profit"] >= 100] = valMax
    Dataset["operating_profit_to_profit"][(Dataset["operating_profit_to_profit"] < 100)&(Dataset["operating_profit_to_profit"] > 80)] = valMedian

    Dataset["invesment_profit_to_profit"][Dataset["invesment_profit_to_profit"] <= 0] = valMin
    Dataset["invesment_profit_to_profit"][Dataset["invesment_profit_to_profit"] >= 3] = valMax
    Dataset["invesment_profit_to_profit"][(Dataset["invesment_profit_to_profit"] < 3)&(Dataset["invesment_profit_to_profit"] > 0)] = valMedian

    Dataset["adjusted_profit_to_profit"][Dataset["adjusted_profit_to_profit"] <= 80] = valMin
    Dataset["adjusted_profit_to_profit"][Dataset["adjusted_profit_to_profit"] >= 100] = valMax
    Dataset["adjusted_profit_to_profit"][(Dataset["adjusted_profit_to_profit"] < 100)&(Dataset["adjusted_profit_to_profit"] > 80)] = valMedian

    Dataset["goods_sale_and_service_to_revenue"][Dataset["goods_sale_and_service_to_revenue"] <= 80] = valMin
    Dataset["goods_sale_and_service_to_revenue"][Dataset["goods_sale_and_service_to_revenue"] >= 110] = valMax
    Dataset["goods_sale_and_service_to_revenue"][(Dataset["goods_sale_and_service_to_revenue"] < 110)&(Dataset["goods_sale_and_service_to_revenue"] > 80)] = valMedian

    Dataset["ocf_to_revenue"][Dataset["ocf_to_revenue"] <= 0] = valMin
    Dataset["ocf_to_revenue"][Dataset["ocf_to_revenue"] >= 80] = valMax
    Dataset["ocf_to_revenue"][(Dataset["ocf_to_revenue"] < 80)&(Dataset["ocf_to_revenue"] > 0)] = valMedian

    Dataset["ocf_to_operating_profit"][Dataset["ocf_to_operating_profit"] <= 0] = valMin
    Dataset["ocf_to_operating_profit"][Dataset["ocf_to_operating_profit"] >= 150] = valMax
    Dataset["ocf_to_operating_profit"][(Dataset["ocf_to_operating_profit"] < 150)&(Dataset["ocf_to_operating_profit"] > 0)] = valMedian

    Dataset["inc_total_revenue_year_on_year"][Dataset["inc_total_revenue_year_on_year"] <= 0] = valMin
    Dataset["inc_total_revenue_year_on_year"][Dataset["inc_total_revenue_year_on_year"] >= 30] = valMax
    Dataset["inc_total_revenue_year_on_year"][(Dataset["inc_total_revenue_year_on_year"] < 30)&(Dataset["inc_total_revenue_year_on_year"] > 0)] = valMedian

    Dataset["inc_total_revenue_annual"][Dataset["inc_total_revenue_annual"] <= 0] = valMin
    Dataset["inc_total_revenue_annual"][Dataset["inc_total_revenue_annual"] >= 30] = valMax
    Dataset["inc_total_revenue_annual"][(Dataset["inc_total_revenue_annual"] < 30)&(Dataset["inc_total_revenue_annual"] > 0)] = valMedian

    Dataset["inc_revenue_year_on_year"][Dataset["inc_revenue_year_on_year"] <= 0] = valMin
    Dataset["inc_revenue_year_on_year"][Dataset["inc_revenue_year_on_year"] >= 30] = valMax
    Dataset["inc_revenue_year_on_year"][(Dataset["inc_revenue_year_on_year"] < 30)&(Dataset["inc_revenue_year_on_year"] > 0)] = valMedian

    Dataset["inc_revenue_annual"][Dataset["inc_revenue_annual"] <= 0] = valMin
    Dataset["inc_revenue_annual"][Dataset["inc_revenue_annual"] >= 30] = valMax
    Dataset["inc_revenue_annual"][(Dataset["inc_revenue_annual"] < 30)&(Dataset["inc_revenue_annual"] > 0)] = valMedian


    Dataset["inc_operation_profit_year_on_year"][Dataset["inc_operation_profit_year_on_year"] <= 0] = valMin
    Dataset["inc_operation_profit_year_on_year"][Dataset["inc_operation_profit_year_on_year"] >= 40] = valMax
    Dataset["inc_operation_profit_year_on_year"][(Dataset["inc_operation_profit_year_on_year"] < 40)&(Dataset["inc_operation_profit_year_on_year"] > 0)] = valMedian

    Dataset["inc_operation_profit_annual"][Dataset["inc_operation_profit_annual"] <= 0] = valMin
    Dataset["inc_operation_profit_annual"][Dataset["inc_operation_profit_annual"] >= 50] = valMax
    Dataset["inc_operation_profit_annual"][(Dataset["inc_operation_profit_annual"] < 50)&(Dataset["inc_operation_profit_annual"] > 0)] = valMedian

    Dataset["inc_net_profit_year_on_year"][Dataset["inc_net_profit_year_on_year"] <= 0] = valMin
    Dataset["inc_net_profit_year_on_year"][Dataset["inc_net_profit_year_on_year"] >= 50] = valMax
    Dataset["inc_net_profit_year_on_year"][(Dataset["inc_net_profit_year_on_year"] < 50)&(Dataset["inc_net_profit_year_on_year"] > 0)] = valMedian

    Dataset["inc_net_profit_annual"][Dataset["inc_net_profit_annual"] <= 0] = valMin
    Dataset["inc_net_profit_annual"][Dataset["inc_net_profit_annual"] >= 50] = valMax
    Dataset["inc_net_profit_annual"][(Dataset["inc_net_profit_annual"] < 50)&(Dataset["inc_net_profit_annual"] > 0)] = valMedian

    Dataset["inc_net_profit_to_shareholders_year_on_year"][Dataset["inc_net_profit_to_shareholders_year_on_year"] <= 0] = valMin
    Dataset["inc_net_profit_to_shareholders_year_on_year"][Dataset["inc_net_profit_to_shareholders_year_on_year"] >= 50] = valMax
    Dataset["inc_net_profit_to_shareholders_year_on_year"][(Dataset["inc_net_profit_to_shareholders_year_on_year"] < 50)&(Dataset["inc_net_profit_to_shareholders_year_on_year"] > 0)] = valMedian

    Dataset["inc_net_profit_to_shareholders_annual"][Dataset["inc_net_profit_to_shareholders_annual"] <= 0] = valMin
    Dataset["inc_net_profit_to_shareholders_annual"][Dataset["inc_net_profit_to_shareholders_annual"] >= 50] = valMax
    Dataset["inc_net_profit_to_shareholders_annual"][(Dataset["inc_net_profit_to_shareholders_annual"] < 50)&(Dataset["inc_net_profit_to_shareholders_annual"] > 0)] = valMedian

    pd.options.mode.chained_assignment = 'warn'  # default='warn'
    return Dataset


# 需要将数据离散化
def CreateDataset(Filename):


    Columns = ["pe_ratio","pe_ratio_lyr","pb_ratio","ps_ratio","pcf_ratio","roe","inc_return","roa",\
               "net_profit_margin","gross_profit_margin","expense_to_total_revenue","operation_profit_to_total_revenue",\
               "net_profit_to_total_revenue","operating_expense_to_total_revenue","ga_expense_to_total_revenue",\
               "financing_expense_to_total_revenue","operating_profit_to_profit","invesment_profit_to_profit",\
               "adjusted_profit_to_profit","goods_sale_and_service_to_revenue","ocf_to_revenue","ocf_to_operating_profit",\
               "inc_total_revenue_year_on_year","inc_total_revenue_annual","inc_revenue_year_on_year","inc_revenue_annual",\
               "inc_operation_profit_year_on_year","inc_operation_profit_annual","inc_net_profit_year_on_year",\
               "inc_net_profit_annual","inc_net_profit_to_shareholders_year_on_year","inc_net_profit_to_shareholders_annual","label_90"]

    Dataset = pd.DataFrame()
    Dataset = pd.read_csv(str(os.getcwd())+ "\\"+Filename)

    # 筛选数据
    Dataset = Dataset.loc[:,Columns]

    # 离散化
    Dataset = Disperse(Dataset)

    return Dataset


# dataset为数据集
# Label为判断依据，只有正例反例两种类型
# FeatVec为划分子特征，有各种取值，本例中每个属性离散化为3类取值，如果为None，则相当于计算根节点的熵
def calcShannonEnt(dataset, Label, FeatVec = None):
    numEntries = len(dataset)
    if FeatVec == None:
        Result_count = dataset[Label].value_counts()
        ShannonEnt = 0
        # 根据标记的结果种类计算熵
        for item in Result_count.iteritems() :
            prob = float(item[1]) / numEntries
            ShannonEnt -= prob * log(prob,2)
        return ShannonEnt
    else:
        Category_count = dataset[FeatVec].value_counts()
        ShannonEnt_Gain = calcShannonEnt(dataset, "label_90")

        for item in Category_count.iteritems():
            DataSubSet = pd.DataFrame()
            DataSubSet = dataset[dataset[FeatVec] == item[0]]

            ShannonEnt_Gain -= calcShannonEnt(DataSubSet,"label_90")* DataSubSet.shape[0] / numEntries

        return ShannonEnt_Gain


def ChooseBestFeat(Dataset,FeatVecs):
    Shannon_Gain = {}
    for FeatVec in FeatVecs:
        Shannon_Gain[FeatVec] = calcShannonEnt(DataSet,"label_90",FeatVec)
    Shannon_Gain = sorted(Shannon_Gain.iteritems(), key=operator.itemgetter(1), reverse=True)
    return Shannon_Gain[0][0]


def splitDataSet(dataSet, feat, value):
    retDataSet = pd.DataFrame()
    retDataSet = dataSet[dataSet[feat] == value]
    # 因为特征已经分类过，所以要将对应的列删除
    retDataSet = retDataSet.drop(feat , axis = 1)
    return retDataSet

def MajorityCnt(DataSet):

    StatisticCount = pd.DataFrame()
    StatisticCount = DataSet["label_90"].value_counts()

    result = 0
    result = sorted(StatisticCount.iteritems(), key=operator.itemgetter(1), reverse=True)
    return result[0][0]


# DataSet是数据集，从数据集中抽取出最佳的特征
# Labels是参考特征集合，如果Labels为0，则为叶节点
def CreateTree(DataSet, Labels):
    # 如果达到三个判别条件，则判断为叶节点

    # 1.如果样本集合为空，无法再划分
    if DataSet.empty:
        return 0

    # 2.属性集为空
    if len(Labels) == 0 :
        return MajorityCnt(DataSet)

    # 3.所有的样本属于同一类别，判定规则为90%的样本为同一类别
    StatisticCount = pd.DataFrame()
    StatisticCount = DataSet["label_90"].value_counts()
    TotalCount = DataSet["label_90"].shape[0]
    for Cnt in StatisticCount.iteritems():
        if float(Cnt[1]/TotalCount) > 0.9:
            return Cnt[0]


    # 开始构建树
    MyTree = {}


    BestFeat = ChooseBestFeat(DataSet,Labels)


    MyTree = {BestFeat:{}}
    Labels.remove(BestFeat)

    # 测试用
    # Labels = ["label_90"]
    UniqueVals = DataSet[BestFeat].value_counts()

    for val in UniqueVals.iteritems():

        # 按照特征的取值分解数据集，对每个分支对应不同的子集进行再分类
        DataSubSet = pd.DataFrame()
        DataSubSet = splitDataSet(DataSet, BestFeat, val[0])

        MyTree[BestFeat][val[0]] = CreateTree(DataSubSet, Labels)


    return MyTree


def storeTree(inputTree, filename):
    import pickle
    fw = open(filename, 'w')
    pickle.dump(inputTree, fw)
    fw.close()


def grabTree(filename):
    import pickle
    fr = open(filename)
    return pickle.load(fr)


def classify(inputTree,featLabels,testVec):
    # print inputTree
    # print featLabels
    # print testVec
    firstStr = inputTree.keys()[0]
    secondDict = inputTree[firstStr]
    featIndex = featLabels.index(firstStr)
    key = testVec[featIndex]
    valueOfFeat = secondDict[key]
    if isinstance(valueOfFeat, dict):
        classLabel = classify(valueOfFeat, featLabels, testVec)
    else:
        classLabel = valueOfFeat

    return classLabel



if __name__ == "__main__":
    DataSet = pd.DataFrame()

    DataSet = CreateDataset("sample.csv")

    Tree_FeatVecs = ["pe_ratio", "pe_ratio_lyr", "pb_ratio", "ps_ratio", "pcf_ratio", "roe", "inc_return", "roa", \
               "net_profit_margin", "gross_profit_margin", "expense_to_total_revenue",
               "operation_profit_to_total_revenue", \
               "net_profit_to_total_revenue", "operating_expense_to_total_revenue", "ga_expense_to_total_revenue", \
               "financing_expense_to_total_revenue", "operating_profit_to_profit", "invesment_profit_to_profit", \
               "adjusted_profit_to_profit", "goods_sale_and_service_to_revenue", "ocf_to_revenue",
               "ocf_to_operating_profit", \
               "inc_total_revenue_year_on_year", "inc_total_revenue_annual", "inc_revenue_year_on_year",
               "inc_revenue_annual", \
               "inc_operation_profit_year_on_year", "inc_operation_profit_annual", "inc_net_profit_year_on_year", \
               "inc_net_profit_annual", "inc_net_profit_to_shareholders_year_on_year",
               "inc_net_profit_to_shareholders_annual"]

    MyTree = {}

    MyTree = CreateTree(DataSet, Tree_FeatVecs)




    print MyTree
    results = pd.DataFrame()
    codes = pd.DataFrame()

    Data = pd.DataFrame()

    Tree_FeatVecs = ["pe_ratio", "pe_ratio_lyr", "pb_ratio", "ps_ratio", "pcf_ratio", "roe", "inc_return", "roa", \
               "net_profit_margin", "gross_profit_margin", "expense_to_total_revenue",
               "operation_profit_to_total_revenue", \
               "net_profit_to_total_revenue", "operating_expense_to_total_revenue", "ga_expense_to_total_revenue", \
               "financing_expense_to_total_revenue", "operating_profit_to_profit", "invesment_profit_to_profit", \
               "adjusted_profit_to_profit", "goods_sale_and_service_to_revenue", "ocf_to_revenue",
               "ocf_to_operating_profit", \
               "inc_total_revenue_year_on_year", "inc_total_revenue_annual", "inc_revenue_year_on_year",
               "inc_revenue_annual", \
               "inc_operation_profit_year_on_year", "inc_operation_profit_annual", "inc_net_profit_year_on_year", \
               "inc_net_profit_annual", "inc_net_profit_to_shareholders_year_on_year",
               "inc_net_profit_to_shareholders_annual"]

    results = pd.read_csv(str(os.getcwd())+ "\\"+"intX.csv").loc[:,"label_90"]
    codes = pd.read_csv(str(os.getcwd())+ "\\"+"intX.csv").loc[:,["code","pubDate"]]


    Data = CreateDataset("intX.csv")
    Data = Data[Tree_FeatVecs]
    Data = Data.dropna(axis = 0 )
    print Data

    row_intX = 0
    win_counts = 0
    total_counts = 0

    row_intX = results.shape[0]



    for i in range(row_intX):
        try:
            predict_result = classify(MyTree,Tree_FeatVecs,Data.iloc[i, :])
        except:
            print "股票：%s 出错"%(codes.iloc[i][0])
            predict_result = 0


        print "%d 股票：%s，发布日期：%s, 预测为%s，实际为：%s" % (
            int(i), str(codes.iloc[i][0]), str(codes.iloc[i][1]), str(predict_result), str(results.iloc[i]))

        if (predict_result == 1):

            total_counts = total_counts + 1
            if (predict_result == results.loc[i]):
                win_counts = win_counts + 1


    print "判断记录总数：%d，正例数：%d,正确数为：%d， 正确率为：%f"%(int(row_intX+1),int(total_counts),int(win_counts),float(win_counts/total_counts))
