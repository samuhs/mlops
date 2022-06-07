import pandas as pd
import mlflow
import mlflow.sklearn

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn import metrics
from sklearn.metrics import confusion_matrix,accuracy_score
from sklearn.metrics import classification_report

class LogisticModel:

    def __init__(self) -> None:
        self.logistic_regression= LogisticRegression()

        pass

    def train_logistic(self, dataframe: pd.DataFrame, class_column: str):

        y = dataframe[class_column]
        X = dataframe.drop(class_column, axis = 1)
        mlflow.log_param("columns", X.columns)

        X_train,X_test,y_train,y_test = train_test_split(X,y,test_size=0.25,random_state=0)

        self.logistic_regression.fit(X_train,y_train)
        y_pred=self.logistic_regression.predict(X_test)

        # confusion_matrix = pd.crosstab(y_test, y_pred, rownames=['Actual'], colnames=['Predicted'])
        conf_matrix = confusion_matrix(y_test, y_pred)
        print(conf_matrix)

        accuracy = accuracy_score(y_test, y_pred)
        print(accuracy)

        self.log_metrics(conf_matrix,accuracy)

        print(classification_report(y_test, y_pred))

        return self.logistic_regression
    
    def apply_logistic(self,dataframe):
        pred = self.logistic_regression.predict(dataframe)
        return pred

    def log_metrics(self, conf_matrix, acurracy):

        true_positive = conf_matrix[0][0]
        true_negative = conf_matrix[1][1]
        false_positive = conf_matrix[0][1]
        false_negative = conf_matrix[1][0]

        mlflow.log_metric("true_positive", true_positive)
        mlflow.log_metric("true_negative", true_negative)
        mlflow.log_metric("false_positive", false_positive)
        mlflow.log_metric("false_negative", false_negative)

        mlflow.log_metric("acurracy", acurracy)