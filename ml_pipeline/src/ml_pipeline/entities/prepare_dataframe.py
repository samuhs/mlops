import pandas as pd

class PrepareDataframe:
    
    def process_dataframe_to_logistic(self, dataframe: pd.DataFrame)-> pd.DataFrame:
        """Função responsavel por preparar o dataframe para modelagem do projeto

        Args:
            dataframe (pd.DataFrame): Dataframe que ira recer a tratativa

        Returns:
            pd.DataFrame: Dataframe processado
        """
        dummies_type_df = self.column_to_dummie(dataframe,'type')
        dummies_god_df = self.column_to_dummie(dataframe,'god')

        dataframe = dataframe.join(dummies_type_df)
        dataframe = dataframe.join(dummies_god_df)

        dataframe_process = self.clean_dataframe(dataframe,['id','name','type','god'])

        return dataframe_process

    def column_to_dummie(self, dataframe: pd.DataFrame, columns: str)-> pd.DataFrame:
        """Função responsavel por transformar colunas em dummies

        Args:
            dataframe (pd.DataFrame): dataframe que será transformado
            columns (str): nome da coluna

        Returns:
            pd.DataFrame: resultado da transformação da coluna do dataframe original
        """
        return pd.get_dummies(dataframe[columns])

    def clean_dataframe(self, dataframe: pd.DataFrame,columns: list )-> pd.DataFrame:
        """Função responsavel por limpar as colunas de um dataframe

        Args:
            dataframe (pd.DataFrame): Dataframe a ser limpado
            columns (list): lista contendo as colunas que serão removidas

        Returns:
            pd.DataFrame: Dataframe limpo
        """
        return dataframe.drop(columns, axis = 1)