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
    
    ## Métodos estáticos para limpieza del dataframe
    @staticmethod
    def remove_punctuation(x):
        try:
            x = ''.join(ch for ch in x if ch not in string.punctuation)
        except:
            print(f'{x} no es un string, no se puede remover símbolos de puntuación')
            pass
        return x
    
    @staticmethod
    #Método para remover dígitos en una cadena de caracteres
    def remove_digits(x):
        try:
            x = ''.join(ch for ch in x if ch not in string.digits)
        except:
            pass
        return x
    @staticmethod
    #Método para remover espacios en blanco
    def remove_whitespace(x):
        try:
            x=''.join(x.split())
        except:
            pass
        return x
    @staticmethod
    #Método para reemplazar texto
    def replace_text(x, to_replace, replacement):
        try:
            x=x.replace(to_replace, replacement)
        except:
            pass
        return x
    @staticmethod
    #Método para convertir una cadenada de caracteres en mayúsculas
    def uppercase_text(x):
        try:
            x=x.upper()
        except:
            pass
        return x
    
    #Método para convertir una cadenada de caracteres en minúsculas
    @staticmethod
    def lowercase_text(x):
        try:
            x=x.lowe()
        except:
            pass
        return x
    
    ## Método para el reporte de calidad de datos
    @staticmethod
    def dqr(data): # dqr(self)
        #%% Lista de variables de la base de datos
        columns = pd.DataFrame(list(data.columns.values), columns=['Nombre columnas'], index=list(data.columns.values))

        #%% Lista de tipos de datos del dataframe
        data_dtypes = pd.DataFrame(data.dtypes, columns=['Tipo de datos'])

        #%% Lista de valores perdidos del dataframe (valores faltante 'nan')
        missing_values = pd.DataFrame(data.isnull().sum(), columns=['valores faltantes'])

        #%% Lista de valores unicos de cada columns
        unique_values = pd.DataFrame(columns=['valores unicos'])
        for col in list(data.columns.values):
            unique_values.loc[col] = [data[col].nunique()]

        #%% Lista de valores unicos de cada columna
        lista_unique_values = pd.DataFrame(columns=['lista valores unicos'])
        for col in list(data.columns.values):
            lista_unique_values.loc[col] = [data[col].unique()]

        #%% Lista de valores presentes
        present_values = pd.DataFrame(data.count(), columns=['Valores presentes'])

        #%% Información estadística
        #%%Lista de valores máximos
        max_values = pd.DataFrame(columns=['Valores Max'])
        for col in list(data.columns.values):
            try:
                max_values.loc[col] = [data[col].max()]
            except:
                pass

        #%%Lista de valores mínimos
        min_values = pd.DataFrame(columns=['Valores Min'])
        for col in list(data.columns.values):
            try:
                min_values.loc[col] = [data[col].min()]
            except:
                pass

        #%% Lista de valores con su media
        #%% Lista de valores con su desviación estándar


        return columns.join(data_dtypes).join(missing_values).join(present_values).join(unique_values).join(lista_unique_values).join(max_values).join(min_values)
    