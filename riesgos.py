# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import pandas_datareader.data as web
import fix_yahoo_finance as yf
from datetime import datetime, timedelta
import numpy as np
import pandas as pd

def calcula_beta(ticker_symbol = 'TEF.MC', ref_index = '^IBEX'):
    """
    Esta función devuelve la beta mensual de 5 años del mercado entre una acción y un índice de referencia. 
    """

    fecha_final =   datetime.today() 
    fecha_inicial = fecha_final - timedelta(days=5*365) 
    try:
        df_stock = web.get_data_yahoo(ticker_symbol,fecha_inicial,fecha_final)
        df_index = web.get_data_yahoo(ref_index,fecha_inicial,fecha_final)
    except:
        return("Problema de conexión con Yahoo. Hablar con Tecnología.")
    
    df_stock = df_stock.resample('M').last() #wip
    df_index = df_index.resample('M').last() #wip
    df_stock['returns'] = df_stock['Adj Close']/ df_stock['Adj Close'].shift(1) -1
    df_stock = df_stock.dropna()
    df_index['returns'] = df_index['Adj Close']/ df_index['Adj Close'].shift(1) -1
    df_index = df_index.dropna()
    df = pd.DataFrame({'stock_returns' : df_stock['returns'],
                            'index_returns' : df_index['returns']},
                            index=df_stock.index)
    df = df.dropna()

    def covariance(a, b):
        if len(a) != len(b):
            return
        a_mean = np.mean(a)
        b_mean = np.mean(b)
        sum = 0
        for i in range(0, len(a)):
            sum += ((a[i] - a_mean) * (b[i] - b_mean))
        return sum/(len(a)-1)

    numerator = covariance(df['stock_returns'],df['index_returns'])
    denominator = covariance(df['index_returns'],df['index_returns'])
    try:
        return(numerator/denominator)
    except:
        return("El índice tiene covarianza 0. División por 0.")
