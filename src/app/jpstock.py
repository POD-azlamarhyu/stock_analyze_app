#-*- coding:<UTF-8> -*-

import pickle
import pandas as pd
import pandas_datareader as pdr
from tqdm import tqdm
import os
import openpyxl as pxl
import pickle as pkl
import pprint
import logging as log
from pandas_datareader.data import DataReader as dr


class JapanStock:
    
    def __init__(self,stockcode):
        self.save_file_root = "./static/"
        self.stock_code= stockcode
        self.terms_year = 10
        self.stock_data = []
        
    def isStockCode(self):
        
        if self.stock_code.isnumeric() == True:
            return True
        else:
            return False
        
    def alterTypeDict(self,data,n):
        
        qs_data = []
        
        date = [""]*n
        open = [""]*n
        high = [""]*n
        low = [""]*n
        close = [""]*n
        volume = [""]*n
        
    
        
        for i in range(0,n):
            date[i] = data.loc[i,"Date"]
            high[i] = data.loc[i,"High"]
            low[i] = data.loc[i,"Low"]
            open[i] = data.loc[i,"Open"]
            close[i] = data.loc[i,"Close"]
            volume[i] = data.loc[i,"Volume"]
        
        print("--------------2")
        print(date)
        print(open)
        print(high)
        print(low)
        print(close)
        print(len(date))
        print(len(open))
            
   
        for i in range(0,n):
            dict_data ={}
            dict_data["date"] = date[i]
            dict_data["open"] = open[i]
            dict_data["high"] = high[i]
            dict_data["low"] = low[i]
            dict_data["close"] = close[i]
            dict_data["vol"] = volume[i]
            
            
            qs_data.append(dict_data)
            
        return qs_data
        
        
        
        
    def getJpStock(self):
        print("\n****************$$$$$$$$$$*****************\n")
        print("銘柄コード : "+str(self.stock_code)+"の株価データを取得する\n")
        
        
        try:
            df = self.getNewStockData()

            df.reset_index("Date",inplace=True)
            print(df)
            qs = self.alterTypeDict(df,len(df))
            
        except Exception as err :
            log.error(err)
            log.error("株式データ取得に失敗しました")
            qs=None
            
        return qs
            
    def getNewStockData(self):
        dfs = []
        
        try:
            code = str(self.stock_code)+".T"
            start_terms = "2022-01-01"
            end_terms = "2022-02-01"
            stock_data= dr(code,"yahoo",start_terms,end_terms)
            print(stock_data.head())
            
        except Exception as err:
            log.error(err)
            log.error("{0},株式データ取得に失敗しました".format(self.stock_code))
        
        return stock_data