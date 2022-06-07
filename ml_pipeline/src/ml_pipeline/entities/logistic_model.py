import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn import metrics
from sklearn.metrics import classification_report

class LogisticModel:

    def __init__(self) -> None:
        self.logistic_regression= LogisticRegression()

        pass

    def train_logistic(self, dataframe: pd.DataFrame, class_column: str):
        y = dataframe[class_column]
        X = dataframe.drop(class_column, axis = 1)

        X_train,X_test,y_train,y_test = train_test_split(X,y,test_size=0.25,random_state=0)

        self.logistic_regression.fit(X_train,y_train)
        y_pred=self.logistic_regression.predict(X_test)

        confusion_matrix = pd.crosstab(y_test, y_pred, rownames=['Actual'], colnames=['Predicted'])

        print(confusion_matrix)

        print(classification_report(y_test, y_pred))

        return True
    
    def apply_logistic(self,dataframe):
        pred= self.logistic_regression.predict(dataframe)
        return pred