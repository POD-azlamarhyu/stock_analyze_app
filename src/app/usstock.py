#-*- coding:<UTF-8> -*-

import pandas_datareader.data as pddr
from pandas_datareader.nasdaq_trader import get_nasdaq_symbols
from tqdm import tqdm
import datetime as dt
import os
import pandas as pd
import openpyxl as pxl
import pickle as pkl

class StockUSStock:
    
    def __init__(self,ticker) -> None:
       self.ticker =  ticker