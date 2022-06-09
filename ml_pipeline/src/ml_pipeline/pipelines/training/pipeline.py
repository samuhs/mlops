"""
This is a boilerplate pipeline 'training'
generated using Kedro 0.18.1
"""

from kedro.pipeline import Pipeline, node, pipeline
from .nodes import process_dataframe, logistic_training

def create_pipeline(**kwargs) -> Pipeline:
    return pipeline(
        [
            node(
                process_dataframe,
                inputs='challenge_train',
                outputs='challenge_train_process',
                name="process_dataframe_node",
            ),
            node(
                logistic_training,
                inputs='challenge_train_process',
                outputs=None,
                name="logistic_training_node",
            ),
        ]
    )
