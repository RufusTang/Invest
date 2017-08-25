# -*- coding:utf-8 -*-
from __future__ import division
import pandas as pd
from numpy import *
import operator
import os



def Disperse(Dataset):
    # # print Dataset["pe_ratio"].mean()
    # pd.options.mode.chained_assignment = None  # default='warn'
    # Avg = float(Dataset["pe_ratio"].mean())
    # Dataset["pe_ratio"][Dataset["pe_ratio"] < Avg] = valMin
    # Dataset["pe_ratio"][Dataset["pe_ratio"] >= Avg] = valMax
    #
    # Avg = float(Dataset["pe_ratio_lyr"].mean())
    # Dataset["pe_ratio_lyr"][Dataset["pe_ratio_lyr"] < Avg] = valMin
    # Dataset["pe_ratio_lyr"][Dataset["pe_ratio_lyr"] >= Avg] = valMax
    #
    # Avg = float(Dataset["pb_ratio"].mean())
    # Dataset["pb_ratio"][Dataset["pb_ratio"] < Avg] = valMin
    # Dataset["pb_ratio"][Dataset["pb_ratio"] >= Avg] = valMax
    #
    # Avg = float(Dataset["ps_ratio"].mean())
    # Dataset["ps_ratio"][Dataset["ps_ratio"] < Avg] = valMin
    # Dataset["ps_ratio"][Dataset["ps_ratio"] >= Avg] = valMax
    #
    # Avg = float(Dataset["pcf_ratio"].mean())
    # Dataset["pcf_ratio"][Dataset["pcf_ratio"] < Avg] = valMin
    # Dataset["pcf_ratio"][Dataset["pcf_ratio"] >= Avg] = valMax
    #
    # Avg = float(Dataset["roe"].mean())
    # Dataset["roe"][Dataset["roe"] < Avg] = valMin
    # Dataset["roe"][Dataset["roe"] >= Avg] = valMax
    #
    # Avg = float(Dataset["inc_return"].mean())
    # Dataset["inc_return"][Dataset["inc_return"] < Avg] = valMin
    # Dataset["inc_return"][Dataset["inc_return"] >= Avg] = valMax
    #
    # Avg = float(Dataset["roa"].mean())
    # Dataset["roa"][Dataset["roa"] < Avg] = valMin
    # Dataset["roa"][Dataset["roa"] >= Avg] = valMax
    #
    # Avg = float(Dataset["net_profit_margin"].mean())
    # Dataset["net_profit_margin"][Dataset["net_profit_margin"] < Avg] = valMin
    # Dataset["net_profit_margin"][Dataset["net_profit_margin"] >= Avg] = valMax
    #
    # Avg = float(Dataset["gross_profit_margin"].mean())
    # Dataset["gross_profit_margin"][Dataset["gross_profit_margin"] < Avg] = valMin
    # Dataset["gross_profit_margin"][Dataset["gross_profit_margin"] >= Avg] = valMax
    #
    # Avg = float(Dataset["expense_to_total_revenue"].mean())
    # Dataset["expense_to_total_revenue"][Dataset["expense_to_total_revenue"] < Avg] = valMin
    # Dataset["expense_to_total_revenue"][Dataset["expense_to_total_revenue"] >= Avg] = valMax
    #
    # Avg = float(Dataset["operation_profit_to_total_revenue"].mean())
    # Dataset["operation_profit_to_total_revenue"][Dataset["operation_profit_to_total_revenue"] < Avg] = valMin
    # Dataset["operation_profit_to_total_revenue"][Dataset["operation_profit_to_total_revenue"] >= Avg] = valMax
    #
    # Avg = float(Dataset["net_profit_to_total_revenue"].mean())
    # Dataset["net_profit_to_total_revenue"][Dataset["net_profit_to_total_revenue"] < Avg] = valMin
    # Dataset["net_profit_to_total_revenue"][Dataset["net_profit_to_total_revenue"] >= Avg] = valMax
    #
    # Avg = float(Dataset["operating_expense_to_total_revenue"].mean())
    # Dataset["operating_expense_to_total_revenue"][Dataset["operating_expense_to_total_revenue"] < Avg] = valMin
    # Dataset["operating_expense_to_total_revenue"][Dataset["operating_expense_to_total_revenue"] >= Avg] = valMax
    #
    # Avg = float(Dataset["ga_expense_to_total_revenue"].mean())
    # Dataset["ga_expense_to_total_revenue"][Dataset["ga_expense_to_total_revenue"] < Avg] = valMin
    # Dataset["ga_expense_to_total_revenue"][Dataset["ga_expense_to_total_revenue"] >= Avg] = valMax
    #
    # Avg = float(Dataset["financing_expense_to_total_revenue"].mean())
    # Dataset["financing_expense_to_total_revenue"][Dataset["financing_expense_to_total_revenue"] < Avg] = valMin
    # Dataset["financing_expense_to_total_revenue"][Dataset["financing_expense_to_total_revenue"] >= Avg] = valMax
    #
    # Avg = float(Dataset["operating_profit_to_profit"].mean())
    # Dataset["operating_profit_to_profit"][Dataset["operating_profit_to_profit"] < Avg] = valMin
    # Dataset["operating_profit_to_profit"][Dataset["operating_profit_to_profit"] >= Avg] = valMax
    #
    # Avg = float(Dataset["invesment_profit_to_profit"].mean())
    # Dataset["invesment_profit_to_profit"][Dataset["invesment_profit_to_profit"] < Avg] = valMin
    # Dataset["invesment_profit_to_profit"][Dataset["invesment_profit_to_profit"] >= Avg] = valMax
    #
    # Avg = float(Dataset["adjusted_profit_to_profit"].mean())
    # Dataset["adjusted_profit_to_profit"][Dataset["adjusted_profit_to_profit"] < Avg] = valMin
    # Dataset["adjusted_profit_to_profit"][Dataset["adjusted_profit_to_profit"] >= Avg] = valMax
    #
    # Avg = float(Dataset["goods_sale_and_service_to_revenue"].mean())
    # Dataset["goods_sale_and_service_to_revenue"][Dataset["goods_sale_and_service_to_revenue"] < Avg] = valMin
    # Dataset["goods_sale_and_service_to_revenue"][Dataset["goods_sale_and_service_to_revenue"] >= Avg] = valMax
    #
    # Avg = float(Dataset["ocf_to_revenue"].mean())
    # Dataset["ocf_to_revenue"][Dataset["ocf_to_revenue"] < Avg] = valMin
    # Dataset["ocf_to_revenue"][Dataset["ocf_to_revenue"] >= Avg] = valMax
    #
    # Avg = float(Dataset["ocf_to_operating_profit"].mean())
    # Dataset["ocf_to_operating_profit"][Dataset["ocf_to_operating_profit"] < Avg] = valMin
    # Dataset["ocf_to_operating_profit"][Dataset["ocf_to_operating_profit"] >= Avg] = valMax
    #
    # Avg = float(Dataset["inc_total_revenue_year_on_year"].mean())
    # Dataset["inc_total_revenue_year_on_year"][Dataset["inc_total_revenue_year_on_year"] < Avg] = valMin
    # Dataset["inc_total_revenue_year_on_year"][Dataset["inc_total_revenue_year_on_year"] >= Avg] = valMax
    #
    # Avg = float(Dataset["inc_total_revenue_annual"].mean())
    # Dataset["inc_total_revenue_annual"][Dataset["inc_total_revenue_annual"] < Avg] = valMin
    # Dataset["inc_total_revenue_annual"][Dataset["inc_total_revenue_annual"] >= Avg] = valMax
    #
    # Avg = float(Dataset["inc_revenue_year_on_year"].mean())
    # Dataset["inc_revenue_year_on_year"][Dataset["inc_revenue_year_on_year"] < Avg] = valMin
    # Dataset["inc_revenue_year_on_year"][Dataset["inc_revenue_year_on_year"] >= Avg] = valMax
    #
    # Avg = float(Dataset["inc_revenue_annual"].mean())
    # Dataset["inc_revenue_annual"][Dataset["inc_revenue_annual"] < Avg] = valMin
    # Dataset["inc_revenue_annual"][Dataset["inc_revenue_annual"] >= Avg] = valMax
    #
    # Avg = float(Dataset["inc_operation_profit_year_on_year"].mean())
    # Dataset["inc_operation_profit_year_on_year"][Dataset["inc_operation_profit_year_on_year"] < Avg] = valMin
    # Dataset["inc_operation_profit_year_on_year"][Dataset["inc_operation_profit_year_on_year"] >= Avg] = valMax
    #
    # Avg = float(Dataset["inc_operation_profit_annual"].mean())
    # Dataset["inc_operation_profit_annual"][Dataset["inc_operation_profit_annual"] < Avg] = valMin
    # Dataset["inc_operation_profit_annual"][Dataset["inc_operation_profit_annual"] >= Avg] = valMax
    #
    # Avg = float(Dataset["inc_net_profit_year_on_year"].mean())
    # Dataset["inc_net_profit_year_on_year"][Dataset["inc_net_profit_year_on_year"] < Avg] = valMin
    # Dataset["inc_net_profit_year_on_year"][Dataset["inc_net_profit_year_on_year"] >= Avg] = valMax
    #
    # Avg = float(Dataset["inc_net_profit_annual"].mean())
    # Dataset["inc_net_profit_annual"][Dataset["inc_net_profit_annual"] < Avg] = valMin
    # Dataset["inc_net_profit_annual"][Dataset["inc_net_profit_annual"] >= Avg] = valMax
    #
    # Avg = float(Dataset["inc_net_profit_to_shareholders_year_on_year"].mean())
    # Dataset["inc_net_profit_to_shareholders_year_on_year"][
    #     Dataset["inc_net_profit_to_shareholders_year_on_year"] < Avg] = valMin
    # Dataset["inc_net_profit_to_shareholders_year_on_year"][
    #     Dataset["inc_net_profit_to_shareholders_year_on_year"] >= Avg] = valMax
    #
    # Avg = float(Dataset["inc_net_profit_to_shareholders_annual"].mean())
    # Dataset["inc_net_profit_to_shareholders_annual"][Dataset["inc_net_profit_to_shareholders_annual"] < Avg] = valMin
    # Dataset["inc_net_profit_to_shareholders_annual"][Dataset["inc_net_profit_to_shareholders_annual"] >= Avg] = valMax
    #
    # # print Dataset
    # pd.options.mode.chained_assignment = 'warn'  # default='warn'
    # return Dataset
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
    Dataset["operating_expense_to_total_revenue"][(Dataset["operating_expense_to_total_revenue"] < 5)&(Dataset["operating_expense_to_total_revenue"] > 5)] = valMedian

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



def Autonorm(Dataset):
    minVals = Dataset.min(0)
    maxVals = Dataset.max(0)
    Ranges = maxVals - minVals

    normDataset = zeros(shape(Dataset))

    m = Dataset.shape[0]
    normDataset = Dataset - tile(minVals, (m, 1))

    normDataset = normDataset / tile(Ranges, (m, 1))

    return normDataset


def CreateDataset(Filename_model, Filename_intX):


    Columns = ["pe_ratio","pe_ratio_lyr","pb_ratio","ps_ratio","pcf_ratio","roe","inc_return","roa",\
               "net_profit_margin","gross_profit_margin","expense_to_total_revenue","operation_profit_to_total_revenue",\
               "net_profit_to_total_revenue","operating_expense_to_total_revenue","ga_expense_to_total_revenue",\
               "financing_expense_to_total_revenue","operating_profit_to_profit","invesment_profit_to_profit",\
               "adjusted_profit_to_profit","goods_sale_and_service_to_revenue","ocf_to_revenue","ocf_to_operating_profit",\
               "inc_total_revenue_year_on_year","inc_total_revenue_annual","inc_revenue_year_on_year","inc_revenue_annual",\
               "inc_operation_profit_year_on_year","inc_operation_profit_annual","inc_net_profit_year_on_year",\
               "inc_net_profit_annual","inc_net_profit_to_shareholders_year_on_year","inc_net_profit_to_shareholders_annual"]
    Dataset = pd.DataFrame()
    Dataset = pd.read_csv(str(os.getcwd())+ "\\"+Filename_model)


    # 输出数据标记
    Label = list(Dataset.loc[:, 'label_90'])

    rows_model = Dataset.shape[0]

    # 合并待测试数据
    Dataset_Test = pd.DataFrame()
    Dataset_Test = pd.read_csv(str(os.getcwd()) + "\\" + Filename_intX)

    Dataset = pd.concat([Dataset,Dataset_Test])



    rows_test = Dataset_Test.shape[0]


    # 筛选数据
    Dataset = Dataset.loc[:,Columns]


    # 按照规则离散化
    Dataset = Disperse(Dataset)

    # 平均值填充
    Dataset = Dataset.fillna(Dataset.mean()["pe_ratio":"inc_net_profit_to_shareholders_annual"])

    # 归一化
    Dataset = Autonorm(Dataset)

    return Dataset , Label ,rows_model ,rows_test


def Classify_kNN(inX, Dataset, Label, k):
    DataSetSize = Dataset.shape[0]
    DiffMat = tile(inX,(DataSetSize,1)) - Dataset
    sqDiffMat = DiffMat ** 2
    sqDistances = sqDiffMat.sum(axis = 1)
    Distances = sqDistances ** 0.5

    # print Distances
    sortedDistIndicies = Distances.argsort()

    ClassCount = {}


    for i in range(k):
        VoteILabel = Label[sortedDistIndicies[i]]
        ClassCount[VoteILabel] = ClassCount.get(VoteILabel,0) + 1

    SortedClassCount = sorted(ClassCount.iteritems(),key = operator.itemgetter(1),reverse= True)

    return SortedClassCount[0][0]


if __name__ == "__main__":
    # data = pd.DataFrame()
    # data = pd.read_csv(str(os.getcwd()) + "\\sample.csv")
    # Disperse(data)


    Data = pd.DataFrame()
    Label = []
    rows_model = 0
    row_intX = 0
    Data, label,rows_model,row_intX = CreateDataset("sample.csv","intX.csv")

    win_counts = 0
    total_counts = 0

    results = pd.read_csv(str(os.getcwd())+ "\\"+"intX.csv").loc[:,"label_90"]
    codes = pd.read_csv(str(os.getcwd())+ "\\"+"intX.csv").loc[:,["code","pubDate"]]
    KPI = pd.read_csv(str(os.getcwd())+ "\\"+"intX.csv").loc[:,["inc_net_profit_year_on_year","net_profit_to_total_revenue","roe"]]

    # print KPI
    # print KPI.loc[0][0]
    # print KPI.loc[0][1]
    for i in range(row_intX):
        predict_result = Classify_kNN(Data.iloc[int(rows_model + i), :],Data.iloc[:rows_model, :], label, 5)

        print "%d 股票：%s，发布日期：%s, 预测为%s，实际为：%s" % (
            int(i), str(codes.loc[i][0]), str(codes.loc[i][1]), str(predict_result), str(results.loc[i]))

        if (predict_result == 1):

        # if (KPI.loc[i][0] > 10) and (KPI.loc[i][1] > 20) and (KPI.loc[i][2] > 15):
            total_counts = total_counts + 1
            if (predict_result == results.loc[i]):
                win_counts = win_counts + 1


    print "判断记录总数：%d，正例数：%d,正确数为：%d， 正确率为：%f"%(int(row_intX+1),int(total_counts),int(win_counts),float(win_counts/total_counts))
