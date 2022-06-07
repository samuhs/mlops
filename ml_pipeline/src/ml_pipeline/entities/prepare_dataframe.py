import pandas as pd

class PrepareDataframe:
    
    def process_dataframe_to_logistic(self, dataframe: pd.DataFrame):
        dummies_type_df = self.column_to_dummie(dataframe,'type')
        dummies_god_df = self.column_to_dummie(dataframe,'god')

        dataframe = dataframe.join(dummies_type_df)
        dataframe = dataframe.join(dummies_god_df)

        dataframe_process = self.clean_dataframe(dataframe,['id','name','type','god'])

        return dataframe_process

    def column_to_dummie(self, dataframe: pd.DataFrame, columns: str)-> pd.DataFrame:
        return pd.get_dummies(dataframe[columns])

    def clean_dataframe(self, dataframe: pd.DataFrame,columns: list ):
        return dataframe.drop(columns, axis = 1)