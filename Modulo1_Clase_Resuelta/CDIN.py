import pandas as pd
import numpy as np
import string

class CDIN:
    def __init__(self,df):
        self.df=df
        self.col_binarios=None
        self.col_cuantitativos=None
        self.col_cualitativos=None
   
    # Métodos para obtener la clasificación de los datos en un dataframe 
    def get_binarios(self):
        col = self.df.columns
        col_binarias = []
        for c in col:
            if self.df[c].nunique()==2:
                col_binarias.append(c)
        
        self.col_binarios = col_binarias
        return self.col_binarios, self.df[self.col_binarios]
        
    def get_cualitativos(self):
        df_cuali = self.df.select_dtypes(include=['object']).copy()
        self.col_cualitativos = df_cuali.columns
        # No se hace distinción entre cat nominales y ordinales
        
        return self.col_cualitativos, df_cuali
    
    def get_cuantitativos(self):
        df_cuanti = df.select_dtypes(include=['number']).copy()
        self.col_cuantitativos = df_cuanti.columns
        return self.col_cuantitativos, df_cuanti
    
    #Métodos para limpieza del dataframe
    
    