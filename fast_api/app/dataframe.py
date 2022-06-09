import pandas as pd

class Dataframe:

    def __init__(self, dataframe_name: str) -> None:
        self.dataframe = pd.read_csv(dataframe_name)
        pass

    def search_dataframe(self, field: str, value):
        result = self.dataframe[self.dataframe[field] == value]
        return result