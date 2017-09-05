# -*- coding:utf-8 -*-
from __future__ import division
import pandas as pd
from numpy import *
import operator
import os
from math import log



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

    Dataset = Dataset.fillna(Dataset.mean()["pe_ratio":"inc_net_profit_to_shareholders_annual"])

    # 离散化
    Dataset = Disperse(Dataset)

    return Dataset

def FreCal(DataSet):

    # 1. 计算大类别的Pc
    Pc = {}

    # 确定标记正反例的属性列名
    Label = "label_90"

    # 总的有效列数
    TotalCount = DataSet[Label].count()

    # 先计算Label的正反例数
    Category_count = DataSet[Label].value_counts()

    for item in Category_count.iteritems():
        Pc[item[0]] = item[1] / TotalCount

    # print Pc

    # 2. 计算在大类别下面各子类别的概率Pxi
    Pxi = {}
    for key in Pc.keys():
        Pxi[key] = {}
        for feat in DataSet:
            if key != Label:
                SubCategory_count = DataSet[DataSet[Label] == key][feat].value_counts()
                SubCount = DataSet[DataSet[Label] == key][feat].count()

                Pxi[key][feat] = {}

                for item in SubCategory_count.iteritems():
                    Pxi[key][feat][item[0]] = item[1] / SubCount

    return Pc,Pxi

def ClassifyBayes(Pc,Pxi,DataSet):
    Columns = ["pe_ratio","pe_ratio_lyr","pb_ratio","ps_ratio","pcf_ratio","roe","inc_return","roa",\
               "net_profit_margin","gross_profit_margin","expense_to_total_revenue","operation_profit_to_total_revenue",\
               "net_profit_to_total_revenue","operating_expense_to_total_revenue","ga_expense_to_total_revenue",\
               "financing_expense_to_total_revenue","operating_profit_to_profit","invesment_profit_to_profit",\
               "adjusted_profit_to_profit","goods_sale_and_service_to_revenue","ocf_to_revenue","ocf_to_operating_profit",\
               "inc_total_revenue_year_on_year","inc_total_revenue_annual","inc_revenue_year_on_year","inc_revenue_annual",\
               "inc_operation_profit_year_on_year","inc_operation_profit_annual","inc_net_profit_year_on_year",\
               "inc_net_profit_annual","inc_net_profit_to_shareholders_year_on_year","inc_net_profit_to_shareholders_annual"]

    DataSet = DataSet[Columns]

    # 正例结果
    Ret1 = 0
    # 反例结果
    Ret0 = 0
    # 1.计算正例
    Pc1 = Pc[1]
    for feat in Columns:
        Ret1 += float(log(Pxi[1][feat][DataSet[feat]],2))


    # 2.计算反例
    Pc0 = Pc[-1]
    for feat in Columns:
        Ret0 += float(log(Pxi[-1][feat][DataSet[feat]],2))

    # 3.比较大小
    if Ret1 > Ret0:
        return 1
    else:
        return -1

if __name__ == "__main__":
    DataSet = pd.DataFrame()

    DataSet = CreateDataset("sample.csv")

    Pc = {}
    Pxi = {}
    Pc,Pxi = FreCal(DataSet)
    DataTestify = CreateDataset("intX.csv")


    rows_model = 0
    row_intX = 0

    win_counts = 0
    total_counts = 0

    results = pd.read_csv(str(os.getcwd())+ "\\"+"intX.csv").loc[:,"label_90"]
    codes = pd.read_csv(str(os.getcwd())+ "\\"+"intX.csv").loc[:,["code","pubDate"]]

    row_intX = results.shape[0]

    for i in range(row_intX):
        predict_result = ClassifyBayes(Pc, Pxi, DataTestify.iloc[i,:])


        print "%d 股票：%s，发布日期：%s, 预测为%s，实际为：%s" % (
            int(i), str(codes.loc[i][0]), str(codes.loc[i][1]), str(predict_result), str(results.loc[i]))

        if (predict_result == 1):

            total_counts = total_counts + 1
            if (predict_result == results.loc[i]):
                win_counts = win_counts + 1


    print "判断记录总数：%d，正例数：%d,正确数为：%d， 正确率为：%f"%(int(row_intX+1),int(total_counts),int(win_counts),float(win_counts/total_counts))
